#!/usr/bin/env python3
"""Quantitative profile of the resume corpus vs. Amar's resume.

Inputs : corpus/github_bullets.jsonl, corpus/github_resumes.jsonl,
         corpus/outcome_resumes.jsonl, a resume .lint.json (for comparison)
Output : research/corpus_stats.md and research/corpus_stats.json

Recency weighting: rows dated 2025+ count 2x, 2024 counts 1x, older excluded.
Every stat is reported overall, for "top" rows (top-tier companies / top outcomes),
and per domain.
"""
import json
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TECH_HINT = re.compile(r"\b[A-Z][A-Za-z0-9+#.]*(?:\.js)?\b")


def load(p):
    p = ROOT / p
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []


def weight(date):
    y = int(str(date)[:4]) if date and str(date)[:4].isdigit() else 0
    return 2 if y >= 2025 else 1 if y == 2024 else 0


def wquantiles(vals_w, qs=(0.25, 0.5, 0.75)):
    xs = sorted((v, w) for v, w in vals_w if w > 0)
    if not xs:
        return [None] * len(qs)
    tot = sum(w for _, w in xs)
    out = []
    for q in qs:
        acc = 0
        for v, w in xs:
            acc += w
            if acc >= q * tot:
                out.append(v)
                break
    return out


def wmean(vals_w):
    tot = sum(w for _, w in vals_w)
    return round(sum(v * w for v, w in vals_w) / tot, 3) if tot else None


def bullets_all():
    rows = []
    res = {r["id"]: r for r in load("corpus/github_resumes.jsonl")}
    for b in load("corpus/github_bullets.jsonl"):
        r = res.get(b.get("resume_id"), {})
        rows.append({**b, "src": "github", "date": b.get("last_modified") or r.get("last_modified"),
                     "top": bool(r.get("top_tier_signal")) or b.get("company_tier") in ("top", "faang", "quant"),
                     "domains": [b.get("domain")] if b.get("domain") else r.get("domains", [])})
    for r in load("corpus/outcome_resumes.jsonl"):
        for b in r.get("bullets", []):
            rows.append({**b, "src": "outcome", "resume_id": r["id"], "date": r.get("date"),
                         "top": r.get("outcome_tier") == "top", "domains": r.get("domains", [])})
    for b in rows:
        t = b.get("text", "")
        b.setdefault("chars", len(t))
        b["words"] = b.get("words") or len(t.split())
        if "has_metric" not in b:
            b["has_metric"] = bool(re.search(r"\d", t))
        b["n_tech"] = len(b.get("techs") or []) or len(set(TECH_HINT.findall(" ".join(t.split()[1:]))))
        b["w"] = weight(b["date"])
    return [b for b in rows if b["w"] > 0 and b.get("text")]


def profile(rows):
    if not rows:
        return {}
    cw = [(b["chars"], b["w"]) for b in rows]
    per_resume = defaultdict(lambda: [0, 0])
    for b in rows:
        per_resume[b["resume_id"]][0] += 1
        per_resume[b["resume_id"]][1] = b["w"]
    verbs = Counter()
    for b in rows:
        v = (b.get("leading_verb") or b["text"].split()[0]).strip(",.").lower()
        verbs[v] += b["w"]
    return {
        "n_bullets": len(rows),
        "n_resumes": len(per_resume),
        "chars_q25_q50_q75": wquantiles(cw),
        "words_median": wquantiles([(b["words"], b["w"]) for b in rows], (0.5,))[0],
        "pct_with_metric": wmean([(1 if b["has_metric"] else 0, b["w"]) for b in rows]),
        "techs_per_bullet_mean": wmean([(b["n_tech"], b["w"]) for b in rows]),
        "bold_per_bullet_mean": wmean([(len(b.get("bold_phrases") or []), b["w"]) for b in rows if "bold_phrases" in b]),
        "pct_bullets_with_any_bold": wmean([(1 if b.get("bold_phrases") else 0, b["w"]) for b in rows if "bold_phrases" in b]),
        "bullets_per_resume_median": wquantiles([(n, w) for n, w in per_resume.values()], (0.5,))[0],
        "pct_has_context": wmean([(1 if b.get("has_context") else 0, b["w"]) for b in rows if "has_context" in b]),
        "pct_has_result": wmean([(1 if b.get("has_result") else 0, b["w"]) for b in rows if "has_result" in b]),
        "top_leading_verbs": verbs.most_common(20),
    }


def section_orders():
    orders = Counter()
    for r in load("corpus/github_resumes.jsonl") + load("corpus/outcome_resumes.jsonl"):
        w = weight(r.get("last_modified") or r.get("date"))
        if w and r.get("section_order"):
            orders[" > ".join(s.lower()[:14] for s in r["section_order"][:6])] += w
    return orders.most_common(12)


def main():
    rows = bullets_all()
    out = {"overall": profile(rows), "top": profile([b for b in rows if b["top"]]),
           "by_source": {s: profile([b for b in rows if b["src"] == s]) for s in ("github", "outcome")},
           "by_domain": {}, "section_orders": section_orders()}
    doms = Counter(d for b in rows for d in (b["domains"] or []))
    for d, _ in doms.most_common():
        out["by_domain"][d] = profile([b for b in rows if d in (b["domains"] or [])])
    mine = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / "resume" / "baseline.lint.json")
    if Path(mine).exists():
        m = json.loads(Path(mine).read_text())["bullets"]
        out["amar"] = {"n_bullets": len(m), "chars_q25_q50_q75": [sorted(b["chars"] for b in m)[int(len(m) * q)] for q in (0.25, 0.5, 0.75)],
                       "bold_per_bullet_mean": round(statistics.mean(b["n_bold"] for b in m), 2),
                       "lines_per_bullet_mean": round(statistics.mean(b["n_lines"] or 0 for b in m), 2),
                       "pct_with_metric": round(sum(bool(re.search(r"\d", b["text"])) for b in m) / len(m), 2)}
    (ROOT / "research" / "corpus_stats.json").write_text(json.dumps(out, indent=2))

    def row(name, p):
        if not p:
            return f"| {name} | – |"
        return (f"| {name} | {p['n_resumes']} / {p['n_bullets']} | {p['chars_q25_q50_q75']} | {p['words_median']} | "
                f"{p['pct_with_metric']} | {p['techs_per_bullet_mean']} | {p.get('bold_per_bullet_mean')} | {p['bullets_per_resume_median']} |")
    md = ["# Corpus statistics (recency-weighted: 2025+ ×2, 2024 ×1, older excluded)", "",
          "| slice | resumes / bullets | chars q25/q50/q75 | words med | % metric | techs/bullet | bold/bullet | bullets/resume |",
          "|---|---|---|---|---|---|---|---|", row("ALL", out["overall"]), row("top-tier/top-outcome", out["top"])]
    md += [row(f"src:{k}", v) for k, v in out["by_source"].items()]
    md += [row(f"domain:{k}", v) for k, v in out["by_domain"].items()]
    if "amar" in out:
        a = out["amar"]
        md += ["", f"**Amar (baseline):** {a['n_bullets']} bullets, chars q25/q50/q75 {a['chars_q25_q50_q75']}, "
               f"bold/bullet {a['bold_per_bullet_mean']}, rendered lines/bullet {a['lines_per_bullet_mean']}, % metric {a['pct_with_metric']}"]
    md += ["", "## Top leading verbs (all)", ", ".join(f"{v} ({c})" for v, c in out["overall"].get("top_leading_verbs", []))]
    md += ["", "## Most common section orders"] + [f"- {o} ({c})" for o, c in out["section_orders"]]
    (ROOT / "research" / "corpus_stats.md").write_text("\n".join(md) + "\n")
    print("\n".join(md))


if __name__ == "__main__":
    main()
