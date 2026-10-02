#!/usr/bin/env python3
"""Render a reviewer-agent prompt.
usage: reviewer_prompt.py <persona_id> <variant> <round_number> "<target description>"
Persona text comes from eval/reviewer_prompts/<persona_id>.md; template from _base.md."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
persona, variant, n, target = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
rd = ROOT / "scores" / variant / f"round_{n:02d}"
tpl = (ROOT / "eval" / "reviewer_prompts" / "_base.md").read_text()
subs = {"{PERSONA}": (ROOT / "eval" / "reviewer_prompts" / f"{persona}.md").read_text().strip(),
        "{PERSONA_ID}": persona, "{TARGET}": target, "{PNG}": str(rd / "resume.png"),
        "{TXT}": str(rd / "resume.txt"), "{RUBRIC}": str(ROOT / "research" / "rubric.yaml"),
        "{OUT}": str(rd / "reviews" / f"{persona}.json")}
for k, v in subs.items():
    tpl = tpl.replace(k, v)
print(tpl)
