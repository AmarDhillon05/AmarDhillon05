#!/usr/bin/env python3
"""Reusable scraper for outcome-backed resume threads on Reddit.

Primary path: old.reddit.com HTML (search pages + thread pages), parsed with the
stdlib only. Fallback path: the Arctic Shift Reddit archive API
(arctic-shift.photon-reddit.com), which returns the same post/comment fields as
JSON. The fallback exists because old.reddit.com frequently redirects anonymous
datacenter traffic to /login (observed 2026-10 from this environment) and the
reddit .json API returns 403.

All raw responses (HTML/JSON/images) are cached under CACHE_DIR so repeated
runs are cheap and reproducible.

Usage examples
--------------
  # search a subreddit (old.reddit first, archive fallback)
  python tools/scrape_outcome_resumes.py search EngineeringResumes "flair:Success" --t year
  # list every post with a given flair since a date (archive API)
  python tools/scrape_outcome_resumes.py flair EngineeringResumes "Success Story!" --after 2024-01-01
  # fetch a thread: body, date, score, image links, top comments w/ flair
  python tools/scrape_outcome_resumes.py thread https://www.reddit.com/r/EngineeringResumes/comments/1sj2rgt/
  # download a thread's resume images (to read/transcribe them)
  python tools/scrape_outcome_resumes.py images 1sj2rgt
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import quote_plus, urlencode

import requests

CACHE_DIR = os.environ.get("OUTCOME_CACHE", "/tmp/claude-0/outcome_cache")
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36 resume-lab/0.1")
ARCTIC = "https://arctic-shift.photon-reddit.com/api"
IMG_RE = re.compile(
    r"https?://(?:i\.redd\.it|preview\.redd\.it|i\.imgur\.com|imgur\.com)/[^\s\"'<>)\]]+",
    re.I)

_session = requests.Session()
_session.headers["User-Agent"] = UA


# --------------------------------------------------------------------------- cache
def _cache_path(key: str, ext: str) -> str:
    os.makedirs(CACHE_DIR, exist_ok=True)
    h = hashlib.sha1(key.encode()).hexdigest()[:16]
    return os.path.join(CACHE_DIR, f"{h}.{ext}")


def fetch(url: str, ext: str = "html", binary: bool = False, sleep: float = 1.0,
          params: dict | None = None):
    """GET with on-disk cache. Returns (text|bytes, final_url) or (None, url)."""
    key = url + ("?" + urlencode(params) if params else "")
    path = _cache_path(key, ext)
    meta = path + ".url"
    if os.path.exists(path):
        final = open(meta).read() if os.path.exists(meta) else key
        mode = "rb" if binary else "r"
        with open(path, mode) as f:
            return f.read(), final
    for attempt in range(5):
        try:
            r = _session.get(url, params=params, timeout=60)
        except requests.RequestException:
            time.sleep(2 * (attempt + 1))
            continue
        if r.status_code == 429 or r.status_code >= 500 or "Timeout" in r.text[:200]:
            time.sleep(5 * (attempt + 1))
            continue
        if r.status_code != 200:
            return None, r.url
        data = r.content if binary else r.text
        if ext == "json" and '"error"' in data[:200] and '"data":null' in data[:200]:
            time.sleep(5 * (attempt + 1))  # archive timeout ("slow down"); retry, don't cache
            continue
        with open(path, "wb" if binary else "w") as f:
            f.write(data)
        with open(meta, "w") as f:
            f.write(r.url)
        time.sleep(sleep)
        return data, r.url
    return None, url


def _blocked(final_url: str, text: str | None) -> bool:
    return (text is None or "/login" in final_url or "js_challenge" in (text or "")
            or "blocked by network security" in (text or ""))


# ------------------------------------------------------------------ data classes
@dataclass
class Comment:
    author: str
    flair: str | None
    score: int | None
    body: str
    depth: int = 0


@dataclass
class Thread:
    id: str
    subreddit: str
    title: str
    url: str
    created_utc: int
    date: str
    score: int | None
    flair: str | None
    author_flair: str | None
    body: str
    image_links: list[str] = field(default_factory=list)
    comments: list[Comment] = field(default_factory=list)
    source: str = "old.reddit"


def _iso(ts: int) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).date().isoformat()


def _post_id(url_or_id: str) -> str:
    m = re.search(r"/comments/([a-z0-9]+)", url_or_id)
    return m.group(1) if m else url_or_id.strip("/").split("_")[-1]


# --------------------------------------------------------- old.reddit HTML parse
class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in ("p", "br", "li", "h1", "h2", "h3", "tr", "pre"):
            self.parts.append("\n")
        if tag == "li":
            self.parts.append("- ")

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(fragment: str) -> str:
    p = _TextExtractor()
    p.feed(fragment)
    return re.sub(r"\n{3,}", "\n\n", "".join(p.parts)).strip()


def _md_block(chunk: str) -> str:
    m = re.search(r'<div class="md">(.*?)</div>\s*</div>\s*</form>', chunk, re.S)
    return html_to_text(m.group(1)) if m else ""


def parse_old_search(page: str) -> list[dict]:
    out = []
    for blk in re.findall(r'<div class="[^"]*search-result-link.*?</div>\s*</div>\s*</div>',
                          page, re.S):
        t = re.search(r'class="search-title[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', blk, re.S)
        if not t:
            t = re.search(r'href="([^"]+)"[^>]*class="search-title[^"]*"[^>]*>(.*?)</a>', blk, re.S)
        if not t:
            continue
        sc = re.search(r'search-score[^>]*>([\-\d,]+)', blk)
        dt = re.search(r'<time[^>]*datetime="([^"]+)"', blk)
        out.append({
            "id": _post_id(t.group(1)), "url": html.unescape(t.group(1)),
            "title": html_to_text(t.group(2)),
            "score": int(sc.group(1).replace(",", "")) if sc else None,
            "date": dt.group(1)[:10] if dt else None,
        })
    return out


def parse_old_thread(page: str, url: str, max_comments: int = 25) -> Thread:
    link = re.search(r'<div class=" thing id-t3_(\w+)[^"]*"([^>]*)>', page)
    attrs = link.group(2) if link else ""
    pid = link.group(1) if link else _post_id(url)
    ts = int(re.search(r'data-timestamp="(\d+)"', attrs).group(1)) // 1000 if 'data-timestamp' in attrs else 0
    score = re.search(r'data-score="(-?\d+)"', attrs)
    sub = re.search(r'data-subreddit="([^"]+)"', attrs)
    title = re.search(r'<a class="title[^"]*"[^>]*>(.*?)</a>', page, re.S)
    lflair = re.search(r'<span class="linkflairlabel[^"]*"[^>]*title="([^"]*)"', page)
    # post body lives in the first .expando usertext
    exp = re.search(r'<div class="expando[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</form>', page, re.S)
    body = html_to_text(exp.group(1)) if exp else ""
    imgs = sorted(set(html.unescape(u) for u in IMG_RE.findall(page[: page.find('class="commentarea"')])))
    th = Thread(id=pid, subreddit=sub.group(1) if sub else "", title=html_to_text(title.group(1)) if title else "",
                url=url, created_utc=ts, date=_iso(ts) if ts else "", score=int(score.group(1)) if score else None,
                flair=lflair.group(1) if lflair else None, author_flair=None, body=body, image_links=imgs)
    carea = page[page.find('class="commentarea"'):]
    for m in re.finditer(r'<div class=" thing id-t1_\w+[^"]*comment[^"]*"([^>]*)>(.*?)(?=<div class=" thing id-t1_|\Z)',
                         carea, re.S):
        a, chunk = m.group(1), m.group(2)
        author = re.search(r'data-author="([^"]+)"', a)
        fl = re.search(r'<span class="flair[^"]*" title="([^"]*)"', chunk)
        sc = re.search(r'<span class="score unvoted" title="(-?\d+)"', chunk)
        bm = re.search(r'<div class="md">(.*?)</div>', chunk, re.S)
        depth = len(re.findall(r'class="child"', chunk[:200]))
        th.comments.append(Comment(author=author.group(1) if author else "[deleted]",
                                   flair=html.unescape(fl.group(1)) if fl else None,
                                   score=int(sc.group(1)) if sc else None,
                                   body=html_to_text(bm.group(1)) if bm else "", depth=depth))
        if len(th.comments) >= max_comments:
            break
    return th


# ------------------------------------------------------------- archive fallback
def arctic_posts(**params) -> list[dict]:
    params.setdefault("limit", 100)
    txt, _ = fetch(f"{ARCTIC}/posts/search", ext="json", params=params)
    return json.loads(txt).get("data", []) if txt else []


def arctic_all(subreddit: str, after: str = "2024-01-01", **filters) -> list[dict]:
    """Paginate an archive query ascending by time."""
    out, cursor, seen = [], after, set()
    while True:
        batch = arctic_posts(subreddit=subreddit, after=cursor, sort="asc", **filters)
        # the archive may return fewer than `limit` rows per page even when more
        # exist (filtered queries), so only stop on an empty page
        batch = [b for b in batch if b["id"] not in seen]
        if not batch:
            return out
        seen.update(b["id"] for b in batch)
        out += batch
        cursor = str(int(max(b["created_utc"] for b in batch)) + 1)


def _media_id(u: str) -> str:
    m = re.search(r"/(?:[^/]*-)?([a-z0-9]{10,16})\.\w+", u)
    return m.group(1) if m else u


def _post_images(p: dict) -> list[str]:
    """Image URLs for a post: full-res i.redd.it first, then signed previews as
    fallbacks (i.redd.it serves a tiny placeholder once an image is removed,
    while preview.redd.it links with their signature often still resolve)."""
    imgs = []
    for mid, mm in (p.get("media_metadata") or {}).items():
        mime = (mm.get("m") or "image/jpg").split("/")[-1].replace("jpeg", "jpg")
        imgs.append(f"https://i.redd.it/{mid}.{mime}")
        if mm.get("s", {}).get("u"):
            imgs.append(mm["s"]["u"])
    url = p.get("url") or ""
    if IMG_RE.match(url):
        imgs.append(url)
    for im in (p.get("preview") or {}).get("images", []):
        if im.get("source", {}).get("url"):
            imgs.append(im["source"]["url"])
    imgs += IMG_RE.findall(p.get("selftext") or "")
    seen, res = set(), []
    for u in imgs:
        u = html.unescape(u)
        if u not in seen:
            seen.add(u)
            res.append(u)
    return res


def _flatten(nodes, depth=0, out=None):
    out = [] if out is None else out
    for n in nodes or []:
        d = n.get("data", n)
        if n.get("kind", "t1") != "t1":
            continue
        out.append(Comment(author=d.get("author", ""), flair=d.get("author_flair_text"),
                           score=d.get("score"), body=d.get("body", ""), depth=depth))
        rep = d.get("replies")
        if isinstance(rep, dict):
            _flatten(rep.get("data", {}).get("children"), depth + 1, out)
        elif isinstance(rep, list):
            _flatten(rep, depth + 1, out)
    return out


def arctic_thread(pid: str, max_comments: int = 40) -> Thread | None:
    txt, _ = fetch(f"{ARCTIC}/posts/ids", ext="json", params={"ids": pid})
    data = json.loads(txt).get("data", []) if txt else []
    if not data:
        return None
    p = data[0]
    ctxt, _ = fetch(f"{ARCTIC}/comments/tree", ext="json", params={"link_id": pid, "limit": 500})
    comments = _flatten(json.loads(ctxt).get("data", [])) if ctxt else []
    top = sorted([c for c in comments if c.depth == 0], key=lambda c: -(c.score or 0))
    # keep top-level by score, plus replies from flaired users (recruiters/mods/HMs)
    flaired = [c for c in comments if c.depth > 0 and c.flair]
    keep = (top + flaired)[:max_comments]
    return Thread(id=p["id"], subreddit=p["subreddit"], title=p["title"],
                  url="https://www.reddit.com" + p["permalink"], created_utc=int(p["created_utc"]),
                  date=_iso(int(p["created_utc"])), score=p.get("score"), flair=p.get("link_flair_text"),
                  author_flair=p.get("author_flair_text"), body=p.get("selftext") or "",
                  image_links=_post_images(p), comments=keep, source="arctic-shift")


# ------------------------------------------------------------------ public API
def search(subreddit: str, q: str, sort: str = "top", t: str = "year") -> list[dict]:
    url = (f"https://old.reddit.com/r/{subreddit}/search?q={quote_plus(q)}"
           f"&restrict_sr=on&sort={sort}&t={t}")
    page, final = fetch(url)
    if not _blocked(final, page):
        res = parse_old_search(page)
        if res:
            return res
    # fallback: archive. "flair:X" -> link_flair_text, otherwise full-text query
    m = re.match(r"flair:\"?([^\"]+)\"?$", q)
    params = {"link_flair_text": m.group(1)} if m else {"query": q}
    after = {"year": "365d", "month": "30d", "week": "7d", "all": None}.get(t, "365d")
    if after:
        params["after"] = after
    posts = arctic_posts(subreddit=subreddit, **params)
    if sort == "top":
        posts.sort(key=lambda p: -(p.get("score") or 0))
    return [{"id": p["id"], "url": "https://www.reddit.com" + p["permalink"], "title": p["title"],
             "score": p.get("score"), "date": _iso(int(p["created_utc"])),
             "flair": p.get("link_flair_text")} for p in posts]


def thread(url_or_id: str, max_comments: int = 40) -> Thread | None:
    pid = _post_id(url_or_id)
    url = url_or_id if url_or_id.startswith("http") else f"https://old.reddit.com/comments/{pid}/"
    url = re.sub(r"https?://(www\.)?reddit\.com", "https://old.reddit.com", url)
    page, final = fetch(url + ("?sort=top" if "?" not in url else ""))
    if not _blocked(final, page):
        th = parse_old_thread(page, url, max_comments)
        if th.title:
            return th
    return arctic_thread(pid, max_comments)


def download_images(th: Thread, out_dir: str | None = None) -> list[str]:
    """Download one image per media id (trying fallbacks in order)."""
    out_dir = out_dir or os.path.join(CACHE_DIR, "img", th.id)
    os.makedirs(out_dir, exist_ok=True)
    groups: dict[str, list[str]] = {}
    for u in th.image_links:
        groups.setdefault(_media_id(u), []).append(u)
    paths = []
    for i, (mid, urls) in enumerate(groups.items()):
        for u in urls:
            data, _ = fetch(u, ext="bin", binary=True, sleep=0.3)
            if not data or len(data) < 5000:  # 404 placeholder / removed image
                continue
            ext = "png" if data[:4] == b"\x89PNG" else ("gif" if data[:3] == b"GIF" else "jpg")
            p = os.path.join(out_dir, f"{i}_{re.sub(r'[^A-Za-z0-9]', '', mid)[-16:]}.{ext}")
            with open(p, "wb") as f:
                f.write(data)
            paths.append(p)
            break
    return paths


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("search"); s.add_argument("subreddit"); s.add_argument("q")
    s.add_argument("--sort", default="top"); s.add_argument("--t", default="year")
    f = sp.add_parser("flair"); f.add_argument("subreddit"); f.add_argument("flair")
    f.add_argument("--after", default="2024-01-01")
    q = sp.add_parser("query"); q.add_argument("subreddit"); q.add_argument("q")
    q.add_argument("--after", default="2024-01-01"); q.add_argument("--field", default="query",
                                                                    choices=["query", "title", "selftext"])
    t = sp.add_parser("thread"); t.add_argument("url"); t.add_argument("--max-comments", type=int, default=40)
    i = sp.add_parser("images"); i.add_argument("url")
    a = ap.parse_args(argv)

    if a.cmd == "search":
        print(json.dumps(search(a.subreddit, a.q, a.sort, a.t), indent=1))
    elif a.cmd == "flair":
        for p in arctic_all(a.subreddit, a.after, link_flair_text=a.flair):
            print(_iso(int(p["created_utc"])), p.get("score"), p["id"], p["title"][:120], sep="\t")
    elif a.cmd == "query":
        for p in arctic_all(a.subreddit, a.after, **{a.field: a.q}):
            print(_iso(int(p["created_utc"])), p.get("score"), p["id"], p.get("link_flair_text"),
                  p["title"][:120], sep="\t")
    elif a.cmd == "thread":
        th = thread(a.url, a.max_comments)
        print(json.dumps(asdict(th), indent=1) if th else "null")
    elif a.cmd == "images":
        th = thread(a.url)
        print("\n".join(download_images(th)) if th else "")


if __name__ == "__main__":
    sys.exit(main())
