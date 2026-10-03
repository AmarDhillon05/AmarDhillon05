# quant_hft / round_01

**passed:** False  |  overall mean 7.33  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 8.33 | 8 |
| concision_readability | 7 | 7 |
| credibility | 7.67 | 7 |
| domain_fit | 7.33 | 7 |
| impact_clarity | 7.33 | 7 |
| overall | 7.33 | 7 |
| quantification | 7.67 | 7 |
| skim_test | 7.33 | 7 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (bs_detector) Reorder the project bullets so correctness (fills/top-of-book) and latency/throughput plus the perf-governor investigation come first; storage benchmarks last.
- (bs_detector) Clarify: 'Published' the batch-sizing negative result — where (README, write-up, repo)? If just a README note, say 'Documented'; otherwise an interviewer will ask for the publication.
- (bs_detector) Rephrase '1.41x a passive mirror book (485.6 ns)' — reads ambiguous; state plainly that the matching engine costs 1.41x a passive book that only tracks state.
- (bs_detector) Be ready to defend 686.7 ns/event and 1.26M events/sec against HFT expectations; the 1.40 GHz base-clock context helps, keep it, but know your hot path breakdown.
- (hft_engineer) clarify: what '1.41× a passive mirror book (485.6 ns)' means; it reads like an overhead ratio but needs a plain explanation of what the mirror book skips
- (hft_engineer) clarify: 'Published' a negative result—where? If it is a README or writeup in the repo, say 'Documented' to avoid implying a publication
- (quant_recruiter) Move the throughput/latency bullet (1.26M events/sec, 686.7 ns/event) to the top of the IEX project; it is the headline an HFT recruiter screens for.
- (quant_recruiter) clarify: what 'Published' means in the adaptive batch-sizing bullet (a writeup, a repo README, a paper?). Otherwise reword to 'Evaluated' or 'Documented'.
- (quant_recruiter) Clarify how the B+ tree vs LSM event-log benchmark relates to the matching engine; right now it reads like a separate storage side-project.

## Accepted-risk flags (logged, non-blocking)
- (hft_engineer) [iex_tail_latency] clarify: whether 686.7 ns/event is a mean only; if you have p50/p99 or other tail numbers, a tail number is what an HFT reviewer looks for first

## Bullet verdicts
- `Engineered a C++17 order book`: {'keep': 2, 'tighten': 1}
- `Benchmarked B+ tree vs LSM`: {'tighten': 2, 'add_context': 1}
- `Published an adaptive batch-sizing policy`: {'reframe': 3}
- `Sustained 1.26M events/sec end-to-end; the`: {'tighten': 2, 'add_context': 1}
- `Traced a 1.65x phantom regression`: {'keep': 1}
- `Writing Java policies that tune`: {'keep': 3}
- `Precomputed a tree-style search index`: {'tighten': 3}
- `Cut LLM workflow generation time`: {'keep': 3}
- `Reduced end-to-end latency 34% for`: {'keep': 3}
- `Automated fine-tuning of a Bedrock`: {'tighten': 3}
- `Built a Python pipeline for`: {'add_context': 1, 'keep': 1, 'tighten': 1}
- `Co-founded a 110+ member campus`: {'tighten': 1, 'keep': 2}
- `Traced a 1.65× phantom regression`: {'keep': 2}

## Structure votes
- reorder_project_bullets: 2
- skills_order: 2
- merge_storage_bullets: 2
- cut_or_merge_batch_sizing: 1
- keep_projects_first: 1
- reorder_iex_bullets: 1
