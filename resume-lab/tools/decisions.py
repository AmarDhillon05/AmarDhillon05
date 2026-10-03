#!/usr/bin/env python3
"""Version history for loop 2 (spec §20): every proposed bullet change and its outcome.

usage: decisions.py add <variant> <round> <fact_id> <accepted|rejected> "<incumbent>" "<candidate>" "<reason>" "<evidence>"
       decisions.py rejected <fact_id>      -> previously rejected candidates (don't re-propose)
Appends to eval/loop2/decisions.jsonl.
"""
import json
import sys
from pathlib import Path

LOG = Path(__file__).resolve().parent.parent / "eval" / "loop2" / "decisions.jsonl"

if sys.argv[1] == "add":
    variant, rnd, fact, outcome, inc, cand, reason, evidence = sys.argv[2:10]
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG, "a") as f:
        f.write(json.dumps({"variant": variant, "round": int(rnd), "fact": fact, "outcome": outcome,
                            "incumbent": inc, "candidate": cand, "reason": reason, "evidence": evidence}) + "\n")
else:
    for l in (LOG.read_text().splitlines() if LOG.exists() else []):
        d = json.loads(l)
        if d["fact"] == sys.argv[2] and d["outcome"] == "rejected":
            print(f"[{d['variant']} r{d['round']}] {d['candidate']}  -- {d['reason']}")
