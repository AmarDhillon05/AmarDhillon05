# base / round_03

**passed:** False  |  overall mean 8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 8.6 | 8 |
| concision_readability | 7.8 | 7 |
| credibility | 7.6 | 7 |
| domain_fit | 8 | 8 |
| impact_clarity | 7 | 7 |
| overall | 8 | 8 |
| quantification | 7 | 7 |
| skim_test | 8 | 8 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (ats_specialist) Skills taxonomy: React and Electron are listed under 'Backend & Data'; move them to a Frontend group (or rename the row) so LLM screeners classify them correctly.
- (ats_specialist) Extracted text inserts a blank line inside every wrapped bullet; confirm the submitted PDF wraps without hard paragraph breaks so Workday/Greenhouse don't split bullets into separate fragments.
- (ats_specialist) Clarify: is the AWS bullet's work deployed or still in design? The only bullet under your top brand currently has no result or scope.
- (bigtech_recruiter) The AWS bullet is the first thing I read under Experience and it is the weakest: one bullet, present-tense, no scope or outcome. clarify: what the tuning changes or targets, even qualitatively (e.g., which decision the backtests inform).
- (bigtech_recruiter) clarify: 'UMD App Development Contracting (Client: Amazon)' vs. 'Amazon Leo' vs. 'Amazon Web Services' reads as three Amazon entities; make the contract relationship unambiguous at a glance.
- (bs_detector) clarify: 34% Kinesis latency cut — what was the pipeline before (batch? synchronous calls?) and how was end-to-end latency measured; adding Kinesis usually adds hops, so an interviewer will probe this immediately
- (bs_detector) clarify: IEX project design — 'paginated hash-based order-book storage' and 'time-based adaptive LSM store' are unusual choices for an order book; reword in plain terms you can defend, and state what the benchmark found (if you have it) or cut the bullet
- (bs_detector) clarify: PhysTwin bullet — say what you personally built for 'automated training'; 'on a PhD-led team targeting ICLR' currently carries the bullet and invites 'what did you do?'
- (senior_swe_hm) clarify: what the LSM vs B+ tree benchmark actually showed — a benchmark bullet with no finding reads as unfinished
- (senior_swe_hm) clarify: what 'checked for drift against IEX historical book data' means concretely (replay reconciliation? per-tick book diff?)
- (senior_swe_hm) PhysTwin bullet states a team goal (targeting ICLR) rather than what you built; clarify your piece of the automated training
- (startup_quant_engineer) AWS bullet is muddled: 'Java-based upper/lower bounds' makes the bounds sound like they are Java. Say what you built in Java and what it does to the bounds.
- (startup_quant_engineer) clarify: the IEX benchmark measured throughput/latency, so report the result (which store won, by roughly how much). As written it invites 'so what did you find?'

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Tuning Java-based upper/lower bounds on`: {'add_context': 1, 'reframe': 2, 'tighten': 2}
- `Rebuilt a legacy test-data workflow`: {'keep': 5}
- `Built a precomputed tree-style search`: {'tighten': 2, 'keep': 2, 'add_context': 1}
- `Cut LLM workflow generation time`: {'keep': 4, 'tighten': 1}
- `Shipped a space-research tool used`: {'tighten': 2, 'keep': 3}
- `Reduced end-to-end latency 34% for`: {'keep': 2, 'add_context': 1, 'tighten': 2}
- `Automated fine-tuning of an AWS`: {'tighten': 3, 'keep': 2}
- `Developing automated training for PhysTwin,`: {'add_context': 3, 'reframe': 2}
- `Engineered a Python pipeline rendering`: {'tighten': 2, 'keep': 3}
- `Shortened research-environment setup time 30%`: {'keep': 1, 'tighten': 4}
- `Co-founded a 110+ member campus`: {'tighten': 4, 'keep': 1}
- `Wrote Prisma SQL queries and`: {'keep': 3, 'tighten': 2}
- `Building a RAG meal-suggestion feature`: {'keep': 5}
- `Implemented a C++ order-book simulator`: {'tighten': 4, 'reframe': 1}
- `Designed paginated hash-based order-book storage`: {'keep': 2, 'add_context': 3}
- `Benchmarked a time-based adaptive LSM`: {'add_context': 5}

## Structure votes
- skills_regroup: 1
- aws_section_label: 1
- aws_bullet_strength: 1
- skills_trim: 1
- ground_iex_project: 1
- reduce_bold: 1
- aws_second_bullet_optional: 1
- trim_terplabs_to_two: 1
- keep_reverse_chron: 1
- trim_skills_line: 1
