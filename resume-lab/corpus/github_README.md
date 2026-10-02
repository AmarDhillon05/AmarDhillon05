# GitHub LaTeX resume corpus (built 2026-10-02)

Files
- `github_resumes.jsonl`: 80 resumes, one row each, anonymized. `id` = sha1(repo:path)[:12]. No names, emails or phones are stored.
- `github_bullets.jsonl`: 1,442 bullets from the experience, project, research and leadership sections.
- `raw/github_candidates.txt`: the 247 candidate repos and the search queries used to find them.
- `raw/github_scrape_report.json`: the status and reject reason for each repo. For repos that passed the content filters it also has the quality score, the number of industry roles and the metric rate.
- To regenerate: `python3 tools/scrape_github_latex.py --candidates corpus/raw/github_candidates.txt --report corpus/raw/github_scrape_report.json`. Clones go to /tmp/claude-0/gh_corpus. The script docstring documents every heuristic.

## Discovery
Candidates came from GitHub code search through the MCP tool. The unauthenticated REST search returned 403 through the proxy. Queries paired `\resumeItem` or `\resumeSubheading` with:
- company names: Jane Street, Citadel, HRT, Optiver, Two Sigma, Jump, Akuna, SIG, DRW, Databricks, NVIDIA, Stripe, Amazon, Google, Meta
- role terms: SWE Intern, Quantitative Developer, Research Intern, firmware/embedded, Kubernetes/SRE, Airflow/Data Engineering
- recency terms: "Summer 2025", "May 2026", "May 2027"

Repos that obviously mass-generate resumes (AI tailoring tools and template repos) were left off the list by hand. The script also rejects them by repo name.

## Funnel (247 repos)
| outcome | n |
|---|---|
| **kept** | **80** |
| below_quality_cutoff: passed every filter but ranked outside the top 80 | 91 |
| quality_floor: no industry role, or metric rate below 0.25 with no top-tier role | 50 |
| too_old: last change to the resume file before 2024 | 8 |
| senior: more than 5 years of full-time work | 7 |
| tool_or_template_repo | 3 |
| non_english_or_too_short | 3 |
| too_few_bullets (fewer than 6) | 2 |
| placeholder text ("your name") / no resume-like .tex / academic CV | 1 / 1 / 1 |

221 resumes passed the content filters. By year of last change: 2026: 163, 2025: 49, 2024: 9.

Selection works in three steps:
1. Apply the floor.
2. Guarantee up to 4 resumes for each primary domain.
3. Fill the remaining slots best-first by quality score, which combines a top-tier role (3), metric rate (3), industry roles, recency and result rate, minus a penalty when more than 70% of bullets are projects.

## Kept set (80)
- **Date of last commit to the resume file and its `\input`s:** 2025-Q1 2, Q2 1, Q3 5, Q4 2; 2026-Q1 11, Q2 13, Q3 44, Q4 2. All are 2025 or later, and 70 of 80 are from 2026.
- **Level:** intern 56, new_grad 16, early_career 8.
- **top_tier_signal (FAANG/Big-N, top startup or quant role):** 68 of 80. Among interns it is 47 of 56.
  - 11 resumes have a quant-firm role: HRT, Citadel/Citadel Securities/Citadel GQS, IMC, Optiver, SIG, Virtu, Headlands.
  - Most frequent companies, counted as resumes containing each: Amazon/AWS 20, Google 8, Apple 7, NVIDIA 6, Shopify 5, Tesla 5, Meta 5.
- **Template:** 78 of 80 use Jake's template family (`\resumeSubheading`/`\resumeItem`). The median resume has 16 bullets and 66 are about one page.
- **Primary domain:** ai_ml_engineering 22, general_swe 14, backend_distributed 12, startup_fullstack 9, cloud_infra_sre 7, embedded_systems 4, ml_research_robotics 4, data_engineering 4, quant_hft 4.
- **Any domain (up to 4 per resume):** ai_ml 34, general 32, backend 24, fullstack 20, infra 18, ml_research 16, quant 8, embedded 7, data_eng 5.
- **Bullets by domain:** ai_ml 290, general 272, backend 209, fullstack 168, infra 164, ml_research 138, embedded 81, data_eng 62, quant 58.
- **Bullets by company_tier:** other_industry 434, project 428, faang_bign 218, unknown 127, academic 105, top_startup 102, quant 28.
- **Bullet stats:** median 19 words. 50% have a metric (count 302, percent 200, scale 174, time 102, money 52). 34% state a result, 21% state context, and 33% contain bold text.
- **Most common opening verbs:** built, developed, designed, implemented, engineered, created, led.

## Caveats
- Every tag is a keyword or regex heuristic; the script docstring lists them. `has_context` is conservative. Domains lean toward ai_ml because LLM, model and agent words are now common in all kinds of bullets.
- A few company and title fields are misparsed in non-Jake layouts, for example a club name or tech stack captured as the company. 127 bullets could not be attached to a role (tier "unknown").
- Level comes from graduation year and full-time years, and can be wrong for co-op students whose titles don't say "intern".
- The date is the last git commit, not when the content was written. A recent repo-wide reformat counts as recent.
- The data is skewed: few data-engineering and embedded resumes passed the quality bar, and quant resumes often have few metrics, so they mostly got in through their top-tier role.
- `source_url` and `file_path` are public provenance but often contain the GitHub username or the person's name in the file name. Drop those two fields before sharing outside the project.
