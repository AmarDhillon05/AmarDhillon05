{PERSONA}

You are reviewing ONE resume, independently. You have no knowledge of prior versions or of anyone else's opinion. Target: **{TARGET}**.

Inputs (read all three):
- Rendered page image: `{PNG}` (read it with the Read tool; judge visual layout from this)
- Extracted text (what an ATS / LLM screener sees): `{TXT}`
- Scoring rubric with anchors: `{RUBRIC}` (use the `dimensions` block; score each 1–10 against the anchors; be calibrated — 9+ means genuinely top ~5% for this level, not "pretty good")

Do your review in character. Then write ONLY a JSON file to `{OUT}` with exactly this shape (no other files, no commentary in the file):

```json
{
  "persona": "{PERSONA_ID}",
  "target": "{TARGET}",
  "seven_second_takeaway": "what you remember after a 7s skim, ≤30 words",
  "scores": {"impact_clarity": 0, "quantification": 0, "technical_depth": 0, "concision_readability": 0,
             "skim_test": 0, "credibility": 0, "ats_parseability": 0, "visual_layout": 0, "domain_fit": 0, "overall": 0},
  "score_rationale": {"<dimension>": "≤25 words, only for dimensions scored < 8"},
  "competitive_for_domain": "Y | N | stretch",
  "must_fix": ["issues that would materially hurt this candidate; empty list if none"],
  "bullets": [
    {"quote": "first ~8 words of the bullet", "verdict": "keep | tighten | add_context | reframe | cut",
     "issue": "≤20 words (omit if keep)", "suggestion": "optional rewrite ≤200 chars — must NOT invent new numbers, technologies, scope or outcomes"}
  ],
  "structure": [{"key": "short_snake_case_id", "change": "section/ordering/layout change you recommend", "rationale": "≤25 words"}],
  "top3": ["the three highest-leverage changes, most important first"]
}
```

Rules:
- Cover EVERY experience/project bullet in `bullets` (in page order).
- Never suggest adding facts the candidate hasn't stated (no new metrics, tools, users, or outcomes). You may suggest cutting, merging, reordering, rephrasing, or asking the candidate to clarify (put clarifications in must_fix or top3 phrased as "clarify: ...").
- Structural changes are welcome but should be justified; prefer conservative changes.
- Keep it honest: if something is already excellent, say keep.
