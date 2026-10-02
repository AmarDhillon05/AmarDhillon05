# Outcome-backed resume corpus (outcome_resumes.jsonl)

21 resumes, all from r/EngineeringResumes "Success Story!" threads (posted 2024-03 to 2026-07), each with a stated outcome (offer, or interview counts). Bullets were transcribed by hand from the posted images (151 bullets; a representative 5-9 per resume, not every bullet). Names, contacts and company names are excluded; `source_url` is retained per row for the sanitizer.

## Counts
- Year: 2024: 8, 2025: 8, 2026: 5
- Level: early_career 9, new_grad 6, intern 6
- Outcome tier: top 3 (Microsoft, Google promotion, NVIDIA), strong 8, moderate 10
- Domains (multi-label): general_swe 12, embedded_systems 9, backend_distributed 7, startup_fullstack 5, cloud_infra_sre 3, ml_research_robotics 2, quant_hft 1, data_engineering 0, ai_ml_engineering 0
- Bullets: 151 total, 70% contain a digit (has_metric), mean 141 chars. First section: Education 10, Experience 4, Skills 4, Summary 2, sidebar 1.

## Caveats
- Target of 30-40 was NOT reached. Quality over quantity: threads with only a failed image download, a blank template, a mechanical/non-software resume, or no resume text were dropped.
- Thin or empty domains: data_engineering (0), quant_hft (1, an FPGA/HFT-adjacent student), ml_research_robotics (2, both embedded/robotics-flavoured), ai_ml_engineering (0). Reddit search was not reachable through WebSearch, the archive API was flaky, and the cached resume_posts.jsonl turned out to be mostly discussion posts (almost none with resume bullets). These domains need another source.
- Survivorship and self-selection: only people who succeeded and chose to post. Many outcomes are "interviews" or "an offer" with no comp data; tiers are my judgement. Several offers followed hundreds to 10,000 applications, so the resume is rarely the sole cause.
- Company tiers are mostly "mid"/"small"/"none" because employers are anonymized; "faang" only where stated.
- The sub's wiki format dominates (r/EngineeringResumes norms), so format homogeneity is partly sub culture. Embedded is over-represented because that sub has many ECE/CompE posters.
- Reviewer feedback is auto-selected from thread comments (longest substantive replies, recruiter flairs first) and truncated to 60 words; congratulatory comments were filtered.

## 10 qualitative observations
1. One page, 3-5 bullets per role, 1-2 lines each. Posters repeatedly credit shortening bullets to one line.
2. Most (70%) bullets carry a number; the strongest use before/after pairs (test pass rate 9% to 84%, 53% to 100%, build time -98%) rather than bare percentages.
3. Experienced (2-4 YoE) product/backend resumes lead with Skills or Experience and put Education last; students and new grads lead with Education.
4. Skills are categorised (Languages / Frameworks / Databases / Tools) on 1-4 lines; a 15-language list drew criticism even though that resume still got an offer.
5. Projects substitute for experience at new-grad level. The ones that landed offers are systems-flavoured (OS kernel, rasterizer, HTTP server, deadlock-free mutex library) or deployed full-stack apps with CI/CD, not clones.
6. Tech stack is stated once per job/project (inline italic tags or a "Technologies:" line) rather than repeated in every bullet.
7. Embedded/firmware resumes lean on protocol and hardware specificity (CAN, I2C, SPI, FreeRTOS, ISO 26262, Verilog) and debugging stories (priority inversion, counter overflow); fewer metrics than product resumes, but concrete numbers where hardware allows (7.8 ns clock, 97% efficiency, 67 ms interrupt).
8. FPGA/HFT-targeted student resume used a short summary as a "hook", tool-by-vendor skills, and verification/simulation vocabulary; the poster said rewriting to "what I can do for you" with proper XYZ unlocked interviews. Only one quant-adjacent example, so treat as anecdotal.
9. Infra/SRE (senior, 6 YoE) uses scope and leverage: "used by 5 other teams", "migrated 1,000+ microservices", "reduced time-to-detect by 50%", plus mentoring bullets; a two-column layout still worked. Product/FAANG resumes use scale numbers (200k QPS, 200M devices, 10M+ users).
10. Gaps and non-traditional paths are shown plainly (explicit "Career Break" line, firefighter work, trades, community-college degree) and offset by projects or cloud certifications; separating promotions into distinct role blocks was credited as a high-impact fix.

## Feedback themes (flaired_comments.jsonl, 1005 comments, ~87% from recruiter/hiring-manager flairs; domain_comments.jsonl has no recruiter flairs and is weighted lower)
Counts are keyword hits among recruiter/HM-flaired comments (crude; "format" is a broad term):
- Format/ATS/template/fonts: ~267 of 873. The most common theme: single column, standard headings, consistent spacing.
- Experience/internship framing: ~301. Show progression, tie each role to impact.
- Projects: ~188. Include them when experience is thin; make them relevant and quantified.
- Quantify impact: ~144. Metrics and outcomes over duties.
- Summary/objective: ~138. Mostly "skip it" for juniors, keep short for career changers.
- Keywords/tailoring to the job description: ~127.
- Education/GPA: ~101. Drop GPA below ~3.0-3.5, keep coursework brief.
- Skills section: ~51. Trim, categorise, avoid listing everything.
- One-page length: ~49.
Domain comments (non-recruiter, ECE/FPGA/embedded/devops/ML subs) emphasise: show hardware or tooling specifics, concrete projects over buzzwords, and domain-matched keywords (e.g. SystemVerilog/FPGA tools, Kubernetes/Terraform, PyTorch). Projects (47) and quantification (29) lead there as well.
