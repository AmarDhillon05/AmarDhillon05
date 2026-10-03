# base / round_05

**passed:** False  |  overall mean 8.6  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 8 | 8 |
| credibility | 8 | 8 |
| domain_fit | 8.4 | 8 |
| impact_clarity | 8 | 8 |
| overall | 8.6 | 8 |
| quantification | 8 | 8 |
| skim_test | 8.2 | 8 |
| technical_depth | 8.4 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) Clarify: the Tortuga bullet pairs a Redis caching change with 20,000+ visits; the traffic number is product reach, not a result of the caching. Make that clear in the wording so an interviewer does not read it as a caching result.
- (bs_detector) AWS bullet: 'operations like patching, backtesting policies' can be misread as backtesting being one of the operations. Split the clauses so the method is clear.

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java to tune upper/lower`: {'tighten': 4, 'keep': 1}
- `Rebuilt a legacy test-data workflow`: {'keep': 5}
- `Precomputed a tree-style search index`: {'keep': 2, 'tighten': 3}
- `Cut LLM workflow generation time`: {'tighten': 1, 'keep': 4}
- `Shipped a space-research tool used`: {'keep': 5}
- `Reduced end-to-end latency 34% for`: {'keep': 5}
- `Automated EventBridge-scheduled fine-tuning of a`: {'keep': 1, 'tighten': 4}
- `Built a Python pipeline for`: {'tighten': 4, 'keep': 1}
- `Shortened research-environment setup time 30%`: {'keep': 5}
- `Co-founded a 110+ member campus`: {'keep': 5}
- `Added Redis query caching over`: {'keep': 2, 'reframe': 1, 'add_context': 2}
- `Building a RAG meal-suggestion feature`: {'keep': 5}
- `Engineered a C++17 order book`: {'keep': 5}
- `Benchmarked B+ tree vs LSM`: {'keep': 4, 'tighten': 1}
- `Sustained 1.26M events/sec end-to-end over`: {'keep': 1, 'tighten': 4}

## Structure votes
- keep_current_order: 3
- bold_consistency: 2
- skills_evidence_alignment: 1
- clarify_amazon_leo: 1
- keep_project_placement: 1
