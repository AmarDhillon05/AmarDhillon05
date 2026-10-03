#!/usr/bin/env python3
"""Human-voice / legibility heuristics for a single bullet (used by lint.py).

usage (calibration): voice.py --calibrate   -> flag rates on the top-tier corpus bullets
Each check returns a short message; lint.py reports them as WARN. They are cheap proxies;
the recruiter and skeptic evaluators are the real judges of "sounds human".
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

INFLATED = re.compile(r"\b(architect(ed|ing)|spearhead(ed|ing)|mission.critical|highly.scalable|cutting.edge|robust|"
                      r"revolutioni[sz]\w*|optimi[sz](ed|ing)|leverag(ed|ing)|utiliz(ed|ing)|seamless(ly)?|"
                      r"state.of.the.art|best.in.class|synerg\w*|world.class|innovative)\b", re.I)
STOP = set("a an the of for to in on at by with from into via and or but as so that which who while when "
           "under over than per each its their his her our this these those it is was were be been".split())
NUM = re.compile(r"(?<![A-Za-z+])(\d[\d,.]*\s?(%|×|x\b|[KMB]\b|ns|µs|ms|s\b|GB)?)")
TECH = None


def _tech_vocab():
    global TECH
    if TECH is None:
        from scrape_github_latex import TECH_VOCAB
        import yaml
        root = Path(__file__).resolve().parent.parent
        pool = yaml.safe_load((root / "resume/facts.yaml").read_text())["skills_pool"]
        extra = [t for v in pool.values() for t in v]
        TECH = sorted({t.lower() for t in TECH_VOCAB + extra if len(t) > 1}, key=len, reverse=True)
    return TECH


def tool_run(text):
    """Longest run of tech names separated only by , / + & or 'and'."""
    t = text.lower()
    spans = []
    for tech in _tech_vocab():
        for m in re.finditer(rf"(?<![\w+]){re.escape(tech)}(?![\w+])", t):
            if not any(a <= m.start() < b for a, b in spans):
                spans.append((m.start(), m.end()))
    spans.sort()
    best = run = 1 if spans else 0
    for (a1, b1), (a2, b2) in zip(spans, spans[1:]):
        gap = t[b1:a2]
        run = run + 1 if re.fullmatch(r"\s*([,/+&(]|\band\b)?\s*(and\s*)?", gap) else 1
        best = max(best, run)
    return best


def noun_stack(text):
    """Longest run of content words with no stopword, verb-ish (-ed/-ing/-ly) or punctuation break.
    Hyphenated compounds count once per part."""
    best = cur = 0
    for tok in re.findall(r"[\w+#.\-]+|[^\w\s]", text):
        w = tok.lower().strip(".")
        if (not re.match(r"[a-z]", w) or w in STOP or re.search(r"(ed|ing|ly)$", w)
                or len(w) < 2 or tok in ",;:()"):
            cur = 0
            continue
        cur += w.count("-") + 1
        best = max(best, cur)
    return best


def metrics(text):
    nums = [m.group(1) for m in NUM.finditer(text) if not re.fullmatch(r"20\d\d", m.group(1).strip())]
    return len(nums)


def issues(text):
    out = []
    m = INFLATED.search(text)
    if m:
        out.append(f"inflated/AI-tell word '{m.group(0)}'")
    if ";" in text:
        out.append("semicolon joins clauses (split or use 'and')")
    if text.count("(") > 1:
        out.append(f"{text.count('(')} parentheticals (max 1)")
    n = noun_stack(text)
    if n >= 5:
        out.append(f"noun stack of {n} words")
    r = tool_run(text)
    if r >= 4:
        out.append(f"tool inventory: {r} techs in a row")
    k = metrics(text)
    if k > 3:
        out.append(f"{k} numbers in one bullet (metric stacking)")
    return out


if __name__ == "__main__" and "--calibrate" in sys.argv:
    root = Path(__file__).resolve().parent.parent
    rows = [json.loads(l) for l in open(root / "corpus/github_bullets.jsonl")]
    from collections import Counter
    c = Counter()
    for r in rows:
        for i in issues(r["text"]):
            c[i.split(" ")[0] if not i[0].isdigit() else "parens/numbers:" + i.split(" ")[1]] += 1
    print(f"{len(rows)} corpus bullets; share flagged per check:")
    for k, v in c.most_common():
        print(f"  {k:30s} {v/len(rows):.1%}")
    ns = sorted(noun_stack(r["text"]) for r in rows); tr = sorted(tool_run(r["text"]) for r in rows)
    mt = sorted(metrics(r["text"]) for r in rows)
    q = lambda a, p: a[int(p * (len(a) - 1))]
    print(f"noun_stack p50/p90/p95: {q(ns,.5)}/{q(ns,.9)}/{q(ns,.95)}; tool_run p50/p90/p95: {q(tr,.5)}/{q(tr,.9)}/{q(tr,.95)}; numbers p50/p90/p95: {q(mt,.5)}/{q(mt,.9)}/{q(mt,.95)}")
