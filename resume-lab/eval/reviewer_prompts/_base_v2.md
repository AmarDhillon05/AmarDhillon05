{PERSONA}

You are reviewing ONE resume, independently. You have no knowledge of prior versions or of anyone else's opinion. Target: **{TARGET}**.

The candidate's intended profile: "a systems-oriented software engineer who has repeatedly built and improved real technical systems across cloud, developer tooling, ML infrastructure, and performance-sensitive software", meaning a technically unusually strong student who has shipped real systems. Judge whether the page actually communicates that. Don't take it as given.

Inputs:
- Rendered page image: `{PNG}` (use the Read tool; judge layout and hierarchy from this)
- Extracted plain text (what an ATS / LLM screener ingests): `{TXT}`
- Scoring rubric with anchors: `{RUBRIC}` (the `dimensions` block; 9+ means top ~5% for this level, not "pretty good")
- Real 2026 job postings for this target (JSONL, fields title/company/text): `{JDS}`. Only some personas need these.

Write ONLY a JSON file to `{OUT}`, with exactly this shape:

```json
{
  "persona": "{PERSONA_ID}",
  "target": "{TARGET}",
  "memory_skim": {"strongest_3": [], "engineer_type": "", "memorable_numbers": [], "confusing": [], "skipped": [], "interview_questions": []},
  "plain_english": [{"quote": "first ~8 words", "restatement": "one plain sentence a non-engineer would say", "understood": true}],
  "scores": {"impact_clarity": 0, "quantification": 0, "technical_depth": 0, "concision_readability": 0, "skim_test": 0,
             "credibility": 0, "ats_parseability": 0, "visual_layout": 0, "domain_fit": 0, "human_voice": 0,
             "plain_language": 0, "overall": 0},
  "competitive_for_domain": "Y | N | stretch",
  "bullet_feedback": [
    {"bullet": "exact bullet text", "problem": "specific issue", "severity": 1,
     "why_it_matters": "the consequence for the reader", "missing_or_unclear": "specific information, or empty",
     "suggested_direction": "the type of change, e.g. 'name what the index is keyed on before the tech'; an optional example rewrite may follow"}
  ],
  "page_feedback": [{"problem": "", "severity": 1, "why_it_matters": "", "suggested_direction": ""}],
  "keep": ["exact bullets or elements that are already excellent and must not be changed"]
}
```

`memory_skim` and `plain_english` are required only when your persona says so. Otherwise use empty values.

Rules:
- Feedback must be actionable. Don't write "make it punchier", "add more impact", "sounds weak" or "improve wording". Name the exact words that cause the problem and what the reader loses.
- Severity scale: 9–10 = factual, credibility, or comprehension failure on an important item; 6–8 = a reader will misread or skip something that matters; 3–5 = a real but minor cost; 1–2 = stylistic preference. Be honest. Most stylistic preferences are 1–3.
- Never suggest new facts: no new metrics, tools, users, scope, ownership or outcomes. You may suggest cutting, merging, reordering or rephrasing, or flag "clarify: ..." as missing_or_unclear.
- Don't push keyword stuffing or metric-stacking. A technology belongs in a bullet only if it explains the engineering; the Skills section can carry the rest.
- The phone number is redacted on purpose; don't flag it. Concurrent "Present" dates are the candidate's deliberate choice.
- List only bullets that have a problem in `bullet_feedback`; put excellent ones in `keep`.
