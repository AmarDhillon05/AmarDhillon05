#!/usr/bin/env python3
"""Deterministic resume gate: layout + bullet-style checks.

usage: lint.py resume.tex [--pdf resume.pdf] [--json out.json]
         [--max-lines 2] [--min-last-line 0.30] [--max-bold 3] [--pages 1]

Checks
  layout  : page count; per-bullet rendered line count; last-line fill ("widows")
  style   : leading verb is an action verb (past tense, or -ing for current roles);
            no repeated leading verbs; bold phrases per bullet capped;
            every experience/project bullet has a metric or explicit outcome word
            and at least one technology (bold or known tech)
Exit code 1 if any ERROR.
"""
import argparse
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import texparse  # noqa: E402

WEAK_STARTS = {"responsible", "helped", "worked", "assisted", "participated", "utilized", "used",
               "involved", "tasked", "handled", "did", "made", "was", "were", "a", "an", "the"}
OUTCOME_WORDS = re.compile(r"\b(adopted|enabling|enabled|reducing|reduced|cut|cutting|eliminat\w*|"
                           r"improv\w*|faster|speedup|avoid\w*|sustain\w*|shipp\w*|serv\w+|"
                           r"launch\w*|used by|ICLR|accuracy|latency|throughput)\b", re.I)
NON_EXPERIENCE_SECTIONS = re.compile(r"skill|education|certif|course", re.I)


class BBoxParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pages = []
        self.cur_line = None
        self.cur_word = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "page":
            self.pages.append([])
        elif tag == "line":
            self.cur_line = {"xMin": float(a["xmin"]), "xMax": float(a["xmax"]),
                             "yMin": float(a["ymin"]), "words": []}
        elif tag == "word":
            self.cur_word = {"xMin": float(a["xmin"]), "xMax": float(a["xmax"]), "t": ""}

    def handle_endtag(self, tag):
        if tag == "word" and self.cur_word is not None:
            self.cur_line["words"].append(self.cur_word)
            self.cur_word = None
        elif tag == "line" and self.cur_line is not None:
            self.pages[-1].append(self.cur_line)
            self.cur_line = None

    def handle_data(self, data):
        if self.cur_word is not None:
            self.cur_word["t"] += data


def pdf_bullets(pdf: Path):
    """Group rendered lines into bullets (lines starting with a bullet glyph +
    continuation lines aligned with the bullet text)."""
    xml = subprocess.run(["pdftotext", "-bbox-layout", str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    p = BBoxParser()
    p.feed(xml)
    groups = []
    glyphs_set = ("•", "∙", "·")
    for lines in p.pages:
        right_edge = max(l["xMax"] for l in lines)
        # the bullet glyph is sometimes its own line/block: remember its position
        glyphs = [l for l in lines if len(l["words"]) == 1 and l["words"][0]["t"] in glyphs_set]
        lines = [l for l in lines if l not in glyphs]
        lines = sorted(lines, key=lambda l: (round(l["yMin"]), l["xMin"]))
        cur = None
        for ln in lines:
            w = ln["words"]
            if not w:
                continue
            glyph_here = any(abs(g["yMin"] - ln["yMin"]) < 3 and 0 <= ln["xMin"] - g["xMax"] < 15 for g in glyphs)
            if w[0]["t"] in glyphs_set and len(w) > 1:
                cur = {"text_x": w[1]["xMin"], "lines": [ln], "right": right_edge}
                groups.append(cur)
            elif glyph_here:
                cur = {"text_x": ln["xMin"], "lines": [ln], "right": right_edge}
                groups.append(cur)
            elif cur and abs(ln["xMin"] - cur["text_x"]) < 3.0:
                cur["lines"].append(ln)
            else:
                cur = None
    out = []
    for g in groups:
        full = g["right"] - g["text_x"]
        last = g["lines"][-1]
        words = [w["t"] for l in g["lines"] for w in l["words"]]
        if words and words[0] in ("•", "∙", "·"):
            words = words[1:]
        out.append({"text": " ".join(words), "n_lines": len(g["lines"]),
                    "last_fill": round((last["xMax"] - g["text_x"]) / full, 2) if len(g["lines"]) > 1 else 1.0})
    return out


def page_count(pdf: Path) -> int:
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", info).group(1))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--pdf")
    ap.add_argument("--json")
    ap.add_argument("--max-lines", type=int, default=2)
    ap.add_argument("--min-last-line", type=float, default=0.30)
    ap.add_argument("--max-bold", type=int, default=3)
    ap.add_argument("--pages", type=int, default=1)
    args = ap.parse_args()

    tex_path = Path(args.tex)
    tex = tex_path.read_text()
    pdf = Path(args.pdf) if args.pdf else tex_path.with_suffix(".pdf")
    issues = []

    def add(level, where, msg):
        issues.append({"level": level, "where": where, "msg": msg})

    bullets = texparse.parse(tex)
    exp = [b for b in bullets if not NON_EXPERIENCE_SECTIONS.search(b.section) and b.fact_id != "skills"]

    # ---- layout
    rendered = []
    if pdf.exists():
        n = page_count(pdf)
        if n != args.pages:
            add("ERROR", "document", f"{n} pages (want {args.pages})")
        rendered = pdf_bullets(pdf)
        for b in exp:
            key = norm(b.text)[:40]
            match = next((r for r in rendered if norm(r["text"])[:40] == key), None)
            if match is None:
                match = next((r for r in rendered if norm(r["text"])[:20] == key[:20]), None)
            if match is None:
                add("WARN", b.text[:50], "could not locate bullet in PDF")
                continue
            b.n_lines, b.last_fill = match["n_lines"], match["last_fill"]
            if match["n_lines"] > args.max_lines:
                add("ERROR", b.text[:50], f"{match['n_lines']} rendered lines (max {args.max_lines})")
            if match["n_lines"] > 1 and match["last_fill"] < args.min_last_line:
                add("ERROR", b.text[:50], f"widow: last line only {int(match['last_fill']*100)}% full")
    else:
        add("ERROR", "document", f"missing PDF {pdf}")

    # ---- style
    seen_verbs = {}
    for b in exp:
        words = b.text.split()
        first = re.sub(r"[^A-Za-z-]", "", words[0]) if words else ""
        fl = first.lower()
        where = b.text[:50]
        if fl in WEAK_STARTS:
            add("ERROR", where, f"weak/non-action opening '{first}'")
        elif not (fl.endswith("ed") or fl.endswith("ing") or fl in {"built", "led", "cut", "wrote", "ran", "drove", "won", "made", "grew", "shipped", "rebuilt", "taught", "sped", "split"}):
            add("WARN", where, f"opening '{first}' may not be an action verb")
        if fl:
            if fl in seen_verbs:
                add("WARN", where, f"leading verb '{first}' repeats (also: {seen_verbs[fl]})")
            seen_verbs.setdefault(fl, where)
        if len(b.bold) > args.max_bold:
            add("ERROR", where, f"{len(b.bold)} bold phrases (max {args.max_bold})")
        if not re.search(r"\d", b.text) and not OUTCOME_WORDS.search(b.text):
            add("WARN", where, "no metric or explicit outcome")
        if not b.bold and not re.search(r"[A-Z][a-zA-Z0-9+#.]+", " ".join(words[1:])):
            add("WARN", where, "no visible technology")

    summary = {
        "tex": str(tex_path),
        "n_bullets": len(exp),
        "bullets": [{"fact": b.fact_id, "chars": len(b.text), "words": len(b.text.split()),
                     "n_bold": len(b.bold), "n_lines": getattr(b, "n_lines", None),
                     "last_fill": getattr(b, "last_fill", None), "text": b.text} for b in exp],
        "issues": issues,
        "errors": sum(i["level"] == "ERROR" for i in issues),
        "warnings": sum(i["level"] == "WARN" for i in issues),
    }
    if args.json:
        Path(args.json).write_text(json.dumps(summary, indent=2))
    for i in issues:
        print(f"[{i['level']}] {i['where']!r}: {i['msg']}")
    print(f"lint: {summary['errors']} errors, {summary['warnings']} warnings, {len(exp)} bullets")
    sys.exit(1 if summary["errors"] else 0)


if __name__ == "__main__":
    main()
