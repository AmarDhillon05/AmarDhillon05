#!/usr/bin/env python3
"""Render a resume variant in the layout of Amar's original .tex ("original-format twin").

usage: to_original_format.py resume/<variant>.tex   -> resume/original_format/<variant>.tex (+ .pdf)

Same preamble, macros, fonts (8.5pt body), header, Education and Certifications blocks as
resume/baseline.tex (the compile-fixed original). Only the words change: role headings,
bullets (with their `% fact:` tags, so fact_check.py still applies) and skills rows come from
the variant. Section order follows the variant (Projects first when the variant leads with it).
Spacing is then fitted (see with_params): spare room is spread over line stretch and bullet/role
gaps up to a cap; an overflow tightens them in small steps. Font size and margins never change.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from texparse import match_brace, strip_iffalse  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "resume/baseline.tex"


def args_after(s, i, n):
    out = []
    for _ in range(n):
        k = s.index("{", i)
        j = match_brace(s, k)
        out.append(s[k + 1:j])
        i = j + 1
    return out, i


def parse_variant(tex):
    body = strip_iffalse(tex.split("\\begin{document}", 1)[1])
    sections, cur, role, fact = [], None, None, None
    pat = re.compile(r"%\s*fact:\s*(\S+)|\\section\*?\{|\\resumeSubheading|\\resumeProjectHeading|\\resumeItem\{|\\item\{")
    i = 0
    while (m := pat.search(body, i)):
        tok = m.group(0)
        if m.group(1):
            fact, i = m.group(1), m.end()
        elif tok.startswith("\\section"):
            j = match_brace(body, m.end() - 1)
            cur = {"name": body[m.end():j], "roles": [], "rows": []}
            sections.append(cur)
            i = j + 1
        elif tok == "\\resumeSubheading":
            a, i = args_after(body, m.end(), 4)
            role = {"kind": "sub", "args": a, "items": []}
            cur["roles"].append(role)
        elif tok == "\\resumeProjectHeading":
            a, i = args_after(body, m.end(), 2)
            role = {"kind": "proj", "args": a, "items": []}
            cur["roles"].append(role)
        else:
            j = match_brace(body, m.end() - 1)
            raw = body[m.end():j]
            if tok == "\\item{" or fact == "skills":
                cur["rows"].append(raw)
            else:
                role["items"].append((fact, raw))
            fact, i = None, j + 1
    return sections


def render_roles(sec):
    out = [f"\\section{{{sec['name']}}}", "\\vspace{3pt}", "\\resumeSubHeadingListStart", ""]
    for n, r in enumerate(sec["roles"]):
        if n:
            out.append("\\vspace{\\gapRole}")
        if r["kind"] == "sub":
            company, dates, title, loc = r["args"]
            out += ["  \\resumeSubheading", f"    {{{title}}}{{{dates}}}", f"    {{{company}}}{{{loc}}}"]
        else:
            out += [f"\\resumeProjectHeading {{{r['args'][0]}}}{{{r['args'][1]}}}"]
        out.append("  \\resumeItemListStart")
        for k, (fact, raw) in enumerate(r["items"]):
            if k:
                out.append("    \\vspace{\\gapItem}")
            out += [f"    % fact: {fact}", f"    \\resumeItem{{{raw}}}"]
        out += ["  \\resumeItemListEnd", ""]
    out += ["\\resumeSubHeadingListEnd", ""]
    return "\n".join(out)


def render_skills(sec):
    rows = [r for r in sec["rows"] if not re.search(r"Certification", r)]
    out = ["\\section{Technical Skills}", "\\vspace{3pt}", "\\resumeSubHeadingListStart", ""]
    for r in rows:
        out += ["% fact: skills", f"\\resumeItem{{{r}\\vspace{{-5pt}}}}", ""]
    out += ["\\resumeSubHeadingListEnd", ""]
    return "\n".join(out)


def build(variant_tex: str) -> str:
    base = BASE.read_text()
    pre, body = base.split("\\begin{document}", 1)
    pre = pre.replace("\\setstretch{0.9}", "\\setstretch{\\fitStretch}")
    pre += "\\newcommand{\\fitStretch}{0.9}\n\\newcommand{\\gapItem}{1pt}\n\\newcommand{\\gapRole}{2pt}\n"
    pre = pre.replace("\\newcommand{\\fitStretch}{0.9}\n", "") .replace("\\usepackage{setspace}",
          "\\usepackage{setspace}\n\\newcommand{\\fitStretch}{0.9}")
    head_end = body.index("%-----------EXPERIENCE-----------")
    head = body[:head_end]
    secs = parse_variant(variant_tex)
    has_courses = any(re.search(r"Course", r) for s in secs for r in s["rows"])
    if not has_courses:
        head = re.sub(r"\n\s*\\resumeItem\{\\textbf\{Courses:\}[^\n]*", "", head)
    # Education heading: take the variant's degree line and dates (wording may have changed)
    edu = next((s for s in secs if s["name"].lower().startswith("education")), None)
    if edu and edu["roles"]:
        school, dates, degree, loc = edu["roles"][0]["args"]
        m = re.search(r"\\resumeSubheading\s*\{[^}]*\}\{[^}]*\}\s*\{[^\n]*\}\{[^}]*\}", head)
        head = head[:m.start()] + f"\\resumeSubheading\n      {{{school}}}{{{loc}}}\n      {{{degree}}}{{{dates}}}" + head[m.end():]
    parts = []
    for s in secs:
        name = s["name"].lower()
        if name.startswith(("experience", "projects")):
            parts.append(f"%-----------{s['name'].upper()}-----------\n" + render_roles(s))
        elif name.startswith("technical skills"):
            parts.append("%-----------PROGRAMMING SKILLS-----------\n" + render_skills(s))
    return pre + "\\begin{document}" + head + "\n".join(parts) + "\n\\end{document}\n"


def compile_pages(tex_path: Path):
    r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name],
                       cwd=tex_path.parent, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"compile failed: {tex_path}\n" + "\n".join(l for l in r.stdout.splitlines() if l.startswith("!")))
    info = subprocess.run(["pdfinfo", str(tex_path.with_suffix(".pdf"))], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", info).group(1))


def with_params(src, t):
    """t in [-1, 1]: 0 = the original's spacing (stretch 0.9, 1pt/2pt gaps). t > 0 spreads lines and
    gaps to fill spare room (capped at stretch 1.02, 3.5pt/6pt gaps); t < 0 tightens (stretch >= 0.81)."""
    if t >= 0:
        stretch, gap, role = 0.9 + 0.12 * t, 1 + 2.5 * t, 2 + 4 * t
    else:
        stretch, gap, role = 0.9 + 0.09 * t, 1 + t, 2 + 2 * t
    src = re.sub(r"\\newcommand\{\\fitStretch\}\{[^}]*\}", lambda m: f"\\newcommand{{\\fitStretch}}{{{stretch:.3f}}}", src)
    src = re.sub(r"\\newcommand\{\\gapItem\}\{[^}]*\}", lambda m: f"\\newcommand{{\\gapItem}}{{{gap:.2f}pt}}", src)
    return re.sub(r"\\newcommand\{\\gapRole\}\{[^}]*\}", lambda m: f"\\newcommand{{\\gapRole}}{{{role:.2f}pt}}", src)


def main():
    src_path = Path(sys.argv[1]).resolve()
    out_dir = ROOT / "resume/original_format"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / src_path.name
    src = build(src_path.read_text())
    def fits(t):
        out.write_text(with_params(src, t))
        return compile_pages(out) == 1
    if fits(1.0):
        best = 1.0
    else:
        lo, hi = (0.0, 1.0) if fits(0.0) else (-1.0, 0.0)
        if lo < 0 and not fits(-1.0):
            sys.exit(f"{out}: does not fit on one page even at the tightest spacing")
        for _ in range(7):  # largest spacing that still fits on one page
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if fits(mid) else (lo, mid)
        best = lo
    out.write_text(with_params(src, best))
    compile_pages(out)
    for ext in ("aux", "out", "log"):
        out.with_suffix("." + ext).unlink(missing_ok=True)
    print(f"wrote {out.relative_to(ROOT)} (spacing t={best:+.2f}; 0 = original spacing)")


if __name__ == "__main__":
    main()
