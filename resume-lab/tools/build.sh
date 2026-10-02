#!/usr/bin/env bash
# Build one or more .tex resumes and run the deterministic gate on each.
# usage: tools/build.sh path/to/resume.tex [...]   (outputs next to the .tex)
set -uo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
status=0
for tex in "$@"; do
  dir="$(cd "$(dirname "$tex")" && pwd)"; base="$(basename "$tex" .tex)"
  ( cd "$dir" && pdflatex -interaction=nonstopmode -halt-on-error "$base.tex" >"$base.build.log" 2>&1 )
  if [ $? -ne 0 ]; then
    echo "BUILD FAILED: $tex"; grep -m5 -A2 '^!' "$dir/$base.build.log"; status=1; continue
  fi
  grep -q 'Overfull \\hbox' "$dir/$base.build.log" && echo "[WARN] overfull hbox in $tex"
  pdftotext -layout "$dir/$base.pdf" "$dir/$base.txt"
  rm -f "$dir/$base".{aux,out}
  echo "== $tex"
  python3 "$here/lint.py" "$dir/$base.tex" --json "$dir/$base.lint.json" ${LINT_ARGS:-} || status=1
  python3 "$here/fact_check.py" "$dir/$base.tex" --json "$dir/$base.facts.json" || status=1
done
exit $status
