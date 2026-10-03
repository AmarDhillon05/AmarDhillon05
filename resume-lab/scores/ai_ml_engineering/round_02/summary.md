# ai_ml_engineering / round_02

**passed:** False  |  overall mean 8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 8.67 | 8 |
| concision_readability | 8 | 8 |
| credibility | 8 | 8 |
| domain_fit | 7.33 | 7 |
| impact_clarity | 8 | 8 |
| overall | 8 | 8 |
| quantification | 7.33 | 7 |
| skim_test | 7.67 | 7 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (ai_hm) clarify: how 'output quality held across multi-run stress tests' was judged (rubric, golden set, pass rate) — I will ask this first in an interview
- (ai_recruiter) clarify: for the Bedrock eval-gated retraining, state what the cross-model eval measures (e.g., agreement with larger LLM labels) so an AI HM sees eval rigor rather than just orchestration
- (ai_recruiter) clarify: 'output quality held across multi-run stress tests' — name how quality was judged (rubric, validator pass rate, human check) if known
- (bs_detector) clarify: 'output quality held across multi-run stress tests' (Capital One). An AI interviewer will ask how quality was judged: eval set, rubric, or diff vs. old outputs? Say which, or soften the claim.
- (bs_detector) clarify: 'tuned its prompts to pick correct grasps and judge depth' (UMIACS) has no outcome. Name what changed (e.g. qualitative improvement on the team's test scenes) if real, or present it as part of the pipeline work rather than a standalone win.

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java policies that tune`: {'keep': 2, 'tighten': 1}
- `Cut LLM workflow generation time`: {'keep': 2, 'tighten': 1}
- `Precomputed a tree-style search index`: {'tighten': 3}
- `Rebuilt a legacy test-data workflow`: {'keep': 3}
- `Automated EventBridge-scheduled fine-tuning of a`: {'keep': 2, 'add_context': 1}
- `Reduced end-to-end latency 34% for`: {'keep': 3}
- `Shipped a space-research tool used`: {'add_context': 1, 'tighten': 1, 'keep': 1}
- `Built a Python pipeline for`: {'tighten': 2, 'add_context': 1}
- `Shortened research-environment setup time 30%`: {'keep': 3}
- `Building a RAG meal-suggestion feature`: {'keep': 3}
- `Co-founded a 110+ member campus`: {'keep': 2, 'tighten': 1}
- `Built a C++17 order book`: {'keep': 3}

## Structure votes
- project_relevance: 2
- order_capital_one_bullets: 1
- ai_variant_project_swap: 1
- aws_bullet_compact: 1
- ai_first_within_entries: 1
