# quant_hft / round_02

**passed:** False  |  overall mean 7  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 8.67 | 8 |
| concision_readability | 7.33 | 7 |
| credibility | 8 | 8 |
| domain_fit | 8 | 8 |
| impact_clarity | 8 | 8 |
| overall | 7 | 7 |
| quantification | 8 | 8 |
| skim_test | 8 | 8 |
| technical_depth | 7.67 | 7 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) Clarify the 1.41× clause: state plainly that full matching costs 1.41× the time of a mirror-only book; as written it reads like a riddle.
- (bs_detector) Clarify 'LSM skip-list stores': it is an LSM tree with a skip-list memtable? Ambiguous naming invites a gotcha follow-up.
- (hft_engineer) clarify: the order book's core data-structure / memory-layout choice (how price levels and order IDs are stored) — this is the first thing an HFT interviewer asks and the page is silent on it
- (hft_engineer) clarify: '1.41× a passive book that only mirrors feed state' — reads ambiguously; state it as overhead of matching vs. a mirror-only baseline
- (quant_recruiter) Clarify: the '1.41x a passive book' comparison is hard to parse; state plainly that full matching costs 1.41x the time of a feed-mirroring-only book.
- (quant_recruiter) Clarify: '686.7 ns/event at a 1.40 GHz base clock' raises the question of why base clock is cited; make sure it is phrased as the fixed-clock test condition so it reads as rigor, not hedging.

## Accepted-risk flags (logged, non-blocking)
- (bs_detector) [iex_tail_latency] Latency is mean-only (686.7 ns/event); an HFT interviewer will immediately ask for p50/p99. Add tail percentiles if measured, or be ready to explain why not.

## Bullet verdicts
- `Built a C++17 order book`: {'keep': 3}
- `Sustained 1.26M events/sec end-to-end, averaging`: {'tighten': 3}
- `Traced a 1.65× phantom regression`: {'keep': 3}
- `Benchmarked B+ tree vs LSM`: {'tighten': 3}
- `Writing Java policies that tune`: {'keep': 2, 'add_context': 1}
- `Precomputed a tree-style search index`: {'add_context': 1, 'tighten': 2}
- `Cut LLM workflow generation time`: {'keep': 3}
- `Reduced end-to-end latency 34% for`: {'keep': 3}
- `Built a Python pipeline for`: {'tighten': 3}
- `Co-founded a 110+ member campus`: {'keep': 3}

## Structure votes
- keep_project_first: 1
- trim_ml_research: 1
- projects_first_keep: 1
- skills_lead_cpp: 1
- keep_projects_first: 1
- skills_cpp_first: 1
- trim_offdomain_ml: 1
