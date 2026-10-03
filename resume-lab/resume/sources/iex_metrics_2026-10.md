# IEX project metrics — provided by Amar, Oct 3 2026 (verbatim)

Order book + matching engine — C++17, live IEX DEEP+ feed
- Replayed 50,959,176 real exchange messages through a free-running matching engine with no resync; 99,122 / 99,123 fills exact — one divergence in 51M messages (37 shares).
- Conservation of shares holds exactly across 6,996,617,788 shares submitted.
- 100.00% of shares placed correctly (16,433,036); top-of-book price agreement 100.00% at every sample, price+size 99.99%.
- Sustained 1.26M events/sec end-to-end over the full stream, 8.0 GB peak RSS.
- Throughput at 1.40 GHz base clock: mirror book 485.6 ns/event (2.06M events/sec); authoritative matching engine 686.7 ns/event (1.46M events/sec) — 1.41× the mirror, for deciding every fill itself.

Storage engine — three log-database backends, shared leaf format
- B+ tree vs LSM skip list, identical 2M-record workloads: 25× fewer node hops (17,938 vs 452,434), 42× fewer summary folds, 22× faster range-summarize, 12.8× higher read throughput, page-cache hit rate 69.4% vs 32.9% — for 27% more bytes on disk.
- Served range queries from 2,602 records per node summary vs 62, answering without opening the node.
- Measured an adaptive batch-sizing policy and published it as a negative result: +71% disk, +23% hops, −32% append rate, no query win — cost is dominated by node lookup, not batch size.

Performance engineering / measurement rigor
- Hardware counters (perf, 5 runs): IPC 1.85, 55.0% cache miss rate, 2.29 branch misses per 1K instructions, wall time reproducible to ±0.09%.
- Top-down: 44.9% retiring, 25.8% frontend-bound, 21.8% backend-bound, 7.5% bad speculation.
- Diagnosed a 1.65× phantom regression as a CPU-governor artifact, not a code change, by instrumenting a null control book and the timing harness itself; cut run-to-run variance from ~6% to 0.06% by pinning and fixing the clock.
- Built a reporting harness recording CPU, core type, governor and turbo state alongside every figure, which suppresses any latency row whose p50 falls within the measured instrument cost.
