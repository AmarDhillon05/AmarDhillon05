#!/usr/bin/env python3
"""Aggregate loop-2 reviews (scores/loop2/<variant>/round_NN/reviews/*_v2.json).

usage: aggregate_v2.py <variant> <round>   -> summary.md + summary.json in the round dir
Groups bullet feedback by bullet (fuzzy first-40-chars key) so cross-evaluator agreement is
visible (spec §8): an issue raised by >= 2 evaluators, or one severity >= 8, is "priority".
Also reports the recruiter's memory skim and plain-English comprehension rate.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def key(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())[:40]


def main():
    variant, n = sys.argv[1], int(sys.argv[2])
    rd = ROOT / "scores" / "loop2" / variant / f"round_{n:02d}"
    revs = [json.loads(p.read_text()) for p in sorted((rd / "reviews").glob("*.json"))]
    dims = list(revs[0]["scores"])
    mean = {d: round(sum(r["scores"][d] for r in revs) / len(revs), 2) for d in dims}
    mins = {d: min(r["scores"][d] for r in revs) for d in dims}
    by_bullet = defaultdict(list)
    for r in revs:
        for f in r.get("bullet_feedback", []):
            by_bullet[key(f["bullet"])].append({**f, "persona": r["persona"]})
    groups = []
    for k, fs in by_bullet.items():
        personas = sorted({f["persona"] for f in fs})
        top = max(f.get("severity", 5) for f in fs)
        groups.append({"bullet": fs[0]["bullet"], "n_evaluators": len(personas), "max_severity": top,
                       "priority": len(personas) >= 2 or top >= 8, "feedback": fs})
    groups.sort(key=lambda g: (-g["priority"], -g["n_evaluators"], -g["max_severity"]))
    rec = next((r for r in revs if r["persona"].startswith("recruiter")), None)
    pe = rec.get("plain_english", []) if rec else []
    understood = sum(bool(x.get("understood")) for x in pe)
    page = [{**f, "persona": r["persona"]} for r in revs for f in r.get("page_feedback", [])]
    out = {"variant": variant, "round": n, "n_reviews": len(revs), "mean": mean, "min": mins,
           "plain_english": f"{understood}/{len(pe)}", "memory_skim": rec.get("memory_skim") if rec else None,
           "bullet_groups": groups, "page_feedback": sorted(page, key=lambda f: -f.get("severity", 5)),
           "keep": {r["persona"]: r.get("keep", []) for r in revs},
           "competitive": {r["persona"]: r.get("competitive_for_domain") for r in revs}}
    (rd / "summary.json").write_text(json.dumps(out, indent=2))
    L = [f"# Loop 2 · {variant} · round {n:02d} ({len(revs)} evaluators)", "",
         "| dim | mean | min |", "|---|---|---|"] + [f"| {d} | {mean[d]} | {mins[d]} |" for d in dims]
    L += ["", f"**Plain-English restatement (recruiter):** {out['plain_english']} bullets understood",
          f"**Competitive:** {out['competitive']}", "", "## Memory skim (recruiter)", "```", json.dumps(out["memory_skim"], indent=1), "```",
          "", "## Bullet issues (priority = ≥2 evaluators or severity ≥8)"]
    for g in groups:
        L.append(f"\n### {'PRIORITY · ' if g['priority'] else ''}{g['n_evaluators']} evaluators · max sev {g['max_severity']}\n> {g['bullet']}")
        for f in g["feedback"]:
            L.append(f"- **{f['persona']}** (sev {f.get("severity", "?")}): {f['problem']}. *Direction:* {f['suggested_direction']}")
    L += ["", "## Page-level"] + [f"- **{f['persona']}** (sev {f.get("severity", "?")}): {f['problem']}. *Direction:* {f['suggested_direction']}" for f in out["page_feedback"]]
    (rd / "summary.md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:20]))


if __name__ == "__main__":
    main()
