# Loop 3: one sentence, one structure (Oct 4, current)

**Your rule:** every bullet is one continuous sentence in one structure. The default is "did X to accomplish Y, which did Z", and "cut <metric> N% by doing X" is also allowed. No colons, semicolons, second sentences, preambles ("For a…", "Because…") or tacked-on endings.

**Why loop 2 failed this:** the voice check only banned semicolons, so rewrites dodged it with colons, periods and appended clauses. Nothing tested for "one natural sentence".

**What changed in the process:**
- `tools/voice.py` now has `structure_errors()`, and `tools/lint.py` treats its findings as **build errors**, not warnings. It catches:
  - colons (but not C++ `::`), semicolons, multiple sentences and dash joins;
  - preamble openers;
  - tacked-on endings: ", guided by / using / with / keeping / running …";
  - multi-clause bullets that aren't in shape A or B. A short single-clause bullet like "Co-founded a 110+ member student product studio that has shipped 5 live products" passes as is.
- The blind judges and the skeptic reviewer were both given the rule. Four judge rounds ran (`eval/loop3`, `loop3b`, `loop3c`, `loop3d`). Any bullet that broke the rule was replaced even when the judges liked it. Otherwise a rewrite went in only when both judges preferred it.

**Result:**
- 0 structure errors across all 4 versions and their original-format twins.
- Every version fits one page, and `fact_check` is clean.
- ATS coverage held: 100% / 92% / 88% / 90%.

**Final review rounds** (recruiter, skeptic with the structure check, domain specialist):

| version | overall | human voice | recruiter restates | competitive |
|---|---|---|---|---|
| General SWE / backend | 7.67 | 7.0 | 11/14 | 3/3 |
| Infra / distributed | 7.67 | 7.0 | 9/12 | 3/3 |
| Systems / quant | 7.0 | 7.0 | 9/10 | 2/3 (skeptic: "stretch", since one C++ project) |
| AI / ML | 7.67 | 7.33 | 10/11 | 3/3 |

These are slightly below loop 2's 8.0 for the base. The template makes bullets longer and denser, and reviewers still mark down the most technical ones (B+ tree vs LSM, PhysTwin, the search index) and the noun stacks in Bedrock and Redshift. The judges kept those two wordings over the alternatives.

## Every bullet that changed (loop 2.1 → loop 3)
| version | before (Loop 2.1) | after (Loop 3) |
|---|---|---|
| main | Writing Java logic that sets the upper and lower bounds on EC2 capacity that Amazon Redshift reserves for operations like patching, balancing availability against cost, and backtesting it | Writing backtested Java capacity-planning logic that sets upper and lower bounds on the EC2 capacity Amazon Redshift reserves for patching to balance availability against cost |
| main | Rebuilt the legacy tool developers use to create test-data workflows as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation, and 90% of 30+ surveyed developers preferred it | Rebuilt a legacy test-data workflow tool as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation to make editing smoother, which 90% of 30+ surveyed developers preferred |
| main | Cut AI workflow generation time 65% to under 15s by replacing a Claude skill's open-ended search with focused sub-skills that call Python tools for workflow search and validation, guided by CloudWatch and OpenSearch latency logs | Cut AI workflow generation time 65% to under 15s by splitting a Claude skill into focused sub-skills that call Python search and validation tools instead of relying on open-ended model search |
| main | Precomputed popular workflows from a 270K+ row PostgreSQL table into a category tree that the Claude skill searches first, with Redis caching full workflows, so lookups rarely touch a database gated by permissions and rate limits | Precomputed popular workflows from a 270K+ row PostgreSQL table into a Redis-cached category tree to keep lookups within the database's permission and rate limits, which became the Claude skill's main search tool |
| main | Co-built a research tool that scores and aggregates topics so Amazon Leo's public-policy staff can see what's popular, running in dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK infrastructure-as-code ready for production | Co-built a topic-scoring research tool and deployed it to dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK to show Amazon Leo's public-policy staff which research topics are popular |
| main | Automated retraining for a production Amazon Bedrock classifier that rates research documents by importance: on an EventBridge schedule a larger LLM grades its ratings, and fine-tuning runs only when the grades shift past a threshold | Built an EventBridge-scheduled LLM-as-judge check for a production Amazon Bedrock classifier that rates research documents by importance to trigger fine-tuning only when its grades shift past a threshold |
| main | For a PhD-led robotics project aimed at ICLR, built a pipeline that overlays AnyGrasp's candidate grasps on camera images in Open3D for a vision-language model, then tuned prompts so it favors grasps that avoid hitting the table | Built and prompt-tuned a pipeline for a PhD-led robotics project aimed at ICLR that overlays AnyGrasp's candidate grasps on camera images in Open3D to help a vision-language model pick grasps that avoid hitting the table |
| main | Built Redis caching in front of the Prisma ORM queries for Tortuga, the studio's class scheduler with 20,000+ visits in its first 30 days, to reduce database load and latency | Built Redis caching in front of Tortuga's Prisma ORM queries to reduce database load and latency for a class scheduler that drew 20,000+ visits in its first 30 days |
| main | Building a RAG meal-suggestion feature for the official UMD app, in which GPT-4o mini writes suggestions from scraped recipes found by SentenceBERT vector search in ChromaDB, and internal testers rated 93% of meals satisfactory | Building RAG meal suggestions for the official UMD app with SentenceBERT vector search in ChromaDB to feed GPT-4o mini real scraped recipes, which internal testers rated satisfactory for 93% of meals |
| main | Built a C++17 order book and matching engine and replayed 50.9M real IEX exchange messages through it without ever resyncing to the exchange's book, agreeing with the exchange on 99,122 of 99,123 fills and 100% of top-of-book prices | Built a C++17 order book and matching engine to replay 50.9M real IEX exchange messages without ever resyncing, which agreed with the exchange on 99,122 of 99,123 fills and 100% of top-of-book prices |
| main | Implemented B+ tree and LSM-tree backends for the event log and benchmarked them on identical 2M-record workloads, where the B+ tree gave 12.8x the read throughput and 22x faster range queries at the cost of 27% more disk space | Implemented B+ tree and LSM-tree backends for the engine's event log to compare them on identical 2M-record workloads, which showed the B+ tree giving 12.8x the read throughput and 22x faster range queries for 27% more disk |
| main | Sustained 1.26M events/sec end-to-end over the full replay, keeping each price level's orders in a std::list FIFO inside a std::map and a hash map from order ID to list iterator for O(1) cancels | Designed the order book with std::list FIFOs per price level in a std::map and an order-ID hash map to make cancels O(1), which ran the full replay at 1.26M events/sec end-to-end |
| systems/quant | Sustained 1.26M events/sec over the full replay and a 1.2 s per-message p99 on a separate 2M-event run, keeping each price level as a FIFO queue (std::list) inside a std::map, with an order-ID hash map for O(1) cancels | Designed the order book with std::list FIFOs per price level in a std::map and an order-ID hash map to make cancels O(1), which ran the full replay at 1.26M events/sec and hit a 1.2 s p99 on a separate 2M-event run |
| systems/quant | Traced an apparent 1.65x regression to the CPU frequency governor, not a code change, using perf counters and a do-nothing control book, then cut run-to-run variance from about 6% to 0.06% by pinning cores and fixing the clock | Traced an apparent 1.65x regression to the CPU frequency governor with perf counters and a do-nothing control book to rule out a code change, which led to core pinning that cut run-to-run variance from 6% to 0.06% |
| infra | Cut research-environment setup time 30% by pinning dependencies with uv and packaging the environment in Docker so every machine gets an identical setup | Cut research-environment setup time 30% by pinning dependencies with uv and packaging environments in Docker |
| AI/ML | Cut LLM workflow generation time 65% to under 15s by splitting one large Claude skill into smaller sub-skills that call Python tools for search and validation, and output quality held in repeated stress-test runs | Split a Claude skill into sub-skills backed by Python search and validation tools to stop open-ended model search, which cut LLM workflow generation time 65% to under 15s with no quality loss in stress tests |

Unchanged and already one sentence: Kinesis (both judges kept it) and Co-founded studio (short single clause). Base Bedrock and the UI rebuild stayed in their first loop-3 template form, since the judges kept them.

---
# Loop 2.1: your Oct 4 answers (current)

**Facts applied** (recorded in `resume/facts.yaml`, judged by two blind judges each, logged in `eval/loop2/decisions.jsonl`):

| bullet | change | result |
|---|---|---|
| Capital One search index | names the constraint plainly ("…so lookups rarely touch a database gated by permissions and rate limits") instead of opening with "Because…" | adopted: both judges agreed |
| Amazon Leo | says what the tool does (scores and aggregates topics so policy staff see what's popular), "co-built", "running in dev", CDK "ready for production" | adopted: judges split, but the old wording was flagged in every panel. It does **not** claim production. |
| PhysTwin | ends on your real criterion: "…tuned prompts so it favors grasps that avoid hitting the table" | adopted: both judges rated it a concrete win |
| Kinesis 34% | adding "averaged over multi-day runs" | **rejected**: one judge rated it worse. The fact is recorded, so you can say it in an interview. |

**Write throughput:** your repo (`order-book-playground` README, `src/bench/metrics.h`, run reports) has no B+ tree vs LSM write or append-throughput result. The only append number is the adaptive-batching −32% (a negative result). The storage bullet still reports reads only. If you run a write benchmark, it can go in.

**Hidden roles:**

| test | judges / panel | decision |
|---|---|---|
| Nanosat (GraphQL telemetry, 23%) in infra | 2/2 blind page judges preferred the page without it | **not used**: a 4th concurrent "Present" role alongside the AWS internship costs more credibility than the bullet adds |
| Nanosat (Rust flight software + telemetry) in systems/quant | 2/2 preferred without | **not used**: same reason (a 5th concurrent role) |
| Northrop (OpenCV C++ mine detection, 74%) in systems/quant | 2/2 page judges marginally preferred **with** it; the 3-evaluator confirmation panel then scored the page 7.33 vs 7.67 without, and flagged the bullet severity 7 (full OpenCV "on microcontrollers" invites doubt; 74% has no latency figure) | **reverted**: not strong enough as written. If you can name the hardware (e.g. a Jetson/companion computer rather than an MCU) and a frame rate or latency, it is worth retesting. |

**Confirmation rounds** (3 evaluators: recruiter, skeptic, domain specialist):
- **Base round 05:** overall 8.0, with every evaluator at 8 or above; domain fit 8.0.
- **Systems/quant:** final version is the one without Northrop; round 01 scored 7.67.

The remaining recurring flags are distinctive technical bullets that a non-engineer can't restate: the B+ tree vs LSM benchmark, PhysTwin, and the search index. Your spec keeps those nouns on purpose.

---
# Loop 2: ATS breadth + human voice (Oct 3, current)

Your feedback on loop 1 was that the bullets were concise but didn't sound human and had lost ATS breadth. Your 22-section spec then governed this loop. **These are the current deliverables. Loop 1 is kept below for history.**

| file (Jake format) | original-format twin | target |
|---|---|---|
| `resume/resume.tex` | `resume/original_format/resume.tex` | General SWE / backend (base) |
| `resume/infra_distributed.tex` | `resume/original_format/infra_distributed.tex` | Infra / distributed systems (was `backend_cloud`) |
| `resume/systems_quant.tex` | `resume/original_format/systems_quant.tex` | Systems / quant-adjacent (was `quant_hft`) |
| `resume/ai_ml_engineering.tex` | `resume/original_format/ai_ml_engineering.tex` | ML infra grounded in engineering |

**About the original-format twins:**
- Each one uses your original `.tex` layout: preamble, 8.5pt bullets, Certifications section, and title-first role headers. Only the words change.
- Spacing is auto-fitted to exactly one page by `tools/to_original_format.py`.
- Put your real phone number back in both formats before uploading.

## Results

| version | round | evaluators | overall | human voice | plain language | recruiter restates | ATS must-have |
|---|---|---|---|---|---|---|---|
| base | 00 (loop-1 final) | 6 | 7.83 | **6.0** | **5.83** | 11/14 | **47%** |
| base | 01 | 6 | 8.0 | 6.83 | 6.67 | 11/14 | 100% |
| base | 02 | 6 | 8.0 | 7.5 | 6.5 | 11/13 | 100% |
| base | 03 | 6 | 7.83 | 7.0 | 6.33 | 12/14 | 100% |
| base | 04 (final) | 6 | 7.83 | 7.33 | 6.83 | 12/14 | 100% |
| infra | 00 → 01 | 6 → 3 | 7.83 → 7.67 | 7.17 → 7.33 | 6.5 → 6.67 | 12/13 → 11/12 | 92% |
| systems/quant | 00 → 01 | 6 → 3 | 7.33 → 7.67 | 7.33 → 7.0 | 6.0 → 6.67 | 8/11 → 9/10 | 94% → 88% |
| AI/ML | 00 → 01 | 6 → 3 | 7.83 → 7.67 | 7.67 → 7.0 | 6.83 → 6.67 | 10/12 → 10/11 | 100% → 90% |

**How to read the table:**
- **Evaluators** (spec §6):
  - non-technical recruiter, who does a memory skim and restates every bullet in plain English;
  - senior SWE;
  - hiring manager;
  - skeptic, who also checks human voice;
  - ATS/LLM screener, reading real 2026 job postings;
  - one domain specialist per version.
- **Confirmation rounds** (variant round 01) used the 3 evaluators that matter most for the remaining issues, so their means are not strictly comparable with the 6-evaluator rounds.
- **"ATS must-have"** means the share of keywords that appear in at least 25% of real postings and that your facts support. A keyword you can't honestly claim never counts against you.

**Convergence (spec §19):**
- The base resume moved fast in rounds 01–02 and then flattened over 02–04, with no material gain for 2 rounds. Every evaluator rated every version competitive except systems/quant: 2 of its 6 evaluators said "stretch", and so did 1 of the 3 in its confirmation round.
- The quant "stretch" is the same structural point loop 1 found: the IEX project is the only C++/low-latency evidence on the page. Wording can't change that.

**What still caps the scores** needs facts, not wording:
1. **Capital One search index.** What kind of "strict access limits": rate limits, permissions, or query quotas?
2. **Leo tool.** What it does for the policy team, and whether you built it or deployed it.
3. **Kinesis 34%.** Per document or per batch, and how it was measured.
4. **B+ tree vs LSM.** Whether write throughput was measured. Reviewers expect the LSM's write side.
5. **PhysTwin.** Any evaluation behind "picks the right grasp more often".

## What changed

**Human voice:**
- 7 of 14 bullets used to stitch clauses with semicolons; none do now.
- Parenthetical tech dumps are gone.
- Noun stacks are broken up. For example, "Bedrock document-importance classifier" became "a production Amazon Bedrock classifier that rates research documents by importance".
- Bullets now say what the thing does for someone: "the legacy tool developers use to create test-data workflows", "a vision-language model ... picks the right grasp".

**ATS breadth:**
- Skills are regrouped into the categories screeners parse, with matchable forms: AWS CDK (infrastructure as code), GitHub Actions (CI/CD), retrieval-augmented generation (RAG), unit testing (Pytest, Jest), data structures and algorithms.
- Each version's Skills carries only items its facts back.
- Three skills you listed originally were dropped from AI/ML because no bullet supports them: PyTorch, CUDA and MongoDB. Add any back only if you can discuss real use. PyTorch is the single most-requested term in the ML postings.
- "Expected May 2028" now replaces "May 2028", so parsers don't read it as a completed degree.

**Ownership:** the TerpLabs studio claim and your own Redis work are now separate bullets, and "20,000+ visits" is no longer bolded on the caching bullet.

**Mechanisms:**
- The Claude-skill bullet now says why it got faster: open-ended model search was replaced by Python search and validation tools.
- The order-book bullet names the real containers: a std::list FIFO per price level and an order-ID → list-iterator hash map for O(1) cancels.

**Structure:**
- Capital One order is tuned per version: the UI tool first in the base, so "workflow" is defined before it is used; backend or AI work first in the variants.
- The research-environment setup bullet leaves the base (it stays in infra). The studio bullet leaves the variants.

## How it was validated

1. **Gate**, now including the voice checks in `tools/voice.py`:
   - inflated words, semicolons, parentheticals, noun stacks, tool inventories, metric stacking;
   - all calibrated against 1,442 bullets from the reference corpus.
   - Plus ≤3 bullets per role, with a documented exception of 4 for the quant IEX project, and the existing 1-page, 2-line and `fact_check` rules.
2. **Two independent blind judges per candidate.** They answered "which communicates more useful information with less reader effort?" under randomized labels.
   - A rewrite was adopted only when both judges preferred it and at least one named a **concrete** advantage.
   - Exceptions are logged and limited to accuracy or parse fixes that 3+ evaluators flagged.
3. **Decision log.** `eval/loop2/decisions.jsonl` has 106 entries: every proposed change, accepted or rejected, with the reason and the evaluator evidence.
4. **Raw material:**
   - every review, summary, PDF and gate result is under `scores/loop2/<version>/round_NN/`;
   - the job postings used are in `corpus/jds/`;
   - 14 redacted reference resumes are in `corpus/references/`.

## Questions only you can answer
These are the five facts listed under Results, plus the following (also in `resume/annotations.yaml`):
- **Nanosat and Northrop:** may they appear in some versions? Nanosat would help the infra and systems versions most.
- **Interview stories:** which story per role would you most want to tell?
- **Ownership:** did you design the search-index tree yourself, and did you build all of the Bedrock loop or only part of it?

---
# Loop 1 (history)

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
- No measured result exists for the Capital One search index, and no pass rate exists for the Claude skill.
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
- **Backend:** steady at 8. The remaining asks need facts you haven't supplied: the AWS backtest results (intentionally omitted). The 6,000+ scope and the index structure were answered later (see below).

**Facts added from your repo** (`resume/sources/order_book_playground_2026-10.md`):
- the order-book data structures
- the p50/p99 from a separate 2M-event run
- the LSM's skip-list node index

The 1.26M/s end-to-end figure, the 686.7 ns matching-engine mean and the 2M-run p99 now each say what they measure. A reviewer caught that the original wording made them look contradictory.

**Post-cap polish:** the last tweaks to each variant were checked only by the gate (and, for the base, a blind judge). No panel reviewed them.

## Final answers applied (Oct 3, not panel-reviewed)
Your last answers were folded in, then checked by the gate on all four files (0 errors, each one page) and by a blind judge on the base (both new phrasings won; `scores/base/final_answers/`). No panel re-reviewed them, because the round caps were already reached.
- **Bedrock:** now "a production EventBridge fine-tuning loop" (base, AI, backend).
- **Search index:** "tree-style" became "category-keyed tree index" (base, backend; the AI variant inherits it from the base).
- **Kinesis (backend):** "a 6,000+ document scraped research corpus", so the 6,000+ reads as the total corpus.
- **Claude skill:** no pass rate exists, so it is logged as accepted risk `claude_skill_eval_metric` and no number was invented.

## Still useful from you
1. A grasp-selection accuracy for PhysTwin, if one is ever measured.
2. AWS Redshift backtest results, once they're final and approved to share.
3. Your real phone number (Overleaf only), and whether to keep the 3.5 GPA on the quant variant (it's kept for now).
