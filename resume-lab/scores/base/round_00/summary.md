# base / round_00

**passed:** False  |  overall mean 7  |  gate errors 28

| dim | mean | min |
|---|---|---|
| ats_parseability | 7 | 7 |
| concision_readability | 4.2 | 4 |
| credibility | 5.6 | 5 |
| domain_fit | 7 | 7 |
| impact_clarity | 6 | 6 |
| overall | 7 | 7 |
| quantification | 6 | 6 |
| skim_test | 6.8 | 6 |
| technical_depth | 6.8 | 6 |
| visual_layout | 5.8 | 5 |

## Must-fix
- (ats_specialist) Replace the '(XXX) XXX-XXXX' placeholder with a real phone number (or remove it) — parsers populate the phone field with garbage.
- (ats_specialist) Standardize date format: use one month style everywhere (e.g., 'Jun 2026 – Aug 2026' to match 'Sep 2026 – Dec 2026').
- (ats_specialist) Clarify: employer for the contract role — 'Amazon (via UMD App Development Contracting)' may parse as Amazon employment; state the actual employer and client explicitly.
- (ats_specialist) Move 'Digital Badge' out of the right-aligned location column (embed the link on the cert name) so it is not parsed as a location.
- (ats_specialist) Fix skills miscategorization: SQS is not observability; CloudFormation/CDK are infrastructure-as-code, not CI/CD.
- (ats_specialist) Cut every bullet to ≤2 lines and ≤2 bold anchors (Capital One ×3, Bedrock bullet currently run 3 lines).
- (bigtech_recruiter) Replace the (XXX) XXX-XXXX phone placeholder with a real number or remove it.
- (bigtech_recruiter) Clarify: what the AWS Redshift internship involves — one generic 'researching and implementing' bullet undersells the most important brand on the page.
- (bigtech_recruiter) Cut bolding to 1–2 anchors per bullet; currently almost every noun is bold.
- (bigtech_recruiter) Bring every bullet to ≤2 lines; Capital One and Amazon contract bullets are 3-line walls.
- (bs_detector) Replace placeholder phone '(XXX) XXX-XXXX' with a real number or remove it.
- (bs_detector) clarify: baselines for '34% speedup' (latency? throughput? vs. what prior design), '90% internal satisfaction report compared to the legacy tool', and '93% meal satisfaction' (how many test users).
- (bs_detector) Cut 3-line bullets to ≤2 lines and reduce bolding to 1–2 anchors per bullet.
- (bs_detector) Prune skills you can't defend in an interview from bullets (Rust, CUDA, Kubernetes/EKS, Spring Boot, Pinecone/LlamaIndex); fix miscategorized SQS and CloudFormation.
- (bs_detector) AWS SDE intern entry has one vague present-tense bullet at the top of Experience; either say concretely what you're working on or keep it brief without filler.
- (senior_swe_hm) Replace the placeholder phone number (XXX) XXX-XXXX with a real number or remove it.
- (senior_swe_hm) Clarify: the IEX project dates (Jul–Aug 2026) overlap the full-time Capital One internship; consider labeling it personal/side project.
- (senior_swe_hm) Cut most of the bolding — currently 4–6 bold terms per bullet; keep at most 1–2 anchors (ideally the metric).
- (senior_swe_hm) Bring every bullet to ≤2 lines; nearly every bullet currently wraps to 3.
- (senior_swe_hm) Clarify: what the 90% and 93% satisfaction figures measure (survey of how many users, on what scale).
- (senior_swe_hm) AWS intern entry has a single vague, present-tense bullet; either flesh it out with what you can state or acknowledge it as in progress.
- (startup_quant_engineer) Replace the (XXX) XXX-XXXX placeholder with a real phone number or remove it.
- (startup_quant_engineer) Bring every bullet to ≤2 lines; Capital One bullets 1–3 and Amazon contract bullet 3 currently run three lines.
- (startup_quant_engineer) Cut bolding to at most ~2 anchors per bullet (the key result and one core tech).
- (startup_quant_engineer) Clarify: report the actual latency/throughput results from the IEX LSM vs B+ tree and hash-storage evaluations, if you have them.
- (startup_quant_engineer) Clarify: what the Amazon Leo research utility does and who uses it; currently unreadable to an outsider.
- (startup_quant_engineer) Clarify: baseline for the Capital One '90% satisfaction' figure (90% of whom, vs what legacy score?).

## Accepted-risk flags (logged, non-blocking)
- (ats_specialist) [concurrent_present_dates] Clarify: how the AWS SDE intern role (Redmond, Sep–Dec 2026) coexists with three 'Present' College Park roles; mark paused/part-time roles or set end dates.
- (bigtech_recruiter) [concurrent_present_dates] Clarify: the scope/hours of the overlapping roles (AWS intern, Amazon contract, UMIACS, TerpLabs all 'Present') so it doesn't read as inflated.
- (bs_detector) [concurrent_present_dates] clarify: concurrent timelines — Amazon contract (Jan 2026–Present), AWS SDE intern (Sep–Dec 2026), UMIACS (Present), TerpLabs (Present), and the IEX project during the Capital One internship. Mark part-time or end dates honestly.
- (senior_swe_hm) [concurrent_present_dates] Clarify: overlapping timelines — AWS intern in Redmond (Sep–Dec 2026) while Amazon contract, UMIACS research, and TerpLabs all show 'Present'; end-date or mark part-time/paused roles.

## Bullet verdicts
- `Researching and implementing Java-based utilization`: {'add_context': 5}
- `Overhauled the legacy UI of`: {'tighten': 5}
- `Engineered a lightweight tree-style workflow`: {'tighten': 3, 'reframe': 2}
- `Developed a Claude skill for`: {'reframe': 1, 'tighten': 4}
- `Deployed an Amazon Leo space`: {'tighten': 1, 'reframe': 3, 'add_context': 1}
- `Achieved a 34% speedup on`: {'tighten': 4, 'add_context': 1}
- `Integrated automated fine-tuning of an`: {'reframe': 4, 'tighten': 1}
- `Developing automated training for PhysTwin,`: {'add_context': 4, 'tighten': 1}
- `Built a Python pipeline linking`: {'tighten': 5}
- `Cut research-environment setup time 30%`: {'tighten': 5}
- `Co-founded and scaled a 110+`: {'tighten': 4, 'reframe': 1}
- `Sustained 20,000+ site visits within`: {'tighten': 1, 'reframe': 4}
- `Building a work-in-progress integration of`: {'tighten': 4, 'add_context': 1}
- `Implemented a C++-based order book`: {'tighten': 5}
- `Wrote and evaluated paginated hash-based`: {'tighten': 2, 'add_context': 3}
- `Designed and assessed the performance`: {'add_context': 5}

## Structure votes
- move_certifications_down: 3
- reduce_bold: 3
- trim_skills: 3
- single_line_contact: 1
- consistent_heading_spacing: 1
- skills_alignment: 1
- trim_bold: 1
- consistent_dates: 1
- move_certifications: 1
- label_part_time: 1
- resolve_concurrent_roles: 1
- debold: 1
- move_certification: 1
- trim_concurrent_roles: 1
- fix_header: 1
