#!/usr/bin/env python3
"""Snapshot a resume version into scores/<variant>/round_NN/, build it, run the
gate, and render review inputs (PDF, PNG, layout text).

usage: prepare_round.py <variant> <path/to/resume.tex> <round_number>
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    variant, tex, n = sys.argv[1], Path(sys.argv[2]), int(sys.argv[3])
    rd = ROOT / "scores" / variant / f"round_{n:02d}"
    (rd / "reviews").mkdir(parents=True, exist_ok=True)
    dst = rd / "resume.tex"
    shutil.copy(tex, dst)
    r = subprocess.run([str(ROOT / "tools" / "build.sh"), str(dst)], capture_output=True, text=True)
    (rd / "gate.txt").write_text(r.stdout + r.stderr)
    lint = json.loads((rd / "resume.lint.json").read_text()) if (rd / "resume.lint.json").exists() else {"errors": 99}
    facts = json.loads((rd / "resume.facts.json").read_text()) if (rd / "resume.facts.json").exists() else {"errors": 99}
    gate = {"errors": lint["errors"] + facts["errors"], "lint_errors": lint["errors"],
            "fact_errors": facts["errors"], "warnings": lint.get("warnings", 0) + facts.get("warnings", 0)}
    (rd / "gate.json").write_text(json.dumps(gate, indent=2))
    if (rd / "resume.pdf").exists():
        subprocess.run(["pdftoppm", "-png", "-r", "110", "-singlefile", str(rd / "resume.pdf"), str(rd / "resume")])
    for junk in ("resume.log", "resume.build.log"):
        (rd / junk).unlink(missing_ok=True)
    print(r.stdout)
    print(f"gate: {gate}  ->  {rd}")


if __name__ == "__main__":
    main()
