#!/usr/bin/env python3
"""Export a small set of redacted reference resumes into corpus/references/.

usage: export_references.py
Re-clones each chosen public repo (shallow, into the scratch workdir), takes the same .tex
the corpus scraper picked, removes the identity header and all contact info, then writes
<variant>_<id>.tex (+ .pdf when it compiles, + .txt). Fails loudly if any email, phone,
URL, the repo owner's handle, or the header name survives redaction.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scrape_github_latex import EMAIL_RE, PHONE_RE, URL_RE, clone, inline_inputs, latex_to_text, strip_comments  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "corpus/references"
WORK = "/tmp/claude-0/gh_refs"

# id -> (variant, why it was picked)
PICKS = {
    "2119c22bc655": ("general_backend", "AWS + Google/YouTube intern; clear backend bullets with scope and results"),
    "4dfbdaf6e9b5": ("general_backend", "Stripe intern; plain-language product/infra bullets"),
    "00391957f094": ("general_backend", "AWS intern; backend + research mix similar to Amar's"),
    "5926ce0c3962": ("infra_distributed", "Amazon/Cloudflare/Tesla intern; highest corpus quality score; infra-heavy"),
    "70c3493688d3": ("infra_distributed", "Google intern; distributed-systems and cloud keywords used in context"),
    "62585d31928d": ("infra_distributed", "Netflix intern; infra/SRE bullets with concrete mechanisms"),
    "f644ba7bc0c5": ("systems_quant", "IMC + Capital One intern; same Capital One brand, quant systems framing"),
    "b05ffc279363": ("systems_quant", "IMC + PEAK6 intern; low-latency/trading-systems bullets"),
    "0c7a2097d593": ("systems_quant", "SIG + Google intern; quant firm resume with research projects"),
    "d54264c23b67": ("ai_ml_engineering", "Amazon new grad; ML systems grounded in engineering"),
    "91339cdb3824": ("ai_ml_engineering", "AWS Redshift team intern (same org as Amar's AWS role); ML + systems"),
    "d5ae27a86afb": ("ai_ml_engineering", "NVIDIA + Baseten intern; ML infra / inference serving"),
}


def redact(tex: str, owner: str):
    tex = strip_comments(tex)
    pre, _, body = tex.partition("\\begin{document}")
    # metadata that can carry the name
    pre = re.sub(r"\\(hypersetup|author|title|pdfauthor)\b.*", "", pre)
    m = re.search(r"\\section\*?\{", body)
    header = body[: m.start()] if m else ""
    hdr_text = latex_to_text(header)
    name = next((ln.strip() for ln in hdr_text.splitlines() if re.search(r"[A-Za-z]{2,}", ln)), "")
    body = "\n\\begin{center}{\\Huge\\scshape Redacted Candidate}\\end{center}\n" + body[m.start():] if m else body
    body = re.sub(r"\\href\{[^}]*\}", "", body)             # keep link text, drop target
    body = re.sub(r"\\url\{[^}]*\}", "[url]", body)
    for rx, rep in ((EMAIL_RE, "[email]"), (URL_RE, "[url]")):
        body = rx.sub(rep, body)
    body = PHONE_RE.sub(lambda x: "[phone]" if re.search(r"\d{3}.*\d{3}.*\d{4}", x.group(0)) else x.group(0), body)
    # drop macros that define identity (\name{..}, \address{..}, \email{..}, \phone{..})
    pre = re.sub(r"\\(name|address|email|phone|homepage|github|linkedin)\{[^}]*\}", "", pre)
    out = pre + "\\begin{document}" + body
    tokens = [t for t in re.split(r"\s+", name) if len(t) >= 3 and t[0].isupper()]
    return out, tokens


def check(text: str, owner: str, name_tokens):
    bad = []
    if EMAIL_RE.search(text): bad.append("email")
    if re.search(r"(github|linkedin)\.com/|https?://", text, re.I): bad.append("url")
    if re.search(r"\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}", text): bad.append("phone")
    if len(owner) >= 4 and re.search(re.escape(owner), text, re.I): bad.append(f"owner:{owner}")
    for t in name_tokens:
        if re.search(rf"\b{re.escape(t)}\b", text): bad.append(f"name:{t}")
    return bad


def main():
    report = {r["id"]: r for r in json.load(open(ROOT / "corpus/raw/github_scrape_report.json")) if r.get("id")}
    meta = {r["id"]: r for r in map(json.loads, open(ROOT / "corpus/github_resumes.jsonl"))}
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for rid, (variant, why) in PICKS.items():
        rep = report[rid]
        repo, path = rep["repo"], rep["file_path"]
        dest = clone(repo, WORK)
        if not dest:
            print(f"skip {rid}: clone failed"); continue
        subprocess.run(["git", "checkout", "-q", "HEAD", "--", "."], cwd=dest)
        src = Path(dest) / path
        if not src.exists():
            print(f"skip {rid}: {path} missing at HEAD"); continue
        files = [str(p.relative_to(dest)) for p in Path(dest).rglob("*.tex")]
        tex, _ = inline_inputs(dest, path, strip_comments(src.read_text(errors="replace")), files)
        red, name_tokens = redact(tex, repo.split("/")[0])
        stem = f"{variant}_{rid}"
        (OUT / f"{stem}.tex").write_text(red)
        # try to compile next to the repo (custom .cls/.sty/fonts live there), then copy the pdf back
        tmp = Path(dest) / src.parent / f"_ref_{rid}.tex"
        tmp.write_text(red)
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tmp.name],
                           cwd=tmp.parent, capture_output=True, timeout=120)
        pdf = tmp.with_suffix(".pdf")
        compiled = r.returncode == 0 and pdf.exists()
        if compiled:
            shutil.copy(pdf, OUT / f"{stem}.pdf")
            txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
        else:
            txt = latex_to_text(red.partition("\\begin{document}")[2])
        (OUT / f"{stem}.txt").write_text(txt)
        bad = check(red, repo.split("/")[0], name_tokens) + check(txt, repo.split("/")[0], name_tokens)
        if bad:
            for ext in ("tex", "pdf", "txt"):
                (OUT / f"{stem}.{ext}").unlink(missing_ok=True)
            print(f"DROPPED {rid}: redaction check failed {sorted(set(bad))}"); continue
        lic = next((p.name for p in Path(dest).iterdir() if p.name.upper().startswith(("LICENSE", "COPYING"))), None)
        m = meta[rid]
        rows.append({"file": stem, "variant": variant, "level": m["level"], "companies": m["companies"],
                     "last_modified": m["last_modified"][:10], "why": why, "compiled_pdf": compiled,
                     "license_file": lic})
        print(f"ok {stem} pdf={compiled}")
    (OUT / "index.json").write_text(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
