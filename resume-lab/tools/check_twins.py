"""Fail if an original-format twin has drifted from its Jake-format resume.

usage: tools/check_twins.py [resume/<name>.tex ...]   (default: every resume with a twin)
Compares bullets by (fact id, text); order may differ because the twin uses the
original section order, and checks each twin PDF is
newer than both its .tex and the Jake .tex it was generated from.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import texparse

ROOT = Path(__file__).resolve().parent.parent
TWINS = ROOT / "resume" / "original_format"


def bullets(path):
    return [(b.fact_id, b.text) for b in texparse.parse(path.read_text()) if b.fact_id != "skills"]


def skills_rows(path):
    """Twin skills rows are \\resumeItem{Category: items} tagged `% fact: skills`."""
    return [b.text for b in texparse.parse(path.read_text()) if b.fact_id == "skills"]


def norm(s):
    return " ".join(s.replace(":", " ").split())


def check(jake: Path) -> list:
    twin = TWINS / jake.name
    if not twin.exists():
        return [f"{jake.name}: no twin at {twin.relative_to(ROOT)}"]
    errs = []
    a, b = bullets(jake), bullets(twin)
    if len(a) != len(b):
        errs.append(f"{jake.name}: {len(a)} bullets in Jake vs {len(b)} in twin")
    for x in sorted(set(a) - set(b)):
        errs.append(f"{jake.name}: twin lacks bullet  {x[0]} | {x[1]}")
    for y in sorted(set(b) - set(a)):
        errs.append(f"{jake.name}: twin has stale bullet  {y[0]} | {y[1]}")
    jake_text = norm(texparse.document_text(jake.read_text()))
    for row in skills_rows(twin):
        if norm(row) not in jake_text:
            errs.append(f"{jake.name}: twin skills row not in Jake version  {row}")
    pdf = twin.with_suffix(".pdf")
    if not pdf.exists():
        errs.append(f"{jake.name}: twin PDF missing")
    elif pdf.stat().st_mtime < max(twin.stat().st_mtime, jake.stat().st_mtime):
        errs.append(f"{jake.name}: twin PDF is older than its source - rerun tools/to_original_format.py")
    return errs


def main(argv):
    targets = [Path(p).resolve() for p in argv] or sorted(
        ROOT / "resume" / t.name for t in TWINS.glob("*.tex"))
    errs = []
    for t in targets:
        e = check(t)
        errs += e
        if not e:
            print(f"[OK] {t.name}: twin in sync ({len(bullets(t))} bullets)")
    for e in errs:
        print(f"[ERROR] {e}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
