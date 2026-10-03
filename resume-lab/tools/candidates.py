#!/usr/bin/env python3
"""Blind incumbent-vs-candidates judging for loop 2 (spec §9).

make : candidates.py make <cands.yaml> <out_dir>
       cands.yaml: {fact_id: {incumbent: "...", candidates: ["...", "..."]}}
       -> out_dir/pairs.json (versions shuffled under labels A, B, C...) + key.json
score: candidates.py score <out_dir>   (reads out_dir/judgments.json written by the judge)
       A candidate is adopted only if it wins with advantage == "concrete"; otherwise the
       incumbent stays (spec §19: the incumbent remains until clearly beaten).
"""
import json
import random
import sys
from pathlib import Path

import yaml

if sys.argv[1] == "make":
    spec = yaml.safe_load(Path(sys.argv[2]).read_text())
    out = Path(sys.argv[3]); out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(sum(map(ord, sys.argv[3])))
    pairs, key = [], {}
    for n, (fid, d) in enumerate(spec.items(), 1):
        versions = [("incumbent", d["incumbent"])] + [(f"cand{i+1}", c) for i, c in enumerate(d["candidates"])]
        rng.shuffle(versions)
        labels = "ABCDE"
        gid = f"g{n:02d}"
        pairs.append({"id": gid, "versions": {labels[i]: t for i, (_, t) in enumerate(versions)}})
        key[gid] = {"fact": fid, "labels": {labels[i]: name for i, (name, _) in enumerate(versions)},
                    "texts": {name: t for name, t in versions}}
    (out / "pairs.json").write_text(json.dumps(pairs, indent=2))
    (out / "key.json").write_text(json.dumps(key, indent=2))
    print(f"{len(pairs)} groups -> {out}")
else:
    out = Path(sys.argv[2])
    key = json.loads((out / "key.json").read_text())
    j = {x["id"]: x for x in json.loads((out / "judgments.json").read_text())}
    res = []
    for gid, k in key.items():
        v = j.get(gid, {})
        w = k["labels"].get(v.get("winner"), "tie")
        adopt = w.startswith("cand") and v.get("advantage") == "concrete"
        res.append({"fact": k["fact"], "winner": w, "advantage": v.get("advantage"), "adopt": adopt,
                    "text": k["texts"][w] if adopt else k["texts"]["incumbent"],
                    "decisive_wording": v.get("decisive_wording", ""), "info": v.get("info_preserved_or_lost", "")})
    (out / "result.json").write_text(json.dumps(res, indent=2))
    for r in res:
        print(f"{'ADOPT ' if r['adopt'] else 'keep  '} {r['fact']}: {r['winner']} ({r['advantage']}) {r['decisive_wording'][:90]}")
