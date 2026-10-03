#!/usr/bin/env python3
"""Render a reviewer-agent prompt.
usage: reviewer_prompt.py <persona_id> <variant> <round_number> "<target description>"
Persona text comes from eval/reviewer_prompts/<persona_id>.md; template from _base.md
(_base_v2.md for loop-2 personas, *_v2). Loop-2 variants live under scores/loop2/<name>."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
persona, variant, n, target = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
rd = ROOT / "scores" / variant / f"round_{n:02d}"
v2 = persona.endswith("_v2")
tpl = (ROOT / "eval" / "reviewer_prompts" / ("_base_v2.md" if v2 else "_base.md")).read_text()
JD = {"base": "general_backend", "infra_distributed": "infra_distributed", "systems_quant": "systems_quant",
      "ai_ml_engineering": "ai_ml_engineering"}
jd_name = JD.get(Path(variant).name, "general_backend")
subs = {"{PERSONA}": (ROOT / "eval" / "reviewer_prompts" / f"{persona}.md").read_text().strip(),
        "{PERSONA_ID}": persona, "{TARGET}": target, "{PNG}": str(rd / "resume.png"),
        "{TXT}": str(rd / "resume.txt"), "{RUBRIC}": str(ROOT / "research" / "rubric.yaml"),
        "{OUT}": str(rd / "reviews" / f"{persona}.json"),
        "{JDS}": str(ROOT / "corpus" / "jds" / f"{jd_name}.jsonl")}
for k, v in subs.items():
    tpl = tpl.replace(k, v)
print(tpl)
