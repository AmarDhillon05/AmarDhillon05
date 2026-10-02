# base / round_01

**passed:** False  |  overall mean 7.8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 8 | 8 |
| concision_readability | 7 | 7 |
| credibility | 6.4 | 6 |
| domain_fit | 7.8 | 7 |
| impact_clarity | 6.8 | 6 |
| overall | 7.8 | 7 |
| quantification | 6.4 | 6 |
| skim_test | 7.6 | 7 |
| technical_depth | 7.4 | 7 |
| visual_layout | 7.4 | 7 |

## Must-fix
- (ats_specialist) Two separate 'Amazon' employer entries (Amazon Web Services and Amazon via UMD contracting) can be merged/deduped incorrectly by parsers; make the contracting employer name unambiguous.
- (ats_specialist) Clarify: what 'Claude skill' means; non-standard term that ATS keyword matching and non-AI recruiters won't recognize (e.g., 'LLM agent workflow').
- (ats_specialist) Contact line wraps onto a second line; keep it on one line so parsers capture GitHub as part of the header block.
- (bigtech_recruiter) Clarify: distinguish 'Amazon Web Services' (internship) from 'Amazon (via UMD App Development Contracting)' so it doesn't look like the same brand listed twice.
- (bigtech_recruiter) AWS internship has a single vague bullet ('Researching and implementing...'); it's your top brand and currently says the least.
- (bs_detector) Clarify: what does '90% satisfaction vs. the old tool' measure, and how many users rated it?
- (bs_detector) Clarify: what metric improved 34% in the Kinesis/Lambda pipeline (throughput, end-to-end latency, cost)?
- (bs_detector) Clarify: what 'adopted into Leo's ecosystem' concretely means (which teams/users, internal vs production).
- (bs_detector) TerpLabs Tortuga bullet attributes 20,000+ visits to the product, not the caching work; state the caching result or decouple the two.
- (senior_swe_hm) clarify: what the 34% speedup measured (end-to-end latency, throughput, cost) and the baseline.
- (senior_swe_hm) clarify: who rated the 90% satisfaction (how many users, what survey) — otherwise soften or cut the number.
- (senior_swe_hm) The AWS Redshift bullet is a placeholder-level task description; either state what is being optimized (component/approach) or accept it as a single brand line.
- (senior_swe_hm) IEX project bullets have no results; state what the LSM vs B+ tree benchmark found, or reframe as design work.
- (startup_quant_engineer) Clarify: the IEX project says throughput/latency were measured with rdtscp and perf but reports no result. State what the LSM vs B+ tree comparison found, or reframe the bullet so it doesn't promise a number.
- (startup_quant_engineer) Clarify: what the 34% speedup measures (end-to-end latency? throughput?) and what the 65% baseline was. Unlabeled percentages fall apart under one follow-up question.
- (startup_quant_engineer) Clarify: '90% satisfaction' and '93% meal satisfaction' need a scope (how many users/testers) or should be softened; otherwise they read as survey filler.

## Accepted-risk flags (logged, non-blocking)
- (ats_specialist) [concurrent_present_dates] Clarify overlapping dates: Amazon contract, UMIACS, and TerpLabs all say 'Present' while AWS internship is in Redmond Sep–Dec 2026; LLM screeners flag 4 simultaneous roles. Confirm which are paused or remote.
- (bigtech_recruiter) [concurrent_present_dates] Clarify: which roles are actually active during the Sep–Dec 2026 Redmond AWS internship? Four College Park roles marked 'Present' alongside it reads as overcommitted or inflated.
- (bs_detector) [concurrent_present_dates] Clarify date overlaps: AWS internship in Redmond (Sep–Dec 2026) overlaps Amazon contract, UMIACS, and TerpLabs all marked 'Present'; mark paused/ended roles or change end dates honestly.
- (senior_swe_hm) [concurrent_present_dates] Clarify timeline overlap: three roles marked 'Present' in College Park while interning at AWS in Redmond Sep–Dec 2026; mark ended/paused roles with end dates or note remote/part-time.
- (startup_quant_engineer) [concurrent_present_dates] Clarify the overlapping dates: an AWS Redmond internship (Sep–Dec 2026) running alongside 'Present' roles in College Park reads as a conflict. Mark the concurrent ones part-time/remote or end-date them.

## Bullet verdicts
- `Researching and implementing Java-based utilization`: {'add_context': 5}
- `Rebuilt the legacy UI of`: {'tighten': 5}
- `Built a precomputed tree-style workflow`: {'tighten': 2, 'add_context': 1, 'reframe': 2}
- `Cut workflow generation time 65%`: {'reframe': 3, 'tighten': 2}
- `Shipped an Amazon Leo space-research`: {'tighten': 4, 'reframe': 1}
- `Sped up a pipeline routing`: {'keep': 1, 'tighten': 1, 'add_context': 3}
- `Automated fine-tuning of an AWS`: {'tighten': 4, 'add_context': 1}
- `Developing automated training for PhysTwin,`: {'add_context': 5}
- `Engineered a Python pipeline rendering`: {'keep': 4, 'tighten': 1}
- `Reduced research-environment setup time 30%`: {'tighten': 4, 'keep': 1}
- `Co-founded and scaled a 110+`: {'keep': 4, 'tighten': 1}
- `Developed Prisma-based SQL querying with`: {'reframe': 5}
- `Building a RAG meal-suggestion feature`: {'tighten': 4, 'add_context': 1}
- `Implemented a C++ order-book simulator`: {'keep': 1, 'tighten': 4}
- `Designed paginated hash-based storage for`: {'tighten': 1, 'add_context': 4}
- `Benchmarked a time-based adaptive LSM`: {'add_context': 5}

## Structure votes
- fix_present_dates: 2
- aws_entry_weight: 2
- header_one_line: 1
- skills_recategorize: 1
- amazon_entry_naming: 1
- aws_bullet_expand: 1
- merge_or_label_amazon: 1
- fix_concurrent_dates: 1
- trim_amazon_contract_stack: 1
- contact_one_line: 1
- trim_skills_aws: 1
- trim_skills: 1
- aws_bullets: 1
- concurrency_labels: 1
- skills_trim: 1
