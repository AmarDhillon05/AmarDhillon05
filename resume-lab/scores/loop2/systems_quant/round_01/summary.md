# Loop 2 · systems_quant · round 01 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.0 | 7 |
| quantification | 7.67 | 7 |
| technical_depth | 7.67 | 7 |
| concision_readability | 7.33 | 7 |
| skim_test | 7.33 | 7 |
| credibility | 7.67 | 7 |
| ats_parseability | 8.0 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 7.33 | 6 |
| human_voice | 7.0 | 6 |
| plain_language | 6.67 | 6 |
| overall | 7.67 | 7 |

**Plain-English restatement (recruiter):** 9/10 bullets understood
**Competitive:** {'recruiter_v2': 'Y', 'skeptic_v2': 'stretch', 'systems_quant_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "IEX Order Book & Matching Engine project in C++ that replayed ~50.9M real exchange messages and matched the exchange almost exactly",
  "Amazon Web Services SDE Intern (Redshift capacity planning)",
  "Capital One Software Engineering Intern (sped up an AI workflow tool by 65%)"
 ],
 "engineer_type": "A C++ / performance-minded systems student who also has a lot of AWS cloud and AI-tooling internship work; reads more 'cloud + AI' in the Experience section and more 'low-latency systems' in the project",
 "memorable_numbers": [
  "50.9M messages",
  "1.26M events/sec",
  "12.8x",
  "65%",
  "34%",
  "GPA 3.5",
  "May 2028"
 ],
 "confusing": [
  "The second project bullet (std::map of std::list FIFOs ... list iterator) - I could not tell what it means beyond 'fast'",
  "'do-nothing control book' in the regression bullet",
  "What 'Amazon Leo' is and whether this is Amazon work or a student contracting group",
  "Why a matching engine needs a B+ tree vs LSM-tree 'event log'"
 ],
 "skipped": [
  "UMIACS robotics bullet",
  "TerpLabs bullet",
  "Most of the Technical Skills section beyond seeing C++17 first"
 ],
 "interview_questions": [
  "Walk me through how you checked your engine against the exchange - what was the one fill that didn't match?",
  "How did you figure out the slowdown was the CPU frequency setting and not your code?",
  "What are you building at AWS and how will you know it works?",
  "At Capital One, what is a 'workflow' and who uses the tool you sped up?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Stored price levels in a std::map of std::list FIFOs with a hash map from order ID to list iterator for O(1) cancels, sustaining 1.26M events/sec over the full replay and a 1.2 µs per-update p99 on a separate 2M-event run
- **recruiter_v2** (sev 7): The first half is a chain of container names ('std::map of std::list FIFOs with a hash map from order ID to list iterator') that a non-engineer cannot parse, and the purpose ('O(1) cancels') is buried in the middle. The two speed results then come from two different runs ('over the full replay' vs 'on a separate 2M-event run'), which adds a qualifier I have to untangle.. *Direction:* Lead with the goal and result, then the structure in fewer nouns; consider trimming the 'separate 2M-event run' qualifier. Example: 'Designed the book so any order can be cancelled in constant time (price levels as FIFO queues in a std::map, indexed by order ID), sustaining 1.26M events/sec with a 1.2 µs p99 per update'
- **skeptic_v2** (sev 5): The first half is a noun stack ('std::map of std::list FIFOs with a hash map from order ID to list iterator') that has to be parsed twice. It also leads with the textbook node-based layout (std::map plus std::list, one heap allocation per order), which is the first thing an HFT interviewer will push on. The bullet presents that layout as the design win without saying it was a deliberate baseline or what it was traded against.. *Direction:* Split the structure into a short plain sentence ('kept each price level as a FIFO queue, with an order-ID lookup so cancels don't scan the queue'), then give the numbers. Keep the STL names to one clause, or move them to the project header.
- **systems_quant_v2** (sev 5): The two performance numbers don't say what they include or how they were run. '1.26M events/sec' doesn't say whether message parsing/decoding is inside the timed loop or whether it ran single-threaded. '1.2 µs per-update p99' doesn't say whether that is book update only or parse+match. Neither says whether it was measured before or after the core-pinning and fixed-clock setup in bullet 4. Also, 'per-update' (p99) and 'events' (throughput) use different units for what may be the same thing.. *Direction:* Use one unit noun for both numbers and add a short scope phrase saying what was timed. If space is tight, cut 'Stored price levels in' and start the bullet at the data structure so the timing scope fits.

### PRIORITY · 3 evaluators · max sev 5
> Traced an apparent 1.65x regression to the CPU frequency governor, not a code change, using perf counters and a do-nothing control book, then cut run-to-run variance from about 6% to 0.06% by pinning cores and fixing the clock
- **recruiter_v2** (sev 5): 'do-nothing control book' is insider shorthand I can't decode, and 'fixing the clock' reads like repairing the system time rather than locking the CPU speed.. *Direction:* Rephrase the two shorthand terms in plain words, e.g. 'a no-op baseline book' and 'locking the CPU frequency'
- **skeptic_v2** (sev 2): 'fixing the clock' can be read as 'repairing a broken clock' rather than 'locking the CPU frequency'. 'not a code change' sits awkwardly in the middle of the sentence.. *Direction:* Say 'locking the CPU frequency' in place of 'fixing the clock'. Otherwise leave this bullet alone.
- **systems_quant_v2** (sev 4): 'run-to-run variance from about 6% to 0.06%' doesn't say which statistic varied (throughput? p99? mean latency?) or how many runs it was measured over. A 100x drop to 0.06% is unusually tight, so readers will want the measure named.. *Direction:* Add the metric noun after 'variance' (e.g., 'run-to-run throughput variance'). 'about 6%' and the method can stay as is.

### PRIORITY · 3 evaluators · max sev 5
> Implemented B+ tree and LSM-tree backends for the event log and benchmarked them on identical 2M-record workloads, where the B+ tree gave 12.8x the read throughput and 22x faster range queries at the cost of 27% more disk space
- **recruiter_v2** (sev 4): 'for the event log' gives no reason why the engine has an event log or why read speed matters for it, so the comparison has no stakes.. *Direction:* Add a short phrase of context on what the log is for before the two backend names; keep the 12.8x / 27% tradeoff, which is a good honest framing
- **skeptic_v2** (sev 5): The comparison only reports the axes where the B+ tree wins (reads, range queries) plus disk space. Write throughput is missing, and write throughput is the whole reason to build an LSM tree. The bullet also never says why a matching engine's event log needs range queries or random reads.. *Direction:* State the access pattern that motivated the comparison first, then report both sides of the trade-off. If no write numbers exist, frame it as 'chose B+ tree because the log is read-heavy' instead of implying a general win.
- **systems_quant_v2** (sev 5): The comparison only shows the axes where the B+ tree wins (reads, range scans) plus disk space. It leaves out write/append throughput, which is the reason anyone builds an LSM tree for an append-heavy event log. '12.8x the read throughput' also doesn't say point reads vs. something else, or whether the LSM side had bloom filters/compaction tuned.. *Direction:* If a write-side number exists, state the tradeoff in both directions instead of reads-only plus disk. Otherwise name the read type ('point lookups') so the 12.8x is scoped.

### PRIORITY · 3 evaluators · max sev 5
> Because the 270K+ row PostgreSQL workflow table had strict access limits, precomputed popular workflows into a category tree that the Claude skill searches first, with Redis caching full workflows to cut database queries
- **recruiter_v2** (sev 5): Opening with a 'Because ...' clause delays the action; 'strict access limits' is vague (permissions? rate limits?); the sentence stitches three components (table, category tree, Redis) into one run-on.. *Direction:* Lead with the verb and what was built, then the constraint; consider splitting the Redis clause off or trimming it
- **skeptic_v2** (sev 5): The sentence opens with a subordinate clause and drops the subject ('precomputed' has no 'I'). 'strict access limits' is ambiguous: rate limits, permissions, or query quotas lead to very different designs. It ends on intent ('to cut database queries') with no result, and the 'with Redis caching' tail is a second idea stitched onto the first.. *Direction:* Lead with the action and put the constraint after it: 'Precomputed popular workflows into a category tree the assistant checks first, so most requests skip the rate-limited 270K-row PostgreSQL table; cached full workflows in Redis.' Cut the Redis clause if space is tight.
- **systems_quant_v2** (sev 3): 'strict access limits' is ambiguous: rate limits, query quotas, or permission restrictions? The reader can't tell what constraint drove the design. 'to cut database queries' ends at intent, with no sense of how much.. *Direction:* Replace 'strict access limits' with the specific constraint type. Keep the rest of the sentence.

### PRIORITY · 3 evaluators · max sev 4
> Built Redis caching in front of the Prisma ORM queries for Tortuga, the studio’s class scheduler with 20,000+ visits in its first 30 days, to reduce database load and latency
- **recruiter_v2** (sev 4): Ends at intent ('to reduce database load and latency'); the only number (20,000+ visits) describes the product, not the effect of the caching. 'the studio's' is unclear since TerpLabs is never described.. *Direction:* If a result exists, state it; otherwise lead with what Tortuga is and the scale, then the caching decision
- **skeptic_v2** (sev 4): The only number (20,000+ visits) measures the product's traffic, not the candidate's work. The bullet ends on intent ('to reduce database load and latency') with no result. 'the studio' is never explained (TerpLabs is apparently a studio). As a co-founder role, the single bullet is a routine cache add, which undersells or blurs what the candidate owned.. *Direction:* Separate the product context from the action: 'Co-built Tortuga, a class scheduler that drew 20,000+ visits in its first month; added a Redis cache in front of its database queries.' Or cut it for this target.
- **systems_quant_v2** (sev 3): 'to reduce database load and latency' states intent, not result. The only number (20,000+ visits) is product traffic, not an effect of the caching. A reader may misattribute it to the engineering.. *Direction:* If there was no measurement, phrase it as what was built and why (load profile) without implying a result, e.g., keep the traffic number as context for why caching was needed.

### PRIORITY · 3 evaluators · max sev 4
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **recruiter_v2** (sev 3): 'S3 staging hops' is jargon; the employer line 'UMD App Development Contracting (Client: Amazon Leo)' leaves me unsure whether this is Amazon work.. *Direction:* Rephrase 'S3 staging hops' as 'intermediate saves to S3' or similar
- **skeptic_v2** (sev 4): 34% has no absolute baseline (seconds per document, or per batch?), and '6,000+ documents' could mean in total, per day, or per run. 'Amazon Leo' in the header is unexplained, so many readers will think it's a typo or a made-up Amazon team.. *Direction:* Anchor the percentage with the absolute before/after if known. Otherwise drop 'end-to-end' and say what the latency is measured from and to.
- **systems_quant_v2** (sev 4): 'end-to-end latency 34%' doesn't say whether it's mean, median, or a tail percentile, or whether it's per document or per batch. There's no absolute baseline, so the reader can't tell if this is 10 s to 6.6 s or 10 min to 6.6 min.. *Direction:* Name the statistic and unit before the percentage (e.g., 'median per-document latency'). Add absolute before/after only if they were actually measured.

### PRIORITY · 3 evaluators · max sev 4
> For a PhD-led robotics project aimed at ICLR, built a pipeline that overlays AnyGrasp’s candidate grasps on camera images in Open3D for a vision-language model, then tuned prompts so the model picks the right grasp more often
- **recruiter_v2** (sev 3): 'more often' is unmeasured, and the bullet is the least relevant to systems/HFT, so it reads as filler for this target.. *Direction:* Keep it short; if a measured improvement exists, state it, otherwise consider trimming the tool names to fit one line
- **skeptic_v2** (sev 4): 'aimed at ICLR' leans on the venue's prestige without saying whether anything was submitted. 'picks the right grasp more often' is an unmeasured outcome. 'tuned prompts' is the weakest engineering claim on the page and has no place on a systems resume.. *Direction:* Cut the venue clause or state the status plainly. Shorten to one line so the space goes to systems evidence, or drop the role's bullet for this target.
- **systems_quant_v2** (sev 3): 'picks the right grasp more often' is the only outcome and has no measure. For this target the bullet carries no systems or performance signal and uses two lines.. *Direction:* For this domain-targeted version, consider trimming to one line by cutting 'aimed at ICLR' and the Open3D detail, keeping the role and what was built.

### PRIORITY · 2 evaluators · max sev 6
> Building capacity planning for Amazon Redshift maintenance like patching: Java logic that sets upper and lower bounds on reserved EC2 capacity to balance availability against cost, validated by backtesting
- **recruiter_v2** (sev 4): 'capacity planning for Amazon Redshift maintenance like patching:' is a compressed, stitched phrase, and the colon followed by 'Java logic that...' reads like a noun fragment rather than a sentence a person would say.. *Direction:* Turn it into one verb-led sentence, e.g. 'Building Java logic that sets upper and lower bounds on reserved EC2 capacity for Redshift maintenance work such as patching, balancing availability against cost; validating it by backtesting'
- **skeptic_v2** (sev 6): Colon-stitched and telegraphic. 'Building capacity planning' is not something you build, 'maintenance like patching' is awkward, and 'Java logic' is a placeholder noun that hides what the code does. It's also unclear what the candidate owns: the whole planner, the bounds algorithm, or one component.. *Direction:* Write it as one full sentence with a subject and verb, for example: 'Writing the Java service that decides how much EC2 capacity to reserve for Redshift patching windows, setting upper and lower bounds that trade availability against cost, and backtesting it against past maintenance.'

### PRIORITY · 2 evaluators · max sev 5
> Cut AI workflow generation time 65% to under 15s by replacing a Claude skill’s open-ended search with focused sub-skills that call Python tools for workflow search and validation, guided by CloudWatch and OpenSearch latency logs
- **recruiter_v2** (sev 5): 'workflow' is never defined, so I don't know what the tool produces or for whom; 'Claude skill' / 'sub-skills' is niche vocabulary; the tail 'guided by CloudWatch and OpenSearch latency logs' is a tool list stitched onto a long sentence.. *Direction:* Name what the workflows are in a few words up front; move CloudWatch/OpenSearch to Skills or cut 'guided by ... logs' to shorten the bullet
- **skeptic_v2** (sev 5): 'AI workflow generation' and 'Claude skill' are internal or vendor jargon that a trading-firm reader can't decode. The tail 'guided by CloudWatch and OpenSearch latency logs' is a tech trailer that adds two keywords but no mechanism. The verb chain (skill → sub-skills → Python tools → workflow search) is also hard to follow on one read.. *Direction:* Open with what the user waits for, then the change: 'Cut the time to generate a [workflow] from ~X to under 15s by splitting one open-ended LLM search into narrow steps backed by Python search and validation tools.' Cut the CloudWatch/OpenSearch trailer or turn it into 'after profiling where the latency went'.

### 1 evaluators · max sev 3
> Built a C++17 order book and matching engine and replayed 50.9M real IEX exchange messages through it without ever resyncing to the exchange’s book, agreeing with the exchange on 99,122 of 99,123 fills and 100% of top-of-book prices
- **recruiter_v2** (sev 3): 'without ever resyncing to the exchange's book' and 'top-of-book prices' are trading jargon a recruiter can't restate; the bullet is still understandable because the fills number carries it.. *Direction:* Optionally rephrase 'without ever resyncing' as 'without ever needing to correct its state from the exchange's data'

## Page-level
- **skeptic_v2** (sev 6): Only one project carries all the low-latency C++ evidence. Every Experience bullet is cloud, LLM-tooling, or ML work, and two of them are Redis caching.. *Direction:* Keep Projects above Experience. Trim or cut the UMIACS and TerpLabs bullets for this target, and use the freed space to make each remaining Experience bullet say what got faster or more reliable in systems terms (throughput, latency, bounds) rather than in product terms.
- **recruiter_v2** (sev 5): The Experience section (5 roles, all cloud/AI/web) visually outweighs the one C++ project, so the skim reads 'cloud + AI engineer' rather than 'low-latency systems engineer'.. *Direction:* Keep Projects first; consider trimming the least relevant experience bullets (UMIACS, TerpLabs) to one line each so the project dominates
- **systems_quant_v2** (sev 4): The project's performance numbers come from three different runs (full 50.9M replay for throughput, separate 2M-event run for p99, 2M-record workloads for storage), and the page doesn't say which run used the pinned/fixed-clock setup from bullet 4.. *Direction:* Make the measurement-setup claim cover the reported numbers explicitly, e.g., reorder so the variance-control bullet precedes the numbers, or add a short phrase showing the numbers were taken on the pinned setup (only if true).
- **recruiter_v2** (sev 3): Roughly the bottom 15% of the page is empty while several bullets are dense two-liners.. *Direction:* Slightly increase spacing between sections or entries to balance the page; do not fill it with new content
- **skeptic_v2** (sev 3): The Skills section carries keywords the page never backs up: Rust, TypeScript, C, Fargate, AWS CDK, GitHub Actions, 'data structures and algorithms'. It also has a parenthetical dump '(hardware counters, top-down analysis)'.. *Direction:* Drop 'data structures and algorithms'. Keep only languages the candidate can be grilled on, and fold 'top-down analysis' into the perf bullet if it was actually used there.
- **systems_quant_v2** (sev 3): Section order puts the IEX project above all experience, which is right for this target. But the Experience block (Capital One's Claude-skill bullets, UMIACS VLM prompting) is almost entirely LLM-tooling and cloud work with no C++ or low-level content.. *Direction:* Within the existing facts, order the experience bullets so the most latency/throughput-oriented ones (Leo Kinesis latency, Capital One latency-log-guided redesign) are the most visible. Consider shortening UMIACS to one line for this version.
- **recruiter_v2** (sev 2): GPA 3.5 sits in the education line with no coursework; HFT screeners often filter on GPA and look for systems/math coursework.. *Direction:* If relevant coursework exists (OS, architecture, algorithms), consider listing it in one line; otherwise leave as is
- **skeptic_v2** (sev 2): About 15% of the page at the bottom is empty, while several bullets are compressed to the point of dropping verbs and subjects.. *Direction:* Use the spare vertical space to let the AWS and Capital One bullets become full, readable sentences instead of adding content.
- **systems_quant_v2** (sev 2): Skills lists Rust and C, but no bullet shows either.. *Direction:* Keep only languages the candidate is ready to be quizzed on. Otherwise leave as is.
- **systems_quant_v2** (sev 2): About 20% of the page at the bottom is blank whitespace, while the experience bullets are compressed to one each.. *Direction:* Slightly increase inter-role spacing or section spacing to balance the page; no new content needed.
