# base / round_08

**passed:** False  |  overall mean 8.8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 7.8 | 7 |
| credibility | 8 | 8 |
| domain_fit | 8.2 | 8 |
| impact_clarity | 8 | 8 |
| overall | 8.8 | 8 |
| quantification | 8 | 8 |
| skim_test | 8.4 | 8 |
| technical_depth | 8.6 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) clarify: the B+ tree vs LSM benchmark is for 'the simulation's event logs' — the link to the order book is unexplained and invites 'why did a matching engine need an event-log store?'
- (bs_detector) clarify: 'the VLM' in the PhysTwin bullet has no antecedent — say what the VLM is doing in the pipeline or drop the clause
- (bs_detector) 'Prisma SQL' is not a thing (Prisma is an ORM); write 'Redis caching in front of a Prisma/SQL data layer' or similar so a backend interviewer doesn't wince
- (senior_swe_hm) UMIACS bullet 1: 'the VLM' is never introduced; reader can't tell which model was prompt-tuned or what the tuning achieved
- (senior_swe_hm) Amazon Leo fine-tuning bullet ends at mechanism (EventBridge, X-Ray, SNS) with no stated outcome; clarify: what did gating or automation change for the team

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java policies that tune`: {'keep': 5}
- `Rebuilt a legacy test-data workflow`: {'keep': 5}
- `Precomputed a tree-style search index`: {'tighten': 5}
- `Cut LLM workflow generation time`: {'keep': 5}
- `Shipped a space-research tool used`: {'keep': 5}
- `Reduced end-to-end latency 34% for`: {'keep': 5}
- `Automated fine-tuning of a Bedrock`: {'tighten': 3, 'add_context': 1, 'keep': 1}
- `Built a Python pipeline for`: {'tighten': 2, 'reframe': 2, 'add_context': 1}
- `Shortened research-environment setup time 30%`: {'keep': 5}
- `Co-founded a 110+ member campus`: {'keep': 4, 'tighten': 1}
- `Building a RAG meal-suggestion feature`: {'keep': 5}
- `Engineered a C++17 order book`: {'keep': 4, 'tighten': 1}
- `Benchmarked B+ tree vs LSM`: {'keep': 3, 'add_context': 1, 'tighten': 1}
- `Sustained 1.26M events/sec end-to-end over`: {'keep': 4, 'tighten': 1}

## Structure votes
- edu_date_on_school_line: 1
- certification_own_line_ok: 1
- bold_consistency: 1
- project_bullet_order: 1
- merge_iex_perf_into_first_bullet: 1
- skills_trim_rag: 1
- keep_order: 1
- trim_skills_cloud: 1
- keep_experience_first: 1
- trim_skills_cloud_line: 1
