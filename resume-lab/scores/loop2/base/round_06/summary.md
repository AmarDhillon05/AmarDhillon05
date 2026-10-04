# Loop 2 · base · round 06 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.33 | 7 |
| quantification | 7.67 | 7 |
| technical_depth | 7.67 | 7 |
| concision_readability | 6.67 | 6 |
| skim_test | 7.67 | 7 |
| credibility | 7.67 | 7 |
| ats_parseability | 8.67 | 8 |
| visual_layout | 7.67 | 7 |
| domain_fit | 7.67 | 7 |
| human_voice | 6.67 | 6 |
| plain_language | 6.67 | 6 |
| overall | 7.67 | 7 |

**Plain-English restatement (recruiter):** 12/14 bullets understood
**Competitive:** {'general_backend_v2': 'Y', 'recruiter_v2': 'Y', 'skeptic_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "Amazon Web Services SDE Intern (current, fall 2026)",
  "Capital One Software Engineering Intern (summer 2026), something about speeding up an AI/Claude tool 65%",
  "IEX Order Book & Matching Engine project in C++ with big bold numbers (50.9M messages, 1.26M events/sec)"
 ],
 "engineer_type": "Backend / cloud engineer who also does AI tooling and has a C++ performance side project; reads as a strong, busy student with two big-name internships",
 "memorable_numbers": [
  "90% of developers preferred",
  "65% faster",
  "50.9M messages",
  "12.8x",
  "1.26M events/sec",
  "93%",
  "110+ member studio"
 ],
 "confusing": [
  "'UMD App Development Contracting (Client: Amazon Leo)' - not sure if this is a company, a class, or a student club, or what Amazon Leo is",
  "Several roles say 'Present' at the same time as the AWS internship, so I wasn't sure what he is doing right now",
  "The AWS bullet - something about Redshift capacity and patching; I got 'capacity planning' but not what he built"
 ],
 "skipped": [
  "Most of the Technical Skills section",
  "The UMIACS research bullet after the first few words",
  "Second and third bullets under TerpLabs",
  "The B+ tree / LSM-tree bullet"
 ],
 "interview_questions": [
  "What is your day-to-day at AWS and what does the capacity tool decide?",
  "What is the Amazon Leo contract and how is it staffed - is it paid client work through UMD?",
  "Walk me through the order book project - why build it and how you checked it against the exchange"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Built an EventBridge-scheduled LLM-as-judge check for a production Amazon Bedrock classifier that rates research documents by importance to trigger fine-tuning only when its grades shift past a threshold
- **general_backend_v2** (sev 4): Two graders appear (the judge and the classifier) and 'its grades shift' is ambiguous: it could mean the classifier's grades drift, or the judge's grades disagree with the classifier. 'rates research documents by importance' also floats between the two subjects.. *Direction:* Split subject and mechanism: name the classifier's job first, then 'a scheduled LLM-as-judge check that re-grades its output and triggers fine-tuning only when <X> drops past a threshold'.
- **recruiter_v2** (sev 7): Three stacked jargon terms up front ('EventBridge-scheduled LLM-as-judge check', 'Amazon Bedrock classifier') before the reader learns what the check is for; the payoff ('trigger fine-tuning only when its grades shift') is at the very end and assumes the reader knows why retraining on a schedule is costly.. *Direction:* Lead with the purpose in plain words (an automatic quality check on an AI document classifier that decides when retraining is needed), then name the mechanism; drop 'EventBridge-scheduled' to Skills or a short 'weekly/scheduled' phrase if accurate.
- **skeptic_v2** (sev 7): Two noun stacks in a row: 'EventBridge-scheduled LLM-as-judge check' and 'production Amazon Bedrock classifier'. 'its grades' could mean the judge's grades or the classifier's grades, so it's unclear what drifts and what is compared against what. The 'to trigger' purpose clause is attached to the classifier, not to the check.. *Direction:* Say what the check does in plain verbs before naming the schedulers. Put the scheduler in a trailing 'on a daily/weekly EventBridge schedule' or drop it. Example shape: 'Built a scheduled check where an LLM re-grades a sample of the Bedrock classifier's importance ratings, triggering fine-tuning only when the two disagree past a threshold'

### PRIORITY · 3 evaluators · max sev 7
> Co-built a research tool that scores and aggregates topics to show Amazon Leo’s public-policy staff what’s popular, which runs in dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK infrastructure-as-code ready for production
- **general_backend_v2** (sev 4): Two ideas stitched by 'which': the product (topic scoring for policy staff) and the deployment status. 'runs in dev ... ready for production' is honest but reads as a contradiction on first pass, and the second half is a tech list (Fargate, GitHub Actions, CDK) with no decision attached. 'Co-built' doesn't say which part was the candidate's.. *Direction:* Keep the product sentence, then state ownership plainly, e.g. '... I set up the Fargate deployment with CDK and GitHub Actions; it runs in dev pending production launch'. Cut whichever tool doesn't explain a decision.
- **recruiter_v2** (sev 5): The second half ('runs in dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK infrastructure-as-code ready for production') is a tool list joined by 'with'; 'runs in dev ... ready for production' is ambiguous about whether it is live. Also 'Amazon Leo' is not explained anywhere on the page.. *Direction:* Split into what it does for the users and one clause on deployment status; move Fargate/CDK/GitHub Actions to Skills (already listed there) unless one of them was a deliberate choice you can explain.
- **skeptic_v2** (sev 7): Breaks the structure rule. The whole second half, 'which runs in dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK infrastructure-as-code ready for production', is a tech list tacked onto the end. 'which' grammatically attaches to 'what's popular', not to the tool. 'Runs in dev ... ready for production' reads as hedged deployment status presented as a result. 'Co-built' doesn't say which part was Amar's.. *Direction:* Make the owned piece the verb's object and end on its purpose. Keep at most one deployment fact and move CDK/GitHub Actions to Skills. Example shape: 'Built the <owned part> of a topic-scoring tool that shows Amazon Leo's public-policy staff which topics are trending, deployed on AWS Fargate through CDK'

### PRIORITY · 3 evaluators · max sev 6
> Precomputed popular workflows from a 270K+ row PostgreSQL table into a Redis-cached category tree to keep lookups within the database’s permission and rate limits, which became the Claude skill’s main search tool
- **general_backend_v2** (sev 5): 'to keep lookups within the database’s permission and rate limits' is the bullet's 'why', but it is phrased as a constraint nobody outside the team can picture. A backend reader can't tell whether the problem was read-only/limited DB access, a query quota, or slow queries, and 'category tree' is never defined (tree of what, keyed on what).. *Direction:* Lead with the constraint in plain words, then the design: state the limit first, then 'so I precomputed ... into a Redis-cached tree of workflows grouped by <X>'. Keep 'which became the Claude skill’s main search tool' as the outcome.
- **recruiter_v2** (sev 4): 'keep lookups within the database's permission and rate limits' is unclear - it sounds like a workaround for access restrictions rather than a performance or usability win; 'category tree' is undefined.. *Direction:* Say the problem first in plain words (the AI assistant couldn't query the large table directly), then the fix (a cached, browsable catalog of popular workflows).
- **skeptic_v2** (sev 6): The mechanism is unclear. Caching explains staying under rate limits, but not how it keeps lookups within 'permission' limits. 'Redis-cached category tree' is a noun stack. The trailing 'which became the Claude skill's main search tool' is an extra clause, and 'which' grammatically refers to the limits.. *Direction:* State the constraint, then the design, then the use. Drop 'permission' unless it can be explained in a few words. Example shape: 'Precomputed popular workflows from a 270K+ row PostgreSQL table into a category tree cached in Redis, giving the Claude skill a search tool that stayed under the database's rate limits'

### PRIORITY · 3 evaluators · max sev 6
> Rebuilt a legacy test-data workflow tool as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation to make editing smoother, which 90% of 30+ surveyed developers preferred
- **general_backend_v2** (sev 3): 'preferred' has no comparison object (over the legacy tool, presumably), and the middle is a four-item stack list (React, TypeScript, Electron, React Flow, Jest) before the reader learns why. 'to make editing smoother' is vague next to such a specific metric.. *Direction:* Say 'preferred over the old tool', trim the stack to what explains the change (visual editor + validated edits), and consider ordering this role's bullets with the PostgreSQL/Redis bullet first for backend targets.
- **recruiter_v2** (sev 3): Four tools stacked mid-sentence ('React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation'); 'make editing smoother' is vague next to them.. *Direction:* Keep 'desktop app with a visual drag-and-drop editor' and one or two tool names; leave the rest to Skills.
- **skeptic_v2** (sev 6): The middle is a tech dump ('React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation'), with React named twice. 'to make editing smoother' is vague. 'which ... preferred' has no stated comparison: preferred over the legacy tool? And 'which' attaches to 'editing smoother'.. *Direction:* Keep one stack phrase ('as an Electron/React app') and name the two features in plain words. Make the comparison explicit. Example shape: 'Rebuilt a legacy test-data workflow tool as an Electron/React app with a drag-and-drop editor and built-in validation, which 90% of 30+ surveyed developers preferred over the old tool'

### PRIORITY · 3 evaluators · max sev 6
> Built a pipeline that overlays AnyGrasp’s candidate grasps on camera images in Open3D to let a vision-language model pick robot grasps for a PhD-led ICLR project, and tuned its prompts to favor grasps that avoid hitting the table
- **general_backend_v2** (sev 3): 'for a PhD-led ICLR project' implies a venue result without saying whether the paper is submitted, under review, or accepted; the bullet also has no outcome.. *Direction:* Scope the venue reference honestly (e.g. 'ICLR submission') or drop the venue and keep 'PhD-led project'.
- **recruiter_v2** (sev 3): 'AnyGrasp's candidate grasps' and 'Open3D' are unfamiliar names placed before the plain purpose (helping an AI choose how a robot grabs objects); 'ICLR' means nothing to most recruiters.. *Direction:* Open with the goal (helping a vision-language model choose robot grasps), then the method; 'ICLR' can stay but reads better as 'a PhD-led project submitted to ICLR' if accurate.
- **skeptic_v2** (sev 6): Breaks the structure rule: ', and tuned its prompts ...' is a second action tacked on after the purpose clause. 'for a PhD-led ICLR project' implies a venue outcome without saying whether it's a submission or an acceptance. There's no result.. *Direction:* Keep one action and fold the prompt tuning into the purpose. Make the venue status explicit, e.g. 'for a PhD student's ICLR submission'. Example shape: 'Built a pipeline that overlays AnyGrasp's candidate grasps on camera images so a vision-language model can pick robot grasps that avoid hitting the table, for a PhD student's ICLR submission'

### PRIORITY · 2 evaluators · max sev 7
> Designed the book as std::list FIFOs per price level inside a std::map with an order-ID hash map to make cancels O(1), which sustained 1.26M events/sec end-to-end over the full replay
- **recruiter_v2** (sev 7): 'std::list FIFOs per price level inside a std::map with an order-ID hash map' is a code-level data-structure description; 'O(1)' is notation a recruiter won't read. Only '1.26M events/sec' survives a non-technical read.. *Direction:* State the design goal in words first (orders kept in time order at each price, plus a lookup by order ID so cancels are instant), and keep the STL names short or move them to the project's tech list.
- **skeptic_v2** (sev 3): 'which sustained 1.26M events/sec' credits the overall throughput to the cancel-path data structure choice. That's a causal overreach unless it was measured against an alternative.. *Direction:* Make the throughput a property of the engine rather than a consequence, e.g. '..., and the engine sustained 1.26M events/sec over the full replay', or split it into its own clause

### PRIORITY · 2 evaluators · max sev 6
> Built Redis caching in front of the Prisma ORM queries for Tortuga, the studio’s class scheduler with 20,000+ visits in its first 30 days, to reduce database load and latency
- **general_backend_v2** (sev 4): Ends at intent: 'to reduce database load and latency' says what the cache was meant to do, not what it did. The 20,000+ visits number describes the product's traffic, not the caching work, so the only metric in the bullet is not attributable to the action.. *Direction:* Either attach an observed effect if one exists, or swap the intent clause for the design detail (what queries were cached and the invalidation rule) so the bullet ends on an engineering choice rather than a goal.
- **skeptic_v2** (sev 6): The only number (20,000+ visits) describes the product's traffic, not the caching work, so it reads as a borrowed metric. The appositive 'the studio's class scheduler with 20,000+ visits in its first 30 days' interrupts the sentence between the action and its purpose. The result is intent only ('to reduce database load and latency').. *Direction:* Introduce Tortuga first, then the action, so the traffic number reads as context. Example shape: 'Added Redis caching in front of the database queries for Tortuga, the studio's class scheduler that drew 20,000+ visits in its first 30 days, to cut database load'

### PRIORITY · 2 evaluators · max sev 5
> Building RAG meal suggestions for the official UMD app with SentenceBERT vector search in ChromaDB to feed GPT-4o mini real scraped recipes, which internal testers rated satisfactory for 93% of meals
- **general_backend_v2** (sev 2): 'to feed GPT-4o mini real scraped recipes' is word-order awkward ('real' reads oddly); the intent is grounding the model in actual recipes.. *Direction:* Rephrase as 'so GPT-4o mini suggests from real scraped recipes instead of inventing them' or similar.
- **skeptic_v2** (sev 5): Tech dump: 'SentenceBERT vector search in ChromaDB' plus 'GPT-4o mini' gives three model and tool names in one line. 'to feed GPT-4o mini real scraped recipes' is a garden-path phrase that reads as feeding recipes to a mini model. 'RAG meal suggestions' is a noun stack that a non-engineer can't parse.. *Direction:* Lead with the purpose in plain words and keep one retrieval noun. Example shape: 'Building meal suggestions for the official UMD app that retrieve real scraped recipes with vector search before GPT-4o mini answers, which internal testers rated satisfactory for 93% of meals'

### PRIORITY · 2 evaluators · max sev 5
> Writing backtested Java capacity-planning logic that sets upper and lower bounds on the EC2 capacity Amazon Redshift reserves for patching to balance availability against cost
- **recruiter_v2** (sev 4): Long noun chain 'backtested Java capacity-planning logic' and 'EC2 capacity Amazon Redshift reserves for patching' need two reads; only one bullet under the top-billed brand.. *Direction:* Reorder to plain cause then action, e.g. 'Writing Java logic that decides how much spare EC2 capacity Redshift keeps for patching, tested against historical data, to balance availability and cost.'
- **skeptic_v2** (sev 5): 'backtested Java capacity-planning logic' is a noun stack. 'the EC2 capacity Amazon Redshift reserves for patching' is a reduced relative clause that most readers will first parse as 'Amazon Redshift reserves' (a noun).. *Direction:* Add the relative pronoun and move 'backtested' into a verb. Example shape: 'Writing Java logic that sets upper and lower bounds on the EC2 capacity that Amazon Redshift holds in reserve for patching, backtested against past demand to balance availability and cost'

### PRIORITY · 2 evaluators · max sev 3
> Cut AI workflow generation time 65% to under 15s by splitting a Claude skill into focused sub-skills that call Python search and validation tools instead of searching open-ended
- **general_backend_v2** (sev 2): 'instead of searching open-ended' is a compressed phrase nobody says aloud; the reader has to infer it means the model previously explored freely without tools.. *Direction:* Rephrase the tail in plain words, e.g. 'instead of letting one prompt search everything on its own'.
- **skeptic_v2** (sev 3): 'searching open-ended' is ungrammatical ('instead of searching open-endedly' or 'instead of open-ended search'). 'AI workflow generation' doesn't say what a workflow is, though the reader can infer it from the earlier test-data bullet.. *Direction:* Fix the ending, e.g. '... that call Python search and validation tools instead of letting one skill search the whole space'

### 1 evaluators · max sev 4
> Implemented B+ tree and LSM-tree backends for the engine’s event log to compare them on identical 2M-record workloads, which showed the B+ tree giving 12.8x the read throughput and 22x faster range queries for 27% more disk
- **skeptic_v2** (sev 4): Three numbers stacked in one clause ('12.8x ... 22x ... 27%'). 'for 27% more disk' is compressed. It never says why a matching engine's event log needs a read-optimized store, so the decision this informed isn't clear.. *Direction:* Keep two numbers at most and phrase the cost as a trade-off: '..., where the B+ tree gave 12.8x the read throughput at the cost of 27% more disk'

### 1 evaluators · max sev 3
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **general_backend_v2** (sev 3): Strong bullet, but '6,000+ scraped research documents' has no time unit (total corpus vs per day/run), and the 34% has no absolute baseline, so an interviewer can't tell if this is seconds or minutes per document.. *Direction:* Add the unit to the volume and, if measured, the absolute before/after; otherwise leave as is.

## Page-level
- **general_backend_v2** (sev 5): The strongest backend/cloud evidence is not what the eye hits first. The top role (AWS) has one bullet with no result, Capital One opens with a frontend Electron/React bullet, and the most database-heavy work on the page (B+ tree vs LSM-tree event log comparison, O(1) cancel design, 1.26M events/sec) sits in Projects at the bottom. The Kinesis and Redis/PostgreSQL bullets are mid-page and mid-role.. *Direction:* Reorder bullets within roles so the backend one leads (PostgreSQL/Redis first at Capital One; Kinesis first at Amazon Leo). Optionally move the order book project directly under Experience's top two roles or keep it but make sure its title signals the storage-engine comparison.
- **recruiter_v2** (sev 5): Section header 'UMD App Development Contracting (Client: Amazon Leo)' is ambiguous - is it a company, a university office, or a student club - and 'Amazon Leo' is not a widely known name.. *Direction:* Clarify the organization type in the header or title line (e.g. what 'UMD App Development Contracting' is) and add a short descriptor for Amazon Leo if space allows.
- **skeptic_v2** (sev 5): The page leans heavily on LLM wrappers (two Claude-skill bullets, a Bedrock classifier, an LLM-as-judge, a VLM prompt pipeline, RAG). Only the IEX project and the Kinesis/Redis bullets clearly show systems engineering.. *Direction:* Within each role, order bullets so the systems or data-path work comes first (Kinesis latency before the research-tool bullet; caching before RAG). Consider whether Projects should sit higher for backend targets.
- **skeptic_v2** (sev 5): The mandated 'which ...' result clause often attaches to the wrong noun: 'what's popular, which runs', 'permission and rate limits, which became', 'editing smoother, which 90% ... preferred'.. *Direction:* Place the noun the result belongs to right before 'which', or switch to ', and it ...' / a participle for those bullets.
- **skeptic_v2** (sev 4): Skills and project headers list tools that no bullet supports: OpenSearch, SQLAlchemy, PyTorch, API Gateway, CloudWatch, Node.js, and 'POSIX, Linux perf' in the IEX header.. *Direction:* Cut tools from Skills that can't be backed up in an interview, and drop 'POSIX, Linux perf' from the project header unless a bullet uses them.
- **general_backend_v2** (sev 3): What a backend interviewer would dig into: (1) Redis tree over PostgreSQL - refresh/invalidation strategy and what 'permission and rate limits' were; (2) Kinesis vs S3 - ordering, retries, shard count, where the 34% came from; (3) B+ tree vs LSM - why LSM lost on reads at 2M records, compaction settings, write throughput side of the tradeoff; (4) the one mismatched fill out of 99,123; (5) the AWS capacity bounds - what is backtested against. Most of these are answerable from the page's framing, but (1) and the Tortuga cache have no stated mechanism or result to anchor the conversation.. *Direction:* Make sure each backend bullet names its constraint or tradeoff in plain words (see bullet feedback); no new metrics needed.
- **general_backend_v2** (sev 3): No bullet shows designing or owning an API surface, schema, or service boundary, although 'REST APIs' leads the Backend & Full-Stack skills line; the backend work shown is caching, streaming, and storage internals.. *Direction:* If any existing bullet involved defining an API or schema (e.g. the Amazon Leo tool or Tortuga), say so in that bullet's wording; otherwise leave 'REST APIs' in skills but don't rely on it.
- **recruiter_v2** (sev 3): Several bullets run to the full two lines with tool lists in the middle (Capital One #1, Amazon Leo #1, EventBridge bullet), making the middle of the page dense.. *Direction:* Trim tool names that already appear in Technical Skills from the longest bullets.
- **skeptic_v2** (sev 3): Text density: nearly every bullet runs a full two lines and the margins are tight, so the page reads as a uniform block.. *Direction:* Trimming the tech dumps flagged above should shorten several bullets to about 1.5 lines without new layout changes.
- **general_backend_v2** (sev 2): Projects header line 'IEX Order Book & Matching Engine | C++17, STL, POSIX, Linux perf' omits that the project also builds and benchmarks two storage engines; a backend reader scanning titles won't expect database work there.. *Direction:* Consider reordering the project's bullets or lightly retitling so the storage-engine comparison is signposted; keep the bullets themselves.
- **recruiter_v2** (sev 2): Bolded metrics (90%, 65%, 34%, 93%, 50.9M, 12.8x, 1.26M) cluster in Capital One and the order-book project, while the AWS role at the top has no bold anchor.. *Direction:* Check bolding is consistent with what you want remembered; it's fine as is if the order-book project is meant to be the headline.
