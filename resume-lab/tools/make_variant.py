#!/usr/bin/env python3
"""Derive a domain variant from the base resume by fact-id operations.

usage: make_variant.py <spec.yaml>

spec keys (all optional except base/out):
  base: resume/resume.tex
  out:  resume/quant.tex
  projects_first: true          # move the Projects section above Experience
  drop: [fact.id, ...]          # remove bullets
  text: {fact.id: "new text"}   # override bullet text (LaTeX)
  order: {first.fact.id: [ids in desired order within that role list]}
  add_after: {existing.fact.id: [{fact: new.id, text: "..."}]}
  retag: {old.id: "a.b+c.d"}    # change a bullet's fact annotation (e.g. after merging)
  skills: ["\\textbf{Row:} a, b", ...]   # replace the skills rows
  extra_roles: ["<raw \\resumeSubheading ... \\resumeItemListEnd block>"]  # appended at the end of Experience
Every bullet keeps its `% fact:` annotation, so tools/fact_check.py still applies.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BUL = re.compile(r"(?P<ind>[ \t]*)% fact: (?P<id>\S+)\n[ \t]*\\resumeItem\{(?P<txt>.*)\}\n")


def main():
    spec = yaml.safe_load(Path(sys.argv[1]).read_text())
    s = (ROOT / spec.get("base", "resume/resume.tex")).read_text()

    for fid in spec.get("drop", []):
        s, n = re.subn(rf"[ \t]*% fact: {re.escape(fid)}\n[ \t]*\\resumeItem\{{.*\}}\n", "", s)
        assert n == 1, f"drop: {fid} not found"

    for fid, txt in (spec.get("text") or {}).items():
        m = next((m for m in BUL.finditer(s) if m.group("id") == fid), None)
        assert m, f"text: {fid} not found"
        s = s[:m.start("txt")] + txt + s[m.end("txt"):]

    for anchor, items in (spec.get("add_after") or {}).items():
        m = next((m for m in BUL.finditer(s) if m.group("id") == anchor), None)
        assert m, f"add_after: {anchor} not found"
        ind = m.group("ind")
        block = "".join(f"{ind}% fact: {it['fact']}\n{ind}\\resumeItem{{{it['text']}}}\n" for it in items)
        s = s[:m.end()] + block + s[m.end():]

    for _, ids in (spec.get("order") or {}).items():
        ms = [m for m in BUL.finditer(s) if m.group("id") in ids]
        assert len(ms) == len(ids), f"order: missing some of {ids}"
        by_id = {m.group("id"): m.group(0) for m in ms}
        start, end = ms[0].start(), ms[-1].end()
        assert s[start:end].count("% fact:") == len(ids), f"order: {ids} are not one contiguous list"
        s = s[:start] + "".join(by_id[i] for i in ids) + s[end:]

    for old, new in (spec.get("retag") or {}).items():
        assert f"% fact: {old}\n" in s, f"retag: {old} not found"
        s = s.replace(f"% fact: {old}\n", f"% fact: {new}\n")

    for block in spec.get("extra_roles") or []:
        exp = s.index("\\section{Experience}")
        end = s.index("\\resumeSubHeadingListEnd", exp)
        s = s[:end] + block.rstrip("\n") + "\n\n" + s[end:]

    if spec.get("projects_first"):
        pm = re.search(r"%-----------PROJECTS-----------\n.*?(?=%-----------SKILLS)", s, re.S)
        proj = pm.group(0)
        s = s[:pm.start()] + s[pm.end():]
        s = s.replace("%-----------EXPERIENCE-----------", proj + "%-----------EXPERIENCE-----------", 1)

    if spec.get("skills"):
        sm = re.search(r"(\\section\{Technical Skills\}\n\\begin\{itemize\}\[[^\]]*\]\n\s*\\small\n)(.*?)(\\end\{itemize\})", s, re.S)
        rows = "".join(f"  % fact: skills\n  \\item{{{r}}}\n" for r in spec["skills"])
        s = s[:sm.start(2)] + rows + s[sm.end(2):]

    out = ROOT / spec["out"]
    out.write_text(s)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
