# ai_ml_engineering / round_01

**passed:** False  |  overall mean 8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 8.33 | 8 |
| concision_readability | 8 | 8 |
| credibility | 8 | 8 |
| domain_fit | 7 | 7 |
| impact_clarity | 7.67 | 7 |
| overall | 8 | 8 |
| quantification | 7 | 7 |
| skim_test | 7 | 7 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (ai_hm) clarify: did output quality/accuracy hold (or how was it checked) after decomposing the Claude skill into sub-skills? Speed alone doesn't show eval discipline.
- (ai_hm) clarify: what does the Bedrock source-relevancy model do and how is a retraining run judged 'redundant' (data-change gate vs. metric gate)?
- (ai_hm) PhysTwin 'tuned its detection prompts' is vague; state what was tuned toward, or cut the clause.
- (ai_recruiter) The IEX order book project is the only Projects entry and is unrelated to LLM/ML; for this domain it competes with the AI story instead of supporting it.
- (ai_recruiter) clarify: what 'source-relevancy model' fine-tuning on Bedrock means (which base model, what task) so an AI HM can probe it.
- (bs_detector) clarify: what 'fine-tuning of a Bedrock source-relevancy model' means. Is it a Bedrock custom-model fine-tune or a classifier hosted near Bedrock, and what is the 'redundant' gate criterion? An AI interviewer will ask both first.
- (bs_detector) clarify: 'tuned its detection prompts' (UMIACS). Say what was tuned and what improved, or cut the clause; as written it is the vaguest AI claim on the page.
- (bs_detector) Skills line 'Claude (skills, sub-skill decomposition)' and 'VLM prompting' read as buzzword padding; list them as tools (Claude, Bedrock) and let the bullets show the technique.

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java policies that tune`: {'keep': 3}
- `Cut LLM workflow generation time`: {'tighten': 1, 'keep': 2}
- `Precomputed a tree-style search index`: {'add_context': 1, 'tighten': 2}
- `Rebuilt a legacy test-data workflow`: {'keep': 3}
- `Automated fine-tuning of a Bedrock`: {'add_context': 3}
- `Reduced end-to-end latency 34% for`: {'keep': 3}
- `Shipped a space-research tool used`: {'tighten': 3}
- `Built a Python pipeline for`: {'reframe': 2, 'tighten': 1}
- `Shortened research-environment setup time 30%`: {'keep': 2, 'tighten': 1}
- `Building a RAG meal-suggestion feature`: {'tighten': 1, 'keep': 2}
- `Co-founded a 110+ member campus`: {'keep': 3}
- `Engineered a C++17 order book`: {'keep': 3}
- `Benchmarked B+ tree vs LSM`: {'cut': 3}

## Structure votes
- skills_ai_first: 3
- bold_ai_wins: 2
- shrink_offdomain_project: 1
- condense_iex_project: 1
- trim_iex_project: 1
