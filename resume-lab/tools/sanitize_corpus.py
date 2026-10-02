#!/usr/bin/env python3
"""Strip identifying fields (source URLs, file paths, author handles) from corpus
JSONL before it is committed to a public repo. The id -> URL mapping is kept in
corpus/raw/private_sources.jsonl (git-ignored) so results stay reproducible."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DROP = {"source_url", "file_path", "author", "username", "repo", "url"}
private = ROOT / "corpus" / "raw" / "private_sources.jsonl"
seen = set(l for l in private.read_text().splitlines()) if private.exists() else set()
for name in ("github_resumes.jsonl", "outcome_resumes.jsonl"):
    p = ROOT / "corpus" / name
    if not p.exists():
        continue
    rows = [json.loads(l) for l in p.read_text().splitlines() if l.strip()]
    for r in rows:
        priv = {k: r.pop(k) for k in list(r) if k in DROP}
        if priv:
            line = json.dumps({"id": r.get("id"), "file": name, **priv})
            seen.add(line)
    p.write_text("".join(json.dumps(r) + "\n" for r in rows))
private.parent.mkdir(parents=True, exist_ok=True)
private.write_text("".join(sorted(l + "\n" for l in seen)))
print("sanitized")
