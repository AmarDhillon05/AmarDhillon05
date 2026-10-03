# quant_hft / round_04

**passed:** False  |  overall mean 7.67  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 8.67 | 8 |
| concision_readability | 7 | 7 |
| credibility | 7.33 | 7 |
| domain_fit | 8 | 8 |
| impact_clarity | 7.67 | 7 |
| overall | 7.67 | 7 |
| quantification | 8 | 8 |
| skim_test | 8 | 8 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) clarify: 120 ns p50 / 1.2 µs p99 per book update vs 686.7 ns/event mean for the matching engine look inconsistent; state what each run measures so it survives the first follow-up
- (bs_detector) clarify: what 'fills' means against IEX DEEP+ (which reports trades, not your fills) and be ready to explain the 1 mismatch
- (bs_detector) Define or drop 'the Claude skill' in Capital One bullets; a quant HM won't know what the object being optimized is
- (hft_engineer) clarify: how the 120 ns p50 / 1.2 µs p99 per book update (2M-event profiling run) relates to the 686.7 ns/event matching-engine mean on the full replay. Name what each covers (book update only vs parse+match, different run/clock) so they don't read as contradicting each other.
- (quant_recruiter) clarify: how the 2M-event profiling run (120 ns p50, 1.2 µs p99) relates to the full replay's 686.7 ns/event mean. State whether they ran under the same clock and whether 686.7 ns includes parsing, so the numbers don't look contradictory.
- (quant_recruiter) clarify: what 'adaptive batch sizing' refers to in the B+ tree vs LSM bullet. As written, the negative result has no context.

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Built a C++17 order book`: {'keep': 3}
- `Indexed orders in a hash`: {'add_context': 1, 'tighten': 2}
- `Sustained 1.26M events/sec end-to-end over`: {'tighten': 2, 'add_context': 1}
- `Traced a 1.65× phantom regression`: {'keep': 3}
- `Benchmarked B+ tree vs LSM`: {'tighten': 1, 'keep': 1, 'add_context': 1}
- `Writing Java policies that tune`: {'keep': 3}
- `Precomputed a tree-style search index`: {'reframe': 2, 'tighten': 1}
- `Cut LLM workflow generation time`: {'tighten': 1, 'keep': 2}
- `Reduced end-to-end latency 34% for`: {'keep': 3}
- `Built a Python pipeline for`: {'tighten': 3}
- `Co-founded a 110+ member campus`: {'keep': 3}

## Structure votes
- keep_project_first: 3
- trim_project_to_four: 2
- use_bottom_whitespace: 1
- split_latency_vs_throughput: 1
- add_coursework_line: 1
