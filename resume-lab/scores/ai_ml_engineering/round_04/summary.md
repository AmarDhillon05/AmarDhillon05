# ai_ml_engineering / round_04

**passed:** False  |  overall mean 8  |  gate errors 0

| dim | mean | min |
|---|---|---|
| ats_parseability | 9 | 9 |
| concision_readability | 8 | 8 |
| credibility | 8 | 8 |
| domain_fit | 7.67 | 7 |
| impact_clarity | 7.67 | 7 |
| overall | 8 | 8 |
| quantification | 7.33 | 7 |
| skim_test | 8 | 8 |
| technical_depth | 8 | 8 |
| visual_layout | 8 | 8 |

## Must-fix
- (ai_hm) clarify: on the Claude sub-skill decomposition, did output quality/validation pass rate hold after the 65% speedup? 'Stress-tested over repeated runs' implies a check but never states the result; an LLM-platform HM will ask immediately.
- (ai_recruiter) clarify: did the Capital One sub-skill decomposition keep or improve workflow output quality (e.g., pass rate in the stress tests)? Right now the 65% reads as speed-only, with no eval signal.
- (bs_detector) clarify: 'targeting ICLR' on PhysTwin: say whether you are on the paper or not; as written an interviewer will ask, and 'PhD-led' already signals you are not first author, so make your contribution unmistakable
- (bs_detector) PyTorch is listed in AI/ML skills but appears in no bullet; either be ready to defend hands-on PyTorch work or drop it so the skills line matches the evidence
- (bs_detector) 'stress-tested on example workflows over repeated runs' is vague filler that invites 'how many, and what did you measure?'; tighten or cut it

## Accepted-risk flags (logged, non-blocking)

## Bullet verdicts
- `Writing Java policies that tune`: {'keep': 3}
- `Cut LLM workflow generation time`: {'add_context': 1, 'tighten': 2}
- `Precomputed a tree-style search index`: {'keep': 2, 'tighten': 1}
- `Rebuilt a legacy test-data workflow`: {'keep': 3}
- `Automated EventBridge-scheduled fine-tuning of a`: {'keep': 3}
- `Reduced end-to-end latency 34% for`: {'keep': 3}
- `Shipped a space-research tool used`: {'keep': 3}
- `Built a Python pipeline for`: {'tighten': 2, 'reframe': 1}
- `Shortened research-environment setup time 30%`: {'keep': 3}
- `Building a RAG meal-suggestion feature`: {'keep': 3}
- `Co-founded a 110+ member campus`: {'keep': 2, 'tighten': 1}
- `Built a C++17 order book`: {'keep': 3}

## Structure votes
- keep_ai_skills_first: 1
- skills_ai_trim: 1
- skills_match_evidence: 1
- ai_bullet_first_in_amazon_leo: 1
