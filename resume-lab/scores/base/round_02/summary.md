# base / round_02

**passed:** False  |  overall mean 7.8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 8.2 | 8 |
| concision_readability | 7.4 | 7 |
| credibility | 6.8 | 6 |
| domain_fit | 8 | 8 |
| impact_clarity | 7.2 | 7 |
| overall | 7.8 | 7 |
| quantification | 6.8 | 6 |
| skim_test | 7.8 | 7 |
| technical_depth | 7.8 | 7 |
| visual_layout | 8 | 8 |

## Must-fix
- (ats_specialist) AWS bullet is a single generic present-tense line ('Researching and implementing...'); the top brand carries the weakest content — clarify: what component/approach and any stated result so far
- (ats_specialist) clarify: baselines for '90% of surveyed users' (how many surveyed) and '30%' setup time (from what) so numbers survive a screener follow-up
- (bigtech_recruiter) AWS internship, the most recognizable line on the page, has one vague in-progress bullet ('Researching and implementing...'); make it say concretely what is being built, even if work-in-progress.
- (bigtech_recruiter) clarify: the Capital One search-index bullet ends at intent ('to minimize DB queries under access limits') with no stated outcome.
- (bs_detector) Clarify the overlap: Jun–Aug 2026 lists Capital One (Richmond) plus IEX project, UMD contracting and UMIACS (College Park) all active; an interviewer will ask how many hours each got.
- (bs_detector) Clarify: what does 'adopted into Leo's ecosystem' concretely mean (who uses it, in what capacity)? As written it reads as puffery.
- (bs_detector) Clarify: is Tortuga the class scheduler? The bullet pairs a caching change with a traffic number, implying causation that isn't there.
- (bs_detector) Clarify sample sizes for '90% of surveyed users' and '93% ... internal testers'; small-n percentages collapse under one question.
- (senior_swe_hm) AWS bullet is a single vague present-tense task line on the top brand; say what component/problem in Redshift you own and the approach, even if results are pending.
- (senior_swe_hm) Clarify baselines/sample sizes: 90% of how many surveyed users, 93% of how many testers, 34% latency from what prior architecture.
- (senior_swe_hm) TerpLabs caching bullet pairs an unquantified optimization with 20,000+ visits that the caching did not cause; separate or reframe so the metric is attributable.
- (startup_quant_engineer) IEX project: the bullets describe measuring throughput and latency but report no results. Clarify: state the measured numbers (e.g., p50/p99 latency, ops/sec, LSM vs B+ tree outcome) or drop the measurement claim.
- (startup_quant_engineer) AWS bullet is a vague one-liner ('Researching and implementing'). Clarify what component or problem is concretely being optimized, without inventing outcomes.

## Accepted-risk flags (logged, non-blocking)
- (bigtech_recruiter) [concurrent_present_dates] clarify: whether UMD App Dev Contracting, UMIACS, and TerpLabs are all actively ongoing during the Sep–Dec 2026 AWS internship; four simultaneous 'Present' roles reads as overcommitted or padded.
- (senior_swe_hm) [concurrent_present_dates] Clarify overlapping timelines: UMD contracting, UMIACS and TerpLabs all 'Present' while interning on-site in Redmond, and the IEX project overlaps the Capital One summer. Mark paused roles or end dates.

## Bullet verdicts
- `Researching and implementing Java-based utilization`: {'add_context': 5}
- `Rebuilt a legacy test-data workflow`: {'tighten': 4, 'keep': 1}
- `Built a precomputed tree-style search`: {'add_context': 5}
- `Cut LLM workflow generation time`: {'keep': 5}
- `Shipped a space-research tool for`: {'tighten': 3, 'reframe': 2}
- `Reduced end-to-end latency 34% for`: {'keep': 3, 'add_context': 1, 'tighten': 1}
- `Automated fine-tuning of an AWS`: {'keep': 2, 'tighten': 3}
- `Developing automated training for PhysTwin,`: {'add_context': 4, 'tighten': 1}
- `Engineered a Python pipeline rendering`: {'keep': 2, 'reframe': 1, 'tighten': 2}
- `Shortened research-environment setup time 30%`: {'keep': 2, 'add_context': 1, 'tighten': 2}
- `Co-founded a 110+ member campus`: {'keep': 3, 'tighten': 2}
- `Wrote Prisma SQL queries and`: {'tighten': 1, 'reframe': 4}
- `Building a RAG meal-suggestion feature`: {'keep': 3, 'add_context': 2}
- `Implemented a C++ order-book simulator`: {'keep': 1, 'tighten': 4}
- `Designed paginated hash-based order-book storage`: {'tighten': 2, 'add_context': 3}
- `Benchmarked a time-based adaptive LSM`: {'add_context': 5}

## Structure votes
- skills_keywords: 1
- bullet_wrap_extraction: 1
- cert_placement: 1
- aws_bullet_upgrade: 1
- bold_on_outcomes: 1
- clarify_concurrent_dates: 1
- aws_bullet_strengthen_or_demote_visual: 1
- explain_concurrency: 1
- trim_skills_dup: 1
- aws_role_substance: 1
- condense_concurrent_roles: 1
- consistent_bold: 1
- bold_anchor_iex: 1
- aws_bullet_count: 1
