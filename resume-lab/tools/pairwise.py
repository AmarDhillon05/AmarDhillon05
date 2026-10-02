#!/usr/bin/env python3
"""Blind pairwise bullet judging.
make : pairwise.py make old.tex new.tex out_dir   -> out_dir/pairs.json (shuffled A/B) + key.json
score: pairwise.py score out_dir                 -> reads out_dir/judgments.json, prints wins per side
Pairs are matched by `% fact:` id; identical bullets are skipped."""
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import texparse  # noqa: E402


def bullets(p):
    return {b.fact_id: b.text for b in texparse.parse(Path(p).read_text()) if b.fact_id and b.fact_id != "skills"}


if sys.argv[1] == "make":
    old, new, out = bullets(sys.argv[2]), bullets(sys.argv[3]), Path(sys.argv[4])
    out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(len(old) * 7919 + len(new))
    pairs, key = [], {}
    for fid in sorted(set(old) & set(new)):
        if old[fid] == new[fid]:
            continue
        flip = rng.random() < 0.5
        a, b = (new[fid], old[fid]) if flip else (old[fid], new[fid])
        pid = f"p{len(pairs) + 1:02d}"
        pairs.append({"id": pid, "A": a, "B": b})
        key[pid] = {"fact": fid, "new_is": "A" if flip else "B"}
    (out / "pairs.json").write_text(json.dumps(pairs, indent=2))
    (out / "key.json").write_text(json.dumps(key, indent=2))
    print(f"{len(pairs)} pairs -> {out}")
else:
    out = Path(sys.argv[2])
    key = json.loads((out / "key.json").read_text())
    j = {x["id"]: x for x in json.loads((out / "judgments.json").read_text())}
    tally = {"new": 0, "old": 0, "tie": 0}
    rows = []
    for pid, k in key.items():
        w = j.get(pid, {}).get("winner", "tie")
        side = "tie" if w == "tie" else ("new" if w == k["new_is"] else "old")
        tally[side] += 1
        rows.append({"fact": k["fact"], "winner": side, "reason": j.get(pid, {}).get("reason", "")})
    (out / "result.json").write_text(json.dumps({"tally": tally, "rows": rows}, indent=2))
    print(tally)
    for r in rows:
        print(f"  {r['winner']:4} {r['fact']}: {r['reason'][:110]}")
