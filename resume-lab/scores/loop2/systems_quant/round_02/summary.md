# Loop 2 · systems_quant · round 02 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.0 | 7 |
| quantification | 7.33 | 7 |
| technical_depth | 7.33 | 7 |
| concision_readability | 6.67 | 6 |
| skim_test | 7.33 | 7 |
| credibility | 7.0 | 6 |
| ats_parseability | 8.0 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 7.0 | 6 |
| human_voice | 7.0 | 6 |
| plain_language | 6.0 | 5 |
| overall | 7.33 | 7 |

**Plain-English restatement (recruiter):** 10/11 bullets understood
**Competitive:** {'recruiter_v2': 'Y', 'skeptic_v2': 'stretch', 'systems_quant_v2': 'stretch'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "IEX Order Book & Matching Engine in C++ - replayed tens of millions of real exchange messages and matched the exchange almost exactly",
  "Amazon Web Services SDE intern (current, Redmond) - capacity planning for Redshift",
  "Capital One SWE intern - made an AI (Claude) workflow tool about 65% faster"
 ],
 "engineer_type": "C++ / systems-performance student who has also done a lot of AWS cloud and backend work; reads as a systems person aiming at trading firms",
 "memorable_numbers": [
  "50.9M messages",
  "1.26M events/sec",
  "12.8x",
  "65%",
  "34%",
  "74%"
 ],
 "confusing": [
  "What 'Amazon Leo' is - client name I don't recognize, couldn't tell if it is an Amazon team or a product",
  "'CPU frequency governor' and 'do-nothing control book' - didn't know what was being fixed",
  "Capital One second bullet - category tree, Redis, permissions, rate limits all in one line; lost the point",
  "B+ tree vs LSM-tree - understood it was a comparison, not why it matters"
 ],
 "skipped": [
  "Technical Skills section",
  "UMIACS robotics bullet (too long, AnyGrasp/Open3D)",
  "TerpLabs bullet",
  "Most of the second line of every bullet"
 ],
 "interview_questions": [
  "Walk me through the order book project - why build it, and what was the one fill that didn't match?",
  "What are you building at AWS right now, and what is your piece of it?",
  "What is Amazon Leo and what was your role on that contract?",
  "How did you make the Capital One AI tool faster, and who used it?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Precomputed popular workflows from a 270K+ row PostgreSQL table into a category tree that the Claude skill searches first, with Redis caching full workflows, so lookups rarely touch a database gated by permissions and rate limits
- **recruiter_v2** (sev 7): Three mechanisms ('category tree', 'Redis caching full workflows', 'database gated by permissions and rate limits') are stitched into one sentence, and the reason it matters only arrives in the last six words. I could not restate it without guessing whether the goal was speed, avoiding rate-limit errors, or avoiding permission failures.. *Direction:* Lead with the problem (the workflow database was permission-gated and rate-limited), then say what you did (precomputed popular workflows into a category tree the skill checks first, with Redis caching), and drop one of the two mechanisms into a shorter clause. Example shape: 'Because the workflow database was permission-gated and rate-limited, precomputed popular workflows from its 270K+ rows into a category tree the skill searches first, cached in Redis'
- **skeptic_v2** (sev 4): The sentence piles three clauses onto 'Precomputed...': 'that the Claude skill searches first', 'with Redis caching...' and 'so lookups rarely touch...'. The real reason for the work, a database gated by permissions and rate limits, comes last. 'Rarely' is an unquantified claim sitting next to precise numbers.. *Direction:* Lead with the constraint ('Because the source database was permission-gated and rate-limited, ...'), then describe the two layers in order. The 270K figure can stay as scope.
- **systems_quant_v2** (sev 3): This is a dense two-line bullet with three mechanisms (precomputed category tree, Redis cache, gated database). 'rarely' is the only outcome, and it is unquantified.. *Direction:* Lead with the constraint (the database is permission-gated and rate-limited), then the two-tier lookup. If there's no hit rate, end on the design choice instead of 'rarely'.

### PRIORITY · 3 evaluators · max sev 7
> Built an OpenCV (C++) vision pipeline that detects ocean mines in real time on drone-mounted microcontrollers, reaching 74% detection accuracy on test footage
- **recruiter_v2** (sev 3): 74% is bolded, so it's one of the numbers I remembered, but with no baseline I can't tell if it is good; bolding it invites the question.. *Direction:* Unbold 74% and let 'real time on drone-mounted microcontrollers' carry the bullet, or add the comparison if one exists.
- **skeptic_v2** (sev 7): Running an OpenCV C++ pipeline 'in real time on ... microcontrollers' is technically suspicious. OpenCV normally needs an application processor or SBC (Linux, MMU), not a microcontroller, and an embedded-aware interviewer will catch it. 'Real time' has no frame rate, '74% detection accuracy' doesn't say whether it is precision, recall or per-frame accuracy, and the '(C++)' parenthetical is a tech tag. 'Built' on a lab team project leaves ownership unclear.. *Direction:* Replace 'microcontrollers' with the exact hardware class if it was an SBC, state the frame rate behind 'real time', and name the metric precisely. Write 'in C++ with OpenCV' instead of the parenthetical.
- **systems_quant_v2** (sev 6): Full OpenCV normally needs an OS and an application-class CPU, so 'microcontrollers' reads like a misnomer for a single-board computer. 'real time' has no frame rate or latency, and '74% detection accuracy' doesn't say whether it is precision, recall, or per-frame accuracy.. *Direction:* Name the hardware class accurately (e.g. 'single-board computer' if that is what it was). If no frame-rate number exists, drop 'in real time'. Name the accuracy metric.

### PRIORITY · 3 evaluators · max sev 6
> Sustained 1.26M events/sec over the full replay and a 1.2 µs per-message p99 on a separate 2M-event run, keeping each price level as a FIFO queue (std::list) inside a std::map, with an order-ID hash map for O(1) cancels
- **recruiter_v2** (sev 4): The first half is a clear speed claim; the second half ('FIFO queue (std::list) inside a std::map', 'O(1) cancels') is code-level detail with parentheticals that I can't read aloud or explain. 'p99' is also unexplained to a non-engineer.. *Direction:* Keep the design choice but phrase it in words before the type names (e.g. 'storing each price level as a first-in-first-out queue, with a lookup table by order ID so cancels are instant'); move std::list/std::map to the interview or drop the parentheticals.
- **skeptic_v2** (sev 5): Two metrics from two different runs are stitched together with 'and', and the reader isn't told why the p99 came from a separate 2M-event run instead of the full replay. The participle 'keeping each price level...' presents std::list inside std::map as the reason it is fast. Most HFT readers see node-based containers as the cache-unfriendly baseline design, not a latency win. The parenthetical '(std::list)' plus 'std::map' plus 'hash map' reads as a type dump.. *Direction:* Split the result from the design. One clause states throughput and tail latency and what was timed. The design goes in a separate plain sentence that names the choice as a baseline or deliberate simplicity ('price levels are linked-list FIFOs in a sorted map; cancels look up the order by ID in a hash map'), so the reader doesn't think it's being sold as the optimization.
- **systems_quant_v2** (sev 6): The two headline performance numbers don't say what they measure or under what conditions. '1.26M events/sec' doesn't say whether feed parsing or file I/O is included, or whether it is single-threaded. '1.2 µs per-message p99' doesn't say what interval is timed or why it comes from 'a separate 2M-event run' and not the full 50.9M replay. Neither says whether it was measured before or after the core pinning and clock fixing in the fourth bullet. The unit also changes across the project, from 'messages' (bullet 1) to 'events' (bullet 2) to 'records' (bullet 3), so the reader can't tell whether 1.26M events/sec equals 1.26M IEX messages/sec.. *Direction:* Use one unit ('messages') throughout the project. Attach a short scope phrase to each number saying what was timed and on which run. If the line gets too long, move the data-structure clause into its own short sentence or into the first bullet, so this bullet is purely about measurement.

### PRIORITY · 3 evaluators · max sev 5
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **recruiter_v2** (sev 5): The bullet is clear, but the header 'UMD App Development Contracting (Client: Amazon Leo)' is not: I don't know what Amazon Leo is or why a research-document pipeline belongs to it. 'staging hops' is also jargon.. *Direction:* Say 'replacing intermediate S3 storage steps' instead of 'S3 staging hops'; if space allows, gloss the client name in the header.
- **skeptic_v2** (sev 4): The 34% has no baseline or unit: per document, per batch, seconds or minutes? '6,000+ documents' is a total corpus size, not a rate, so it says nothing about load. 'Routing ... to inference' doesn't say what the inference is. 'UMD App Development Contracting (Client: Amazon Leo)' doesn't make clear whether this is a student org, a company, or solo work.. *Direction:* Name what the pipeline does in plain words first, then the change ('stopped writing each document to S3 between stages and streamed it through Kinesis instead'), then the result with its unit.
- **systems_quant_v2** (sev 5): 'end-to-end latency 34%' doesn't say whether it is mean, median, or tail latency, or what the absolute before/after values were (seconds? minutes per document?). '6,000+ scraped research documents' doesn't say whether that is a total, per day, or per batch.. *Direction:* Add the statistic name (median/p95/mean) and either the before or after absolute value next to 34%, using numbers that already exist. Add the time window to the document count.

### PRIORITY · 3 evaluators · max sev 5
> Built Redis caching in front of the Prisma ORM queries for Tortuga, the studio's class scheduler with 20,000+ visits in its first 30 days, to reduce database load and latency
- **recruiter_v2** (sev 3): The 20,000+ number describes the product's traffic, not the effect of the caching; 'to reduce database load and latency' states intent, not a result. The bullet ends on a goal.. *Direction:* Either state an observed outcome if one exists, or reorder so the product context comes first and the cache is clearly the contribution ('For Tortuga, the studio's class scheduler (20,000+ visits in its first 30 days), added Redis caching in front of database queries').
- **skeptic_v2** (sev 5): The bullet ends at intent ('to reduce database load and latency'), so no effect of the cache is stated. The only number, 20,000+ visits in 30 days, measures the product, not the cache. That traffic averages under one request every two minutes, so a skeptic will ask why a cache was needed. 'The studio' and TerpLabs are never explained.. *Direction:* Name the specific expensive query the cache sits in front of (for example, schedule lookups during registration peaks, if that's true) and keep the visits number as scope, not as the result. If there's no measured effect, give one plain reason the cache was needed.
- **systems_quant_v2** (sev 4): The bullet ends at intent ('to reduce database load and latency'), with no outcome. The only scale number, 20,000+ visits in 30 days, averages under one request per minute, which undercuts the reason for adding a cache.. *Direction:* If the cache addressed a specific burst or slow query, name that instead of the monthly visit total. If not, shorten this bullet or deprioritize it for HFT-targeted versions so its space goes to the C++ evidence.

### PRIORITY · 3 evaluators · max sev 5
> Cut AI workflow generation time 65% to under 15s by replacing a Claude skill's open-ended search with focused sub-skills that call Python tools for workflow search and validation, guided by CloudWatch and OpenSearch latency logs
- **recruiter_v2** (sev 3): 'Claude skill' and 'sub-skills' are insider terms, and 'workflow' is never defined - I don't know what workflows are generated or for whom. The closing 'guided by CloudWatch and OpenSearch latency logs' is a tool list tacked on.. *Direction:* Add a few words on who the workflows are for; consider cutting 'CloudWatch and OpenSearch' to 'latency logs' since the tools are already in Skills.
- **skeptic_v2** (sev 5): 'AI workflow generation' is never defined, so a non-engineer can't say what got faster or who used it. 'Claude skill', 'sub-skills' and 'Python tools' are three layers of agent jargon. The trailing 'guided by CloudWatch and OpenSearch latency logs' reads as keyword attachment, not as part of the mechanism.. *Direction:* Start with what the user gets ('generating a <kind of> workflow from a request') and then state the fix as one idea: one broad search was replaced with narrow steps. Either drop the logging tools or turn them into a short clause about how the slow step was found ('after latency logs showed most time went to search').
- **systems_quant_v2** (sev 3): The ending 'guided by CloudWatch and OpenSearch latency logs' names tools without saying what the logs revealed. 'Claude skill' and 'sub-skills' are product-specific terms a trading-firm screener won't know.. *Direction:* Cut the 'guided by ...' clause or replace it with what the logs showed (e.g. which step dominated latency), if known. Keep CloudWatch/OpenSearch in Skills.

### PRIORITY · 3 evaluators · max sev 4
> For a PhD-led robotics project aimed at ICLR, built a pipeline that overlays AnyGrasp's candidate grasps on camera images in Open3D for a vision-language model, then tuned prompts so it favors grasps that avoid hitting the table
- **recruiter_v2** (sev 4): 'AnyGrasp's candidate grasps', 'Open3D' and 'vision-language model' stack three unfamiliar names in the middle of the sentence; the purpose (helping a robot pick grips that don't hit the table) only arrives at the very end.. *Direction:* Lead with the goal (helping a vision-language model choose robot grasps that avoid the table), then the method; consider dropping 'Open3D' to Skills since it doesn't explain the engineering.
- **skeptic_v2** (sev 4): The bullet has no result: we don't learn whether the prompt tuning changed grasp success or collision rate. 'Tuned prompts' is the weakest kind of engineering signal for this target. The bullet uses two lines on work that a systems/HFT reader won't weigh.. *Direction:* Shorten it to one line for this target: the overlay pipeline is the engineering, and the prompt tuning can be a short clause. If there's no outcome, say the work is ongoing so the bullet doesn't read as unfinished.
- **systems_quant_v2** (sev 2): There is no outcome, and the work (visualization overlay plus prompt tuning) has no connection to systems or performance.. *Direction:* In an HFT-targeted version, shorten this to one line if space is needed for the project's measurement details.

### PRIORITY · 2 evaluators · max sev 6
> Implemented B+ tree and LSM-tree backends for the event log and benchmarked them on identical 2M-record workloads, where the B+ tree gave 12.8x the read throughput and 22x faster range queries at the cost of 27% more disk space
- **skeptic_v2** (sev 6): The comparison reports only reads, range queries and disk space. Write throughput, the one thing an LSM tree is built to win and the main workload for an append-heavy event log, is missing. That looks like a cherry-picked comparison. It is also unclear why an event log needs point reads or range queries at all, and '12.8x the read throughput' and '22x faster range queries' use two different comparison forms in one sentence.. *Direction:* Open with why the log needs reads, then state the tradeoff both ways using the same comparison form. If writes weren't measured, scope the claim down to 'for read-heavy replay queries' so it doesn't read as a general verdict.
- **systems_quant_v2** (sev 6): The comparison reports only the axes where the B+ tree wins (reads, range queries) plus disk space. It leaves out write/ingest performance, which is the reason anyone builds an LSM tree. It also doesn't say why an order book needs an 'event log' backend, or whether '22x faster range queries' means throughput or latency.. *Direction:* Name what the event log is for in a few words before the tech. Then give the tradeoff in both directions using numbers that already exist. If write results weren't measured, say the workload was read-heavy so the omission reads as deliberate.

### PRIORITY · 2 evaluators · max sev 5
> Building capacity planning for Amazon Redshift maintenance like patching: Java logic that sets upper and lower bounds on reserved EC2 capacity to balance availability against cost, validated by backtesting
- **skeptic_v2** (sev 5): Colon-stitched clause with a telegraphic second half ('Java logic that sets...'). 'Building capacity planning' uses a process as the object of 'building', and 'maintenance like patching' is phrasing nobody would say out loud. 'Java logic' is vague about what the candidate actually wrote: a model, a heuristic, a service?. *Direction:* Rewrite as one plain sentence with a subject and verb: 'Writing the Java service that decides how much reserved EC2 capacity Redshift keeps for maintenance such as patching, ...'. Name what the bounds are derived from before naming the language.
- **systems_quant_v2** (sev 3): 'Building capacity planning for ... maintenance like patching' is an awkward noun phrase, and the colon splits the bullet into a heading and a fragment.. *Direction:* Rephrase as one sentence with a verb: what is being built (Java logic that sets upper/lower bounds on reserved EC2 capacity), what it serves (Redshift maintenance such as patching), and how it is checked (backtesting).

### PRIORITY · 2 evaluators · max sev 4
> Traced an apparent 1.65x regression to the CPU frequency governor, not a code change, using perf counters and a do-nothing control book, then cut run-to-run variance from about 6% to 0.06% by pinning cores and fixing the clock
- **recruiter_v2** (sev 4): 'CPU frequency governor', 'do-nothing control book' and 'pinning cores and fixing the clock' are three jargon phrases in one bullet. I got the gist (the slowdown wasn't his code) only on a second read.. *Direction:* Put the plain conclusion first ('Showed an apparent 1.65x slowdown came from the CPU's power-saving clock, not the code') and then the method; consider cutting 'do-nothing control book' or saying 'a control version that did no work'.
- **systems_quant_v2** (sev 4): 'run-to-run variance' doesn't say which metric varied: throughput, p99, or total replay time. A 100x reduction to 0.06% is believable for throughput on a deterministic replay but surprising for a tail-latency percentile, so the missing metric matters.. *Direction:* Insert the metric name directly before 'variance' (e.g. 'run-to-run throughput variance'). Change nothing else; the diagnosis story and control-book detail are excellent.

### 1 evaluators · max sev 6
> Built a C++17 order book and matching engine and replayed 50.9M real IEX exchange messages through it without ever resyncing to the exchange’s book, agreeing with the exchange on 99,122 of 99,123 fills and 100% of top-of-book prices
- **skeptic_v2** (sev 6): The mechanism behind 'agreeing with the exchange on ... fills' is unclear. A market-data replay feeds the book resting adds, cancels and the exchange's own execution messages. If the engine just applies those executions, it isn't matching anything and agreement on fills is trivially true. If it generates fills itself, the bullet has to say what incoming orders it matched against.. *Direction:* Say in plain words what the engine computed on its own and what it was compared against. Keep the exact counts. If the engine only reconstructs the book, call it 'order book reconstruction' and drop 'matching engine' from the claim.

## Page-level
- **skeptic_v2** (sev 6): All the evidence for low-latency/systems work comes from one two-month personal project. Every Experience entry is cloud, AI-agent, or web/CV work, and the page never mentions concurrency, memory layout/cache behaviour, networking, or a threading model.. *Direction:* Keep Projects first, as it is now. For this target, compress the UMIACS and TerpLabs bullets to one line each and move the saved space to the strongest performance angle in the existing roles, such as the latency-cutting work, phrased around the measurement and bottleneck found. Don't add new facts.
- **systems_quant_v2** (sev 6): All of the low-latency/C++ evidence sits in one two-month side project. Every Experience entry except Northrop is cloud, AI-tooling, or web, and the Skills line 'data structures and algorithms, benchmarking' is generic filler next to the specific perf items.. *Direction:* Keep the project at the top. In the HFT version, keep each cloud/AI experience to one tight line so the performance numbers there (34% latency, 65% time) stay but take less space. Cut 'data structures and algorithms, benchmarking' from Skills; the project already demonstrates both.
- **recruiter_v2** (sev 5): Every bullet runs the full width of the page for two full lines, and almost every one packs a 'by/using/with' clause onto the end. The page reads as one uniform dense block; on a skim I only took in the first half of each first line.. *Direction:* Put the plain-English point of each bullet in the first ~10 words and let the technical method trail; trim trailing tool lists where Skills already carries them.
- **skeptic_v2** (sev 5): The project is dated Jul–Aug 2026, which overlaps the full-time Capital One internship (Jun–Aug 2026). Over those same weeks it claims a matching engine, a 50.9M-message replay, two storage engines and a perf investigation.. *Direction:* If there is a public repo, link it on the project title line so the claims can be checked. Make sure each bullet's scope (prototype backends, single-threaded engine, etc.) is stated honestly so the volume reads as plausible.
- **skeptic_v2** (sev 4): Most bullets fill two full lines (about 200–230 characters) and chain several clauses with 'by', 'with', 'so' and participles. On Capital One #2, AWS and IEX #2 the reader has to re-read to separate mechanism from result.. *Direction:* Limit each bullet to one main clause plus one supporting clause. Where two results share a bullet (throughput + p99; reads + range + disk), keep the one that carries the point or give each its own short clause.
- **systems_quant_v2** (sev 4): Measurement vocabulary is inconsistent across the page: 'messages', 'events', 'records', 'end-to-end latency', 'generation time', 'latency' (TerpLabs). Only the project states a percentile (p99).. *Direction:* Use one unit per system, and name the statistic (mean/median/p99) wherever a latency is quoted.
- **recruiter_v2** (sev 3): Six experience entries each have a single bullet, so Experience reads like a list of affiliations; the brands (AWS, Capital One) get the same visual weight as the student club and lab.. *Direction:* Keep the ordering (it is correct), but consider whether the weakest single-bullet role adds enough to keep for this target, or whether that space would let a stronger bullet breathe.
- **recruiter_v2** (sev 3): Bold numbers are spread evenly (50.9M, 1.26M, 12.8x, 65%, 34%, 74%), so the headline result - 99,122 of 99,123 fills matching the exchange - isn't bolded and is easy to miss.. *Direction:* Choose the bold anchor on the first project bullet deliberately; consider unbolding the weaker numbers lower on the page.
- **skeptic_v2** (sev 3): Skills look keyword-driven: Rust and C appear with no supporting bullet, 'data structures and algorithms' is filler for this reader, 'B+ trees, LSM trees' repeat the project, and '(hardware counters, top-down analysis)' and '(Lambda, Kinesis, EC2, Fargate, CloudWatch monitoring)' are parenthetical dumps. The project title line '| C++17, STL, POSIX, Linux perf' lists POSIX, but no bullet shows a POSIX call being used.. *Direction:* Cut 'data structures and algorithms' and anything you wouldn't want to be quizzed on. Drop the duplicate B+/LSM entries. If POSIX was used for core pinning, the variance bullet can say 'pinning the process to a core', with no need for the tag.
- **skeptic_v2** (sev 3): Several things a non-engineer can't restate: 'Claude skill / sub-skills', 'do-nothing control book', 'S3 staging hops', 'AnyGrasp's candidate grasps', 'Amazon Leo'.. *Direction:* Add a few plain words of gloss next to each distinctive noun ('a control order book that does no work, used to measure noise'), but keep the technical noun itself.
- **systems_quant_v2** (sev 2): Bold is applied to the largest numbers (50.9M, 1.26M, 12.8x) but not to the most distinctive HFT signals (1.2 µs p99, 99,122 of 99,123 fills, 6% to 0.06%).. *Direction:* Consider moving the bold in bullets 1-2 to the correctness figure and the p99, keeping one bold per bullet.
