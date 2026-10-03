# quant_hft / round_03

**passed:** False  |  overall mean 7.67  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 7.67 | 7 |
| credibility | 7 | 7 |
| domain_fit | 8 | 8 |
| impact_clarity | 8 | 8 |
| overall | 7.67 | 7 |
| quantification | 7.33 | 7 |
| skim_test | 8 | 8 |
| technical_depth | 8.33 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) clarify: 1.26M events/sec and 686.7 ns/event don't match (1/686.7 ns ≈ 1.46M/s). State what each one measures (e.g. parse+match vs match only, or wall-clock vs per-event timer) or make them agree.
- (bs_detector) clarify: p50 120 ns / p99 1.2 µs (2M-event run) vs 686.7 ns mean (full run, 1.40 GHz). If they come from different runs, clock settings or scopes, say so. Otherwise the mean is far above p50 but below p99 in a way that needs a heavy p99.9 tail to explain.
- (hft_engineer) clarify: 1.26M events/sec and 686.7 ns/event average don't match (1/686.7 ns is ~1.46M/s); state whether they come from different runs or include different work (parse, I/O)
- (hft_engineer) clarify: what the 120 ns p50 / 1.2 µs p99 measures (book update only vs end-to-end) and whether it was on the same fixed 1.40 GHz clock, so it reconciles with the 686.7 ns mean
- (quant_recruiter) clarify: the latency numbers across bullets 2 and 3 (p50 120 ns, p99 1.2 us, mean 686.7 ns/event, 1.26M events/sec = ~794 ns/event). Say which run and which scope (book op only vs. end-to-end with parsing/I/O) each one measures, or an interviewer will go after the gap first.
- (quant_recruiter) clarify: what 'full matching takes 1.41x the time of a mirror-only book' means. Most screeners won't know 'mirror-only'.

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Built a C++17 order book`: {'keep': 3}
- `Indexed orders in a hash`: {'add_context': 2, 'tighten': 1}
- `Sustained 1.26M events/sec end-to-end, averaging`: {'reframe': 1, 'tighten': 1, 'add_context': 1}
- `Traced a 1.65× phantom regression`: {'keep': 3}
- `Benchmarked B+ tree vs LSM`: {'tighten': 2, 'keep': 1}
- `Writing Java policies that tune`: {'keep': 3}
- `Precomputed a tree-style search index`: {'tighten': 3}
- `Cut LLM workflow generation time`: {'keep': 3}
- `Reduced end-to-end latency 34% for`: {'keep': 3}
- `Built a Python pipeline for`: {'tighten': 3}
- `Co-founded a 110+ member campus`: {'keep': 3}

## Structure votes
- keep_project_first: 3
- split_latency_metrics: 1
- skills_order: 1
- gpa_placement: 1
- trim_offdomain_experience: 1
