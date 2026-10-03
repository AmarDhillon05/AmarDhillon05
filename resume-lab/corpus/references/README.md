# Reference resumes (redacted)

About a dozen strong, recent resumes kept as reading references, 2–3 per resume variant. They come from the 80-resume GitHub corpus (`corpus/github_resumes.jsonl`, ranked by the scraper's quality score) and from the outcome-backed set (`corpus/outcome_resumes.jsonl`).

**Redaction** (`tools/export_references.py`):
- The header block (name, email, phone, links) is replaced with "Redacted Candidate".
- Every email, phone number and URL in the body is stripped.
- Identity macros and PDF metadata are removed.
- A post-check fails the export if any email, phone, URL, the repo owner's handle or the header name survives. One resume was dropped on that check.
- Bullets, companies and structure are kept, because they are what we learn from.

| file | variant | level | companies | last edited | why it's here | PDF |
|---|---|---|---|---|---|---|
| `general_backend_2119c22bc655` | general_backend | intern | Amazon (Amazon Web Services), Google (YouTube), VideoLAN | 2026-09-29 | AWS + Google/YouTube intern; clear backend bullets with scope and results | no (custom fonts/engine); see .txt |
| `general_backend_4dfbdaf6e9b5` | general_backend | intern | Stripe, Stanford Carta, LastingLearn, Inc., Baker Engineering and Risk Consultants | 2026-09-08 | Stripe intern; plain-language product/infra bullets | yes |
| `general_backend_00391957f094` | general_backend | intern | Amazon Web Services (AWS), Stanford Center For Artificial Intelligence In Medicine & Imaging, Sundial | 2026-07-29 | AWS intern; backend + research mix similar to Amar's | yes |
| `infra_distributed_5926ce0c3962` | infra_distributed | intern | Tesla, Amazon, Cloudflare, Morgan Stanley | 2026-10-01 | Amazon/Cloudflare/Tesla intern; highest corpus quality score; infra-heavy | yes |
| `infra_distributed_70c3493688d3` | infra_distributed | intern | Google, MaiAgent Co., Ltd. | 2026-09-18 | Google intern; distributed-systems and cloud keywords used in context | no (custom fonts/engine); see .txt |
| `infra_distributed_62585d31928d` | infra_distributed | intern | Netflix, Intelligible AI | 2026-08-12 | Netflix intern; infra/SRE bullets with concrete mechanisms | yes |
| `systems_quant_f644ba7bc0c5` | systems_quant | intern | IMC Trading, Capital One, UBS, Olympus | 2026-01-28 | IMC + Capital One intern; same Capital One brand, quant systems framing | yes |
| `systems_quant_b05ffc279363` | systems_quant | intern | IMC Trading, PEAK6 Capital Management, LinkedIn, Discovery Day | 2026-04-22 | IMC + PEAK6 intern; low-latency/trading-systems bullets | yes |
| `systems_quant_0c7a2097d593` | systems_quant | intern | Susquehanna International Group, Google, Stanford Ophthalmic Informatics and Artificial Intelligence Group | 2026-05-14 | SIG + Google intern; quant firm resume with research projects | no (custom fonts/engine); see .txt |
| `ai_ml_engineering_d54264c23b67` | ai_ml_engineering | new_grad | Amazon, dotLumen, Thales | 2026-08-23 | Amazon new grad; ML systems grounded in engineering | no (custom fonts/engine); see .txt |
| `ai_ml_engineering_d5ae27a86afb` | ai_ml_engineering | intern | Nvidia, Baseten, AMD, eSentire | 2026-09-09 | NVIDIA + Baseten intern; ML infra / inference serving | yes |
| `general_backend_outcome_4669d64b` | general_backend | intern |  | 2026-04-12 | outcome-backed: NVIDIA Graphics Systems SWE intern offer (sophomore CS at T50 school; also several other interns listed) | no (custom fonts/engine); see .txt |
| `general_backend_outcome_6d7c86e1` | general_backend | new_grad |  | 2025-11-21 | outcome-backed: Full-time new grad SWE offer after ~80 applications (rising senior at top-10 CS school, no SWE internship) | no (custom fonts/engine); see .txt |
| `systems_quant_outcome_7f0fa981` | systems_quant | intern |  | 2026-05-08 | outcome-backed: HFT-adjacent FPGA role/internship offer after 4 interview rounds (EE + Physics student, Australia) following resume rewr | no (custom fonts/engine); see .txt |

Provenance: each file's id is the corpus id. The id-to-repo mapping lives only in the gitignored `corpus/raw/github_scrape_report.json`, so this folder carries no handles. Outcome-backed files come from public reddit posts, also listed in `corpus/outcome_resumes.jsonl` without usernames.
