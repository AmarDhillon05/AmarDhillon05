"""Atomic advice claims extracted (by hand) from KEPT sources in corpus_sources.py.

Row: (source_id, key, category, domain, claim, quote<=25 words, strength, stance)
  key      canonical claim id used to count independent sources in research/advice_synthesis.md
  strength strong = explicit directive backed by data/official policy; moderate = explicit directive from
           a credible practitioner; weak = hedged, anecdotal or single-instance
  stance   for = supports the canonical claim named by `key`; against = contradicts/qualifies it
"""

G = "general_swe"
C = []


def c(sid, key, cat, dom, claim, quote, strength="moderate", stance="for"):
    C.append((sid, key, cat, dom, claim, quote, strength, stance))


# ---------------- S001 Tech Interview Handbook (ex-Meta staff eng)
c("S001", "pdf_text_selectable", "ats", G, "Submit a PDF built in Word/Google Docs so text is highlightable and parseable; avoid design tools and online builders.", "Submit your resume as a PDF file to preserve formatting... ensure that the text in your resume is easily highlightable", "strong")
c("S001", "no_header_footer", "ats", G, "Do not put content in Word/Docs header/footer; reduce margins instead.", "Do not use the header or footer sections in a Word/Google Docs file - reduce margins instead", "moderate")
c("S001", "margins_half_inch", "formatting", G, "Use narrow margins of about 0.5 inch to maximize space.", "narrow margins are 0.5 on each side", "moderate")
c("S001", "font_standard_10pt", "formatting", G, "Use standard fonts (Arial, Calibri, Garamond) at minimum 10 pt.", "Fonts you should use - Arial, Calibri, Garamond... use a minimum size of 10 pt for readability", "strong")
c("S001", "standard_headings", "ats", G, "Use standard section headings without symbols so ATS can parse them.", "Never add symbols to your headers to avoid ATS readability issues.", "moderate")
c("S001", "education_first_student", "section_order", G, "If still in school or under 3 years of experience, education may go first.", "if you are still in school or have less than 3 years of experience, you may put Education first", "moderate")
c("S001", "summary_use", "section_order", G, "A short (<50 words) professional summary/headline stating fit for the job is recommended.", "frame them into a short summary of less than 50 words", "moderate")
c("S001", "contact_basics", "formatting", G, "Must-haves: name, personal phone, city/state, personal email, LinkedIn; GitHub/personal site are good-to-haves.", "Location - City, State, Zip. Just enough for recruiters to determine if you are a local or international candidate", "moderate")
c("S001", "xyz_formula", "bullet_structure", G, "Write accomplishments as action that resulted in a quantifiable outcome.", "[Accomplishment summary] : [Action] that resulted in [quantifiable outcome]", "strong")
c("S001", "dates_format", "formatting", G, "List roles reverse-chronologically with company, location, title and MM/YYYY dates.", "List your work experience in a familiar format and reverse chronological order", "moderate")
c("S001", "gpa_threshold", "education", G, "List GPA only if above 3.50/4.00.", "List GPA if more than 3.50/4.00", "moderate")
c("S001", "projects_include", "projects", G, "Include at least 2 projects and link each to GitHub or a live view.", "Include at least 2 projects you have contributed to... link your project name to GitHub", "moderate")
c("S001", "one_page", "length", G, "Use only one page.", "Use only 1 page for your resume", "strong")
c("S001", "relevance_prune", "anti_pattern", G, "A few best achievements beat many average ones; filter ruthlessly.", "Highlighting a few of your best achievements is better than including many \"average\" achievements", "moderate")
c("S001", "tailor_keywords", "tech_keywords", G, "Mirror must-have keywords from the job description in Skills and Experience.", "always analyze the job description for must-have and good-to-have skills... ensure the keywords are added", "strong")
c("S001", "keyword_stuffing_bad", "anti_pattern", G, "Do not keyword-stuff; a human will read the resume eventually.", "do not do keyword stuffing for the sake of it", "moderate")
c("S001", "ats_auto_reject_risk", "ats", G, "Claims many top companies use ATS rules that can auto-reject candidates.", "In many companies, the ATS may even use certain rules to reject candidates automatically.", "weak")
c("S001", "skills_section_format", "skills", G, "Skills formatted as [category]: items separated by '|' (languages, frameworks, databases).", "[Skill summary] : [List skills separated by \"|\"]", "weak")
c("S001", "awards_quantified", "other", G, "Only include job-relevant awards and quantify them (e.g., 'Best product out of 50 teams').", "Only include achievements related to the job application and try to quantify your achievements", "moderate")

# ---------------- S002 interviewing.io study (2024)
c("S002", "brands_matter", "domain_specific", G, "Experience at a top-tier tech company is the strongest predictor of a recruiter wanting to interview (35% more likely).", "Most predictive... was experience at a top company — these candidates were 35% more likely to be picked", "strong")
c("S002", "screen_time", "other", G, "Median recruiter resume evaluation time was 31 seconds.", "the median time spent on resume evaluations was just 31 seconds", "strong")
c("S002", "recruiter_noise", "other", G, "Recruiter judgments were only slightly better than a coin flip (55% accuracy) and recruiters disagreed with each other.", "recruiters chose correctly 55% of the time, which is just slightly better than a coin flip", "strong")
c("S002", "skills_stated_vs_actual", "skills", G, "Recruiters say 'missing skill' is the main rejection reason, but actual rejections correlated most with 'no top firm'.", "The main rejection reason isn’t “missing skill” — it’s “no top firm.”", "strong")
c("S002", "referrals_outreach", "other", G, "Stop relying on online applications; reach out to hiring managers directly.", "stop spending energy on applying online, full stop. Instead, reach out to hiring managers.", "moderate")
c("S002", "ats_score_noise", "ats", G, "Simple ML models (XGBoost) on minimal resume features out-predicted human recruiters.", "both models made predictions more accurately than human recruiters", "moderate")

# ---------------- S003 snake oil (2025)
c("S003", "brands_matter", "domain_specific", G, "Recruiters skim primarily for recognizable companies and schools.", "they are mainly skimming for recognizable companies and schools", "strong")
c("S003", "metrics", "metrics", G, "Quantified impact did NOT drive recruiter decisions in the 76-recruiter study.", "What's missing? Things like, for example, having a quantifiable impact or demonstrating teamwork.", "moderate", "against")
c("S003", "niche_skills_ml", "domain_specific", "ai_ml_engineering", "Niche skills such as ML engineering modestly raise recruiter interest.", "To some extent, if you have niche skills (e.g., ML engineering)", "moderate")
c("S003", "brands_top_placement", "section_order", G, "If you have top brands, move them to the very top; buried brands get missed.", "We edited this candidate’s resume to put all the things recruiters look for at the very top", "strong")
c("S003", "projects_skeptic", "projects", G, "Side projects are generally useless for getting in the door (useful in interviews).", "In general, side projects are useless for getting in the door.", "moderate")
c("S003", "referrals_outreach", "other", G, "Without top brands, outreach to hiring managers beats rewriting.", "stop applying and start doing outreach to hiring managers", "moderate")
c("S003", "screen_time", "other", G, "Recruiters spend about 30 seconds and cannot read every bullet.", "they spend an average of 30 seconds reviewing them. That's not enough time to read every bullet.", "strong")

# ---------------- S004 don't make recruiters think (2025)
c("S004", "summary_use", "section_order", G, "Use the summary to spell out your 2-3 most impressive facts in plain English, not buzzwords.", "use this section to explicitly tell recruiters the 2-3 most impressive things about you in plain English", "strong")
c("S004", "buzzword_avoid", "anti_pattern", G, "Avoid filler like 'passionate self-starter' or 'results-driven'.", "meaningless jargon like \"passionate self-starter\" or \"detail-oriented team player.\"", "strong")
c("S004", "gpa_threshold", "education", G, "Only include GPA if 3.8 or higher (notes co-author Gayle says 3.0+).", "only include your GPA if it's 3.8 or higher", "moderate")
c("S004", "gpa_threshold", "education", G, "Beyond Cracking the Coding Interview (2025) recommends including GPA if 3.0 or more.", "Gayle recommends including it if it’s 3.0 or more", "moderate")
c("S004", "competitions_signal", "education", G, "If GPA is weak, highlight hackathons, competitions, fellowships, scholarships instead.", "focus on other academic achievements: hackathons, technical competitions, fellowships or scholarships", "moderate")
c("S004", "company_context", "bullet_structure", G, "For lesser-known companies add a one-line description with metrics/investors.", "For lesser-known companies, include a one-line description explaining what the company does", "strong")
c("S004", "promotions_visible", "formatting", G, "Group multiple roles under one company heading to show promotion, not job-hopping.", "group different roles under the same company heading", "moderate")
c("S004", "work_auth", "formatting", G, "State work authorization explicitly in header or summary.", "Make your work status explicit in your header or summary section", "strong")

# ---------------- S005 interviewing.io AI model (2026)
c("S005", "brands_matter", "domain_specific", G, "46% of candidates who got offers at top companies lacked top schools/companies (brands are overweighted).", "46% of candidates who got offers at top companies didn't have top schools or top companies on their resumes", "strong", "against")
c("S005", "llm_bias", "ats", G, "LLM/AI screeners trained on biased data favor pedigreed and demographically-signaled candidates.", "other models are heavily biased toward pedigreed candidates", "moderate")
c("S005", "activity_metrics_weak", "metrics", G, "Commits/PR counts/lines of code are inputs (effort), not outcomes.", "metrics like number of commits, pull requests, or lines of code written are inputs", "moderate")

# ---------------- S006 interviewing.io channels (2024)
c("S006", "referrals_outreach", "other", G, "Most useful channels were in-house recruiter outreach and warm referrals.", "the most useful channels were in-house recruiters (when they reached out to you) and warm referrals", "strong")
c("S006", "brands_matter", "domain_specific", G, "In-house recruiters reach out to people with top companies/schools; companies matter more than schools.", "you have top-tier companies and/or schools on your resume (in our experience, companies matter more)", "moderate")

# ---------------- S007 Laszlo Bock XYZ (foundational)
c("S007", "xyz_formula", "bullet_structure", G, "Accomplished [X] as measured by [Y], by doing [Z].", "Accomplished [X] as measured by [Y], by doing [Z]", "strong")
c("S007", "metrics", "metrics", G, "Every bullet should carry a measurement of the accomplishment.", "as measured by [Y]", "strong")
c("S007", "accomplishments_not_duties", "bullet_structure", G, "State results, not responsibilities.", "Accomplished [X] as measured by [Y], by doing [Z]", "moderate")

# ---------------- S008 Ladders (foundational)
c("S008", "screen_time", "other", G, "Initial screen averages 7.4 seconds (2018 eye-tracking).", "The average initial screening time for a candidate's resume clocks in at just 7.4 seconds", "moderate")
c("S008", "single_column_simple", "formatting", G, "Simple layouts that follow F/E-pattern reading with bold job titles over bulleted accomplishments performed best.", "Layouts that took advantage of F-pattern and E-pattern reading tendencies, with bold job titles supported by bulleted lists", "moderate")

# ---------------- S009 Pragmatic Engineer: hiring managers 2025
c("S009", "volume_flood", "other", G, "1,000+ candidates per role is not uncommon in 2025.", "1,000+ candidates for a single role is not uncommon", "strong")
c("S009", "referrals_outreach", "other", G, "Despite floods of inbound, many companies hire most engineers via reachouts and referrals.", "many companies hire most engineers via reachouts and referrals", "strong")
c("S009", "ai_written_fatigue", "anti_pattern", G, "AI-enhanced inbound applications tailored to the listing are flooding LinkedIn; some companies turned off inbound.", "we turned off the job postings for inbound because of the high volume of low-quality applicants, or AI-enhanced inbounds", "strong")
c("S009", "fake_applicants", "anti_pattern", G, "Fake applicants and AI-assisted cheating are a growing problem, especially for remote roles.", "Fake applicants + AI: a growing problem.", "moderate")
c("S009", "role_match", "tech_keywords", G, "Many applicants match almost none of the requirements; matching the role's actual stack matters.", "We get tons of applicants who match almost NONE of the requirements.", "moderate")
c("S009", "ai_engineering_demand", "domain_specific", "ai_ml_engineering", "Massive increase in demand for AI engineers and product engineers in 2025.", "Massive increase in demand for AI engineers", "moderate")
c("S009", "startup_product_engineer", "domain_specific", "startup_fullstack", "Higher demand for founding engineers and product engineers at startups.", "Higher demand for founding engineers and product engineers.", "moderate")

# ---------------- S010 PE part 3
c("S010", "referrals_outreach", "other", G, "Referrals seem the only way to consistently get interviews in late 2025.", "Referrals seem like the only way to consistently get interviews.", "strong")
c("S010", "ai_product_engineer", "domain_specific", "ai_ml_engineering", "In-demand profile: AI product engineers who build end-to-end (fullstack + LLMs + evals + RAG).", "Those who can build AI products end-to-end (fullstack + LLMs + evals + RAG).", "moderate")
c("S010", "ai_native_skills", "skills", G, "AI-native engineers who use AI tools to boost productivity are in demand.", "AI-native engineers: Engineers who are experts in how to use AI tools to significantly boost productivity.", "moderate")

# ---------------- S011 / S012 Tech Resume Inside Out (foundational)
c("S011", "ats_myth", "ats", G, "People who work with ATSes say real people look at resumes, not robots.", "Real people look at resumes, not robots.", "strong")
c("S012", "screen_time", "other", G, "Recruiters spend around 7 seconds deciding whether to keep reading.", "On average recruiters spend around 7 seconds on a CV", "moderate")
c("S012", "two_pages_ok", "length", G, "One page is not mandatory for experienced engineers.", "a resume has to be 1 page long. If you’re an experienced person, it can and should be longer.", "moderate")
c("S012", "no_photo_personal", "formatting", G, "No photo, birth date, gender, marital status or mailing address.", "avoid photos and non-required personal information such as your birth date, gender, religion", "strong")
c("S012", "no_sub_bullets", "formatting", G, "Use bullets but avoid sub-bullets.", "while using bullet points is preferable because of easy readability, avoid sub-bullets", "moderate")
c("S012", "pdf_text_selectable", "ats", G, "Send PDF only; it renders the same everywhere.", "avoid any other format than PDF", "moderate")
c("S012", "no_skill_ratings", "skills", G, "Don't rate your proficiency in technologies; just list what you're comfortable with.", "avoid rating your knowledge of technologies", "strong")
c("S012", "single_column_simple", "formatting", G, "Flashy designs usually go straight to the 'no' pile.", "come up with a flashy design... In most cases it won’t work, your CV will go directly to the no category", "moderate")
c("S012", "promotions_visible", "formatting", G, "Make promotions clearly visible.", "Make your promotions clearly visible", "moderate")

# ---------------- S013 YC Ryan Choi (foundational)
c("S013", "what_how_impact", "bullet_structure", "startup_fullstack", "For each position cover What (context), How (technologies), and Impact.", "For each position on your resume, be sure to cover what, how and impact.", "strong")
c("S013", "company_context", "bullet_structure", "startup_fullstack", "Assume reviewers don't know your last company; describe the product line.", "Assume that recruiters and hiring managers don’t know much about your last company or role.", "strong")
c("S013", "skills_in_bullets", "skills", "startup_fullstack", "Put technologies with each position, not in one big Technology section at the bottom.", "Do not dump them all into one big “Technology” section at the bottom of your resume.", "strong")
c("S013", "metrics", "metrics", "startup_fullstack", "Share business impact: growth, cost savings, sales.", "Share your impact on the business — growth numbers, cost savings, sales increase", "strong")
c("S013", "relevance_prune", "anti_pattern", "startup_fullstack", "Remove side projects that don't match the job.", "Remove side projects that don’t necessarily match the job", "moderate")
c("S013", "startup_initiative", "domain_specific", "startup_fullstack", "Standouts showed initiative: product ideas, sample code; being a genuine user is a plus.", "Being a genuine user is a huge plus.", "moderate")

# ---------------- S014 YC student edition (foundational)
c("S014", "one_page", "length", G, "Keep it to one page.", "Keep it to one page. In most cases, you can cover all your experiences in a single sheet.", "strong")
c("S014", "experience_first", "section_order", G, "Put work experience at the top, especially if from a lesser-known school.", "If you come from a lesser-known school, having work experience first might help.", "moderate")
c("S014", "skills_in_bullets", "skills", G, "Avoid a standalone skills list; embed skills in each experience bullet.", "Avoid a section listing skills/proficiencies.", "moderate")
c("S014", "projects_skeptic", "projects", G, "Add a Projects section sparingly; side projects/hackathons carry limited signal.", "Add a “Projects” section sparingly. There’s not enough signal", "moderate")

# ---------------- S015 Anthropic careers
c("S015", "research_oss_top", "projects", "ml_research_robotics", "Put independent research, thoughtful blog posts or open-source contributions at the top of the resume.", "If you’ve done interesting independent research, written a thoughtful blog post, or contributed to open source, put that at the top of your resume.", "strong")
c("S015", "credentials_not_required", "education", "ml_research_robotics", "Anthropic cares what you can do, not where you learned it; ~half of technical staff had no prior ML experience.", "We care about what you can do, not where you learned to do it.", "strong")
c("S015", "apply_as_engineer", "domain_specific", "ai_ml_engineering", "If you have an engineering background, apply as an engineer (research and engineering overlap).", "If you have an engineering background, apply as an engineer", "moderate")

# ---------------- S016 Anthropic AI guidance
c("S016", "ai_use_refine_ok", "other", G, "Write your first draft yourself, then use AI to refine it.", "Please create your first draft yourself, then use Claude to refine it.", "strong")
c("S016", "ai_fabrication_bad", "anti_pattern", G, "Using AI to create experiences you haven't had is not allowed and yields generic content.", "Using Claude to create experiences❌ Not allowed", "strong")
c("S016", "metrics", "metrics", G, "Using AI to help quantify the impact of real work is encouraged.", "Help me think of ways to quantify the impact of the platform migration that I led.", "moderate")

# ---------------- S017 Jane Street
c("S017", "no_finance_needed", "domain_specific", "quant_hft", "No finance experience is required.", "Nope! But those with previous finance experience are of course welcome to apply.", "strong")
c("S017", "no_ocaml_needed", "tech_keywords", "quant_hft", "You don't need OCaml/functional programming; interview in the language you know best.", "Most of the software engineers we hire come in without any OCaml or even functional programming experience.", "strong")
c("S017", "extra_context_box", "other", "quant_hft", "Put things that don't fit on the resume in the application's free-text box.", "If there’s something you think we should know about that doesn’t fit nicely onto your resume/CV, feel free to include it in the text box", "moderate")

# ---------------- S018 Stripe
c("S018", "gpa_matters", "education", G, "Stripe factors GPA into review and recruits from schools with consistent strong performance.", "GPA matters to us, and we factor it into our review.", "strong")
c("S018", "brands_matter", "education", G, "School pedigree is used as a signal, though not the only one.", "We also recruit from schools where we’ve consistently seen strong performance.", "strong")

# ---------------- S019 D. E. Shaw
c("S019", "show_initiative", "domain_specific", "quant_hft", "More interested in talent, curiosity and analytical thinking than specific skills; show initiative and achievements.", "We’re more interested in talent, curiosity, and analytical thinking than in any particular skill or experience", "strong")
c("S019", "no_finance_needed", "domain_specific", "quant_hft", "No prior finance experience required for interns.", "No prior finance experience is required", "strong")

# ---------------- S020 Optiver
c("S020", "clean_code_signal", "domain_specific", "quant_hft", "Optiver grad SWEs build simple, well-architected solutions with traders and researchers; signal clean engineering over flash.", "develop simple, well-architected solutions that meet the needs of our business", "weak")

# ---------------- S021/S022 NACE
c("S021", "skills_with_examples", "skills", G, "Employers want examples demonstrating skills, not just a list.", "It is not enough for candidates to simply list their skills: Employers want to see examples.", "strong")
c("S021", "gpa_declining", "education", G, "Recruiting is increasingly based on skills rather than GPA and major.", "a recruiting environment that is increasingly based on skills that translate to the workplace instead of GPA and major", "strong")
c("S021", "teamwork_problem_solving", "other", G, "Top desired attributes: teamwork, problem-solving, communication.", "employers want to see that candidates have the ability to work in a team, problem-solve, and communicate effectively", "moderate")
c("S022", "teamwork_problem_solving", "other", G, "~90% of employers seek evidence of problem solving, ~80% teamwork on resumes.", "nearly 90% of employers... seeking evidence of a student’s ability to solve problems and nearly 80%... teamwork", "strong")
c("S022", "technical_skills_valued", "skills", G, "Technical skills important to at least 70% of employers.", "Written communication skills, initiative, strong work ethic, and technical skills are important to at least 70%", "moderate")

# ---------------- S023 Greenhouse docs
c("S023", "file_types", "ats", G, "Greenhouse accepts .doc/.docx/.pdf/.rtf/.txt up to 100 MB.", "Candidate uploads can be up to 100 MB", "strong")
c("S023", "no_external_images", "formatting", G, "Externally linked images are not loaded in the PDF preview.", "Greenhouse Recruiting does not load externally linked images when converting a resume to PDF for preview.", "moderate")

# ---------------- S024 Greenhouse AI report
c("S024", "ai_screening_prevalence", "ats", G, "~25% of hiring managers use AI to screen; 53% of US recruiters say AI/ATS completes screening checks.", "more than half (53%) of US recruiters admit that either AI or ATS systems complete screening checks", "strong")
c("S024", "prompt_injection_detection", "anti_pattern", G, "41% of job seekers report prompt-injecting AI; 61% of US hiring managers use AI-detection software.", "61% in the US... use software to detect when AI has been used", "strong")
c("S024", "fake_applicants", "anti_pattern", G, "91% of recruiters have spotted candidate deception.", "91% of recruiters surveyed have spotted candidate deception", "strong")

# ---------------- S025 HR Dive / Greenhouse
c("S025", "ai_written_fatigue", "anti_pattern", G, "More than a quarter of candidates say AI makes it harder to stand out; nearly a third claimed AI skills they lack.", "nearly a third have claimed AI skills they don’t have", "strong")
c("S025", "honesty", "anti_pattern", G, "59% of candidates altered resumes and 45% of those embellished.", "59% of candidates said they’ve altered their resumes, and among those, 45% said they’ve embellished", "moderate")

# ---------------- S026 75% myth
c("S026", "ats_myth", "ats", G, "No credible study supports '75% of resumes auto-rejected'; traced to Preptel marketing (2012).", "No credible study supports the popular claim that 75 percent of resumes... are auto-rejected", "strong")
c("S026", "knockout_questions", "ats", G, "The real auto-reject mechanism is recruiter-configured knockout rules/questions.", "The narrow exception, a recruiter-configured knockout rule, is real", "strong")
c("S026", "ats_parse", "ats", G, "A parse failure is a fixable formatting problem; Greenhouse still creates the candidate record.", "a machine that cannot read a resume... is a formatting problem you can fix in ten minutes", "moderate")

# ---------------- S027 HackerRank ATS experiment
c("S027", "ats_score_noise", "ats", G, "An LLM-based screener gave the same resume 74-90/100 across runs; project judgments flip randomly.", "If your company’s cutoff sits at 85, I fail 65% of the time. Same exact resume, different luck.", "strong")
c("S027", "skills_checklist_stable", "skills", G, "Technical-skills checklists are scored consistently by LLM screeners; subjective project quality is not.", "Look at technical skills: I scored 8/10 in 98 out of 100 runs.", "strong")
c("S027", "llm_screen_github", "projects", G, "LLM screeners pull GitHub and give bonus points for portfolio sites/blogs/startup experience.", "Up to 20 bonus points for startup experience, a portfolio site, a technical blog", "moderate")

# ---------------- S028 HN thread
c("S028", "referrals_outreach", "other", G, "Cold applying is a black hole; recruiters, HM outreach and referrals still work.", "cold-applying has always worked essentially as a black hole, and LLMs haven't changed that much", "moderate")
c("S028", "llm_bias", "ats", G, "AI resume filters readily capture demographic biases.", "AIs are very, very good at capturing biases", "weak")

# ---------------- S029 CNN
c("S029", "ai_screening_prevalence", "ats", G, "48% of hiring managers report using AI to screen resumes (Resume Genius data).", "48% of hiring managers report using AI to screen resumes and applications", "moderate")
c("S029", "llm_semantic_matching", "tech_keywords", G, "New AI screeners infer skills semantically rather than matching exact keywords.", "new AI tools can understand the content of a resume, meaning they can help spot candidates even if their resumes don’t mention certain words", "moderate")

# ---------------- S030 From Day One
c("S030", "volume_flood", "other", G, "AI-generated applications create floods; employers respond with more AI screening and verification.", "job seekers are using AI-powered tools to churn out applications at an unprecedented rate", "moderate")
c("S030", "fake_applicants", "anti_pattern", G, "Fake/fraudulent applications are prompting identity verification.", "Fake and fraudulent job applications have employers arming up even more", "moderate")

# ---------------- S031/S032/S033 LLM bias papers
c("S031", "llm_bias", "ats", G, "All 22 LLMs showed gender-name preferences and most showed positional bias (first candidate listed).", "most models exhibited a substantial positional bias to select the candidate listed first in the prompt", "strong")
c("S032", "llm_bias", "ats", G, "LLM ranking is highly sensitive to demographic and even non-demographic perturbations.", "exhibit high ranking sensitivity to both gender and race perturbations", "strong")
c("S033", "llm_bias", "ats", G, "ChatGPT ranked resumes with disability-related honors lower than identical resumes without them.", "ChatGPT consistently ranked resumes with disability-related honors and credentials... lower", "strong")

# ---------------- S035 Stanford
c("S035", "tailor_keywords", "tech_keywords", G, "Highlight the skills and experiences the specific employer cares about.", "ensure that you are highlighting the skills and experiences an employer cares about", "moderate")
c("S035", "skimmable_headers", "formatting", G, "Organize headers so key skills stand out as an employer initially skims.", "skills stand out as an employer initially skims your document", "moderate")

# ---------------- S036 UIUC
c("S036", "tailor_keywords", "tech_keywords", G, "Make a list of the top ten keywords from the posting and include them.", "Make a list of the top ten keywords based on the position's responsibilities.", "strong")
c("S036", "skills_in_bullets", "skills", G, "Put language keywords inside experience bullets (e.g., 'Java' in a bullet).", "you may choose to include \"Java\" in one of your bullet points for a previous role", "moderate")
c("S036", "action_verbs", "tense_verbs", G, "Start bullets with action verbs and diversify them.", "Start with an action verb in your bullet points and diversity action verbs.", "moderate")

# ---------------- S037 UW Allen School
c("S037", "one_page", "length", G, "Allen School guide is for a one-page technical resume.", "best practices, tips, and suggestions for each section of a one page technical resume", "moderate")
c("S037", "purpose_interview", "other", G, "The resume's purpose is to land an interview, not to be an autobiography.", "The purpose of a resume is to land an interview, not to provide an autobiography.", "moderate")
c("S037", "online_presence", "other", G, "Maintain a descriptive LinkedIn/Handshake profile; HMs search there.", "Hiring managers are increasingly utilizing platforms like LinkedIn and Handshake to search for new talent.", "moderate")

# ---------------- S038 Richmond/Mentra
c("S038", "projects_include", "projects", G, "Without work experience, emphasize projects and skills.", "Don’t have work experience? Put extra focus on projects and skills", "moderate")
c("S038", "one_page", "length", G, "Keep to one page and tailor with ATS-friendly keywords.", "Keep your resume to one page and tailor it to each job posting using ATS-friendly keywords.", "moderate")
c("S038", "problem_solving_bullets", "bullet_structure", G, "Describe how you debugged, optimized or improved code.", "describe how you debugged, optimized, or improved your code", "moderate")

# ---------------- S039 ULTMECHE wiki (r/EngineeringResumes lineage)
c("S039", "single_column_simple", "formatting", G, "Use a simple format (Harvard-style); no tables, graphs, infographics or images.", "Don’t use colorful tables, graphs, infographics, or images", "strong")
c("S039", "margins_half_inch", "formatting", G, "Margins about 0.5 inch.", "Resume margins should be approx ~0.5 inches", "moderate")
c("S039", "one_page", "length", G, "One page unless 10+ years; rule of thumb one page per decade.", "One page resume unless you have 10+ years experience", "strong")
c("S039", "bullet_one_sentence", "bullet_structure", G, "One sentence per bullet; concrete, not narrative.", "One sentence per bullet (you’re not telling a story)", "moderate")
c("S039", "bullet_order_impressive_first", "bullet_structure", G, "Order bullets most impressive first; readers go top-down.", "impressive at top, least impressive at bottom", "moderate")
c("S039", "no_first_person", "tense_verbs", G, "No 'I' or 'my'; no trailing periods.", "Don’t get personal (I or my)", "moderate")
c("S039", "bullet_no_widow", "bullet_structure", G, "If a bullet's second line has only a few words, condense to one line.", "If the 2nd line has a few words, condense the bullet down such that it is one line", "moderate")
c("S039", "action_verbs", "tense_verbs", G, "Strong action verbs (led, designed, reduced); avoid weak ones (collaborated, participated).", "Bad action word – collaborated, participated, gained experience", "moderate")
c("S039", "xyz_formula", "bullet_structure", G, "Use STAR, XYZ or CAR frameworks.", "Use frameworks such as STAR, XYZ, or CAR", "moderate")
c("S039", "dates_format", "formatting", G, "Month + year dates, en-dash ranges, right-aligned; 'Present' for current roles.", "Dates should be aligned to right margin", "moderate")
c("S039", "summary_skip", "section_order", G, "Do not include a professional summary for students/early career; no references.", "Do not include a professional summary (it is redundant as your resume is a summary)", "moderate")
c("S039", "education_first_student", "section_order", G, "Student order: Education -> Experience -> Projects -> Skills.", "Education -> Work Experience -> Projects -> Skills", "moderate")
c("S039", "coursework_low", "education", G, "Coursework is unimpressive; include only relevant coursework when lacking experience.", "coursework is very unimpressive as hiring managers and recruiters know what basic curriculum is", "moderate")
c("S039", "soft_skills_avoid", "anti_pattern", G, "Do not list soft skills; list hard technical skills.", "Avoid soft skills such as collaboration, teamwork, and leadership", "moderate")
c("S039", "metrics", "metrics", G, "Quantify results and accomplishments (most important).", "Quantify your results and accomplishments (most important)", "strong")
c("S039", "skills_in_bullets", "skills", G, "Treat software as keywords inside bullets with numerical impact.", "Treat software as keywords and add numerical impact along with the software and action verb", "moderate")
c("S039", "italics_avoid", "formatting", G, "Avoid italics except sparingly; use bold/CAPS/italics independently.", "Don’t italicize text – it is ok to use sparingly", "moderate")
c("S039", "contact_basics", "formatting", G, "Contact: City, ST | phone | email | LinkedIn; no physical address, no https/www.", "Don’t list physical address", "moderate")
c("S039", "brands_matter", "domain_specific", G, "Recruiters scan for where you worked and went to school.", "Specific things recruiters will be scanning for consist of WHERE you worked and WHERE you went to school.", "moderate")
c("S039", "embedded_sensitive", "domain_specific", "embedded_systems", "For defense/proprietary work, describe at a high level (e.g., 'military aircraft').", "If you work on sensitive stuff such as military aircraft... just be high level about it.", "moderate")

# ---------------- S040 jonkl91 (recruiter)
c("S040", "screen_order", "section_order", G, "Recruiters look first at companies, titles and dates, then scan for keywords, then read.", "Companies, titles, and dates are typically the first things we look at. Then we scan to see if they have relevant keywords.", "strong")
c("S040", "bold_minimal", "bolding", G, "Bold only section titles, job titles, company and dates; bolding keywords is distracting.", "Bold section titles, job titles, dates, and job titles. Bolding more than that makes a resume harder to read.", "strong")
c("S040", "bold_minimal", "bolding", G, "Bolding fragments in bullets doesn't have the impact people think.", "Bolding fragments is bad advice. It doesn't really have the impact people thinks it does.", "strong")
c("S040", "skills_top", "section_order", G, "Put technical skills at the top for technical resumes; it's the first thing this recruiter reads.", "Put your technical skills on the top. This is the first thing I look at for technical resumes.", "strong")
c("S040", "dates_clear", "formatting", G, "Bold the dates; move location next to company so nothing competes with dates.", "You don't want anything to compete with the dates.", "moderate")
c("S040", "italics_avoid", "formatting", G, "Remove italics; they hurt skimmability.", "Get rid of the italics also. Formatting is the number 1 thing hurting you.", "moderate")
c("S040", "font_standard_10pt", "formatting", G, "Don't go smaller than 11 pt; tiny previews are a pain to zoom.", "I don't recommend smaller than 11.", "moderate")
c("S040", "margins_half_inch", "formatting", G, "Margins of 0.4-0.5 inch; avoid cramming.", "Increase your margins to 0.4-0.5.", "moderate")
c("S040", "whitespace", "formatting", G, "Walls of text hurt; leave spacing between jobs and projects.", "This is a wall of text. You need some white space between your jobs and projects.", "strong")
c("S040", "no_graphics_logos", "ats", G, "Remove logos/colored bars/text boxes; non-text elements can break ATS.", "Get rid of the little logos. Can cause issues in an ATS.", "moderate")
c("S040", "bullets_per_role", "length", G, "No hard 3-bullet rule; 4-6 relevant bullets are fine; 3-4 good beats 5-6 bad.", "3-4 good impactful bullet points are better than 5-6 bad bullet points.", "moderate")
c("S040", "bullet_length", "bullet_structure", G, "A 2-line bullet is fine if relevant; avoid spilling 1-4 words onto a new line.", "Don't spill bullets onto the following line with only 1–4 words on it. It's an extreme waste of space.", "moderate")
c("S040", "skills_in_bullets", "skills", G, "Skills listed must also appear in bullets to show where you used them.", "The keywords in the skills section need to be mentioned IN the bullet points themselves", "strong")
c("S040", "metrics", "metrics", G, "Add more metrics and context (how many users, how big, what improved).", "Bullet points need more impact. Put some more metrics on.", "moderate")
c("S040", "ai_written_fatigue", "anti_pattern", G, "Don't worry about sounding like AI; worry about long, fluffed-up lines.", "Don't worry about sounding like AI. Focus on clarity and relevancy. The big issue is when lines are too long", "moderate", "against")
c("S040", "title_accuracy", "formatting", G, "Use 'Software Engineering Intern' rather than 'Volunteer'; titles shape perception.", "You are better off saying you are a software engineering intern. Don't put volunteer.", "moderate")
c("S040", "work_auth", "formatting", G, "Put US citizen at the top of the resume.", "Put US citizen on the top of the resume.", "strong")
c("S040", "two_pages_ok", "length", G, "1-page is not a hard rule; exceptional students can go to 2 pages.", "The 1 page rule isn't a hard rule. It's all about relevancy", "moderate")
c("S040", "one_page", "length", G, "For typical early-career candidates there is zero reason to go to 2 pages.", "There is 0 reason someone with your experience should go to 2 pages.", "moderate")
c("S040", "coursework_low", "education", G, "Remove basic courses; they waste space.", "Remove the courses too. They are too basic.", "moderate")
c("S040", "experience_first", "section_order", G, "With 2+ years of experience, lead with experience not education.", "You are a worker with 2 years of experience. Why are you leading with education?", "moderate")
c("S040", "projects_depth", "projects", G, "Experienced candidates should go deeper on real experience instead of weak projects.", "You are better off going deeper on your actual experience.", "moderate")
c("S040", "skills_compact", "skills", G, "Consolidate skills, e.g., 'Python (NumPy, PyTorch, Django)'.", "Python (NumPy, PyTorch, Django), Java (Springboot), JavaScript (Node.js, React.js).", "moderate")
c("S040", "screen_time", "other", G, "7-15 seconds is the average because most resumes are unqualified; qualified ones get longer looks.", "Recruiters average 7-15 seconds but that's because most resumes are garbage", "moderate")
c("S040", "volume_flood", "other", G, "Recruiter sometimes reviews 1K+ resumes/day; >80% aren't qualified and some fake experience.", "Sometimes I am looking at 1K+ resumes in a day.", "strong")
c("S040", "communication_signal", "other", G, "Hiring teams' #1 complaint is poor communication; non-tech jobs can show it for early career.", "The number 1 feedback for engineering roles I get from hiring teams is that candidates have terrible communication.", "moderate")
c("S040", "referrals_outreach", "other", G, "Referrals are often the first ones in.", "the referrals are often the first ones in", "moderate")
c("S040", "dates_format", "formatting", G, "Show months on dates (was it a 2- or 6-month internship?).", "Please put the months on your resume.", "moderate")

# ---------------- S041 HeadlessHeadhunter
c("S041", "single_column_simple", "formatting", G, "Single column, black and white, ~10.5 font.", "Single column resume, black and white, 10.5 Font", "strong")
c("S041", "first_bullet_summary", "bullet_structure", G, "First bullet under each job: plain-language summary of duties; then What + How + Why bullets.", "Your bullet points need to be in the following format: What + How + Why", "moderate")
c("S041", "stack_focus", "tech_keywords", G, "Make the target stack obvious (FE, BE Python, BE Java, full stack); keywords differ by stack.", "SWE hiring is based on the tech stack you have.", "strong")
c("S041", "tailor_keywords", "tech_keywords", "data_engineering", "DE recruiters look for Python/Scala, SQL, Spark, cloud, ETL, BI tools, communicating data plans.", "SQL, Big Data (Spark), Cloud", "moderate")
c("S041", "tailor_keywords", "tech_keywords", "ai_ml_engineering", "ML engineer keywords: degree, ML, models, LLM/NLP/AI, Python.", "The keywords I would be looking for in an ML Engineer are", "moderate")
c("S041", "ats_myth", "ats", G, "ATSs don't reject people; recruiters do. Write for the recruiter and the HM.", "ATS don't reject people recruiters do", "strong")
c("S041", "ai_written_fatigue", "anti_pattern", G, "Recruiter strongly dislikes AI-written resumes.", "I also really really really hate AI resumes, they typically are crap.", "moderate")
c("S041", "skills_concise", "skills", G, "Skills section no more than 3 lines.", "you should have it be no more than 3 lines", "moderate")
c("S041", "education_one_line", "education", G, "Education 1-2 lines (GPA, Dean's list); drop to one line after a year or two.", "You need to have it be one line, or two lines and include the Deans list and GPA", "moderate")
c("S041", "projects_first_intern", "section_order", G, "For internship applicants, projects can go above weak experience.", "projects should be above your experience since you are applying to internships", "moderate")
c("S041", "work_auth", "formatting", G, "If US citizen/green card, state it under contact info; use a US number.", "If you are a US Citizen or Green Card holder you need to put that on your resume", "strong")
c("S041", "summary_skip", "section_order", G, "Lose the summary; you don't need it.", "Lose the summary you don't need it.", "moderate")
c("S041", "file_types", "ats", G, "PDF and Word show up in most ATS; never images/photos of resumes.", "PDF and Word.doc will show up in most ATS", "moderate")

# ---------------- S042 emmanuelgendre (ex-Google recruiter)
c("S042", "tech_depth", "bullet_structure", "backend_distributed", "Go deeper on technical details: techniques, engineering problems solved, patterns.", "mentioning techniques, engineering problems solved, and paradigms/patterns", "strong")
c("S042", "summary_use", "section_order", G, "A profile summary is convenient for skimming recruiters; make it an elevator pitch covering key requirements.", "A good Profile Summary is super convenient because it does that job for us.", "moderate")
c("S042", "two_pages_ok", "length", G, "Total length is not that important; recruiters skim rather than read top to bottom.", "Total length is not that important.", "moderate")
c("S042", "bold_keywords", "bolding", G, "Bolding key tools, metrics and concepts helps recruiters parse quickly.", "Bolding key tools/technologies, metrics and important concets help recruiters parse key information quickly", "moderate")
c("S042", "great_exp_bad_resume", "bullet_structure", G, "Good-company candidates with thin descriptions lose at shortlist stage to those who describe achievements.", "their resumes would suffer in comparison to those who clearly described their achievements", "strong")
c("S042", "reapply_avoid", "other", G, "Don't reapply to the same role; ATS merges profiles. Reach out instead.", "Modern ATS have cross-referencing features and will merge profiles.", "moderate")
c("S042", "ats_score_noise", "ats", G, "Free resume-scan scores are arbitrary and tied to selling services.", "most of these tools give poor scanning reviews, based on arbitrary components", "moderate")
c("S042", "metrics", "metrics", G, "Tangible metrics (e.g., 'reducing server costs by 32%') are a strength.", "Your resume includes clear and tangible metrics to quantify your impact", "moderate")

# ---------------- S043 LaFantasmita
c("S043", "summary_use", "section_order", G, "Recruiter read order: summary (right position), skills (right skillset), experience (how good).", "I looked for is this the right position (summary), the right skillset (skills), and are they sufficiently good at it (experience)", "moderate")
c("S043", "keyword_stuffing_bad", "anti_pattern", G, "Don't make the resume unreadable for keywords; a person will read it.", "A person is gonna read your resume at some point, and if it's a nightmare to read it's gonna go in the trash.", "strong")
c("S043", "bullets_per_role", "length", G, "Five bullets per job maximum; summary readable in ~10 seconds.", "5 bullets per job MAX.", "moderate")
c("S043", "title_accuracy", "formatting", G, "Keep titles close to the job titles you're applying for.", "I keep it close to the job titles I'm applying for.", "moderate")
c("S043", "metrics", "metrics", G, "Get numbers into bullets, even counts and team sizes.", "Get some numbers in your bullet points", "moderate")

# ---------------- S044 RealisticRecruiting (Teal)
c("S044", "ats_myth", "ats", G, "ATSes aren't evil machines; scary ATS stories come from people with something to sell.", "most scary ATS stories and myths come from people who have something to gain from these stories", "strong")
c("S044", "ai_use_refine_ok", "other", G, "You won't be eliminated for using AI, but for using it poorly; AI reads like AI.", "You're not going to get eliminated because you use AI, you're going to get eliminated because you use AI poorly.", "strong")
c("S044", "ai_written_fatigue", "anti_pattern", G, "Low-effort AI resumes are common in tech and consistently weaker.", "I'm seeing a ton of resumes and applications that are AI with no effort put into it", "moderate")
c("S044", "bullet_length", "bullet_structure", G, "Trend toward efficient resumes; bullets of 3-4 lines are outdated.", "paragraphs or bullet points that are 3 or 4 lines long", "moderate")

# ---------------- S045 Diligent_Working2363 (embedded recruiter)
c("S045", "title_keyword_embedded", "domain_specific", "embedded_systems", "The title 'embedded software engineer' with dates is enough to trigger outreach.", "What I saw was the words embedded software engineer with a date next to it. That is all I need", "moderate")
c("S045", "projects_skeptic", "projects", "embedded_systems", "This recruiter doesn't look at projects; billable experience matters much more.", "As a recruiter, billable hours matter more to me than projects. Much more.", "moderate")
c("S045", "embedded_scarcity", "domain_specific", "embedded_systems", "Embedded software engineers are among the hardest candidates to find in aerospace/defense.", "Embedded Software is probably the most difficult and expensive candidate to find in the entire industry.", "weak")

# ---------------- S046 PhenomEng (hiring manager)
c("S046", "coursework_low", "education", G, "Don't list related classes; HMs know the curriculum. Exception: specific technical electives.", "don't put related classes. Engineering hiring managers are generally engineers too, and we know what classes you take", "strong")
c("S046", "accomplishments_not_duties", "bullet_structure", G, "A list of job descriptions isn't a resume; show accomplishments.", "this is just a series of job descriptions, not a resume", "strong")
c("S046", "summary_skip", "section_order", G, "Drop the objective statement; it means nothing.", "get rid of the objective statement. It means nothing.", "strong")
c("S046", "honesty", "anti_pattern", G, "Never exaggerate or lie; integrity matters to HMs.", "Why would you tell someone to exagerrate and lie? Have some integrity.", "strong")
c("S046", "ats_myth", "ats", G, "ATSs don't screen resumes in general; optimize for the job description instead.", "You should do job description optimization, not ATS. ATSs don't screen resumes (in general).", "strong")
c("S046", "tense_past", "tense_verbs", G, "Don't use present tense; write accomplishments, not a job description.", "don't use current tense in your resume", "moderate")
c("S046", "typos", "anti_pattern", G, "Obvious grammatical errors undermine the resume; proofread.", "The amount of obvious grammatical errors in this resume is...astounding.", "strong")
c("S046", "single_column_simple", "formatting", G, "Ditch two-column formats, icons and symbols; use a wiki template.", "Ditch the two column format.", "strong")
c("S046", "project_context", "projects", G, "Explain what problem a project solved and how; don't assume reviewers know niche terms.", "I have no idea what your capstone was, what problem you solved or how you solved it.", "moderate")
c("S046", "projects_not_experience", "section_order", G, "Projects are not experience; keep them in their own section.", "Projects are not experience.", "moderate")

# ---------------- S047-S051 other recruiters
c("S047", "margins_whitespace", "formatting", G, "Slightly larger margins make the resume breathable and skimmable.", "make the margins a bit larger so everything is more breathable", "weak")
c("S047", "accomplishments_not_duties", "bullet_structure", G, "Make bullets impact-oriented.", "you can make your bullet points more impact oriented", "weak")
c("S048", "metrics", "metrics", G, "Quantifying impact is not a deal breaker; proof of technical skills matters more.", "The impact/quantifying portion that people like to peddle are not a deal breaker to me", "moderate", "against")
c("S048", "no_text_boxes", "ats", G, "Remove text boxes; missing education dates may be a deal breaker.", "Get rid of the text box. No dates on the education may a deal breaker for some.", "moderate")
c("S049", "experience_first", "section_order", "general_swe", "Put experience at the top; ATS re-renders resumes as plain text and can split comma-separated skills.", "I always suggest that candidates put their experience at the top. Skills shouldnt be at the top.", "moderate")
c("S049", "ats_parse", "ats", G, "ATSs generate their own plain-text version of your resume; complex layouts get mangled.", "they generate and format their own resume, which is basically a notepad file", "moderate")
c("S050", "ats_parse", "ats", G, "Both PDF and DOCX are readable; avoid graphics, text boxes, unusual characters and multiple columns; verify parsed fields.", "As long as your resume doesn't have graphics, text boxes, unusual characters or fonts, or multiple columns, it should parse", "strong")
c("S051", "contact_basics", "formatting", G, "Use a Gmail address (US norm) and condense skills white space.", "Get a Gmail account instead of Hotmail", "weak")
c("S051", "bold_minimal", "bolding", G, "Bold university name and skill categories to guide the eye.", "Add more bold like the University name and the skill category names", "weak")

# ---------------- S052 HM: hiring broken (2026)
c("S052", "ai_written_fatigue", "anti_pattern", G, "Almost all resumes are LLM-optimized to the JD with key requirements bolded; HM can't trust them.", "Almost all the resumes have been run through an LLM to be optimized for the job description", "strong")
c("S052", "bold_keywords", "bolding", G, "Bolding JD requirements throughout is now a red flag of LLM optimization.", "Every candidate sounds like a perfect fit with key requirements bolded throughout the resume", "strong", "against")
c("S052", "referrals_outreach", "other", G, "Personal referrals are at a premium in 2026.", "personal referrals are at a premium", "strong")
c("S052", "ats_score_noise", "ats", G, "LLM ranking pulls the most gamified resumes to the top.", "It pulls the most gamified resumes to the top of the stack", "moderate")
c("S052", "volume_flood", "other", G, "400 applicants in a few days from a LinkedIn post.", "Get 400 applicants in a few days just by posting on LinkedIn", "moderate")

# ---------------- S053 ExperiencedDevs GPT metrics (2025)
c("S053", "metrics_skepticism", "metrics", G, "Interviewers see uniform, GPT-style bogus metrics and distrust them.", "Every single resume we are getting sounds, looks and flows the same now. It's all full of BS bogus metrics from GPT.", "strong")
c("S053", "metrics_defensible", "metrics", G, "Interviewers probe metrics; candidates who can't explain them look bad.", "they're just too stupid to come up with a plausible explanation for the metric", "moderate")
c("S053", "metrics_not_always_applicable", "metrics", G, "Much valuable work isn't %-measurable (e.g., features that win a contract).", "There's no metric for \"implemented a feature that secured a tender for a government contract,\"", "moderate")

# ---------------- S054 cloud costs 20%
c("S054", "metrics_defensible", "metrics", "cloud_infra_sre", "Cost/latency metrics are conversation starters; interviewers ask how you measured your contribution.", "the more interesting question isn't how they saved the money but how they measured their contribution", "strong")
c("S054", "metrics", "metrics", "cloud_infra_sre", "Cloud cost savings are straightforward to measure from billing and are legitimate metrics.", "Cloud providers make it pretty straightforward to budget and analyze costs since it's how they bill you", "moderate")

# ---------------- S055 statistics everywhere (2026)
c("S055", "metrics_skepticism", "metrics", G, "Resume reviewers lose trust when every bullet carries an improvement percentage.", "I personally am losing trust as I start to see all the numbers dotted all over the place.", "strong")
c("S055", "metrics", "metrics", G, "Metrics exist because recruiters respond to them ('reduced latency by 30%' > 'implemented redis cache').", "reduced latency by 30% sounds incredible, while implemented redis cache and reduced latency sounds less sexy to recruiters", "moderate")

# ---------------- S056 Global 500 recruiter (2026)
c("S056", "proof_of_profit", "bullet_structure", G, "Show a pattern of adding value: make money, save money, or mitigate risk; execute rather than explain.", "Does my resume EXECUTE rather than EXPLAIN?", "moderate")
c("S056", "metrics_skepticism", "metrics", G, "Readers assume '% this and million that' metrics are often lies.", "If I saw % this and million that I’d assume most people are lying.", "moderate")
c("S056", "ghost_postings", "other", G, "Instant rejections can come from capped/ghost postings, not your skills.", "If you get rejected immediately, means it capped off or its a ghost posting", "weak")

# ---------------- S057 leaked agency spec (2025)
c("S057", "brands_matter", "education", "startup_fullstack", "Agency specs for funded startups filter on elite schools, GPA and specific prior companies.", "are MIT degree and 4-10 years of experience really necessary to develop a React app?", "moderate")

# ---------------- S058 Jake's resume (2026)
c("S058", "latex_template_ok", "formatting", G, "The plain 'Jake's resume' LaTeX template passes ATS and gets interviews; colorful templates are a risk.", "jakes got me past ATS and in person interviews at plenty of companies", "moderate")
c("S058", "recruiter_noise", "other", G, "Screening is noisy; people extrapolate patterns from noise.", "resume screenings are super random and people are trying to extrapolate a pattern from noise", "moderate")

# ---------------- S059 2 pages (2025)
c("S059", "one_page", "length", G, "Under 10 YOE a single page is best; 15-17 YOE engineers also trimmed to one page.", "If you’ve got 10+ yoe... make it 2 pages. Otherwise a single page is always best.", "moderate")
c("S059", "concise_leave_talking_points", "bullet_structure", G, "Make direct statements and leave details for the interview.", "make a direct/bold statement, leaving out some detail - so i have something to talk about later", "weak")

# ---------------- S060 AI tools on resume (2026)
c("S060", "ai_tools_listing", "skills", "ai_ml_engineering", "Show AI tool use through accomplishments (e.g., built shared agent skills) rather than a bare list.", "I'd put it in a better way instead of just listing it", "weak")
c("S060", "ai_tools_listing", "skills", G, "Listing 'Claude Code, Cursor' as skills is seen by some as meaningless.", "it's like pointing out you've mastered java by saying \"Java classes, JVM, inheritance with Java\"", "weak", "against")

# ---------------- S061 per-job LLM tailoring (2025)
c("S061", "tailor_keywords", "tech_keywords", G, "Rewriting the resume per job (even with an LLM) sharply increased reply rate for one engineer.", "I started taking my original resume and having chatGPT or whatever re-write it per job... AND I AM GETTING A REPLY TO EVERY JOB.", "weak")

# ---------------- S062 FAANG intern (2026)
c("S062", "internship_signal", "domain_specific", G, "A FAANG internship is expected to at least double interview hit rate the next cycle.", "I expect your hit rate next cycie will be at least 2 times x.", "weak")

# ---------------- S063 skills section (2026)
c("S063", "skills_section_keep", "skills", G, "Recruiters find a skills section helpful; HMs focus on per-job descriptions - keep both.", "I've been told by multiple recruiters that they found the skill section very helpful.", "moderate")
c("S063", "skills_in_bullets", "skills", G, "Reviewers read skills under each job; standalone lists don't show proficiency.", "When I am reviewing resumes I look at what is listed under each job.", "moderate")

# ---------------- S064-S070 embedded
c("S064", "skills_top", "section_order", "embedded_systems", "Embedded reviewers want technologies (SPI/I2C/UART, IDEs, compilers) up front.", "Skills up front. What parts did you work with? Do you know SPI/I2C/UART?", "moderate")
c("S064", "whitespace", "formatting", "embedded_systems", "Tighten wordy experience by ~50% and leave breathing room.", "Work experience is also too wordy. Tighten it up 50% and leave some breathing room here.", "moderate")
c("S065", "projects_own_code", "projects", "embedded_systems", "Interviewers are impressed by candidates who owned ~99% of their project code, not pasted examples.", "I was impressed by candidates who owned 99% of the code.driving their project.", "strong")
c("S065", "embedded_projects", "projects", "embedded_systems", "A from-scratch self-balancing robot (PID, sensor fusion, RTOS, PCB) is not 'basic'.", "PID control, sensor fusion, motor control, concurrency, various types of communications, power management", "moderate")
c("S066", "embedded_projects", "projects", "embedded_systems", "Basic I2C drivers are expected; show power-efficiency, sleep modes, wireless protocols instead.", "Writing an I2C driver for an Atmel is not something to put on your resume... it is expected", "moderate")
c("S066", "embedded_industry_parts", "tech_keywords", "embedded_systems", "Arduino isn't used in commercial products; choose industry-standard architectures.", "Arduino isn't really much used in commercial products.", "moderate")
c("S067", "embedded_projects", "projects", "embedded_systems", "Custom peripheral drivers are worth highlighting for embedded new grads if you can discuss the hardware.", "For an embedded resume having made custom drivers is something you'd definitely want to highlight.", "moderate", "against")
c("S068", "typos", "anti_pattern", "embedded_systems", "Broken typesetting/kerning signals weak computer skills.", "Fix your typesetting.", "moderate")
c("S068", "embedded_domain_keywords", "tech_keywords", "embedded_systems", "Automotive embedded roles expect process keywords (V-model, ASPICE, requirements management).", "Automotive skills are missing. Process (V-model / ASPICE), Requirements manage", "moderate")
c("S069", "projects_explainable", "projects", "embedded_systems", "A simple project you can discuss extensively beats a massive one you're unsure of.", "a “simple” project that you can talk about extensively because you are excited about it is always more valuable", "strong")
c("S070", "open_source_upstream", "projects", "embedded_systems", "Accepted upstream contributions (e.g., Zephyr) prove you write solid code.", "if you had a contribution accepted it means you write solid code", "moderate")

# ---------------- S071-S073 quant
c("S071", "quant_nda_metrics", "metrics", "quant_hft", "Don't disclose precise alpha/PnL that breaks NDAs; firms probe methodology (testing, data setup, drawdowns).", "how you test an assumption, how you set up your data for your model, how you protect yourself against drawdowns", "moderate")
c("S072", "projects_explainable", "projects", "quant_hft", "Quant projects get you hired only if you fully understand every working part; pure replication is weak.", "Replication is not the best way.", "moderate")
c("S072", "metrics", "metrics", "quant_hft", "For experienced quants, put the numbers that impacted PnL and your participation.", "I’d put the numbers that impacted the PnL and your participation in the projects.", "weak")
c("S073", "projects_explainable", "projects", "quant_hft", "Projects substitute for experience; what matters is talking through design and tradeoffs.", "being able to talk through your design, tradeoffs you made, what you learned", "strong")

# ---------------- S074 ML grad work
c("S074", "ml_research_fit", "domain_specific", "ml_research_robotics", "Grad research is valued when applying to research/applied ML teams; generic roles discount it.", "Grad student work is appreciated on a resume if you apply for jobs that are looking for the kinda work you did", "strong")
c("S074", "purpose_interview", "other", "ai_ml_engineering", "ML hiring manager: a resume only gets the recruiter to forward you and the HM to interview.", "A resume can convince the recruiter to show me the resume, and convince me that I should spend my time interviewing you", "moderate")

# ---------------- S075 robotics
c("S075", "typos", "anti_pattern", "ml_research_robotics", "Missing punctuation and messy spacing hurt robotics applicants.", "Tons of missing punctuation, doesnt look good to an employer", "moderate")
c("S075", "project_context", "projects", "ml_research_robotics", "Explain how you built things; listing without context is worse than no experience.", "explaining what you did without context is worse than no experience", "moderate")
c("S075", "robotics_stack", "tech_keywords", "ml_research_robotics", "Add programming specifics, GitHub projects; MISRA/AUTOSAR for automotive.", "Get up to speed on MISRA and basics of AUTOSAR if your trying to get into automotive.", "moderate")
c("S075", "gpa_threshold", "education", "ml_research_robotics", "Listing a mediocre GPA might hurt.", "Listing your GPA might actually be hurting your chances a little.", "weak")

# ---------------- S076/S077 devops/platform
c("S076", "homelab_projects", "projects", "cloud_infra_sre", "For freshers, a homelab (K8s, Argo CD, Grafana) is a positive; list as project, not experience; be ready to defend it.", "For a fresher, this is a positive addition to the resume and as a hiring manager I would like to ask questions", "moderate")
c("S076", "honesty", "anti_pattern", "cloud_infra_sre", "List it as a personal lab, not professional experience.", "list it under projects/personal labs, highlight the skills... without calling it professional experience", "moderate")
c("S077", "platform_framing", "domain_specific", "cloud_infra_sre", "Platform/DevEx roles want builder proof: tools developers use, not just infra/CI-CD operations.", "it doesnt say if you built any tools for developers to actually use", "moderate")
c("S077", "platform_framing", "domain_specific", "cloud_infra_sre", "Mention platform-as-a-product and core platform keywords.", "Zero mention of platform as a product", "weak")

# ---------------- S078/S079 data engineering
c("S078", "de_sql_core", "tech_keywords", "data_engineering", "SQL remains ~95% of DE work; cloud is easy to learn and list.", "entire DE is still and heavily done using 95% SQL, even at FAANG companies", "moderate")
c("S079", "de_demos", "projects", "data_engineering", "A live pipeline demo beats any resume bullet.", "A live pipeline you can walk them through beats any resume bullet.", "weak")

# ---------------- S080 AI labs (aggregator)
c("S080", "research_oss_top", "projects", "ml_research_robotics", "At Anthropic independent projects are primary evidence of capability; build visible public artifacts.", "At Anthropic, they're the primary evidence of capability.", "moderate")
c("S080", "ml_papers", "domain_specific", "ml_research_robotics", "DeepMind Research Scientists need top-venue publications; Research Engineers do not.", "Research Engineers at DeepMind do NOT require publications as a prerequisite.", "moderate")
c("S080", "github_readme", "projects", "ml_research_robotics", "GitHub repos without READMEs and problem statements are invisible to researchers.", "Repositories without READMEs, without context, without clear problem statements, are invisible to researchers.", "moderate")
c("S080", "replication_analysis", "projects", "ml_research_robotics", "Paper replication is table stakes; document what was unclear and what mattered.", "Reproducing a paper's results is table stakes.", "moderate")
c("S080", "referrals_outreach", "other", "ml_research_robotics", "Lab resume screens favor candidates whose work is already known internally; referrals carry context.", "They're candidates whose names or work are already known to someone in the room", "moderate")

# ---------------- S081 Sundeep Teki
c("S081", "ml_papers", "domain_specific", "ml_research_robotics", "NeurIPS/ICML publications reportedly raise interview chances 30-40% (unverified).", "ML engineers with publications in NeurIPS, ICML have 30-40% higher chance of securing interviews.", "weak")
c("S081", "research_sensibility", "domain_specific", "ml_research_robotics", "Research engineers need research sensibility: read papers, implement novel ideas.", "Research Sensibility: Ability to read papers, implement novel ideas, and think critically about AI safety", "moderate")
c("S081", "metrics", "metrics", "ml_research_robotics", "Be specific with metrics and concrete outcomes.", "Be specific with metrics and concrete outcomes.", "weak")

# ---------------- S082 MLEPath HM
c("S082", "metrics", "metrics", "ai_ml_engineering", "Include quantifiable ML achievements, e.g., inference-time reduction.", "Include quantifiable achievements (e.g., \"Reduced inference time by 40% through model optimization\")", "moderate")
c("S082", "referrals_outreach", "other", "ai_ml_engineering", "At Adobe a trusted referral earned a careful look and often bypassed initial screening.", "a recommendation from a trusted team member would always earn a candidate a careful look", "strong")
c("S082", "tailor_cover_letter", "other", "ai_ml_engineering", "Spend less time personalizing the resume and more on targeted cover letters.", "People spend too much time personalizing their resume, instead write a personalized cover letters", "weak", "for")

# ---------------- S083 TechieCV ML
c("S083", "ml_production", "domain_specific", "ai_ml_engineering", "ML resumes that read like research logs (papers, Kaggle) without serving stack or latency stall.", "no serving stack, no latency figures, no model the business actually relies on, stalls before any screening call", "strong")
c("S083", "summary_use", "section_order", "ai_ml_engineering", "Profile summary of 4-5 bullets: target title/years, domain, stack, collaboration, leadership.", "The opening 4-5 lines that set up everything that follows.", "moderate")
c("S083", "standard_headings", "ats", "ai_ml_engineering", "Use simple section titles: Profile Summary, Technical Skills, Work Experience, Education.", "Title them Profile Summary, Technical Skills, Work Experience, Education.", "moderate")
c("S083", "pdf_text_selectable", "ats", "ai_ml_engineering", "Don't build in Canva/Figma; parsers extract text, not pictures.", "Make the file in Canva, Figma, or a similar graphics app, and the wording exits the page as a flat picture.", "strong")
c("S083", "skills_in_bullets", "skills", "ai_ml_engineering", "Five categorized skill rows, every skill backed by a bullet.", "5 ordered rows of skills, with every chip pointing to a bullet.", "moderate")

# ---------------- S084 TechieCV backend
c("S084", "backend_metrics", "metrics", "backend_distributed", "Backend metrics to cite: P95/P99 latency, requests per second, error rate, uptime, cost per request.", "Metrics P95 / P99 latency Requests per second Error rate", "moderate")
c("S084", "backend_role_profile", "domain_specific", "backend_distributed", "Cover the backend role profile: API design, domain modeling, data layer, architecture, async messaging, performance/caching.", "You own the data layer: schema, indexes, queries that scale.", "moderate")
c("S084", "ats_parse", "ats", "backend_distributed", "Claims broken parsing knocks out 95% of applications before a human looks (unsupported figure).", "it's broken parsing that knocks you out of 95% of applications before a human ever looks", "weak")
c("S084", "summary_use", "section_order", "backend_distributed", "No resume should skip the profile summary.", "Whatever you've read elsewhere, no resume should skip the Profile Summary.", "moderate")

# ---------------- S085 Black Coffee Robotics founder
c("S085", "brands_matter", "education", "ml_research_robotics", "Startup founder ignores institute and GPA; cares about work.", "We don’t care about your institute or your GPA — we care about your work.", "strong", "against")
c("S085", "github_readme", "projects", "ml_research_robotics", "Code should be clean, reproducible, ideally used by others; usefulness over complexity.", "Not just a raw, undocumented script — but something clean, reproducible, and ideally, used by others.", "strong")
c("S085", "buzzword_avoid", "anti_pattern", "ml_research_robotics", "Explain projects plainly without jargon (which ROS nodes, which planner).", "No buzzwords needed.", "moderate")

# ---------------- S086 Careers in Robotics
c("S086", "robotics_stack", "tech_keywords", "ml_research_robotics", "Foundational robotics skills: C++/Python, ROS, a simulator, frames/transforms, kinematics, linear algebra.", "C++/Python programming, working knowledge of ROS, working knowledge of at least one simulator (Gazebo, PyBullet, Isaac Gym, etc.)", "strong")
c("S086", "projects_depth", "projects", "ml_research_robotics", "Show ~3 well-documented robotics projects with tests rather than many unfinished ones.", "It’s better to show 3 well-explained robotics projects with clear communication, tests, and documentation than 30 unfinished experiments.", "strong")
c("S086", "github_portfolio", "projects", "ml_research_robotics", "A web-based portfolio (GitHub, site) is strongly preferred.", "A web-based portfolio (GitHub, personal site) is strongly preferred.", "moderate")
c("S086", "metrics", "metrics", "ml_research_robotics", "Concrete impact (latency reduction, accuracy improvement, sim runtime scaling) advances candidates.", "Candidates who highlight concrete impact — such as system latency reduction, model accuracy improvements, or simulation runtime scaling — tend to advance.", "moderate")
c("S086", "internship_signal", "domain_specific", "ml_research_robotics", "Path to full-time robotics roles almost always runs through an internship.", "The path to a full-time offer almost always runs through an internship.", "moderate")
c("S086", "robotics_software_demand", "domain_specific", "ml_research_robotics", "Software skills dominate robotics postings (back end, UI, data, computer vision).", "software skills dominate", "moderate")

# ---------------- S087 Wiz SRE
c("S087", "infra_metrics", "metrics", "cloud_infra_sre", "Quantified reliability metrics (MTTR, uptime, automation hours saved) separate strong SRE resumes.", "Quantified reliability metrics like MTTR reduction, uptime percentages, and automation hours saved", "moderate")
c("S087", "infra_keywords", "tech_keywords", "cloud_infra_sre", "SRE skill categories scanned: cloud, observability, IaC, containers, programming languages.", "cloud platforms, monitoring and observability, infrastructure as code, containerization, and programming languages", "moderate")
c("S087", "infra_code_not_ops", "domain_specific", "cloud_infra_sre", "Show software-engineering depth and reliability impact, not just DevOps tools or sysadmin duties.", "not just list DevOps tools or sysadmin duties", "moderate")
c("S087", "infra_modern_sre", "domain_specific", "cloud_infra_sre", "Modern SRE resumes cite error budgets, production readiness reviews, automated remediation.", "error budget management, production readiness reviews, and automated remediation pipelines", "moderate")

# ---------------- S088 Exponent DE (recruiter)
c("S088", "de_metrics", "metrics", "data_engineering", "Each DE role should show measurable results (e.g., faster reports, pipeline efficiency).", "Each role should have demonstrable, measurable results.", "moderate")
c("S088", "de_balance", "projects", "data_engineering", "Projects should balance technical skills (cloud, data tools, APIs) with business impact.", "Each project should balance technical skills (cloud, data tools, APIs) with the impact it had on the business.", "moderate")
c("S088", "tailor_keywords", "tech_keywords", "data_engineering", "Relevant DE keywords help resumes get discovered by ATS search.", "Relevant data engineering keywords help resumes get discovered and scanned by applicant tracking systems.", "moderate")
c("S088", "summary_use", "section_order", "data_engineering", "Present a clear value proposition in the summary.", "Always present a clear value proposition in the resume summary", "weak")

# ---------------- S089/S090 quant guides
c("S089", "screen_time", "other", "quant_hft", "Quant recruiters spend 15-30 seconds per resume.", "Recruiters at quantitative firms spend 15 to 30 seconds on an initial screen", "moderate")
c("S089", "gpa_threshold", "education", "quant_hft", "Include GPA if 3.7+/First/2:1; otherwise leave it off.", "if it's strong (First Class, 2:1, or 3.7+ on a 4.0 scale), include it", "moderate")
c("S089", "skills_defensible", "skills", "quant_hft", "Only list tools you can discuss confidently; listing everything is a red flag.", "Only list tools you could discuss confidently in an interview.", "strong")
c("S089", "projects_include", "projects", "quant_hft", "Projects are arguably the most important section without industry experience.", "This is arguably the most important section on a quant resume", "moderate")
c("S089", "metrics", "metrics", "quant_hft", "Quantified results everywhere (e.g., Sharpe, annualized return on backtests).", "Quantified results everywhere", "moderate")
c("S090", "one_page", "length", "quant_hft", "One page, no exceptions before ~5 years.", "One page. No exceptions before ~5 years of experience.", "strong")
c("S090", "single_column_simple", "formatting", "quant_hft", "Single column, no graphics, no skill bars.", "Single column, no graphics. Photos, skill bars, and two-column layouts break ATS parsers and add zero information.", "strong")
c("S090", "education_first_student", "section_order", "quant_hft", "Order: Education, Experience, Projects, Skills & Awards for students.", "Section order: Education, Experience, Projects, Skills & Awards.", "moderate")
c("S090", "gpa_threshold", "education", "quant_hft", "State GPA if ~3.7+; omission is read as hiding it.", "Omitting GPA is read as hiding it.", "moderate")
c("S090", "xyz_formula", "bullet_structure", "quant_hft", "Bullet = action verb + specific method + scale + measured result.", "action verb + specific method + scale + measured result", "strong")
c("S090", "cpp_lowlatency", "domain_specific", "quant_hft", "Developer bullets should show latency work (e.g., p99 from 8us to 1.9us via allocation changes).", "cut p99 message-processing latency from 8μs to 1.9μs", "moderate")
c("S090", "competitions_signal", "domain_specific", "quant_hft", "Trader track: lead with competitions, math contests, poker/chess, Zetamac scores.", "Trader: lead with speed and competition.", "moderate")
c("S090", "metrics_defensible", "metrics", "quant_hft", "An honest 'found nothing and here's why' beats an unverifiable Sharpe of 3.", "\"I found nothing and here’s why\" defended honestly beats an unverifiable Sharpe ratio of 3", "moderate")

# ---------------- S091 levels.fyi review (foundational-ish)
c("S091", "skills_in_bullets", "skills", G, "Skills section should include technologies used in bullets.", "Your skills are missing a lot of the content in your bulletpoints", "weak")
c("S091", "xyz_formula", "bullet_structure", G, "Lead with the result (e.g., 'Reduced login time by 90%') then the method.", "[Optimized login time from 12 seconds to 2 seconds/Reduced login time by 90%] via a Python and Selenium script", "moderate")

# ---------------- S092 Gayle (foundational)
c("S092", "accomplishments_not_duties", "bullet_structure", G, "Accomplishments, not responsibilities ('Reduced time to perform X by 75% by optimizing Y').", "\"Reduced time to perform X by 75% by optimizing Y\" looks much more impressive than \"Responsible for optimizing X.\"", "strong")
c("S092", "projects_include", "projects", G, "Have a projects section; 3-4 projects is ideal.", "3 to 4 projects is ideal, whether they're class project or personal projects", "strong")
c("S092", "one_page", "length", G, "Recent grads: one page.", "if you're a recent college graduate (last few years), your resume should probably be one page", "strong")
c("S092", "gpa_threshold", "education", G, "Missing GPA is assumed below 3.0; list a 3.2.", "If your GPA isn't on your resume, the assumption is that it's below a 3.0.", "moderate")
c("S092", "soft_skills_avoid", "anti_pattern", G, "Kill the fluff (claims of teamwork skills).", "I have never once said \"oooh... this person claims to have great team working skills. Let's hire them!\"", "moderate")
c("S092", "skills_defensible", "skills", G, "Only list languages you can actually use; you may be tested.", "If you list C++, you should be able to write in C++ - and they might just test you on it.", "strong")
c("S092", "screen_time", "other", G, "Employers glance for 10-15 seconds.", "they glance at it for, oh, 10 - 15 seconds", "moderate")
c("S092", "typos", "anti_pattern", G, "Check spelling, grammar and typos; have many people review.", "make sure to check for spelling mistakes, grammatical mistakes and typos", "moderate")
c("S092", "no_photo_personal", "formatting", G, "Don't list age, marital status or gender for US positions.", "Please don't list your age, marital status, gender, etc.", "moderate")

# ---------------- S093 metrics made up (community)
c("S093", "metrics_fabrication", "metrics", G, "Students report guessing or inventing metrics because quantification is demanded; an LLM 'called bs'.", "people just guesstimate or make stuff up. i hate that it’s seen as standard", "moderate")
