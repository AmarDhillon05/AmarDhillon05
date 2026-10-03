#!/usr/bin/env python3
"""Meaning-preservation gate. Every experience/project bullet must carry a
`% fact: <role>.<bullet>` annotation pointing into resume/facts.yaml.

usage: fact_check.py resume.tex [--facts facts.yaml] [--json out.json]

ERROR if
  - a bullet has no / an unknown fact annotation
  - a required number of that fact is missing from the bullet
  - a core technology of that fact is missing from the bullet
  - a number appears in a bullet that is not in that fact's claim (invented or
    mis-attached metric), or anywhere in the document that is not in facts.yaml
  - a fact is used twice
WARN if a used role's title/org/dates don't appear in the document.
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import texparse  # noqa: E402

NUM_RE = re.compile(r"(?<![A-Za-z0-9.])(\d[\d,]*(?:\.\d+)?)\s*([KkMm](?![a-z]))?")
SECTION_SKIP = re.compile(r"skill|education|certif|course", re.I)


def numbers(s: str):
    vals = set()
    for m in NUM_RE.finditer(s):
        try:
            v = float(m.group(1).replace(",", ""))
        except ValueError:
            continue
        if m.group(2):
            v *= 1000 if m.group(2).lower() == "k" else 1_000_000
        vals.add(v)
    return vals


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9+#]", "", s.lower())


def tech_present(tech: str, text: str) -> bool:
    t, n = norm(tech), norm(text)
    cands = {t, norm(re.sub(r"^(AWS|Amazon)\s+", "", tech)), norm(re.sub(r"\.js$", "", tech))}
    return any(c and c in n for c in cands)


def flatten_facts(facts):
    out = {}
    for group in ("roles", "projects"):
        for rid, role in (facts.get(group) or {}).items():
            for bid, b in (role.get("bullets") or {}).items():
                out[f"{rid}.{bid}"] = (role, b)
    return out


def strip_whitelist(s, wl):
    for w in sorted(wl, key=len, reverse=True):
        s = s.replace(w, " ")
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--facts", default=str(Path(__file__).parent.parent / "resume" / "facts.yaml"))
    ap.add_argument("--json")
    args = ap.parse_args()

    tex = Path(args.tex).read_text()
    facts_raw = Path(args.facts).read_text()
    facts = yaml.safe_load(facts_raw)
    wl = facts.get("number_whitelist", [])
    table = flatten_facts(facts)
    allowed_global = numbers(strip_whitelist(facts_raw, wl))
    issues = []

    def add(level, where, msg):
        issues.append({"level": level, "where": where, "msg": msg})

    used = {}
    used_roles = set()
    for b in texparse.parse(tex):
        if SECTION_SKIP.search(b.section) or b.fact_id == "skills":
            continue
        where = b.text[:50]
        if not b.fact_id:
            add("ERROR", where, "missing `% fact:` annotation")
            continue
        # a merged bullet may cite several facts: `% fact: a.b+c.d`
        ids = b.fact_id.split("+")
        unknown = [i for i in ids if i not in table]
        if unknown:
            add("ERROR", where, f"unknown fact id(s) {unknown}")
            continue
        for i in ids:
            if i in used:
                add("ERROR", where, f"fact {i} used twice")
            used[i] = b.text
            r_i, f_i = table[i]
            if f_i.get("superseded") or r_i.get("superseded"):
                add("ERROR", where, f"fact {i} is superseded (corrected by candidate); do not use")
            used_roles.add(i.split(".")[0])
        parts = [table[i] for i in ids]
        role = parts[0][0]
        f = {"claim": " ".join(p[1]["claim"] for p in parts),
             "required_numbers": [n for p in parts for n in (p[1].get("required_numbers") or [])],
             "core_techs": [t for p in parts for t in (p[1].get("core_techs") or [])]}
        text_wo = strip_whitelist(b.text, wl)
        for req in f.get("required_numbers") or []:
            alts = req.split("|")
            if not any(numbers(a) <= numbers(text_wo) for a in alts):
                add("ERROR", where, f"required number '{req}' missing")
        for t in f.get("core_techs") or []:
            if not tech_present(t, b.text):
                add("ERROR", where, f"core tech '{t}' missing")
        claim_nums = numbers(strip_whitelist(f["claim"], wl)) | {
            v for r in (f.get("required_numbers") or []) for a in r.split("|") for v in numbers(a)}
        extra = numbers(text_wo) - claim_nums
        if extra:
            add("ERROR", where, f"number(s) {sorted(extra)} not in fact claim (invented/mis-attached)")

    doc = texparse.document_text(tex)
    stray = numbers(strip_whitelist(doc, wl)) - allowed_global
    if stray:
        add("ERROR", "document", f"numbers not found anywhere in facts.yaml: {sorted(stray)}")

    for rid in used_roles:
        group = "roles" if rid in (facts.get("roles") or {}) else "projects"
        role = facts[group][rid]
        for key in ("title", "dates"):
            v = role.get(key)
            if v and norm(v) not in norm(doc):
                add("WARN", rid, f"{key} '{v}' not found verbatim in document")

    summary = {"used_facts": sorted(used), "issues": issues,
               "errors": sum(i["level"] == "ERROR" for i in issues),
               "warnings": sum(i["level"] == "WARN" for i in issues)}
    if args.json:
        Path(args.json).write_text(json.dumps(summary, indent=2))
    for i in issues:
        print(f"[{i['level']}] {i['where']!r}: {i['msg']}")
    print(f"fact_check: {summary['errors']} errors, {summary['warnings']} warnings, {len(used)} facts used")
    sys.exit(1 if summary["errors"] else 0)


if __name__ == "__main__":
    main()
