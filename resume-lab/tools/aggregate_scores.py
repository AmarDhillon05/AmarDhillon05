#!/usr/bin/env python3
"""Aggregate reviewer JSON for one round and check stop criteria.

Layout: scores/<variant>/round_NN/reviews/<persona>.json  (schema: eval/review_schema.json)
usage: aggregate_scores.py scores/<variant>/round_NN [--rubric research/rubric.yaml]

Writes round_NN/summary.json + summary.md and appends to scores/history.csv.
Stop criteria (thresholds read from rubric.yaml `pass:` block):
  every reviewer >= min_dim on every dimension, mean overall >= min_overall_mean,
  no must_fix items, and lint+fact_check clean (round_NN/gate.json).
"""
import argparse
import csv
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("round_dir")
    ap.add_argument("--rubric", default=str(ROOT / "research" / "rubric.yaml"))
    args = ap.parse_args()

    rd = Path(args.round_dir)
    variant, rnd = rd.parent.name, rd.name
    rubric = yaml.safe_load(Path(args.rubric).read_text()) if Path(args.rubric).exists() else {}
    thr = {"min_dim": 8, "min_overall_mean": 8.5, **(rubric.get("pass") or {})}

    reviews = [json.loads(p.read_text()) for p in sorted((rd / "reviews").glob("*.json"))]
    if not reviews:
        sys.exit(f"no reviews in {rd}/reviews")
    dims = sorted({d for r in reviews for d in r["scores"]})
    per_dim = {d: [r["scores"][d] for r in reviews if d in r["scores"]] for d in dims}
    overall = [r["scores"].get("overall") for r in reviews if r["scores"].get("overall") is not None]
    must_fix = [(r["persona"], m) for r in reviews for m in r.get("must_fix", [])]
    low = [(r["persona"], d, v) for r in reviews for d, v in r["scores"].items() if v < thr["min_dim"]]
    gate = json.loads((rd / "gate.json").read_text()) if (rd / "gate.json").exists() else {"errors": None}

    # bullet verdict consensus
    verdicts = defaultdict(Counter)
    for r in reviews:
        for b in r.get("bullets", []):
            key = b.get("fact") or " ".join(b.get("quote", "?").split()[:5])
            verdicts[key][b.get("verdict", "?")] += 1
    structure = Counter()
    for r in reviews:
        for s in r.get("structure", []):
            structure[s.get("key") or s.get("change", "")[:60]] += 1

    passed = (not low and not must_fix and overall and statistics.mean(overall) >= thr["min_overall_mean"]
              and gate.get("errors") == 0)
    summary = {
        "variant": variant, "round": rnd, "n_reviewers": len(reviews),
        "mean_by_dim": {d: round(statistics.mean(v), 2) for d, v in per_dim.items()},
        "min_by_dim": {d: min(v) for d, v in per_dim.items()},
        "overall_mean": round(statistics.mean(overall), 2) if overall else None,
        "below_threshold": low, "must_fix": must_fix, "gate_errors": gate.get("errors"),
        "bullet_verdicts": {k: dict(v) for k, v in verdicts.items()},
        "structure_votes": dict(structure.most_common()),
        "competitive": {r["persona"]: r.get("competitive_for_domain") for r in reviews},
        "passed": bool(passed), "thresholds": thr,
    }
    (rd / "summary.json").write_text(json.dumps(summary, indent=2))

    md = [f"# {variant} / {rnd}", "", f"**passed:** {passed}  |  overall mean {summary['overall_mean']}  |  gate errors {gate.get('errors')}", "",
          "| dim | mean | min |", "|---|---|---|"]
    md += [f"| {d} | {summary['mean_by_dim'][d]} | {summary['min_by_dim'][d]} |" for d in dims]
    md += ["", "## Must-fix"] + [f"- ({p}) {m}" for p, m in must_fix] or ["- none"]
    md += ["", "## Bullet verdicts"] + [f"- `{k}`: {dict(v)}" for k, v in verdicts.items()]
    md += ["", "## Structure votes"] + [f"- {k}: {v}" for k, v in structure.most_common()]
    (rd / "summary.md").write_text("\n".join(md) + "\n")

    hist = ROOT / "scores" / "history.csv"
    new = not hist.exists()
    with hist.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["variant", "round", "n_reviewers", "overall_mean", "min_any_dim", "n_must_fix", "gate_errors", "passed"] + [f"mean_{d}" for d in dims])
        w.writerow([variant, rnd, len(reviews), summary["overall_mean"],
                    min(min(v) for v in per_dim.values()), len(must_fix), gate.get("errors"), passed]
                   + [summary["mean_by_dim"].get(d) for d in dims])
    print((rd / "summary.md").read_text())


if __name__ == "__main__":
    main()
