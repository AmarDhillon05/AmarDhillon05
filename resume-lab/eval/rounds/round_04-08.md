# Rounds 04–08 (v5 → v9) decisions

| round | version reviewed | overall | blocking items | what changed for the next version |
|---|---|---|---|---|
| 04 | v5 | 8.4 | 11 (IEX bullet clarity, ×5 each) | Dropped the opaque "1.41× mirror book" clause; stated the B+ tree won and that the stores hold the simulation's event logs; restructured PhysTwin; bold reserved for outcome metrics |
| 05 | v6 | 8.6 (all dims ≥ 8) | 2 (BS detector) | Moved Tortuga's traffic onto the studio bullet (it is the product's traffic, not the caching's); AWS bullet now leads with the method; dropped the clock detail |
| 06 | v7 | 8.2 | 5 | Merged the caching bullet into the studio bullet (it was left outcome-less; 3/5 said cut or merge); Bedrock now leads with the decision gates; "averaging" names the ns/event statistic (derived from throughput) |
| 07 | v8 | 8.4 | 2 (HM) | PhysTwin prompt work gets a stated purpose; AWS gets its stage ("initial backtests complete") |
| 08 | v9 | 8.8 (four 9s) | 5 | Hit the round cap. Two post-cap accuracy fixes, gate + blind judge only (2/2 wins), not panel-reviewed: "Prisma ORM" (Prisma is an ORM, not "Prisma SQL"); the VLM is introduced before it is referenced |

Tooling fixes along the way:
- `fact_check` supports merged bullets (`% fact: a+b`) and rejects superseded facts.
- The text helper now renders `$\times$` correctly. Before this fix, the judge saw "12.8 read".
- Reviewers get plain `pdftotext` output.
