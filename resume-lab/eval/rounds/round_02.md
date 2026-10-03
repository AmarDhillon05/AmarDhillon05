# Round 02 → v3 decisions

**Panel result on v2:** overall 7.8 (unchanged), but every dimension rose:
- credibility 6.4 → 6.8
- quantification 6.4 → 6.8
- visual 7.4 → 8.0

See `scores/base/round_02/summary.md`.

## Candidate input (Amar, Oct 2026)
- **AWS Redshift:** tuning upper/lower bounds on EC2 capacity reserved for Redshift operations (e.g. patching), with backtested policies. Backtest numbers are omitted (preliminary/internal).
- **Leo tool:** used by Leo's public-policy team and maintained by Leo engineers.
- **Capital One 90%:** survey of 30–40 developers, so the bullet reads "90% of 30+ surveyed developers".
- **Search-index result:** unknown → accepted risk `search_index_no_result`.
- **RAG 93% tester count:** unknown → accepted risk `rag_sample_size`.

## v3 changes
| bullet | change | why |
|---|---|---|
| AWS Redshift | concrete what/why/method from candidate | 5/5 reviewers' must-fix |
| Leo | "adopted into ecosystem" → who uses and maintains it | BS detector must-fix |
| Tortuga | "for Tortuga, a class scheduler that drew 20,000+ visits…" | BS detector + HM (attribution) |
| Capital One UI | tighter; "90% of 30+ surveyed developers" | 4/5 tighten + sample size |
| IEX LSM | harness rewording tried → **reverted** (judge preferred v2) | blind pairwise |

Blind pairwise v2 vs v3: 3 of 5 went to the new wording. The other two use the judge's preferred text.
