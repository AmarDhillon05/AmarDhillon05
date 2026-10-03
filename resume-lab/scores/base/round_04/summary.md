# base / round_04

**passed:** False  |  overall mean 8.4  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 7.6 | 7 |
| credibility | 8 | 8 |
| domain_fit | 8.4 | 8 |
| impact_clarity | 7.8 | 7 |
| overall | 8.4 | 8 |
| quantification | 8 | 8 |
| skim_test | 8.2 | 8 |
| technical_depth | 8.4 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (ats_specialist) Clarify the order-book third bullet: '1.41× the cost of a passive mirror book for deciding every fill itself' needs re-reading by humans and LLM screeners alike.
- (ats_specialist) Clarify how the B+ tree vs LSM benchmark relates to the order book (event log storage?); as written it reads like a separate project.
- (bigtech_recruiter) Order-book bullet 3 ('1.41x the cost of a passive mirror book for deciding every fill itself') is unreadable for a non-specialist. Simplify it or drop the comparison clause.
- (bigtech_recruiter) Order-book bullet 2 (B+ tree vs LSM stores) doesn't explain how it relates to the matching engine. Clarify: is this the engine's log/storage layer? If not, it looks bolted on.
- (bs_detector) Tortuga bullet: 20,000+ visits is product traction, not the result of your Prisma/Redis work; as written it reads like borrowed credit. Separate the claim or state what caching achieved.
- (bs_detector) Order book benchmark bullet: unclear which store won (B+ tree or LSM) and how it relates to the order book; the direction of 12.8x / 22x / 27% must be readable in one pass.
- (bs_detector) Order book throughput bullet: '1.41x the cost of a passive mirror book for deciding every fill itself' is opaque; an interviewer will stop here and ask what it means.
- (senior_swe_hm) Clarify the order-book project's B+ tree vs LSM bullet: say what the log store holds (e.g., the replayed event log) so it reads as part of the engine, not a separate benchmark.
- (senior_swe_hm) Rephrase '1.41× the cost of a passive mirror book for deciding every fill itself'; as written it takes two reads to see it means matching overhead vs. passively mirroring the feed.
- (startup_quant_engineer) Order book bullet 3: '1.41× the cost of a passive mirror book for deciding every fill itself' is hard to parse; rephrase so the comparison reads in one pass.
- (startup_quant_engineer) Order book bullet 2: B+ tree vs LSM benchmark lacks context on what is being stored (the engine's event log?) and how it ties to the engine; clarify: what the log stores.

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java to tune upper/lower`: {'tighten': 4, 'keep': 1}
- `Rebuilt a legacy test-data workflow`: {'keep': 5}
- `Precomputed a tree-style search index`: {'keep': 4, 'tighten': 1}
- `Cut LLM workflow generation time`: {'tighten': 1, 'keep': 4}
- `Shipped a space-research tool used`: {'keep': 5}
- `Reduced end-to-end latency 34% for`: {'keep': 5}
- `Automated Bedrock source-relevancy model fine-tuning`: {'keep': 3, 'tighten': 2}
- `Built a Python pipeline for`: {'tighten': 5}
- `Shortened research-environment setup time 30%`: {'keep': 5}
- `Co-founded a 110+ member campus`: {'keep': 4, 'add_context': 1}
- `Wrote Prisma SQL queries and`: {'keep': 3, 'reframe': 1, 'tighten': 1}
- `Building a RAG meal-suggestion feature`: {'keep': 5}
- `Engineered a C++17 order book`: {'keep': 5}
- `Benchmarked B+ tree vs LSM`: {'add_context': 4, 'reframe': 1}
- `Sustained 1.26M events/sec end-to-end with`: {'reframe': 3, 'tighten': 2}

## Structure votes
- keep_section_order: 2
- expand_acronyms_once: 1
- keep_current_order: 1
- terplabs_bullet_merge: 1
- keep_education_top: 1
- terplabs_lead_with_engineering: 1
- trim_skills_cloud_line: 1
- bold_consistency: 1
