# backend_cloud / round_01

**passed:** False  |  overall mean 8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 8 | 8 |
| credibility | 8 | 8 |
| domain_fit | 8 | 8 |
| impact_clarity | 8 | 8 |
| overall | 8 | 8 |
| quantification | 8 | 8 |
| skim_test | 8 | 8 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) Skills lists X-Ray, SNS, API Gateway and Node.js but no bullet uses them; be ready to defend each in an interview or cut them, because a backend interviewer will ask about one.
- (infra_hm) Capital One search-index bullet is hard to parse: 'as the Claude skill's main search tool under DB access limits' buries the why; restate the constraint and purpose up front.
- (infra_hm) UMIACS PhysTwin bullet is VLM/grasp-prompt work with no backend signal; it takes two lines of prime space an infra HM will skip.

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java policies that tune`: {'keep': 3}
- `Precomputed a tree-style search index`: {'tighten': 2, 'reframe': 1}
- `Cut LLM workflow generation time`: {'keep': 3}
- `Rebuilt a legacy test-data workflow`: {'keep': 1, 'tighten': 2}
- `Reduced end-to-end latency 34% for`: {'keep': 3}
- `Shipped a space-research tool used`: {'keep': 2, 'reframe': 1}
- `Automated EventBridge-scheduled fine-tuning of a`: {'tighten': 1, 'keep': 2}
- `Built a Python pipeline for`: {'reframe': 1, 'tighten': 2}
- `Shortened research-environment setup time 30%`: {'keep': 3}
- `Co-founded a 110+ member campus`: {'keep': 2, 'tighten': 1}
- `Engineered a C++17 order book`: {'tighten': 1, 'keep': 2}
- `Benchmarked B+ tree vs LSM`: {'keep': 3}
- `Sustained 1.26M events/sec end-to-end over`: {'keep': 3}

## Structure votes
- trim_umiacs: 2
- prune_skills: 1
- skills_order: 1
- skills_evidence_alignment: 1
- umiacs_trim_for_target: 1
