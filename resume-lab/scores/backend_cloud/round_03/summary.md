# backend_cloud / round_03

**passed:** False  |  overall mean 8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 8 | 8 |
| credibility | 8 | 8 |
| domain_fit | 8 | 8 |
| impact_clarity | 7.67 | 7 |
| overall | 8 | 8 |
| quantification | 7.33 | 7 |
| skim_test | 8 | 8 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) Clarify: what "6,000+ scraped research documents" means (total corpus vs per run/day) so the 34% latency claim has scope an interviewer can probe.
- (bs_detector) Clarify: "tree-style search index" and "strict DB access limits" are vague; name the actual constraint/structure in the candidate's own terms or one follow-up question exposes it.
- (infra_hm) clarify: the AWS bullet's outcome or scope (which ops, what backtesting showed) if any can be stated; the most prestigious line currently ends at method
- (sre_engineer) clarify: what the AWS backtesting showed (e.g., whether the policy held availability while reducing reserved capacity); right now the strongest SRE bullet ends at method, with no outcome

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java policies that tune`: {'keep': 1, 'add_context': 2}
- `Precomputed a tree-style search index`: {'tighten': 3}
- `Cut LLM workflow generation time`: {'tighten': 1, 'keep': 2}
- `Rebuilt a legacy test-data workflow`: {'keep': 3}
- `Reduced end-to-end latency 34% for`: {'add_context': 1, 'keep': 2}
- `Shipped a space-research tool to`: {'keep': 3}
- `Automated EventBridge-scheduled fine-tuning of a`: {'tighten': 2, 'keep': 1}
- `Shortened research-environment setup time 30%`: {'keep': 3}
- `Co-founded a 110+ member campus`: {'tighten': 1, 'keep': 2}
- `Engineered a C++17 order book`: {'keep': 3}
- `Benchmarked B+ tree vs LSM`: {'keep': 3}
- `Sustained 1.26M events/sec end-to-end over`: {'keep': 3}

## Structure votes
- reorder_leo_before_capital_one_bullets: 1
- skills_storage_line: 1
- keep_current_order: 1
- keep_order: 1
- skills_cloud_first: 1
