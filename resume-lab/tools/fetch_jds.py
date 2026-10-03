#!/usr/bin/env python3
"""Fetch current intern / new-grad SWE job postings from public job-board APIs.

usage: fetch_jds.py            -> corpus/jds/<variant>.jsonl  (+ corpus/jds/README.md counts)
Boards: Greenhouse (boards-api.greenhouse.io), Lever (api.lever.co), Ashby (api.ashbyhq.com).
A posting goes to a variant by title keywords first, then by the company's default variant.
Only postings whose title says intern / new grad / university / early career / graduate AND
software / engineer / developer are kept; at most PER_VARIANT per variant, newest first.
"""
import html
import json
import re
import time
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "corpus/jds"
PER_VARIANT = 30

BOARDS = {  # (kind, token): default variant
    ("gh", "stripe"): "general_backend", ("gh", "robinhood"): "general_backend", ("gh", "figma"): "general_backend",
    ("gh", "pinterest"): "general_backend", ("gh", "coinbase"): "general_backend", ("gh", "affirm"): "general_backend",
    ("gh", "lyft"): "general_backend", ("ashby", "ramp"): "general_backend", ("ashby", "notion"): "general_backend",
    ("lever", "palantir"): "general_backend",
    ("gh", "databricks"): "infra_distributed", ("gh", "datadog"): "infra_distributed",
    ("gh", "cloudflare"): "infra_distributed", ("gh", "elastic"): "infra_distributed",
    ("gh", "jumptrading"): "systems_quant", ("gh", "imc"): "systems_quant", ("gh", "drweng"): "systems_quant",
    ("gh", "akunacapital"): "systems_quant", ("gh", "virtu"): "systems_quant", ("gh", "point72"): "systems_quant",
    ("gh", "scaleai"): "ai_ml_engineering", ("ashby", "openai"): "ai_ml_engineering",
    ("ashby", "perplexity"): "ai_ml_engineering",
}
TITLE_VARIANT = [
    (r"machine learning|\bml\b|\bai\b|llm|applied (ai|ml)|inference|model", "ai_ml_engineering"),
    (r"low.?latency|\bc\+\+|trading|quant|hft|execution", "systems_quant"),
    (r"infra|platform|distributed|reliability|\bsre\b|cloud|storage|systems|devops|database", "infra_distributed"),
]
LEVEL = re.compile(r"\bintern(ship)?\b|new grad|university|early career|graduate|campus", re.I)
SWE = re.compile(r"software|engineer|developer", re.I)
NOT_SWE = re.compile(r"hardware|mechanical|electrical|fpga|asic|sales|recruit|account|legal|design(er)?\b|finance|trader\b|"
                     r"research scientist|senior|staff|principal|manager|\bios\b|android|\bux\b|frontend|ui software|"
                     r"high school|industrialization|analytics|c# |\bit engineer|phd", re.I)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "resume-lab/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def text(h):
    h = html.unescape(h or "")
    h = re.sub(r"<(br|/p|/li|/h\d)[^>]*>", "\n", h)
    return re.sub(r"[ \t]+", " ", re.sub(r"<[^>]+>", " ", h)).strip()


def postings(kind, token):
    if kind == "gh":
        for j in get(f"https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true")["jobs"]:
            yield j["title"], text(j.get("content")), j.get("updated_at", ""), j.get("absolute_url", "")
    elif kind == "lever":
        for j in get(f"https://api.lever.co/v0/postings/{token}?mode=json"):
            body = j.get("descriptionPlain", "") + "\n" + "\n".join(
                f"{l.get('text','')}\n{text(l.get('content'))}" for l in j.get("lists", []))
            ts = j.get("createdAt")
            date = time.strftime("%Y-%m-%d", time.gmtime(ts / 1000)) if ts else ""
            yield j["text"], body, date, j.get("hostedUrl", "")
    else:
        for j in get(f"https://api.ashbyhq.com/posting-api/job-board/{token}")["jobs"]:
            yield j["title"], j.get("descriptionPlain") or text(j.get("descriptionHtml")), j.get("publishedAt", ""), j.get("jobUrl", "")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    by_var = defaultdict(list)
    for (kind, token), default in BOARDS.items():
        try:
            items = list(postings(kind, token))
        except Exception as e:  # board moved / rate-limited: skip, record in README
            print(f"skip {kind}:{token}: {e}"); continue
        for title, body, date, url in items:
            if not (LEVEL.search(title) and SWE.search(title)) or NOT_SWE.search(title) or len(body) < 400:
                continue
            var = next((v for rx, v in TITLE_VARIANT if re.search(rx, title, re.I)), default)
            by_var[var].append({"company": token, "title": title, "date": date[:10], "url": url, "text": body})
    lines = ["# Job postings used for ATS keyword scoring", "",
             "Fetched by `tools/fetch_jds.py` from public Greenhouse, Lever and Ashby job-board APIs.", "",
             "| variant | postings | companies |", "|---|---|---|"]
    for var, rows in sorted(by_var.items()):
        seen, keep = set(), []
        for r in sorted(rows, key=lambda r: r["date"], reverse=True):
            k = (r["company"], re.sub(r"\W+", " ", re.sub(r"\s[-–(].*$", "", r["title"].lower())).strip())
            if k not in seen:
                seen.add(k); keep.append(r)
        keep = keep[:PER_VARIANT]
        with open(OUT / f"{var}.jsonl", "w") as f:
            for r in keep:
                f.write(json.dumps(r) + "\n")
        lines.append(f"| {var} | {len(keep)} | {', '.join(sorted({r['company'] for r in keep}))} |")
        print(var, len(keep))
    (OUT / "README.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
