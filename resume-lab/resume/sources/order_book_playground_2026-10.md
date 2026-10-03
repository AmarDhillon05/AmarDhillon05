# Facts read from github.com/AmarDhillon05/order-book-playground (commit af3ae95), Oct 2026
(read at Amar's request; quoted/paraphrased from source comments and committed run reports)

## Data structures (src/books/naive_book.h, exchange_book.h)
- symbol -> hash map (std::unordered_map) to a per-instrument book
- price -> ordered map (std::map; bids std::greater, asks std::less, so begin() is the inside) to the FIFO queue (std::list of order ids) resting at that price
- order id -> hash map to the order, holding an iterator into its queue (O(1) cancel/dequeue)
- ExchangeBook: price-time priority; IEX executes are DROPPED on ingest so fills are the engine's own decisions; conservation of shares asserted (submitted == traded_taker + traded_maker + cancelled + resting)
- drift counters: crossed_adds, orphans

## Latency distribution (src/logs/report_0002.txt; 2M-event run, 2026-08-14, unpinned laptop, instrument cost ~16.6 ns/sample)
- exchange book, ns per apply(), ALL messages: p50 120, p90 232, p99 1216, p99.9 2304, mean 243.7
- naive mirror, ALL: p50 100, p99 1024, p99.9 2176, mean 174.5
- NOTE: different run/config from the full-stream 686.7 ns/event mean in iex_metrics_2026-10.md; never present them as the same run.

## Log store (src/logdb/logdb.h, src/store/file_index.h)
- append-only log databases sharing a fixed-width record/leaf format; nodes reached via "a skip list hop, a tree descent"
- "The skip list belongs one level down, inside the LSM" -> the LSM backend indexes its nodes with a skip list
