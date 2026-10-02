#!/usr/bin/env python3
"""Build corpus/sources.jsonl, corpus/advice.jsonl, research/sources.md and research/claim_stats.json.

Inputs:
  tools/corpus_sources.py   hand-scored KEPT sources + rejection overrides
  tools/corpus_claims.py    hand-extracted atomic claims for KEPT sources
  corpus/raw/sources/index.jsonl + *.txt   fetch cache written by tools/fetch_sources.py
  corpus/raw/reddit/*.jsonl                Arctic Shift dumps of flaired recruiter/HM comments

Also verifies that every quote appears (modulo whitespace/ellipses) in the cached source text and
prints any mismatches.
"""
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import corpus_claims  # noqa: E402
import corpus_sources as cs  # noqa: E402

RAW = ROOT / "corpus" / "raw"
DOMAINS = ["general_swe", "startup_fullstack", "backend_distributed", "cloud_infra_sre", "ai_ml_engineering",
           "ml_research_robotics", "quant_hft", "data_engineering", "embedded_systems"]

# Sources that share an author/organisation are not independent.
ORG = {
    "S002": "interviewing.io", "S003": "interviewing.io", "S004": "interviewing.io", "S005": "interviewing.io",
    "S006": "interviewing.io", "S009": "pragmatic_engineer", "S010": "pragmatic_engineer", "S011": "gergely_orosz",
    "S012": "gergely_orosz", "S013": "yc_ryan_choi", "S014": "yc_ryan_choi", "S015": "anthropic", "S016": "anthropic",
    "S021": "nace", "S022": "nace", "S023": "greenhouse", "S024": "greenhouse", "S025": "greenhouse",
    "S042": "techiecv", "S083": "techiecv", "S084": "techiecv", "S027": "hackerrank_ats_experiment",
    "S028": "hackerrank_ats_experiment",
}

SEO_HOSTS = ("beamjobs", "enhancv", "cvcompiler", "resumeworded", "zety", "tealhq", "huntr", "owlapply", "wahresume",
             "cvowl", "resumatic", "resumepuppy", "swooped", "projectpro", "coursera", "joinleland", "designgurus",
             "interviewkickstart", "jobsprout", "foundersarehiring", "paraform", "elitebrains", "cirby", "levstack",
             "resumemate", "interviewnode", "applr", "rezi", "kraftcv", "artisantalent", "fuzehr", "wobo",
             "standout-cv", "resumeheatmap", "distinctrecruitment", "chiefofstaff", "sweresume", "faangtechleads",
             "inskill", "dataengineeracademy", "nextmantra", "getsmartresume", "extern.com", "quantt.co.uk/resources/quant-internships",
             "tradermath", "quantblueprint", "simplify.jobs", "techinterview.org", "sds.io", "jugaldb", "teamblind",
             "underdog", "wrok.app", "careersinrobotics.com/x", "roboticscareer", "pennwest.edu/", "medium.com",
             "igotanoffer", "inc.com", "hr.com", "skillfuel", "herohunt", "livecareer", "theladders.com")


def uhash(url: str) -> str:
    return hashlib.sha1(url.strip().encode()).hexdigest()[:16]


def norm(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("\\", "")
    s = re.sub(r"[^\w%$'\"<>+:/.,()\[\]|-]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def load_index():
    idx = {}
    for line in open(RAW / "sources" / "index.jsonl"):
        r = json.loads(line)
        prev = idx.get(r["url"])
        if prev is None or (r.get("path") and not prev.get("path")) or ("published" in r):
            if prev and prev.get("path") and not r.get("path"):
                continue
            idx[r["url"]] = {**(prev or {}), **r}
    return idx


def reddit_rows():
    rows = []
    for f in ("flaired_comments.jsonl", "domain_comments.jsonl"):
        p = RAW / "reddit" / f
        if p.exists():
            rows += [json.loads(l) for l in open(p)]
    return rows


def source_text(src, idx, rrows):
    sid, url = src[0], src[1]
    parts = []
    p = RAW / "sources" / f"{uhash(url)}.txt"
    if p.exists():
        parts.append(p.read_text())
    m = re.search(r"u/(\S+) \(", src[2])
    if src[4] == "reddit_comments":
        cid = re.search(r"/_/([a-z0-9]+)/", url)
        author = m.group(1) if m else None
        for r in rrows:
            if (author and r.get("author") == author) or (cid and r.get("id") == cid.group(1)):
                parts.append(r.get("body", ""))
    return "\n".join(parts)


def quote_found(quote: str, text: str) -> bool:
    t = norm(text)
    frags = [f for f in re.split(r"\.\.\.|…", quote) if len(norm(f)) > 3]
    return all(norm(f) in t for f in frags)


def guess_domains(url: str, title: str):
    s = (url + " " + (title or "")).lower()
    d = []
    for kw, dom in (("quant", "quant_hft"), ("hft", "quant_hft"), ("jane", "quant_hft"), ("citadel", "quant_hft"),
                    ("hudson", "quant_hft"), ("optiver", "quant_hft"), ("two-sigma", "quant_hft"), ("jump", "quant_hft"),
                    ("machine-learning", "ai_ml_engineering"), ("ml-", "ai_ml_engineering"), ("ai-", "ai_ml_engineering"),
                    ("research", "ml_research_robotics"), ("robot", "ml_research_robotics"), ("deepmind", "ml_research_robotics"),
                    ("data-engineer", "data_engineering"), ("dataengineering", "data_engineering"), ("embedded", "embedded_systems"),
                    ("firmware", "embedded_systems"), ("fpga", "embedded_systems"), ("sre", "cloud_infra_sre"),
                    ("reliability", "cloud_infra_sre"), ("devops", "cloud_infra_sre"), ("platform", "cloud_infra_sre"),
                    ("infrastructure", "cloud_infra_sre"), ("backend", "backend_distributed"), ("back-end", "backend_distributed"),
                    ("distributed", "backend_distributed"), ("startup", "startup_fullstack"), ("ycombinator", "startup_fullstack")):
        if kw in s and dom not in d:
            d.append(dom)
    return d or ["general_swe"]


def main():
    idx = load_index()
    rrows = reddit_rows()
    kept_urls = {s[1] for s in cs.KEPT}
    sources, advice = [], []
    demoted = set()

    for (sid, url, title, date, stype, role, tier, doms, outcome, valid, found, sc) in cs.KEPT:
        r, o, rec, v = sc
        sources.append({
            "id": sid, "url": url, "title": title, "date": date, "source_type": stype, "author_role": role,
            "author_org_tier": tier, "domains": doms, "outcome_evidence": outcome, "community_validation": valid,
            "foundational": found,
            "credibility": {"role": r, "outcome": o, "recency": rec, "validation": v, "total": r + o + rec + v},
            "kept": True, "reject_reason": None, "independence_group": ORG.get(sid, sid),
        })
        # enforce the keep rule instead of asserting: demote failures to rejected
        if r + o + rec + v < 5 or not (found or date >= "2024"):
            sources[-1]["kept"] = False
            sources[-1]["reject_reason"] = ("credibility<5" if r + o + rec + v < 5 else "") + \
                (" pre-2024 non-foundational" if not (found or date >= "2024") else "")
            demoted.add(sid)

    # ---- rejected candidates from the fetch index
    n = 0
    for url, rec in idx.items():
        if url in kept_urls:
            continue
        n += 1
        title = rec.get("title") or url
        date = rec.get("published") or ""
        txt = RAW / "sources" / f"{rec['hash']}.txt"
        if not date and txt.exists():
            m = re.search(r"^DATE: (\d{4}-\d{2}-\d{2})", txt.read_text()[:3000], re.M)
            date = m.group(1) if m else ""
        status = rec.get("status", "")
        if url in cs.REJECT_OVERRIDES:
            reason, role = cs.REJECT_OVERRIDES[url]
        elif not rec.get("path"):
            reason, role = f"fetch_failed ({status}); not independently verifiable", "unknown"
        elif "reddit.com" in url and url in cs.REJECT_REDDIT:
            reason, role = cs.REJECT_REDDIT[url][1], "community"
            date = cs.REJECT_REDDIT[url][0]
        elif any(h in url for h in SEO_HOSTS):
            reason, role = "SEO/resume-builder or aggregator content: no named hiring-side author or outcome evidence", "vendor"
        elif date and date < "2024":
            reason, role = "pre-2024 and not foundational", "unknown"
        else:
            reason, role = "low credibility score (<5) or no resume-screening advice", "unknown"
        recency = 2 if date >= "2025" else 1 if date >= "2024" or not date else 0
        rs = {"vendor": 0, "community": 1, "company_official": 3, "career_center": 2, "recruiter": 2,
              "hiring_manager": 2, "engineer": 2, "study": 2}.get(role, 0)
        sources.append({
            "id": f"R{n:03d}", "url": url, "title": title[:200], "date": date or "unknown",
            "source_type": "reddit_thread" if "reddit.com" in url else "hn_thread" if "ycombinator.com/item" in url else "web",
            "author_role": role, "author_org_tier": "unknown", "domains": guess_domains(url, title),
            "outcome_evidence": "", "community_validation": "", "foundational": False,
            "credibility": {"role": rs, "outcome": 0, "recency": recency, "validation": 0, "total": rs + recency},
            "kept": False, "reject_reason": reason, "independence_group": None,
        })
    for key, (date, reason) in cs.REJECT_REDDIT.items():
        if key in idx:
            continue
        n += 1
        sources.append({
            "id": f"R{n:03d}", "url": key if key.startswith("http") else "", "title": key, "date": date,
            "source_type": "reddit_comments" if key.startswith("u/") else "reddit_thread", "author_role": "community",
            "author_org_tier": "community", "domains": ["general_swe"], "outcome_evidence": "", "community_validation": "",
            "foundational": False, "credibility": {"role": 1, "outcome": 0, "recency": 2 if date >= "2025" else 1,
                                                   "validation": 0, "total": 1 + (2 if date >= "2025" else 1)},
            "kept": False, "reject_reason": reason, "independence_group": None,
        })

    # ---- advice rows + quote verification
    by_id = {s[0]: s for s in cs.KEPT}
    texts = {sid: source_text(s, idx, rrows) for sid, s in by_id.items()}
    bad = []
    for (sid, key, cat, dom, claim, quote, strength, stance) in corpus_claims.C:
        if sid in demoted:
            continue
        assert sid in by_id, sid
        assert dom in DOMAINS, (sid, dom)
        assert len(quote.split()) <= 25, (sid, quote)
        ok = quote_found(quote, texts[sid])
        if not ok:
            bad.append((sid, quote))
        advice.append({"source_id": sid, "claim": claim, "category": cat, "domain": dom, "quote": quote,
                       "strength": strength, "key": key, "stance": stance, "quote_verified": ok})

    (ROOT / "corpus").mkdir(exist_ok=True)
    with open(ROOT / "corpus" / "sources.jsonl", "w") as f:
        for s in sources:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    with open(ROOT / "corpus" / "advice.jsonl", "w") as f:
        for a in advice:
            f.write(json.dumps(a, ensure_ascii=False) + "\n")

    # ---- stats for synthesis
    kept = {s["id"]: s for s in sources if s["kept"]}
    stats = collections.defaultdict(lambda: {"for": set(), "against": set(), "for_groups": set(),
                                             "against_groups": set(), "domains": collections.Counter(),
                                             "cred_for": 0, "category": None})
    for a in advice:
        st = stats[a["key"]]
        st[a["stance"]].add(a["source_id"])
        st[a["stance"] + "_groups"].add(kept[a["source_id"]]["independence_group"])
        st["domains"][a["domain"]] += 1
        st["category"] = st["category"] or a["category"]
    out = {}
    for k, st in stats.items():
        out[k] = {"category": st["category"], "n_for": len(st["for_groups"]), "n_against": len(st["against_groups"]),
                  "sources_for": sorted(st["for"]), "sources_against": sorted(st["against"]),
                  "mean_cred_for": round(sum(kept[s]["credibility"]["total"] for s in st["for"]) / max(1, len(st["for"])), 1),
                  "domains": dict(st["domains"])}
    dom_cov = {d: sorted(s for s, v in kept.items() if d in v["domains"]) for d in DOMAINS}
    (ROOT / "research").mkdir(exist_ok=True)
    json.dump({"claims": out, "domain_coverage": dom_cov,
               "counts": {"collected": len(sources), "kept": len(kept), "advice": len(advice),
                          "quotes_unverified": len(bad)}},
              open(ROOT / "research" / "claim_stats.json", "w"), indent=1, sort_keys=True)

    write_sources_md(sources, dom_cov)
    print(f"sources collected={len(sources)} kept={len(kept)} advice={len(advice)} unverified_quotes={len(bad)}")
    for d, ids in dom_cov.items():
        print(f"  {d:22s} {len(ids)}")
    for sid, q in bad:
        print("UNVERIFIED", sid, q[:90])


def write_sources_md(sources, dom_cov):
    kept = [s for s in sources if s["kept"]]
    rej = [s for s in sources if not s["kept"]]
    L = ["# Sources reviewed for the SWE resume-advice corpus", "",
         f"Collected **{len(sources)}** candidate sources; kept **{len(kept)}** after credibility scoring; "
         f"rejected **{len(rej)}**. Machine-readable rows: `corpus/sources.jsonl`; claims: `corpus/advice.jsonl`.", "",
         "## Scoring rubric (0-10)", "",
         "| Dimension | 0 | 1 | 2 | 3 |", "|---|---|---|---|---|",
         "| role | unknown/SEO | community, aggregator | engineer-interviewer, career center, domain vendor, coach | recruiter / hiring manager / company official / rigorous study |",
         "| outcome | none | anecdotal or secondary | author screens or hires for the role | outcome data (interview/hire results) or hires at scale |",
         "| recency | pre-2024 | 2024 or undated live page | 2025-2026 | |",
         "| validation | none | moderate (50-500 votes, some citations) | widely cited, >500 votes, peer-reviewed | |", "",
         "Keep rule: total >= 5, dated 2024+ unless `foundational`, and contains resume-screening advice. "
         "Foundational pre-2024 sources (Ladders 2018 eye-tracking, Bock's XYZ formula, Orosz's *Tech Resume Inside Out*, "
         "McDowell, YC's Work-at-a-Startup posts) are marked with (F). Sources sharing an author/org are grouped for "
         "independence counting (column *group*).", "",
         "## Kept sources", "",
         "| id | title | date | author role | domains | cred | group |", "|---|---|---|---|---|---|---|"]
    for s in sorted(kept, key=lambda s: (-s["credibility"]["total"], s["id"])):
        f = " (F)" if s["foundational"] else ""
        L.append(f"| {s['id']} | [{s['title'].replace('|', '/')}]({s['url']}){f} | {s['date']} | {s['author_role']} | "
                 f"{', '.join(s['domains'])} | {s['credibility']['total']} | {s['independence_group']} |")
    L += ["", "## Domain coverage (kept sources tagged with each domain)", "", "| domain | n | sources |", "|---|---|---|"]
    for d, ids in dom_cov.items():
        L.append(f"| {d} | {len(ids)} | {', '.join(ids)} |")
    L += ["", "## Rejected sources", "", "| id | title / url | date | reason |", "|---|---|---|---|"]
    for s in sorted(rej, key=lambda s: s["reject_reason"]):
        t = (s["title"] or s["url"]).replace("|", "/")[:110]
        link = f"[{t}]({s['url']})" if s["url"] else t
        L.append(f"| {s['id']} | {link} | {s['date']} | {s['reject_reason']} |")
    (ROOT / "research" / "sources.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
