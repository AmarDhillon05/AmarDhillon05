# Resume Lab: base resume report

**Deliverable:** `resume/resume.tex`, an Overleaf-ready file (pdfLaTeX, standard packages only), with compiled output at `resume/resume.pdf`.

**Before you upload it:** the phone number in the committed file is a placeholder `(XXX) XXX-XXXX`. Put your real number back in Overleaf.

## Outcome
- The resume went through **8 panel rounds** with 5 independent reviewer agents each time: big-tech recruiter, senior SWE hiring manager, startup/quant engineer, ATS specialist, and a skeptical "BS detector".
- Overall score went from **7.0 to 8.8**.
- In the final round, 4 of the 5 reviewers gave 9/10 and one gave 8/10. All five marked the resume competitive.

| round | version | overall | min dim | must-fixes | credibility | concision | impact | quantification |
|---|---|---|---|---|---|---|---|---|
| 00 | your original | 7.0 | 4 | 27 | 5.6 | 4.2 | 6.0 | 6.0 |
| 01 | v1 (research rules) | 7.8 | 6 | 16 | 6.4 | 7.0 | 6.8 | 6.4 |
| 02 | v2 | 7.8 | 6 | 10 | 6.8 | 7.4 | 7.2 | 6.8 |
| 03 | v3 (+Redshift, Leo facts) | 8.0 | 7 | 13 | 7.6 | 7.8 | 7.0 | 7.0 |
| 04 | v5 (+IEX metrics, PhysTwin fix) | 8.4 | 7 | 11 | 8.0 | 7.6 | 7.8 | 8.0 |
| 05 | v6 | 8.6 | **8** | 2 | 8.0 | 8.0 | 8.0 | 8.0 |
| 06 | v7 | 8.2 | 7 | 5 | 7.8 | 8.0 | 7.8 | 7.6 |
| 07 | v8 | 8.4 | 7 | 2 | 8.0 | 8.0 | 7.8 | 8.0 |
| 08 | v9 | **8.8** | 7 | 5 | 8.0 | 7.8 | 8.0 | 8.0 |

*(Columns from credibility onward are panel means.)*

**Did it meet the stop rule?** **No, not strictly.** The rule required every reviewer ≥ 8 on every dimension, a mean ≥ 8.5, and zero must-fixes, all on 2 consecutive rounds.
- Round 05 came closest: every dimension was ≥ 8 and the mean was 8.6, but there were 2 wording must-fixes.
- Rounds 06 and 08 each had one reviewer give a 7 on a single dimension.

**Why it plateaued:**
- The remaining notes are mostly about *density*. Nearly every bullet uses its two lines, and the IEX/UMIACS bullets carry niche terms like AnyGrasp, DEEP+ and 99,122/99,123.
- Several notes ask for facts that don't exist yet, such as the outcome of the Bedrock gating or the search-index result.
- Reviewers also disagree with each other from round to round (e.g. goal-first vs action-first on the AWS bullet), so further wording changes were oscillating rather than improving.

**After round 08 (not panel-reviewed), plus your later answers on Bedrock and PhysTwin (blind-judged: 3 of 4 new phrasings won, and the search-index rewrite was reverted):** two accuracy fixes, each checked only by the gate and a blind judge:
- "Prisma SQL" → "Prisma ORM", because Prisma is an ORM.
- The VLM is now introduced before it is referenced.

## What changed, and why (evidence: `research/findings.md`)

**Research basis:**
- 80 recent (2025–26) public LaTeX resumes, 68 of them from people with top-tier internships
- 21 resumes posted alongside their results (offers, interviews)
- 91 credible recruiter/HM sources, kept from 287 collected

**Layout and density**

| what | your original | strong 2025–26 resumes (corpus) | now |
|---|---|---|---|
| median bullet length | 240 chars | 132 chars | ~170 chars |
| bold phrases per bullet | 3.9 | 0.7 | ≤ 1, metrics only |
| body font size | ~8pt | (sources say ≥10pt) | 10pt |

- Every bullet is ≤ 2 lines, with no orphaned last lines.
- Coursework is cut; 3 credible sources rate it low value. The AWS certification is folded into Skills.
- Skills only list items that a bullet backs up.

**Bullet content:**
- Every metric now names what it measures and its baseline: the 34% is *end-to-end latency* versus S3 staging hops, and the 90% is *of 30+ surveyed developers*.
- Traffic is attributed to the product, not to an engineering change. Tortuga's 20,000+ visits now sit on the studio bullet.

**Facts you supplied mid-loop, all recorded in `resume/facts.yaml`:**
- **AWS Redshift:** the real work is tuning EC2 reservation bounds with backtested Java policies.
- **Leo:** the tool is used by the public-policy team and maintained by Leo engineers.
- **IEX:** real results: 50.9M messages replayed, 99,122/99,123 fills exact, the B+ tree 12.8× vs LSM, and 1.26M events/s.
- **PhysTwin correction:** it was *not* "automated training". The bullet now describes what you actually built.

**Structure:** the contract role is now "UMD App Development Contracting (Client: Amazon Leo)", so it no longer reads as a second Amazon entry. 3 or more reviewers flagged the old heading.

## Accepted risks (your decisions; reviewers will still notice)
- Three roles are marked "Present" alongside the full-time AWS internship. Be ready to say what's active.
- No measured result exists for the Capital One search index.
- The 93% has no tester count, and the 30% setup-time figure has no baseline.

## How every change was validated
1. **Deterministic gate (`tools/lint.py`, `tools/fact_check.py`):**
   - 1 page, ≤ 2 rendered lines per bullet, no widows, ≤ 2 bold phrases, action verbs, no repeated leading verbs.
   - **Every number and core technology must match `resume/facts.yaml`**: nothing invented, nothing misattached, and nothing superseded (e.g. the corrected PhysTwin claim).
2. **Blind pairwise judge:** an independent agent compared each changed bullet, old vs new, in randomized A/B order. Losing rewrites were reverted or replaced with the judge's version.
3. **Panel:** 5 independent reviewers per round, each with no memory of earlier rounds. They scored against `research/rubric.yaml`.

All raw reviews, scores, PDFs and decisions are in `scores/base/round_NN/` and `eval/rounds/`. Progression is in `scores/history.csv`.

## Domain variants (final)
Four versions, all built from the base by `tools/make_variant.py` (specs in `variants/*.yaml`). Variants change ordering, emphasis, bullet selection and the skills rows only. Every bullet still passes `fact_check.py` against `resume/facts.yaml`. Each variant had a 3-reviewer domain panel: domain recruiter, domain HM/engineer, and the BS detector. The cap was 4 rounds.

| file | target | rounds | overall by round | final reviewer verdicts |
|---|---|---|---|---|
| `resume/resume.tex` | General SWE / big tech | 8 (5 reviewers) | 7.0 → 8.8 | all 5 competitive |
| `resume/ai_ml_engineering.tex` | AI/ML engineering (LLM apps, agents, RAG, ML platform) | 4 | 8.0 → 8.0 → 8.0 → 8.0 | 3/3 competitive |
| `resume/backend_cloud.tex` | Backend + cloud infra / SRE | 3 (stopped: remaining must-fixes need facts) | 8.0 → 8.0 → 8.0 | 3/3 competitive |
| `resume/quant_hft.tex` | Quant dev / HFT SWE | 4 | 7.33 → 7.0 → 7.67 → 7.67 | HFT engineer: competitive; quant recruiter + BS detector: stretch |

**What each variant changes**
- **Quant**
  - Projects first.
  - 5 IEX bullets: correctness; order-book layout + p99; throughput with the scopes stated; the CPU-governor investigation; storage + negative result.
  - Skills lead with C++17/perf.
  - Cloud/LLM bullets are trimmed.
- **AI/ML**
  - Claude-skill, Bedrock and RAG bullets lead each role.
  - IEX is cut to 1 bullet.
  - The AI/ML skills row comes first.
- **Backend/cloud**
  - Search index, Kinesis and IaC/Leo lead.
  - The PhysTwin and RAG bullets are cut.
  - The skills rows list only tools a bullet backs.

**Why each variant plateaued**
- **Quant:** the project is what HFT screens want. The GPA (3.5 against a ~3.7 bar) and having only one quant-relevant item keep the recruiter at "stretch". No wording can fix that.
- **AI/ML:** steady at 8. The AWS capacity role (non-AI) sits on top in reverse-chronological order, and the reviewers want eval numbers that don't exist yet: a pass rate for the Claude skill and a grasp-accuracy figure for PhysTwin.
- **Backend:** steady at 8. The remaining asks need facts you haven't supplied: the 6,000+ document scope, the AWS backtest results (intentionally omitted), and the name of the "tree-style" index structure.

**Facts added from your repo** (`resume/sources/order_book_playground_2026-10.md`):
- the order-book data structures
- the p50/p99 from a separate 2M-event run
- the LSM's skip-list node index

The 1.26M/s end-to-end figure, the 686.7 ns matching-engine mean and the 2M-run p99 now each say what they measure. A reviewer caught that the original wording made them look contradictory.

**Post-cap polish:** the last tweaks to each variant were checked only by the gate (and, for the base, a blind judge). No panel reviewed them.

## Still useful from you
1. Are the 6,000+ documents a total corpus, or per day/per run?
2. Is the Bedrock retraining loop running in production, or built and scheduled?
3. Do you have a validation pass rate for the Claude skill, or a grasp-selection accuracy for PhysTwin?
4. What concretely is the "tree-style" search index?
