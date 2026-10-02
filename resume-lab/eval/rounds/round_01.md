# Round 01 → v2 decisions

**Panel result on v1 (round_01):**
- Overall 7.8, up from 7.0 at baseline.
- The weakest dimensions were credibility (6.4) and quantification (6.4).
- All gates were clean.

See `scores/base/round_01/summary.md`.

## Candidate input this round (Amar, Oct 2026)
| item | answer | effect |
|---|---|---|
| 34% (Kinesis pipeline) | end-to-end latency | bullet now says "Reduced end-to-end latency 34%" |
| 90% (Capital One UI) | % of surveyed internal users preferring the new tool | "90% of surveyed users preferred it over the old tool" |
| 93% (RAG meal app) | % of generated meal suggestions rated satisfactory | "93% of generated meals rated satisfactory by internal testers" |
| IEX results | none measured | bullets stay method-focused; no implied results |
| overlapping "Present" dates | keep as-is | **accepted risk** (`rubric.yaml: accepted_risks`); flagged but non-blocking |
| AWS Redshift details | pending (no text received yet) | bullet unchanged |

## Changes applied in v2 (each had ≥2 reviewers or a rubric rule behind it)

**Metrics and attribution**
- Every percentage now names its metric, using the candidate's answers. All 5 reviewers asked for this.
- Tortuga: the caching work is decoupled from the 20K visits. The BS detector, HM, and recruiter all asked for this, because the old wording implied the caching caused the traffic.
- UMIACS environment setup: profiling and Pytest are split from the 30% setup-time claim (BS detector + HM).

**Wording**
- "Claude skill using sub-skill decomposition" became "decomposing a Claude skill into sub-skills" plus "LLM workflow generation" for context. 4 reviewers called it jargon.
- TerpLabs studio: dropped the filler words "scaled" and "agile" (BS detector). "Has shipped" now carries the honest scope.
- IEX: "replaying historical IEX data" replaced the confusing "live" data wording (HM + BS detector).

**Structure**
- The contract role now shows its real employer: "UMD App Development Contracting (Client: Amazon)". 3 reviewers flagged the two Amazon entries (ATS ×2, recruiter), which meets the 3-of-5 structural rule.
- The contact line fits on one line ("NYC Area"). ATS + BS detector + startup engineer asked for this.
- Trimmed unevidenced skills (IAM, Hugging Face). HM + BS detector.

## Blind pairwise check (v1 vs v2)
v2 won 12 of 15 bullets. For the 3 v1 wins, I took the v1 wording or the judge's better rewrite:
- **Bedrock:** used the judge's rewrite, restoring "AWS Bedrock" and "EventBridge cron".
- **Leo:** restored "so new engineers can contribute".
- **Redshift:** dropped the redundant "(in progress)".

## Still open (needs candidate facts; not fixable by wording)
- What the AWS Redshift work concretely is.
- What "adopted into Leo's ecosystem" means: who uses it.
- Rater counts for 90% / 93%.
- The 65% baseline beyond "previous tooling".
