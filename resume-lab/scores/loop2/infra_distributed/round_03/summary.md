# Loop 2 · infra_distributed · round 03 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.33 | 7 |
| quantification | 7.67 | 7 |
| technical_depth | 7.67 | 7 |
| concision_readability | 7.33 | 7 |
| skim_test | 7.33 | 7 |
| credibility | 8.0 | 7 |
| ats_parseability | 8.33 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 7.33 | 6 |
| human_voice | 7.0 | 6 |
| plain_language | 6.33 | 6 |
| overall | 7.67 | 7 |

**Plain-English restatement (recruiter):** 9/12 bullets understood
**Competitive:** {'infra_v2': 'Y', 'recruiter_v2': 'Y', 'skeptic_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "AWS SDE Intern (Redmond, Sep-Dec 2026): capacity planning for Amazon Redshift / EC2",
  "Capital One Software Engineering Intern: made an AI workflow tool 65% faster",
  "IEX Order Book & Matching Engine in C++: replayed 50.9M real exchange messages at 1.26M events/sec"
 ],
 "engineer_type": "Cloud/backend engineer who lives on AWS, with a side of AI tooling and one serious C++ performance project. Reads as 'backend + cloud' more than pure distributed systems.",
 "memorable_numbers": [
  "65%",
  "90% of developers preferred",
  "34% latency cut",
  "50.9M messages",
  "1.26M events/sec",
  "12.8x",
  "30%",
  "20,000+ visits"
 ],
 "confusing": [
  "'UMD App Development Contracting (Client: Amazon Leo)': is this Amazon work or a student club? What is Amazon Leo?",
  "'Claude skill' / 'sub-skills': what a skill is and what 'AI workflow generation' produces",
  "'LLM-as-judge' check for a Bedrock classifier",
  "'Tortuga' in the TerpLabs bullet: never introduced",
  "The 'std::list FIFOs ... std::map ... O(1)' line"
 ],
 "skipped": [
  "Technical Skills section beyond the AWS line",
  "Third order-book bullet (the data-structure detail)",
  "TerpLabs and UMIACS details",
  "Certification dates"
 ],
 "interview_questions": [
  "At AWS, how do you decide the upper and lower bounds on Redshift's patching capacity, and what does 'backtested' mean here?",
  "At Capital One, what was the AI tool generating, and why did splitting it into smaller pieces make it faster?",
  "What is the Amazon Leo engagement, and what part of the Kinesis/Lambda pipeline did you own?",
  "In the order book project, why did the B+ tree beat the LSM-tree on reads, and when would you pick the LSM-tree instead?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Built an EventBridge-scheduled LLM-as-judge check for a production Amazon Bedrock classifier that rates research documents by importance to trigger fine-tuning only when its grades shift past a threshold
- **infra_v2** (sev 5): The clause 'that rates research documents by importance to trigger fine-tuning' attaches the purpose to the classifier rather than to the check, so on first read it sounds like the classifier triggers fine-tuning. 'its grades' is also ambiguous: the judge's grades or the classifier's.. *Direction:* Put the actor and the trigger next to each other, then describe the classifier in its own clause. Example: 'Built an EventBridge-scheduled LLM-as-judge check that grades a production Amazon Bedrock classifier (which ranks research documents by importance) and triggers fine-tuning only when the grades shift past a threshold'
- **recruiter_v2** (sev 7): Four jargon terms stacked before the reader learns the purpose: 'EventBridge-scheduled', 'LLM-as-judge', 'Amazon Bedrock classifier', 'fine-tuning'. The sentence is also ambiguous: 'that rates research documents' could attach to the check or the classifier, and 'its grades' could be either.. *Direction:* Lead with the purpose: 'Built a scheduled check that has a second model grade a production document classifier and triggers retraining only when its grades drift past a threshold'. Move EventBridge/Bedrock to the end or to Skills.
- **skeptic_v2** (sev 7): Two stacked noun phrases ('EventBridge-scheduled LLM-as-judge check', 'production Amazon Bedrock classifier') carry the whole bullet, and the ending is ambiguous: it is unclear whether 'to trigger fine-tuning' attaches to the check or the classifier, and whether 'its grades' means the judge's grades or the classifier's. Nobody says 'an EventBridge-scheduled LLM-as-judge check' out loud.. *Direction:* Unpack the noun stack into a verb sequence: say what runs on a schedule, what it compares, and what it triggers, and drop the product names that don't explain the mechanism. Example: 'Built a scheduled job that has an LLM re-grade a sample of documents our Bedrock importance classifier already scored, and kicks off fine-tuning only when the two disagree past a threshold'.

### PRIORITY · 3 evaluators · max sev 7
> Ran the full replay at 1.26M events/sec end-to-end on an order book that keeps std::list FIFOs per price level in a std::map with an order-ID hash map to make cancels O(1)
- **infra_v2** (sev 3): The throughput number has no setting (single thread? what machine?), and the second half is a data-structure description stacked behind it. 'Ran the full replay at' frames the number as a run, not as the result of the design described next.. *Direction:* Lead with the design choice and land on the number as its result. Example: 'Kept per-price-level FIFO lists in a std::map plus an order-ID hash map so cancels are O(1), sustaining 1.26M events/sec end-to-end on a single thread' (only if single-threaded is true).
- **recruiter_v2** (sev 7): The first half (1.26M events/sec) is clear; the second half 'std::list FIFOs per price level in a std::map with an order-ID hash map' is a type-signature read aloud. Nobody would say it this way in an interview, and 'O(1)' means nothing to a recruiter.. *Direction:* Keep the 1.26M events/sec first, then say the design choice in words: 'keeping orders in a first-in-first-out queue per price and indexing them by order ID so cancels take constant time'. The std:: type names can go or move to a parenthetical.
- **skeptic_v2** (sev 6): Two unrelated claims stitched into one sentence (a throughput number and a data-structure layout), and the second half is a telegraphic container dump ('std::list FIFOs per price level in a std::map with an order-ID hash map'). 'Ran ... at' is a weak verb for a performance claim, and there is no hint of how 1.26M/sec was measured or on what machine.. *Direction:* Pick one idea per bullet, or make the data structure the cause of the number in plain words: say that each order is indexed by ID so a cancel is a direct lookup, then give the throughput. Avoid naming three std containers in a row.

### PRIORITY · 3 evaluators · max sev 6
> Precomputed popular workflows from a 270K+ row PostgreSQL table into a Redis-cached category tree to keep lookups within the database’s permission and rate limits, which became the Claude skill’s main search tool
- **infra_v2** (sev 4): 'to keep lookups within the database’s permission and rate limits' doesn't say what the constraint was. Permission limits and rate limits are different problems, and a cache only solves the rate one in an obvious way.. *Direction:* Name the constraint in plain words before naming the mechanism. Example: 'Because the Claude skill couldn’t query a 270K+ row PostgreSQL table directly under its permission and rate limits, precomputed popular workflows into a Redis-cached category tree, which became the skill’s main search tool'
- **recruiter_v2** (sev 4): 'permission and rate limits' is unclear (permission limits are not something caching usually solves), and the payoff 'became the Claude skill's main search tool' depends on the reader having decoded 'Claude skill' in the previous bullet.. *Direction:* Consider moving it first under Capital One for this target, and rephrase the why in plain words ('so the AI assistant could search them without exceeding the database's rate limits').
- **skeptic_v2** (sev 6): 'Redis-cached category tree' is a noun stack, the mechanism behind 'permission' limits is unexplained (caching avoids rate limits, but how does it address permissions?), and 'which became' has an ambiguous antecedent: grammatically it points at the limits, not the tree.. *Direction:* Name the problem first in plain words (the skill could not query the table live), then the fix, and put the 'main search tool' result immediately after the thing that became it. Replace 'Redis-cached category tree' with a verb phrase, e.g. 'grouped ... into a category tree and cached it in Redis'.

### PRIORITY · 3 evaluators · max sev 6
> Rebuilt a legacy test-data workflow tool as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation to make editing smoother, which 90% of 30+ surveyed developers preferred
- **infra_v2** (sev 3): This is a frontend/desktop app bullet with four framework names (React, TypeScript, Electron, React Flow, Jest) and no infrastructure angle. 'to make editing smoother' is vague.. *Direction:* For this target, trim the framework list to what explains the work (e.g. 'an Electron app with a visual flow editor and tested validation') and leave React/Jest to Skills, or move this bullet last in a version tailored to infra.
- **recruiter_v2** (sev 4): Five tech names (React, TypeScript, Electron, React Flow, Jest) sit between what was rebuilt and why; the purpose 'to make editing smoother' is vague. For an infra target this is also the least relevant Capital One bullet.. *Direction:* Name the change in plain terms (a desktop app with a drag-and-drop editor and automatic validation), drop the redundant 'React and TypeScript' since Skills carries them, and end on the 90% result.
- **skeptic_v2** (sev 6): Five technologies in one clause (React, TypeScript, Electron, React Flow, Jest) reads as a keyword dump; 'legacy test-data workflow tool' is a noun stack; 'make editing smoother' is vague; and '90% preferred' has no stated comparison (preferred over the legacy tool?).. *Direction:* Cut the tech list to the one or two that explain the design (e.g. the visual flow editor), state the comparison explicitly, and consider shortening or dropping this bullet for infra versions so the two backend bullets carry the role.

### PRIORITY · 3 evaluators · max sev 6
> Built Redis caching in front of Tortuga’s Prisma ORM queries to reduce database load and latency for a class scheduler that drew 20,000+ visits in its first 30 days
- **infra_v2** (sev 4): 'Tortuga’s' is an unexplained proper noun; a reader can't tell whether Tortuga is the class scheduler, a separate product, or a company. 'to reduce database load and latency' states intent with no observed effect, and the 20,000+ visits measures the product's traffic, not the cache.. *Direction:* Lead with the product so the name resolves itself, then the mechanism. Example: 'Built Redis caching in front of the Prisma ORM queries for Tortuga, a class scheduler that drew 20,000+ visits in its first 30 days, to cut database load and latency'. Add a measured effect only if one exists.
- **recruiter_v2** (sev 4): 'Tortuga' is never introduced (the reader has to infer it is the class-scheduler product). 'to reduce database load and latency' is intent, so the only number (20,000+ visits) describes the app's popularity, not the caching work.. *Direction:* Introduce the product first ('Tortuga, a class scheduler that drew 20,000+ visits in its first 30 days'), then the caching. Drop 'Prisma ORM' if space is tight.
- **skeptic_v2** (sev 6): 'Tortuga' is never introduced (product? company?), 'reduce database load and latency' states intent with no outcome, and the only number (20,000+ visits) measures the product's popularity, not the caching work, so the metric is attached to the wrong claim.. *Direction:* Introduce the product in a few words before naming it, and restructure so the 20,000+ visits reads as the load the cache had to handle (context) rather than as its result.

### PRIORITY · 3 evaluators · max sev 5
> Implemented B+ tree and LSM-tree backends for the engine’s event log to compare them on identical 2M-record workloads, which showed the B+ tree giving 12.8x the read throughput and 22x faster range queries for 27% more disk
- **infra_v2** (sev 3): The comparison reports only the read side. An LSM tree is chosen for write throughput, so a storage-engine comparison that only shows the B+ tree winning on reads and losing on disk invites the question of what happened on writes.. *Direction:* If a write number exists, swap it in for one of the read figures so the bullet shows both sides of the tradeoff. If not, naming the workload shape ('on an append-then-query workload') explains why the B+ tree won.
- **recruiter_v2** (sev 3): Three comparative numbers (12.8x, 22x, 27%) in one clause; 'for 27% more disk' is compressed and reads as a cost only after a second pass.. *Direction:* Split the tradeoff explicitly ('... 12.8x the read throughput and 22x faster range queries, at the cost of 27% more disk'). Consider whether both read numbers are needed.
- **skeptic_v2** (sev 5): Three stacked metrics in the closing clause, and the comparison is one-sided: it reports only where the B+ tree wins, while the standard reason to pick an LSM tree (write throughput) is not mentioned, so the result looks like the expected textbook outcome. 'for 27% more disk' is compressed.. *Direction:* Drop to the one or two numbers that carry the conclusion and state the trade-off in words ('at the cost of 27% more disk'); if write results exist, name the conclusion rather than adding another metric.

### PRIORITY · 2 evaluators · max sev 7
> Cut AI workflow generation time 65% to under 15s by splitting a Claude skill into focused sub-skills that call Python search and validation tools instead of relying on open-ended model search
- **recruiter_v2** (sev 7): 'AI workflow generation' and 'Claude skill' / 'sub-skills' are never defined. I can repeat the 65% but not what the tool generates, who uses it, or what a 'skill' is. The only hint of what a workflow is ('test-data workflow') comes two bullets later.. *Direction:* Open with what the tool does for whom in plain words ('an internal AI assistant that drafts test-data workflows for developers'), then the 65%, then the method. Replace 'Claude skill into focused sub-skills' with plainer wording such as 'splitting one large Claude prompt-tool into smaller steps' if that is accurate.
- **skeptic_v2** (sev 4): 'AI workflow generation time' is a noun stack and 'workflow' is never defined, so a non-engineer cannot say what was being generated or for whom.. *Direction:* Spend two or three words saying what the workflows are, e.g. 'Cut the time to generate a test-data workflow from a prompt ...'.

### PRIORITY · 2 evaluators · max sev 6
> Co-built a topic-scoring research tool and deployed it to dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK to show Amazon Leo's public-policy staff which research topics are popular
- **recruiter_v2** (sev 5): The purpose ('to show ... staff which research topics are popular') comes after a three-tool deployment chain; 'deployed it to dev' will be read by a non-engineer as either 'shipped' or nothing.. *Direction:* Put who it is for first, then say his part: 'Co-built a tool that shows Amazon Leo's policy staff which research topics are popular, and set up its automated deployment to a dev environment on AWS Fargate using CDK and GitHub Actions'.
- **skeptic_v2** (sev 6): Two actions stitched with 'and' (co-built, deployed), a three-item tech dump (Fargate, GitHub Actions CI/CD, CDK) with no decision attached to any of them, and the purpose clause trails at the end. 'Co-built' leaves ownership open, and 'deployed it to dev' quietly signals it never reached production.. *Direction:* Lead with the part the candidate personally owned and keep only the tech that explains it; move purpose to the front or cut it. Example shape: 'Wrote the CDK stack and GitHub Actions pipeline that deploy our team's topic-scoring tool to Fargate, so Amazon Leo's policy staff can see which research topics are trending'.

### 1 evaluators · max sev 5
> Writing backtested Java capacity-planning logic that sets upper and lower bounds on the EC2 capacity Amazon Redshift reserves for patching to balance availability against cost
- **skeptic_v2** (sev 5): 'backtested Java capacity-planning logic' is a noun stack, and 'the EC2 capacity Amazon Redshift reserves for patching' is a garden-path phrase: 'reserves' first reads as a noun. The purpose clause 'to balance availability against cost' is tacked onto the end.. *Direction:* Put the problem in plain order: Redshift keeps spare EC2 capacity while it patches clusters; the candidate is writing the Java logic that sets how much, backtested against history, so it neither runs short nor overpays. Keep it one sentence.

### 1 evaluators · max sev 2
> Cut end-to-end latency 34% on a data pipeline that sends 6,000+ scraped research documents to model inference by streaming them through Amazon Kinesis into AWS Lambda instead of staging each step in S3
- **infra_v2** (sev 2): 'end-to-end latency' doesn't say per document or per batch run, and the 6,000+ figure reads as a total, not a rate.. *Direction:* Add one word of scope if it fits, e.g. 'per-document end-to-end latency' or 'batch run time'.

## Page-level
- **skeptic_v2** (sev 6): The infra story is thin at the top. The AWS role has one in-progress bullet, Capital One is mostly LLM-skill and React work, and the clearest systems evidence (Kinesis pipeline, order book replay, B+ tree vs. LSM study) sits in the middle or in Projects. Nothing on the page shows reliability or operations work (monitoring, failure handling, on-call, scaling incidents).. *Direction:* Reorder within roles so infra-relevant bullets come first (e.g. the Postgres/Redis precompute bullet before the Claude-skill bullet), trim or drop the React bullet for this target, and consider whether Projects should sit closer to the top for infra versions.
- **infra_v2** (sev 5): The strongest infra and performance evidence (1.26M events/sec, B+ tree vs LSM-tree comparison, 50.9M-message replay) is in the last section above Skills. The top of the page shows an AWS bullet with no result (by design) and Capital One bullets about splitting a Claude skill.. *Direction:* Keep Experience first, but within the Amazon Leo contract lead with the Kinesis latency bullet (already done) and consider ordering Capital One so the caching/rate-limit bullet comes before the sub-skill bullet in an infra-targeted version. Alternatively, a one-line project mention is not needed; the reorder within roles is enough.
- **recruiter_v2** (sev 5): The employer line 'UMD App Development Contracting (Client: Amazon Leo)' is ambiguous: a recruiter can't tell whether this is Amazon work, a student organization, or freelance, and 'Amazon Leo' is not a widely known name.. *Direction:* Clarify the relationship in the header in plain words (e.g. a university contracting program doing client work for Amazon Leo, Amazon's satellite internet project, if accurate).
- **recruiter_v2** (sev 5): Jargon density: about a quarter of the bullets (Claude sub-skills, LLM-as-judge, std::list FIFOs) can't be restated by a non-engineer.. *Direction:* Rephrase those three bullets purpose-first, keeping one distinctive technical noun each and moving secondary tool names to Skills.
- **recruiter_v2** (sev 4): The 'systems engineer' thread isn't the first impression. The Capital One block leads with AI-assistant and Electron front-end work, so the middle of the page reads as 'AI tooling / full-stack', and the strongest systems evidence (Kinesis pipeline, order book speed) is spread out.. *Direction:* Within each role, order bullets so the infra/performance one comes first (e.g. the caching/rate-limit bullet at Capital One). No new content needed.
- **skeptic_v2** (sev 4): The Skills section lists technologies that no bullet uses: API Gateway, SNS, CloudWatch, X-Ray, OpenSearch, SQLAlchemy, Node.js. 'observability (CloudWatch, X-Ray)' and 'AWS CDK (infrastructure as code)' are parenthetical keyword dumps.. *Direction:* Keep only skills the candidate can tell a specific story about, and drop the explanatory parentheticals ('infrastructure as code', 'CI/CD') that only an ATS needs.
- **infra_v2** (sev 3): Skills lists API Gateway, SNS, OpenSearch, CloudWatch and X-Ray, none of which appear in any bullet. 'B+ tree and LSM-tree storage' under 'Backend, Full-Stack & Data' and 'data structures and algorithms' under Practices are concepts, not tools.. *Direction:* Keep only tools you can point to in a bullet or defend in an interview. Drop 'data structures and algorithms' and let the order book project carry B+/LSM-tree storage.
- **skeptic_v2** (sev 3): Several bullets follow the 'did X to Y, which Z' template mechanically, so the page has a repetitive cadence ('..., which became', '..., which 90% ... preferred', '..., which agreed', '..., which showed'), and a 'which' clause often has an ambiguous antecedent.. *Direction:* Keep the allowed shape, but make sure each 'which' sits directly after the noun it refers to; where it can't, use the 'cut <metric> by doing X' form instead.
- **infra_v2** (sev 2): Around 10% of the page is empty below the Certification line while several bullets are tightly compressed.. *Direction:* Use the spare space for a little more vertical spacing between roles rather than adding content.
- **skeptic_v2** (sev 2): About 10% of the page at the bottom is empty while the AWS role has a single bullet and several bullets are crammed to the two-line limit.. *Direction:* Use the freed space to split the stitched bullets (the order-book throughput/data-structure one) rather than to add new claims.
