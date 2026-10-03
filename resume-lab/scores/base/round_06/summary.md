# base / round_06

**passed:** False  |  overall mean 8.2  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 8 | 8 |
| credibility | 7.8 | 7 |
| domain_fit | 8.2 | 8 |
| impact_clarity | 7.8 | 7 |
| overall | 8.2 | 8 |
| quantification | 7.6 | 7 |
| skim_test | 8.2 | 8 |
| technical_depth | 8.2 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bigtech_recruiter) The AWS role is the top brand but carries one task-only bullet; a skimmer gets no sense of what it achieved — reframe around purpose/scope already stated (availability vs cost for Redshift).
- (bigtech_recruiter) TerpLabs Redis caching bullet states intent ('to reduce database load') with no observed outcome; tighten or merge so it does not read as filler.
- (bs_detector) Bedrock fine-tuning bullet names EventBridge, Bedrock, X-Ray, SNS but ends with no outcome; it reads as AWS service listing. Lead with what the gates decide and why.
- (startup_quant_engineer) TerpLabs Redis caching bullet states intent ('to reduce database load and latency') with no outcome; tighten to what was actually observed, or merge into the Tortuga bullet.
- (startup_quant_engineer) clarify: is 686.7 ns/event a mean, median, or p50 from perf, and on what hardware? Methodology-minded interviewers will ask immediately.

## Accepted-risk flags (logged, non-blocking)
- (bs_detector) [concurrent_present_dates] Timeline: Amazon Leo contract, UMIACS and TerpLabs all show 'Present' while the AWS internship is full-time in Redmond; be ready to state what is active (or mark part-time) since an interviewer will ask.

## Bullet verdicts
- `Writing and backtesting Java policies`: {'keep': 3, 'reframe': 1, 'tighten': 1}
- `Rebuilt a legacy test-data workflow`: {'keep': 5}
- `Precomputed a tree-style search index`: {'tighten': 4, 'keep': 1}
- `Cut LLM workflow generation time`: {'tighten': 1, 'keep': 4}
- `Shipped a space-research tool used`: {'keep': 5}
- `Reduced end-to-end latency 34% for`: {'keep': 5}
- `Automated EventBridge-scheduled fine-tuning of a`: {'keep': 2, 'tighten': 2, 'reframe': 1}
- `Built a Python pipeline for`: {'tighten': 5}
- `Shortened research-environment setup time 30%`: {'keep': 4, 'add_context': 1}
- `Co-founded a 110+ member campus`: {'keep': 5}
- `Added Redis query caching over`: {'add_context': 2, 'cut': 2, 'tighten': 1}
- `Building a RAG meal-suggestion feature`: {'keep': 5}
- `Engineered a C++17 order book`: {'keep': 5}
- `Benchmarked B+ tree vs LSM`: {'keep': 4, 'tighten': 1}
- `Sustained 1.26M events/sec end-to-end over`: {'keep': 3, 'tighten': 2}

## Structure votes
- keep_project_placement: 2
- skills_evidence_alignment: 1
- skills_category_split: 1
- concurrent_roles_signal: 1
- aws_bullet_count: 1
- keep_order: 1
- merge_tortuga_redis: 1
- skills_trim_unshown: 1
- trim_terplabs_redis: 1
- merge_terplabs_redis: 1
