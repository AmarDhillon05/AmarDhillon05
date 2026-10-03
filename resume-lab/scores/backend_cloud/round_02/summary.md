# backend_cloud / round_02

**passed:** False  |  overall mean 8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 8 | 8 |
| credibility | 8 | 8 |
| domain_fit | 7.67 | 7 |
| impact_clarity | 7.67 | 7 |
| overall | 8 | 8 |
| quantification | 7.67 | 7 |
| skim_test | 8 | 8 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) Clarify: is 6,000+ documents a total corpus or a per-day/per-run volume? Choosing Kinesis over S3 for 6K total docs invites an immediate 'why streaming?' follow-up.
- (bs_detector) Replace insider jargon 'the Claude skill's main search tool' / 'sub-skills' with plain backend terms a non-Capital-One HM understands (e.g., LLM agent's search tool).
- (infra_hm) AWS bullet ends with 'initial backtests complete', which is weak; clarify what the backtests showed or state the policy design choice more concretely
- (infra_hm) Clarify: what the 34% Kinesis latency reduction is measured from (absolute end-to-end time before/after, if known)
- (sre_engineer) clarify: Kinesis bullet — what were the 'S3 staging hops' (write-then-poll?) so the 34% latency win reads as a design decision, not a service swap
- (sre_engineer) clarify: Bedrock fine-tuning bullet ends at mechanism; state what the threshold-gated retraining avoids (e.g., unnecessary retrain runs) if the candidate can stand behind it

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java policies that tune`: {'keep': 2, 'add_context': 1}
- `Precomputed a tree-style search index`: {'tighten': 3}
- `Cut LLM workflow generation time`: {'tighten': 1, 'keep': 2}
- `Rebuilt a legacy test-data workflow`: {'keep': 2, 'tighten': 1}
- `Reduced end-to-end latency 34% for`: {'add_context': 2, 'keep': 1}
- `Shipped a space-research tool to`: {'keep': 3}
- `Automated EventBridge-scheduled fine-tuning of a`: {'tighten': 1, 'keep': 1, 'add_context': 1}
- `Shortened research-environment setup time 30%`: {'keep': 2, 'tighten': 1}
- `Co-founded a 110+ member campus`: {'tighten': 1, 'keep': 2}
- `Engineered a C++17 order book`: {'keep': 3}
- `Benchmarked B+ tree vs LSM`: {'keep': 3}
- `Sustained 1.26M events/sec end-to-end over`: {'keep': 3}

## Structure votes
- lead_project_with_storage_benchmark: 1
- skills_cloud_first: 1
- capital_one_bullet_order: 1
- keep_section_order: 1
- keep_order: 1
- project_bullet_order: 1
