# Loop 2 · systems_quant · round 04 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.67 | 7 |
| quantification | 7.33 | 7 |
| technical_depth | 7.67 | 7 |
| concision_readability | 7.33 | 7 |
| skim_test | 7.33 | 7 |
| credibility | 7.33 | 7 |
| ats_parseability | 8.0 | 8 |
| visual_layout | 7.67 | 7 |
| domain_fit | 7.0 | 6 |
| human_voice | 7.0 | 6 |
| plain_language | 6.67 | 6 |
| overall | 7.0 | 6 |

**Plain-English restatement (recruiter):** 9/10 bullets understood
**Competitive:** {'recruiter_v2': 'Y', 'skeptic_v2': 'stretch', 'systems_quant_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "IEX Order Book & Matching Engine in C++, the first thing under Projects, replaying ~50M real exchange messages",
  "Amazon Web Services SDE Intern (current, fall 2026)",
  "Capital One Software Engineering Intern (summer 2026), something with Claude / AI workflows"
 ],
 "engineer_type": "Systems/performance-leaning backend engineer: a C++ trading-engine project on top, then cloud/AWS and AI-tooling internships",
 "memorable_numbers": [
  "50.9M messages",
  "1.26M events/sec",
  "12.8x",
  "65%",
  "34%",
  "20,000+ visits"
 ],
 "confusing": [
  "What 'Amazon Leo' is, and whether that role was at Amazon or a student contracting group",
  "The std::map / std::list / hash map wording in the second order-book bullet",
  "What a 'Claude skill' and 'AI workflow generation' are at Capital One"
 ],
 "skipped": [
  "UMIACS robotics bullet (long, lots of tool names)",
  "TerpLabs bullet",
  "Most of the Technical Skills section beyond seeing C++17 first"
 ],
 "interview_questions": [
  "Walk me through the order book project: what made it hard to match the exchange, and what was the one fill that didn't match?",
  "What are you doing at AWS right now, and how big is the team?",
  "What was the Capital One AI tool for, and who used it?",
  "Is the Amazon Leo work done for Amazon directly or through a UMD student program?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Designed the order book with std::list FIFOs per price level in a std::map and an order-ID hash map to make cancels O(1), which ran the full replay at 1.26M events/sec and hit a 1.2 µs p99 on a separate 2M-event run
- **recruiter_v2** (sev 4): The first half is a stack of four C++ type names ('std::list FIFOs per price level in a std::map and an order-ID hash map') before the reader learns the goal ('make cancels O(1)'). The numbers at the end are strong but come after the hardest part to read.. *Direction:* Put the purpose (instant cancels, orders kept in arrival order at each price) before the data-structure names, or name the structures in plain terms ('a queue per price level, plus a lookup by order ID').
- **skeptic_v2** (sev 7): The opening is a noun stack ('std::list FIFOs per price level in a std::map and an order-ID hash map') that must be parsed twice. The ending tacks two results onto one 'which' clause ('ran the full replay at ... and hit a 1.2 µs p99 on a separate 2M-event run'), breaking the one-sentence 'did X to accomplish Y, which did Z' rule. 'p99' of what (per-event processing, per-order, wall clock including parsing?) is not stated, and the 1.2 µs is from a different run than the 1.26M events/sec, so the two numbers can't be read together. Also, an HFT interviewer will see std::list + std::map (node-based, cache-unfriendly) and immediately ask why; the bullet presents this as a design win without showing awareness of that tradeoff.. *Direction:* Say the structure in plain words before the type names (a FIFO queue at each price, plus a lookup from order ID to its spot in the queue), keep one result in the 'which' clause, and label the p99. Move or drop the second metric rather than stitching it on with 'and'.
- **systems_quant_v2** (sev 6): The p99 does not say what it is the 99th percentile of (per-message processing in the book? per add/cancel/execute? including parsing?), and the bullet switches units from 'messages' (bullet 1: 50.9M messages) to 'events' (here: 1.26M events/sec) without saying whether they are the same thing. It also does not say whether these numbers were taken before or after the core-pinning fix described in bullet 4.. *Direction:* Name the timed operation next to the percentile and use one noun (messages or events) across bullets 1-2, e.g. '...1.2 µs p99 per-message book update on a separate 2M-message run'. If the runs were pinned, a two-word 'pinned core' tag removes the ambiguity with bullet 4.

### PRIORITY · 3 evaluators · max sev 6
> Built and prompt-tuned a pipeline for a PhD-led robotics project aimed at ICLR that overlays AnyGrasp's candidate grasps on camera images in Open3D to help a vision-language model pick grasps that avoid hitting the table
- **recruiter_v2** (sev 3): This is the longest bullet in Experience and stacks two tool names (AnyGrasp, Open3D) between the setup and the purpose. It also has nothing to do with the low-latency target.. *Direction:* Trim to the purpose and method (draw candidate grasps on images so the VLM avoids collisions), and move 'Open3D' to Skills if it's needed.
- **skeptic_v2** (sev 6): Four nested qualifiers ('for a PhD-led robotics project aimed at ICLR that overlays ... in Open3D to help ...') make the sentence a chain rather than one clean 'did X to accomplish Y, which did Z'. There is no 'which did Z' outcome at all. 'aimed at ICLR' signals an unaccepted submission and the candidate's contribution vs. the PhD student's is ambiguous. 'in Open3D' is a tool mention that doesn't explain the engineering.. *Direction:* Cut 'PhD-led' / 'aimed at ICLR' or move them out of the sentence's critical path, drop 'in Open3D', and end on what the overlay accomplished. Shortening is the main lever.
- **systems_quant_v2** (sev 2): No outcome, and the content (prompt-tuning, VLM grasp selection) is unrelated to low-latency systems; it takes two lines of a page whose strength is the C++ project.. *Direction:* Acceptable to keep; if space is needed for clarifications in the project bullets, this is the first candidate to shorten to one line.

### PRIORITY · 3 evaluators · max sev 6
> Traced an apparent 1.65x regression to the CPU frequency governor with perf counters and a do-nothing control book to rule out a code change, which led to core pinning that cut run-to-run variance from 6% to 0.06%
- **recruiter_v2** (sev 3): 'do-nothing control book' is a coined phrase that a non-engineer, and maybe some engineers, will stumble on. The 'which led to' chain makes it one long breath.. *Direction:* Rephrase 'do-nothing control book' as a plain description, e.g. 'a baseline build that did no matching work', keeping the rest as is.
- **skeptic_v2** (sev 3): Slight mechanism gap: the cause is the frequency governor, but the fix named is core pinning, which addresses migration rather than frequency scaling. Also long for two lines.. *Direction:* Make the fix match the diagnosis in wording, or be ready to explain the link; otherwise leave this bullet alone, it is the most interview-ready one on the page.
- **systems_quant_v2** (sev 6): 'run-to-run variance from 6% to 0.06%' does not say which metric varied (throughput? p99?), how it is computed (coefficient of variation? max-min spread?), or over how many runs. The cause is the frequency governor but the fix named is core pinning; a reader expects the governor to be fixed (performance mode / fixed frequency) and wonders whether pinning alone explains a 100x drop.. *Direction:* Name the measured quantity and run count in place of the bare word 'variance' (e.g. 'cut throughput spread across N runs from 6% to 0.06%'), and make the fix match the cause ('...led to pinning cores and [the governor change, if one was made]').

### PRIORITY · 3 evaluators · max sev 5
> Cut AI workflow generation time 65% to under 15s by splitting a Claude skill into focused sub-skills that call Python search and validation tools instead of relying on open-ended model search
- **recruiter_v2** (sev 5): 'AI workflow generation' and 'Claude skill' aren't defined: I don't know what a workflow is here or who generated them.. *Direction:* Add a short noun phrase saying what the generated workflows are; shorten 'instead of relying on open-ended model search' to make room.
- **skeptic_v2** (sev 5): 'AI workflow' is never defined, so a non-engineer (and many HFT engineers) can't say what was being generated or for whom. 'Claude skill' and 'sub-skills' are vendor jargon. 'Python search and validation tools' is a near noun stack where 'Python' is doing keyword work rather than explaining the engineering.. *Direction:* Name the thing being generated in a few plain words before the mechanism, and drop 'Python' unless the language matters to the speedup.
- **systems_quant_v2** (sev 4): 'under 15s' does not say whether it is a typical, average, or worst-case generation time, or over how many requests; for this persona every latency should name its statistic. The bold on '65%' pulls the eye to a non-domain metric.. *Direction:* Add the statistic in one word ('median generation time ...') and drop the bold here so bold stays on the C++ project.

### PRIORITY · 3 evaluators · max sev 5
> Built Redis caching in front of Tortuga's Prisma ORM queries to reduce database load and latency for a class scheduler that drew 20,000+ visits in its first 30 days
- **recruiter_v2** (sev 5): 'Tortuga' is never introduced. Is it the product, the company, or a library? 'to reduce database load and latency' states intent with no result, so the only number (20,000+ visits) describes traffic, not this work.. *Direction:* Name the product once in plain terms ('Tortuga, our class scheduler'), and cut 'Prisma ORM' from the bullet since it doesn't explain the engineering.
- **skeptic_v2** (sev 5): 'Tortuga' is never explained. The only number (20,000+ visits) measures the product's traffic, not the caching work, so 'to reduce database load and latency' is an unquantified intent claim sitting next to a number that looks like a result. 'Prisma ORM' reads as a keyword.. *Direction:* Name the scheduler plainly in the first clause and attach the visit count to the product, not the cache (e.g. 'for Tortuga, our class scheduler, which drew ...'). If no cache result exists, keep the intent wording but don't let the traffic number imply one.
- **systems_quant_v2** (sev 3): 'Tortuga' is undefined (product name? company?), and 'to reduce database load and latency' states an intent with no result.. *Direction:* Introduce Tortuga in two words where it first appears (e.g. 'our class scheduler, Tortuga') and either state an observed effect or rephrase the ending so it doesn't promise a result it doesn't give.

### PRIORITY · 3 evaluators · max sev 4
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **recruiter_v2** (sev 4): The heading 'UMD App Development Contracting (Client: Amazon Leo)' doesn't explain what Amazon Leo is, and 'routing ... to inference' and 'S3 staging hops' are jargon. The bullet is clear to an engineer, but I could misread who the employer was.. *Direction:* Keep the heading structure and swap 'to inference' for 'to an ML model'. The tech names can stay because they are the change.
- **skeptic_v2** (sev 4): 'routing ... to inference' drops the noun a reader needs (to a model? to which inference step?). No baseline for the 34% (seconds per document? minutes per batch?). 'Amazon Leo' in the heading is unexplained for readers who don't know the brand.. *Direction:* Replace 'to inference' with 'to a model for inference' or similar, and add the baseline only if it's known.
- **systems_quant_v2** (sev 4): 'end-to-end latency 34%' does not say per-document or whole-batch, nor mean vs a percentile, and gives no baseline magnitude.. *Direction:* Name what is timed ('per-document end-to-end latency') and the statistic; consider removing the bold on 34% for the same reason as above.

### PRIORITY · 2 evaluators · max sev 7
> Precomputed popular workflows from a 270K+ row PostgreSQL table into a Redis-cached category tree to keep lookups within the database's permission and rate limits, which became the Claude skill's main search tool
- **recruiter_v2** (sev 7): Three unexplained ideas are packed into one sentence: 'category tree', 'permission and rate limits', and 'the Claude skill'. I can't tell what problem the limits caused (was the tool blocked, slow, or not allowed to query directly?) or who benefited.. *Direction:* Lead with the constraint in plain words, then the fix, then that it became the main search tool; drop either 'PostgreSQL' or 'Redis-cached' from the sentence if the Skills line already carries it.
- **skeptic_v2** (sev 6): 'Redis-cached category tree' is a noun stack, and 'Precomputed popular workflows ... into a ... category tree' doesn't say what was precomputed (rankings? groupings? the workflows themselves?). The mechanism for 'within the database's permission ... limits' is unclear: caching explains rate limits, but not how it resolves a permissions constraint. 'which became the Claude skill's main search tool' is an adoption claim with unclear ownership (did the candidate wire it in, or did the team choose it?).. *Direction:* Lead with the constraint in plain words (the skill couldn't query the table directly / often enough), then say what was cached and how it was organized. Replace 'Redis-cached category tree' with a verb phrase such as 'grouped them by category and cached them in Redis'.

### PRIORITY · 2 evaluators · max sev 6
> Implemented B+ tree and LSM-tree backends for the engine’s event log to compare them on identical 2M-record workloads, which showed the B+ tree giving 12.8x the read throughput and 22x faster range queries for 27% more disk
- **skeptic_v2** (sev 6): Mechanism is unclear: an event log is normally append-only, so the reader doesn't know why a matching engine's log needs indexed reads or range queries at all, or what was being looked up. LSM trees are write-optimized, yet only read results are reported, which looks like the comparison was framed to favor the B+ tree. 'for 27% more disk' is a telegraphic fragment (dropped 'at the cost of'). Three metrics stacked in one clause.. *Direction:* State the read pattern that motivated the comparison before naming the trees, and spell out the tradeoff in words ('at the cost of 27% more disk'). Consider dropping one of the three numbers.
- **systems_quant_v2** (sev 6): Only the read-side results are reported; write/ingest throughput, which is the LSM tree's main reason to exist and the dominant operation for an append-heavy event log, is absent, and the workload mix ('identical 2M-record workloads') is not described.. *Direction:* State the workload shape in a few words before the result (e.g. 'on identical read-heavy 2M-record workloads') or, if write numbers exist, give the trade-off in both directions instead of '27% more disk' alone.

### 1 evaluators · max sev 4
> Writing backtested Java capacity-planning logic that sets upper and lower bounds on the EC2 capacity Amazon Redshift reserves for patching to balance availability against cost
- **skeptic_v2** (sev 4): 'backtested Java capacity-planning logic' is a three-adjective noun stack; 'Java' is keyword filler. Ownership is ambiguous: 'sets upper and lower bounds' reads as if the logic is live, while 'Writing' says it isn't finished.. *Direction:* Turn the stack into verbs ('Writing and backtesting logic that sets ...') and drop 'Java'; keep the present tense so the in-progress status is honest.

### 1 evaluators · max sev 3
> Built a C++17 order book and matching engine to replay 50.9M real IEX exchange messages without ever resyncing, which agreed with the exchange on 99,122 of 99,123 fills and 100% of top-of-book prices
- **systems_quant_v2** (sev 3): The single mismatched fill is reported but not explained, and '100% of top-of-book prices' does not say how often top of book was compared (every message? every BBO update?).. *Direction:* Keep as is unless space allows a short '(checked at every BBO update)'-style qualifier; be ready to explain the one miss.

## Page-level
- **skeptic_v2** (sev 6): Only the IEX project speaks to low-latency C++; every Experience bullet is cloud, LLM tooling, or robotics, and none mentions C++ or latency at the microsecond scale.. *Direction:* Keep Projects above Experience (correct for this target). Within Experience, order or trim so the performance/latency-flavored bullets (Kinesis latency, caching) read before the LLM/robotics ones, and shorten the UMIACS bullet.
- **recruiter_v2** (sev 5): All the low-latency C++ evidence sits in one summer project. Every Experience entry is cloud, AI tooling or ML, so after the top block the page reads as 'cloud/AI engineer' rather than 'systems engineer'.. *Direction:* Within existing facts, lead each Experience bullet with its performance or systems angle (latency, caching, capacity bounds), as the Leo and TerpLabs bullets already partly do.
- **systems_quant_v2** (sev 5): All low-latency/C++ evidence lives in one two-month side project; every Experience entry is cloud, Java, or LLM work, and there is no evidence of concurrency, threading, memory layout/allocation, or networking anywhere on the page.. *Direction:* Keep the project first (correct choice). If any experience bullet involved real performance trade-offs, lead with the performance mechanism rather than the AI/cloud framing; otherwise accept the gap and be ready to discuss threading/cache behavior of the engine in interviews.
- **recruiter_v2** (sev 3): About the bottom 15% of the page is blank, while the body text is fairly small and the bullets wrap to two dense lines.. *Direction:* Use the free space for slightly larger body text or more spacing between entries instead of adding content.
- **recruiter_v2** (sev 3): Several bullets chain clauses with 'which ...' ('which agreed with', 'which ran', 'which showed', 'which led to', 'which became'). It happens five times across the page.. *Direction:* Split a couple of the 'which' clauses into a second short clause or vary the connector. Don't change any facts.
- **skeptic_v2** (sev 3): Skills lists Rust, TypeScript and Fargate with no supporting bullet, and 'data structures and algorithms' and 'benchmarking' are generic filler. 'debugging and profiling with Linux perf (hardware counters, top-down analysis)' is a parenthetical tech dump.. *Direction:* Cut entries that no bullet or real project supports and drop 'data structures and algorithms'.
- **systems_quant_v2** (sev 3): Project dates (Jul 2026 – Aug 2026) overlap completely with the Capital One internship (Jun 2026 – Aug 2026).. *Direction:* No change required; be ready to explain the timeline. If the work started earlier, the dates could reflect that.
- **recruiter_v2** (sev 2): The AWS internship (the biggest brand, and current) has a single present-tense bullet with no outcome, so it reads lighter than the Capital One entry below it.. *Direction:* Leave as is; just keep the bullet in plain words. It already is.
- **skeptic_v2** (sev 2): Roughly the bottom 15% of the page is empty while several bullets are squeezed to the full two lines.. *Direction:* Rebalance spacing (slightly more space between sections) rather than adding content.
- **systems_quant_v2** (sev 2): Bold is applied to 65% (Capital One) and 34% (Amazon Leo) as well as to the order-book numbers, giving five bold anchors of equal weight.. *Direction:* Limit bold to the project's numbers (e.g. 50.9M, 1.26M events/sec, the p99) so the 7-second read lands on the systems story.
- **systems_quant_v2** (sev 2): Roughly the bottom sixth of the page is empty while several project bullets need a few more words to define their measurements.. *Direction:* Spend the slack on the project bullets' measurement qualifiers rather than on new content.
- **systems_quant_v2** (sev 2): Skills lists C and Rust, and generic entries 'data structures and algorithms, benchmarking', none of which are backed by a bullet.. *Direction:* Keep only languages you are comfortable being quizzed on; consider dropping the generic 'data structures and algorithms' phrase.
