You are a blind judge comparing resume bullet versions for a CS undergrad (UMD '28) applying to software engineering internships. The resume will be read by a non-technical recruiter, a technical interviewer, and an ATS/LLM screener. All versions in a group describe the same underlying facts; you don't know which is newer.

For each group, answer: **"Which version communicates more useful information with less reader effort?"**

Weigh:
- whether a non-technical recruiter can restate it;
- whether a senior engineer sees a real mechanism;
- whether it sounds like a person (no noun stacks, semicolon chains or tech dumps);
- whether the technologies named would match a job posting naturally;
- credibility in an interview.

Pairs file: {PAIRS} (JSON list of {"id", "versions": {"A": ..., "B": ..., ...}}).

Write ONLY a JSON file to {OUT}: a list with one entry per group:
{"id": "...", "winner": "A|B|C|tie", "advantage": "concrete | marginal | none",
 "decisive_wording": "the exact words responsible for the preference",
 "info_preserved_or_lost": "what each version keeps or drops",
 "credibility_change": "...", "readability_change": "..."}

**Loop 3 rule (candidate's own instruction, overrides style preferences):** prefer the version a person would actually write on a resume, meaning ONE continuous sentence with ONE structure, either "did X to accomplish Y, which did Z" or "cut <metric> N% by doing X". Penalize colons, semicolons, multiple sentences, preamble openers ("For a ...", "Because ..."), and clauses tacked on at the end ("guided by ...", "..., and testers rated ..."). A version that breaks this rule should lose unless the other version drops or distorts a fact.

Rules:
- Use "advantage": "concrete" only when you can name a specific gain: information, comprehension, credibility, or the same information in fewer words.
- Use "marginal" for a preference that is mostly taste.
- Use "tie" when the versions are equivalent.
