#!/usr/bin/env python3
"""Fetch a list of URLs, strip HTML to text, and cache to corpus/raw/sources/<hash>.txt.

Usage:
    python tools/fetch_sources.py URL [URL ...]
    python tools/fetch_sources.py -f urls.txt          # one URL per line, '#' comments ok
    python tools/fetch_sources.py -f urls.txt --force  # refetch even if cached
    python tools/fetch_sources.py --reddit-flair "Recruiter" --sub EngineeringResumes --q bullet

Notes
- Uses the proxy environment as-is (HTTPS_PROXY / REQUESTS_CA_BUNDLE are honoured by requests;
  if REQUESTS_CA_BUNDLE is unset we fall back to /root/.ccr/ca-bundle.crt when it exists).
- Sends a browser-like User-Agent.
- Reddit: www.reddit.com is rewritten to old.reddit.com; if old.reddit answers with a login
  wall / 403 we fall back to the Arctic Shift archive API (post + comment tree as text).
- Hacker News item pages fall back to the public Algolia API.
- Writes an index line per URL to corpus/raw/sources/index.jsonl (url, hash, status, chars).
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
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import requests

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "corpus" / "raw" / "sources"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36 resume-lab-research/0.1")
ARCTIC = "https://arctic-shift.photon-reddit.com/api"

if not os.environ.get("REQUESTS_CA_BUNDLE") and os.path.exists("/root/.ccr/ca-bundle.crt"):
    os.environ["REQUESTS_CA_BUNDLE"] = "/root/.ccr/ca-bundle.crt"

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})


def url_hash(url: str) -> str:
    return hashlib.sha1(url.strip().encode()).hexdigest()[:16]


class _TextExtractor(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "header", "form", "iframe"}
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "section",
             "article", "blockquote", "pre", "ul", "ol", "table"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.skip_depth = 0
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip_depth += 1
        elif tag == "title":
            self._in_title = True
        elif tag in self.BLOCK:
            self.out.append("\n")
            if tag == "li":
                self.out.append("- ")
            if tag in {"h1", "h2", "h3", "h4"}:
                self.out.append("#" * int(tag[1]) + " ")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip_depth:
            self.skip_depth -= 1
        elif tag == "title":
            self._in_title = False
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if not self.skip_depth:
            self.out.append(data)


def html_to_text(raw: str) -> tuple[str, str]:
    p = _TextExtractor()
    try:
        p.feed(raw)
    except Exception:  # malformed html: degrade to regex strip
        return "", re.sub(r"<[^>]+>", " ", raw)
    text = "".join(p.out)
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return p.title.strip(), text.strip()


def _get(url: str, **kw) -> requests.Response:
    return SESSION.get(url, timeout=kw.pop("timeout", 30), allow_redirects=True, **kw)


# ---------------------------------------------------------------- reddit
def _reddit_post_id(url: str) -> str | None:
    m = re.search(r"/comments/([a-z0-9]+)", url)
    return m.group(1) if m else None


def _reddit_comment_id(url: str) -> str | None:
    m = re.search(r"/comments/[a-z0-9]+/[^/]*/([a-z0-9]+)", url)
    return m.group(1) if m else None


def _flatten_tree(nodes, depth=0, out=None):
    out = [] if out is None else out
    for n in nodes or []:
        d = n.get("data", n)
        if "body" in d:
            flair = d.get("author_flair_text") or ""
            out.append(f"{'  ' * depth}[{d.get('author')} | flair={flair} | score={d.get('score')}] "
                       f"{html.unescape(d.get('body', ''))}")
        rep = d.get("replies")
        if isinstance(rep, dict):
            _flatten_tree(rep.get("data", {}).get("children"), depth + 1, out)
        elif isinstance(rep, list):
            _flatten_tree(rep, depth + 1, out)
        for c in d.get("children", []) if isinstance(d.get("children"), list) else []:
            if isinstance(c, dict):
                _flatten_tree([c], depth + 1, out)
    return out


def fetch_reddit_archive(url: str) -> tuple[str, str]:
    pid = _reddit_post_id(url)
    if not pid:
        raise ValueError("no post id in reddit url")
    post = _get(f"{ARCTIC}/posts/ids", params={"ids": pid}).json().get("data") or [{}]
    post = post[0] if post else {}
    title = post.get("title", "")
    created = post.get("created_utc")
    lines = [f"TITLE: {title}",
             f"DATE: {time.strftime('%Y-%m-%d', time.gmtime(created)) if created else ''}",
             f"SCORE: {post.get('score')}  AUTHOR: {post.get('author')} flair={post.get('author_flair_text')}",
             "", html.unescape(post.get("selftext", "") or ""), "", "COMMENTS:"]
    cid = _reddit_comment_id(url)
    if cid:
        c = _get(f"{ARCTIC}/comments/ids", params={"ids": cid}).json().get("data") or []
        lines += _flatten_tree(c)
    tree = _get(f"{ARCTIC}/comments/tree", params={"link_id": pid, "limit": 400}).json().get("data") or []
    lines += _flatten_tree(tree)
    return title, "\n".join(lines)


def search_reddit_comments(sub: str, flair: str = "", q: str = "", after: str = "2024-01-01",
                           limit: int = 100) -> list[dict]:
    """Arctic Shift comment search; returns raw dicts (body, author, flair, score, permalink...)."""
    params = {"subreddit": sub, "after": after, "limit": limit}
    if flair:
        params["author_flair_text"] = flair
    if q:
        params["body"] = q
    for attempt in range(4):
        r = _get(f"{ARCTIC}/comments/search", params=params, timeout=60)
        js = r.json()
        if js.get("data") is not None:
            return js["data"]
        time.sleep(3 * (attempt + 1))
    return []


# ---------------------------------------------------------------- HN
def fetch_hn(url: str) -> tuple[str, str]:
    item = parse_qs(urlparse(url).query).get("id", [None])[0]
    js = _get(f"https://hn.algolia.com/api/v1/items/{item}").json()

    def walk(n, d=0, out=None):
        out = [] if out is None else out
        if n.get("text"):
            _, t = html_to_text(n["text"])
            out.append(f"{'  ' * d}[{n.get('author')} pts={n.get('points')}] {t}")
        for ch in n.get("children", []):
            walk(ch, d + 1, out)
        return out

    head = f"TITLE: {js.get('title')}\nDATE: {js.get('created_at', '')[:10]}\nPOINTS: {js.get('points')}\n"
    return js.get("title") or "", head + "\n".join(walk(js))


def _pdf_to_text(data: bytes) -> str:
    """Use poppler's pdftotext if installed; return '' otherwise."""
    import shutil
    import subprocess
    import tempfile
    if not shutil.which("pdftotext"):
        return ""
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(data)
        f.flush()
        out = subprocess.run(["pdftotext", "-layout", f.name, "-"], capture_output=True, timeout=60)
    return out.stdout.decode("utf-8", "ignore").strip()


# ---------------------------------------------------------------- main fetch
def fetch_one(url: str, force: bool = False) -> dict:
    CACHE.mkdir(parents=True, exist_ok=True)
    h = url_hash(url)
    path = CACHE / f"{h}.txt"
    if path.exists() and not force and path.stat().st_size > 200:
        return {"url": url, "hash": h, "status": "cached", "chars": path.stat().st_size, "path": str(path)}
    title, text, status = "", "", "error"
    host = urlparse(url).netloc
    try:
        if "reddit.com" in host:
            old = re.sub(r"https?://(www\.)?reddit\.com", "https://old.reddit.com", url)
            r = _get(old)
            if r.ok and "/login" not in r.url and "reddit.com/comments" in r.text:
                title, text = html_to_text(r.text)
                status = "ok_old_reddit"
            else:
                title, text = fetch_reddit_archive(url)
                status = "ok_reddit_archive"
        elif "news.ycombinator.com" in host:
            title, text = fetch_hn(url)
            status = "ok_hn_api"
        else:
            r = _get(url)
            ctype = r.headers.get("content-type", "")
            if not r.ok:
                status = f"http_{r.status_code}"
            elif "pdf" in ctype or r.content[:5] == b"%PDF-":
                text = _pdf_to_text(r.content)
                status = "ok_pdf" if text else "pdf_unsupported"
            else:
                title, text = html_to_text(r.text)
                status = "ok" if len(text) > 500 else "ok_thin"
    except Exception as e:  # network / parse errors are recorded, not raised
        status = f"error:{type(e).__name__}:{str(e)[:80]}"
    if text:
        path.write_text(f"URL: {url}\nTITLE: {title or ''}\nFETCHED: {time.strftime('%Y-%m-%d')}\n\n{text}\n")
    rec = {"url": url, "hash": h, "status": status, "chars": len(text), "title": (title or "")[:200],
           "path": str(path) if text else None}
    with open(CACHE / "index.jsonl", "a") as f:
        f.write(json.dumps(rec) + "\n")
    return rec


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="*")
    ap.add_argument("-f", "--file")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.5)
    ap.add_argument("--reddit-flair", help="search Arctic Shift comments by author flair")
    ap.add_argument("--sub", default="cscareerquestions")
    ap.add_argument("--q", default="")
    ap.add_argument("--after", default="2024-01-01")
    a = ap.parse_args(argv)
    if a.reddit_flair is not None:
        rows = search_reddit_comments(a.sub, a.reddit_flair, a.q, a.after)
        for r in rows:
            print(json.dumps({k: r.get(k) for k in ("id", "author", "author_flair_text", "score",
                                                     "created_utc", "link_id", "body")}))
        return
    urls = list(a.urls)
    if a.file:
        urls += [l.strip() for l in open(a.file) if l.strip() and not l.startswith("#")]
    for u in urls:
        rec = fetch_one(u, a.force)
        print(f"{rec['status']:<20} {rec['chars']:>7}  {u}")
        time.sleep(a.sleep)


if __name__ == "__main__":
    main()
