# Findings: what 2025–26 SWE resumes look like and what screeners want

Evidence base:
- **Resume corpus.** 80 public LaTeX resumes with 1,442 bullets, all last edited 2025–26. 68 of them show a FAANG, top-startup or quant role. Stats are in `corpus_stats.md`.
- **Advice corpus.** 287 sources were collected and 91 kept after credibility scoring for role, outcome evidence, recency and validation. They yield 344 atomic claims with verified quotes. See `sources.md` and `../corpus/advice.jsonl`. Counts below are *independent* credible sources; sources from the same org are counted once.
- **Outcome-backed resumes.** These are in `../corpus/outcome_resumes.jsonl` and qualify the statements below where they are noted.

## 1. Quantitative targets (corpus vs. Amar's baseline)

| metric | corpus (all) | corpus (top-tier) | Amar baseline | target |
|---|---|---|---|---|
| bullet length, median chars | 132 | 124 | **240** | 120–180 |
| bullet length, q75 chars | 195 | 190 | **297** | ≤ 200 (hard cap ~2 rendered lines) |
| bold phrases / bullet | 0.68 | 0.61 | **3.88** | ≤ 1 (cap 2) |
| bullets with a number | 50% | 47% | 56% | 50–75%. Not every bullet needs one. |
| tech terms / bullet | 1.9 | 1.9 | ~4–5 | 2–3 that carry a decision |
| bullets / resume | 16 | 17 | 16 | 13–17 |
| section order | Edu > Exp > Projects > Skills dominates (~60%) | | Edu > Cert > Exp > Proj > Skills | Edu > Exp > Projects > Skills |

Top leading verbs in the corpus are built, developed, designed, implemented, engineered, led, integrated, optimized and automated. Strong resumes vary their verbs and rarely open with "Achieved" or "Utilized".

## 2. Consensus advice (≥3 independent credible sources, little or no dissent)

1. **Quantify impact** (14 for, 2 against). The dissent is real. A 76-recruiter study found quantification did not drive decisions; brands and skills did. Three further sources warn that **uniform, GPT-style % metrics on every bullet reduce trust**, and interviewers probe metrics. Takeaway: give a number wherever a real one exists, state its baseline, and keep it defensible. Don't manufacture symmetry.
2. **One page** for students and new grads (9–0). Quant firms make no exceptions.
3. **A ~6–30 second skim** decides the first pass (6 sources). Brands, titles, dates and the first words of each bullet must carry the story.
4. **Simple single-column layout, standard headings, selectable PDF text** (6 sources). The "ATS rejects 75%" claim is a **myth** (5 sources). Parse-safety still matters, and 2025–26 sources add LLM screeners (5 sources on bias and noise).
5. **Skills should be backed by bullets** (6 sources). A skills list full of things that appear nowhere else reads as padding, and "only list what you can discuss" is a stated red-flag rule for quant.
6. **Tailor keywords to the role**, but don't keyword-stuff (6 for; 2 against stuffing).
7. **AI-written fatigue** (5 for, 1 qualified). Recruiters and HMs in 2025–26 explicitly distrust LLM-polished, JD-mirrored resumes with bolded keywords. The dissent says not to worry about *sounding* like AI but to worry about long, fluffed-up lines. Both point the same way: plain, specific, short.
8. **Accomplishments, not duties**, written as XYZ/CAR: action + method + scale + result (4 + 4 sources). One startup source frames it as **What (context) → How (tech) → Impact**, which is exactly the goal here.
9. **Coursework is low value**. Remove basic courses and keep only distinctive electives, if any (3 sources, cred 7.7).
10. **Formatting basics:**
    - month-year dates with en-dash ranges
    - margins of about 0.5in
    - font **≥10–11pt**: tiny text gets zoomed past or skipped
    - minimal italics (2 sources)
    - **bold reserved for structure** (titles, companies) or at most one anchor per line (2 sources say keyword-bolding is distracting; 1 says to bold to guide the eye)

## 3. What this means for Amar's resume (diagnosis)

- **Density is the main problem.**
  - Bullets average 1.8× the corpus median.
  - Four bullets run to 3 lines.
  - The body is set at about 8pt (`\footnotesize` inside a 10pt class), well under the ≥10pt guidance.
  - About 4 bold fragments per bullet turn bold into noise. The eye can't find the anchor, which defeats the skim.
- **Context is present but buried.** Most bullets put the why ("to minimize database queries under access constraints", "to allow contribution from non-familiar engineers") mid-sentence after a tech list. Rewrites should lead with the action and the object, then the method, then the result.
- **Metric hygiene.**
  - Most metrics are good and specific: 65% → <15s, 270K rows, 20K visits.
  - A few lack a baseline or an owner, e.g. "90% internal satisfaction compared to legacy" and "93% satisfaction on internal test users". These are what a skeptical HM probes, so phrase them honestly ("in an internal survey of N users" only if N is known; otherwise keep it as-is but understated).
- **Brands are strong.** AWS (incoming), Capital One, Amazon contract work, and a research lab targeting ICLR. The layout should make these unmissable in a 7-second skim.
- **Space sinks:**
  - the Certification section, which could fold into a single line
  - generic coursework
  - a 7-line skills block with many unbacked items (Spring Boot, MongoDB, Kubernetes/EKS, CUDA, Rust, Pinecone/FAISS/LangChain/LlamaIndex, Bitbucket)
- **GPA 3.5:** fine for big tech and startups. For quant the advice is "include if ≥3.7; omission is read as hiding", which is contested. This is left to the quant panel.

## 4. What differs by domain

| domain | what screeners weight | implications for Amar |
|---|---|---|
| General SWE (big tech) | brands, skim, clean structure, standard keywords | AWS/Capital One up top; short bullets; standard skills |
| Startup / full-stack | What→How→Impact; shipping to real users; initiative; product context for unknown companies | TerpLabs (20K visits, 5 live products) and the Capital One UI overhaul lead; add a short product context for Tortuga |
| Backend / distributed | p95/p99, RPS, caching, data layer, API design; deeper technique | Search index + Redis, Kinesis/Lambda pipeline; keep technique words (precomputed index, caching layer) |
| Cloud / infra / SRE | software depth over ops; IaC, observability, reliability metrics; platform-as-product; cost/latency metrics that are defensible | CDK/Fargate/GitHub Actions, EventBridge decision gates, CloudWatch/X-Ray/SNS; AWS cert matters here |
| AI / ML engineering | end-to-end AI product engineers (LLM + RAG + evals + serving); production over research logs; AI-tool use shown via accomplishments | Claude skill (65%, <15s), Bedrock fine-tuning automation, RAG meal app (93%) |
| ML research / robotics | research sensibility, papers/venues, public artifacts, C++/Python + robotics stack, internships | UMIACS/PhysTwin/ICLR target, AnyGrasp/Open3D/VLM pipeline; optionally the hidden Northrop robotics role |
| Quant dev / HFT | 15–30s skim; one page; GPA ≥3.7 stated; C++ + latency methodology (p99 numbers, measurement); clean engineering over flash; projects you can fully defend | IEX engine leads, with rdtscp/perf methodology. Skills trimmed to defensible ones. **Gap:** no latency numbers in the IEX project; facts don't allow adding any |
| Data engineering | SQL core, pipelines/ETL, Spark/cloud keywords, measurable pipeline results | Kinesis pipeline (6K docs, 34%), SQLAlchemy/Postgres distillation (270K rows) |
| Embedded / systems | title keyword, hands-on hardware, industry-standard parts (not Arduino), drivers/protocols up front | Only the hidden nanosat (Rust/KubOS) and Northrop roles; **stretch** domain |

## 5. Rules adopted for rewriting (fed into `rubric.yaml` and `tools/lint.py`)

**Bullet structure**
1. Each bullet is **action verb + what (with context) → how (1–3 techs that carry a decision) → result**, and stays ≤ 2 rendered lines.
2. Target 120–180 characters; the hard cap is two rendered lines with the last line ≥30% full.

**Bolding**
3. Bold is limited to **≤1–2 anchors per bullet**: the metric, or the single most important tech.

**Metrics**
4. Keep every true metric with its baseline, but don't push a % into bullets that don't have one.
5. Use understatement over puffery. Avoid "achieved", "spearheaded", "leveraged" and "utilized".

**Section content**
6. Coursework is cut or reduced to distinctive electives, and the Certification folds into Skills or Education.
7. Skills show only items backed by a bullet or defensible in an interview, grouped into 3–5 rows.

**Typography**
8. Body text is ≥ 9.5–10pt, margins ~0.5in, and only standard packages are used (Overleaf-safe).
