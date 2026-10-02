"""Minimal parser for Jake-style LaTeX resumes.

Extracts bullets (\\resumeItem{...}) with brace matching, the `% fact: <id>`
annotation preceding each bullet, bold phrases, and a plain-text rendering.
Text inside \\iffalse ... \\fi and comments is ignored.
"""
import re
from dataclasses import dataclass, field


def strip_comments(tex: str) -> str:
    # remove % comments but keep \%; keep `% fact:` annotations as markers
    out = []
    for line in tex.splitlines():
        m = re.match(r"\s*%\s*fact:\s*(\S+)", line)
        if m:
            out.append(f"\x00FACT:{m.group(1)}\x00")
            continue
        out.append(re.sub(r"(?<!\\)%.*$", "", line))
    return "\n".join(out)


def strip_iffalse(tex: str) -> str:
    return re.sub(r"\\iffalse.*?\\fi\b", "", tex, flags=re.S)


def match_brace(s: str, i: int) -> int:
    """s[i] == '{'; return index of matching '}'."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    raise ValueError("unbalanced braces")


def latex_to_text(s: str) -> str:
    s = s.replace("\\%", "%").replace("\\&", "&").replace("\\$", "$").replace("\\#", "#")
    s = s.replace("--", "–").replace("~", " ")
    s = re.sub(r"\$\|\$", "|", s)
    s = re.sub(r"\\[vh]space\*?\{[^}]*\}", "", s)
    s = re.sub(r"\\fontsize\{[^}]*\}\{[^}]*\}", "", s)
    s = re.sub(r"\\(?:setlength|addtolength)\{[^}]*\}\{[^}]*\}", "", s)
    s = re.sub(r"\\(?:href)\{[^}]*\}", "", s)
    # unwrap \cmd{...} keeping content
    for _ in range(5):
        s = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\*?", "", s)
    s = s.replace("{", "").replace("}", "").replace("$", "")
    return re.sub(r"\s+", " ", s).strip()


def bold_phrases(s: str):
    out = []
    for m in re.finditer(r"\\textbf\{", s):
        j = match_brace(s, m.end() - 1)
        out.append(latex_to_text(s[m.end():j]))
    return out


@dataclass
class Bullet:
    fact_id: str | None
    raw: str
    text: str
    bold: list = field(default_factory=list)
    section: str = ""
    role: str = ""


def parse(tex: str):
    body = tex.split("\\begin{document}", 1)[-1]
    body = strip_iffalse(strip_comments(body))
    bullets = []
    section = ""
    role = ""
    pending_fact = None
    i = 0
    pat = re.compile(r"\x00FACT:(\S+?)\x00|\\section\*?\{|\\resumeSubheading|\\resumeProjectHeading|\\resumeItem\{")
    while True:
        m = pat.search(body, i)
        if not m:
            break
        tok = m.group(0)
        if tok.startswith("\x00FACT:"):
            pending_fact = m.group(1)
            i = m.end()
        elif tok.startswith("\\section"):
            j = match_brace(body, m.end() - 1)
            section = latex_to_text(body[m.end():j])
            i = j + 1
        elif tok in ("\\resumeSubheading", "\\resumeProjectHeading"):
            k = body.index("{", m.end())
            j = match_brace(body, k)
            role = latex_to_text(body[k + 1:j])
            i = j + 1
        else:
            j = match_brace(body, m.end() - 1)
            raw = body[m.end():j]
            bullets.append(Bullet(pending_fact, raw, latex_to_text(raw), bold_phrases(raw), section, role))
            pending_fact = None
            i = j + 1
    return bullets


def document_text(tex: str) -> str:
    body = tex.split("\\begin{document}", 1)[-1]
    body = strip_iffalse(strip_comments(body)).replace("\x00", " ")
    body = re.sub(r"FACT:\S+", "", body)
    return latex_to_text(body)
