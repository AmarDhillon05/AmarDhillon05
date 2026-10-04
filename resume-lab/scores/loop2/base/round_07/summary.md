# Loop 2 · base · round 07 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.33 | 7 |
| quantification | 7.67 | 7 |
| technical_depth | 7.67 | 7 |
| concision_readability | 7.33 | 7 |
| skim_test | 7.33 | 7 |
| credibility | 7.67 | 7 |
| ats_parseability | 8.33 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 7.67 | 7 |
| human_voice | 7.0 | 6 |
| plain_language | 6.33 | 6 |
| overall | 7.67 | 7 |

**Plain-English restatement (recruiter):** 11/14 bullets understood
**Competitive:** {'general_backend_v2': 'Y', 'recruiter_v2': 'Y', 'skeptic_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "Amazon Web Services SDE Intern (fall 2026), working on capacity planning for Redshift",
  "Capital One Software Engineering Intern (summer 2026): rebuilt an internal tool and made an AI workflow generator 65% faster",
  "IEX order book / matching engine project in C++ that replayed tens of millions of real exchange messages and almost exactly matched the exchange"
 ],
 "engineer_type": "Backend / cloud engineer who also does AI tooling and some low-level C++ performance work; feels like a strong builder rather than a researcher",
 "memorable_numbers": [
  "50.9M messages",
  "99,122 of 99,123 fills",
  "1.26M events/sec",
  "65% faster",
  "90% of developers preferred",
  "34% latency cut",
  "12.8x read throughput",
  "20,000+ visits",
  "93% of meals",
  "110+ member studio",
  "3.5 GPA"
 ],
 "confusing": [
  "What 'Amazon Leo' is and why a UMD student contracting group has it as a client",
  "'Claude skill' and 'sub-skills' at Capital One",
  "The robot grasp bullet (AnyGrasp, Open3D)",
  "B+ tree vs LSM-tree comparison and the std::list / std::map bullet",
  "What 'Tortuga' is in the TerpLabs bullet"
 ],
 "skipped": [
  "Technical Skills section beyond the first line",
  "Most of the UMIACS bullet",
  "Third Amazon Leo bullet about the LLM-as-judge check",
  "Certification line"
 ],
 "interview_questions": [
  "What does the Redshift capacity logic actually decide, and how do you check it against history?",
  "Walk me through how you made the Capital One workflow generator 65% faster",
  "What was the one fill out of 99,123 that didn't match the exchange?",
  "How are you balancing the Amazon Leo contract, UMIACS and TerpLabs alongside the AWS internship?",
  "What did your role look like at TerpLabs beyond co-founding it?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Precomputed popular workflows from a 270K+ row PostgreSQL table into a Redis-cached category tree to keep lookups within the database's permission and rate limits, which became the Claude skill's main search tool
- **general_backend_v2** (sev 4): 'within the database's permission and rate limits' is ambiguous: 'permission limits' is not a standard concept, so the reader cannot tell whether the cache solved a throttling problem, an access-control problem, or both. It is also the most backend-shaped bullet in the internship but is placed last.. *Direction:* Name the constraint in plain words before the tech, e.g. 'Because the skill could only query PostgreSQL at a limited rate, precomputed ...'. Move this bullet to the top of Capital One.
- **recruiter_v2** (sev 7): The bullet leads with the mechanism ('Precomputed ... Redis-cached category tree') and the reason ('permission and rate limits') is a constraint a non-engineer can't picture. The payoff clause 'became the Claude skill's main search tool' depends on knowing what a 'Claude skill' is.. *Direction:* Open with the problem (the AI tool couldn't query the workflow database directly because of access and rate limits), then say what was built (a cached, category-organized index of popular workflows), then say it became the tool's main search path. Reuse the 'AI workflow generator' wording from the bullet above instead of 'Claude skill' so the two bullets read as one story.
- **skeptic_v2** (sev 6): Two problems. Mechanism: it is unclear how precomputing keeps lookups within 'permission' limits (rate limits make sense; permissions do not). Grammar: 'which became the Claude skill's main search tool' grammatically attaches to 'limits', not to the tree, and is an extra clause tacked on at the end.. *Direction:* Name the constraint plainly and put the 'main search tool' fact earlier so 'which' has an unambiguous referent, e.g. 'Built the Claude skill's main search tool by caching popular workflows from a 270K-row PostgreSQL table in Redis, so lookups stayed within the database's rate limits'.

### PRIORITY · 3 evaluators · max sev 6
> Co-built a topic-scoring research tool and deployed it to dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK to show Amazon Leo's public-policy staff which research topics are popular
- **general_backend_v2** (sev 4): The middle of the bullet is a tech list ('AWS Fargate with GitHub Actions CI/CD and AWS CDK') with no decision attached, and 'Co-built' plus 'deployed it to dev' leaves the candidate's own share and the tool's status unclear. The purpose arrives only at the end.. *Direction:* Lead with what the tool does for the policy staff, then state the candidate's own piece, e.g. 'Wrote the AWS CDK stack and GitHub Actions pipeline that deploy ...'. Keep 'dev' — it is honest scoping.
- **recruiter_v2** (sev 3): 'deployed it to dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK' is a three-tool chain in the middle of the sentence, and 'to dev' is easy to miss, so the honest scoping (not production) gets lost.. *Direction:* Keep 'deployed to a dev environment' in plain words and one infra term that shows ownership (e.g., 'with infrastructure as code'), and leave the rest to Skills.
- **skeptic_v2** (sev 6): 'Co-built' leaves ownership unclear: what did Amar build versus the team? 'deployed it to dev' honestly admits it never reached production, but then the bullet's purpose ('to show ... staff') reads as if it is in use. 'on AWS Fargate with GitHub Actions CI/CD and AWS CDK' is a tech dump of three tools with no engineering decision attached.. *Direction:* Name Amar's piece first and keep only the tool that explains it (e.g., if he wrote the infra-as-code, say 'Wrote the AWS CDK stack and CI pipeline that deploy...'); let Skills carry the rest.

### PRIORITY · 3 evaluators · max sev 6
> Built Redis caching in front of Tortuga's Prisma ORM queries to reduce database load and latency for a class scheduler that drew 20,000+ visits in its first 30 days
- **general_backend_v2** (sev 4): 'to reduce database load and latency' states intent, not result, and the only number (20,000+ visits) measures the product's traffic, not the cache. 'Tortuga' is an unexplained proper noun until 'class scheduler' arrives at the end.. *Direction:* Introduce the product first ('For Tortuga, a class scheduler that drew 20,000+ visits in its first 30 days, ...') so the traffic number reads as scale context, then the caching decision (what was cached / invalidation) if no measured result exists.
- **recruiter_v2** (sev 4): 'Tortuga' is never introduced, and a reader can't tell whether it's the product, a client, or a library. 'Prisma ORM queries' is jargon placed ahead of what the product is. The result is traffic (20,000+ visits), not the effect of the cache, so it's unclear what the caching achieved.. *Direction:* Name the product first ('For Tortuga, TerpLabs' class scheduler (20,000+ visits in its first 30 days), added Redis caching in front of database queries to cut load and latency') and drop 'Prisma ORM' or move it to Skills, where Prisma already appears.
- **skeptic_v2** (sev 6): The only number (20,000+ visits) measures the product's traffic, not the caching, so the bullet borrows a metric for work it does not measure. 'reduce database load and latency' ends at intent. 'Tortuga' is an unexplained proper noun and 'Tortuga's Prisma ORM queries' is a possessive noun stack.. *Direction:* Introduce the product first and frame the traffic as context, e.g. 'Added a Redis cache in front of the database for Tortuga, a class scheduler that drew 20,000+ visits in its first 30 days, ...'; drop 'Prisma ORM' from the sentence.

### PRIORITY · 3 evaluators · max sev 6
> Built and prompt-tuned a pipeline that overlays AnyGrasp's candidate grasps on camera images in Open3D to help a vision-language model pick robot grasps that avoid hitting the table for a PhD-led project targeting ICLR
- **general_backend_v2** (sev 2): Two trailing purpose clauses ('to help ... that avoid ... for a PhD-led project') make this a long chain; it is also the least backend-relevant item on the page.. *Direction:* Optional: split the purpose from the project context, or trim 'Built and prompt-tuned' to one verb. Fine to leave as is.
- **recruiter_v2** (sev 5): 'AnyGrasp's candidate grasps' and 'in Open3D' come before the purpose, so the reader has to get through two unfamiliar names before learning it's about helping a robot choose where to grip. 'targeting ICLR' means nothing to most recruiters.. *Direction:* Reorder to goal, then method, then tools: helping a robot's AI model choose grips that avoid the table, by drawing candidate grips onto camera images, with AnyGrasp/Open3D named last or moved to Skills. 'targeting ICLR' can stay as the context at the end.
- **skeptic_v2** (sev 6): Tacks an extra clause onto the end ('for a PhD-led project targeting ICLR'), which violates the one-clause structure rule. 'targeting ICLR' reads as a venue claim for unsubmitted work. There is no outcome: the bullet ends at intent ('to help ... pick').. *Direction:* Cut the trailing project/venue clause (move 'PhD-led' context to the role line if needed) and end on what the pipeline does for the robot.

### PRIORITY · 3 evaluators · max sev 5
> Rebuilt a legacy test-data workflow tool as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation to make editing smoother, which 90% of 30+ surveyed developers preferred
- **general_backend_v2** (sev 5): This is the first Capital One bullet a backend reader sees, and it is a desktop UI rebuild: React, TypeScript, Electron, React Flow and Jest are packed into one clause before the reader learns why. The backend-relevant Capital One work (the PostgreSQL/Redis lookup and the sub-skill split) sits below it.. *Direction:* Reorder Capital One so the PostgreSQL/Redis bullet or the 65% generation-time bullet leads, and move this one to third. Within the bullet, lead with the tool and outcome and drop one of the stacked tech names (Electron or React Flow) to Skills if it does not explain the engineering.
- **recruiter_v2** (sev 3): Four technologies ('React and TypeScript Electron ... React Flow ... Jest-tested') sit between the action and the result, so the bullet runs to two dense lines before the reader reaches '90%'.. *Direction:* Keep the visual editor and the validation, which explain the design, and cut 'React and TypeScript' or 'Jest-tested' (both are already in Skills).
- **skeptic_v2** (sev 5): Parenthetical-style tech dump of five names (React, TypeScript, Electron, React Flow, Jest) in one stretch. 'make editing smoother' is vague. 'which 90% ... preferred' has no stated comparison (preferred over the legacy tool, presumably) and 'which' attaches to 'editing' rather than the app.. *Direction:* Keep Electron and the visual editor, cut the rest to Skills, and state the comparison, e.g. '...which 90% of 30+ surveyed developers preferred over the old tool'.

### PRIORITY · 2 evaluators · max sev 7
> Built an EventBridge-scheduled LLM-as-judge check for a production Amazon Bedrock classifier that rates research documents by importance to trigger fine-tuning only when its grades shift past a threshold
- **recruiter_v2** (sev 7): Five jargon terms in a row ('EventBridge-scheduled LLM-as-judge check ... Amazon Bedrock classifier ... fine-tuning'), and 'its grades' could refer to the judge or to the classifier. The why (avoid retraining when nothing has changed) is implied, not stated.. *Direction:* Say the plain idea first, e.g. 'a scheduled check that uses a second model to spot when the production document classifier's ratings drift, so it is retrained only when needed', and move 'EventBridge' to Skills, where it already appears.
- **skeptic_v2** (sev 6): Noun stacks: 'EventBridge-scheduled LLM-as-judge check' and 'production Amazon Bedrock classifier'. 'its grades' is ambiguous (the judge's grades or the classifier's?), and it is unclear whether the classifier or the check triggers fine-tuning. No result is given.. *Direction:* Say the loop in plain order: a scheduled job has a second LLM re-grade the classifier's outputs and kicks off fine-tuning only when the two disagree past a threshold. Keep 'Bedrock' or 'EventBridge', not both, in the sentence.

### PRIORITY · 2 evaluators · max sev 7
> Ran the full replay at 1.26M events/sec end-to-end on an order book that keeps std::list FIFOs per price level in a std::map with an order-ID hash map to make cancels O(1)
- **recruiter_v2** (sev 7): The second half ('std::list FIFOs per price level in a std::map with an order-ID hash map ... O(1)') is pure code vocabulary. A non-engineer gets the throughput number and nothing else. The bullet also mixes two separate ideas: overall speed and how cancels are made fast.. *Direction:* Put the design in words first ('orders kept in time-ordered queues per price, plus a lookup by order ID so cancels take constant time') and keep at most one concrete type name if it helps an engineer reader. Leave 1.26M events/sec as the result at the end.
- **skeptic_v2** (sev 6): Breaks the structure rule: 'Ran ... at 1.26M events/sec' is a measurement, not 'did X to accomplish Y', and the data-structure description is tacked on as a second idea. 'std::list FIFOs per price level in a std::map with an order-ID hash map' is a three-container noun stack nobody says aloud. The throughput number has no baseline or hardware context, and std::list is a well-known cache-unfriendly choice that a performance-minded interviewer will challenge immediately.. *Direction:* Lead with the design choice and its purpose in one sentence, then attach the throughput as the result, e.g. 'Kept a hash map from order ID to each resting order so cancels run in O(1), which let the full replay run at 1.26M events/sec'. Be ready to defend std::list or drop the container names.

### PRIORITY · 2 evaluators · max sev 5
> Building RAG meal suggestions for the official UMD app with SentenceBERT vector search in ChromaDB to feed GPT-4o mini real scraped recipes, which internal testers rated satisfactory for 93% of meals
- **general_backend_v2** (sev 3): 'to feed GPT-4o mini real scraped recipes' is a stitched phrase that reads as if GPT-4o mini is being fed meals; the reader has to re-parse to understand that retrieval grounds the model's suggestions in real recipes.. *Direction:* Rephrase the purpose in plain words, e.g. '... using SentenceBERT search over scraped recipes in ChromaDB so GPT-4o mini suggests real dishes, which ...'.
- **skeptic_v2** (sev 5): 'to feed GPT-4o mini real scraped recipes' is a garden-path double object that readers stumble on. 'SentenceBERT vector search in ChromaDB' plus 'GPT-4o mini' is three named tools in one sentence. 'RAG meal suggestions' is a noun stack.. *Direction:* Say the user-facing behavior first, then the mechanism once, e.g. 'Building meal suggestions for the official UMD app that retrieve real scraped recipes before the LLM answers, which internal testers rated satisfactory for 93% of meals'.

### PRIORITY · 2 evaluators · max sev 4
> Writing backtested Java capacity-planning logic that sets upper and lower bounds on the EC2 capacity Amazon Redshift reserves for patching to balance availability against cost
- **general_backend_v2** (sev 3): 'the EC2 capacity Amazon Redshift reserves for patching' is a reduced relative clause that reads as a noun stack on first pass ('EC2 capacity Amazon Redshift reserves').. *Direction:* Add 'that' to break the noun stack: '... bounds on the EC2 capacity that Amazon Redshift reserves for patching, balancing availability against cost'.
- **skeptic_v2** (sev 4): 'backtested Java capacity-planning logic' is a noun stack, and 'the EC2 capacity Amazon Redshift reserves for patching' is a reduced relative clause that reads at first as 'Amazon Redshift reserves' (a noun).. *Direction:* Add 'that' and unstack, e.g. 'Writing Java logic, checked against historical data, that sets bounds on how much EC2 capacity Amazon Redshift holds back for patching, to balance availability against cost'.

### 1 evaluators · max sev 5
> Implemented B+ tree and LSM-tree backends for the engine’s event log to compare them on identical 2M-record workloads, which showed the B+ tree giving 12.8x the read throughput and 22x faster range queries for 27% more disk
- **skeptic_v2** (sev 5): Stacks three metrics in the tail clause. Reports only read-side results; LSM-trees exist to win on writes, so omitting write throughput looks cherry-picked to an informed reader. Why an append-heavy event log needs range queries is not explained.. *Direction:* Keep one headline number and say which backend the engine kept and why, rather than listing three ratios.

### 1 evaluators · max sev 3
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **general_backend_v2** (sev 3): Strong design-change bullet, but '6,000+ scraped research documents' has no time unit (total corpus vs. per day) and the 34% has no absolute scale (seconds vs. minutes).. *Direction:* If known, add the time unit or absolute latency in a few words; otherwise leave as is — the S3-to-Kinesis change is the right thing to emphasize.

### 1 evaluators · max sev 3
> Cut AI workflow generation time 65% to under 15s by splitting a Claude skill into focused sub-skills that call Python search and validation tools instead of relying on open-ended model search
- **skeptic_v2** (sev 3): Correct form, but 'instead of relying on open-ended model search' is a tacked-on contrast clause, and 'Claude skill' / 'sub-skills' is insider jargon a recruiter cannot restate.. *Direction:* Drop the 'instead of...' tail; the contrast is implied by 'focused sub-skills that call ... tools'.

## Page-level
- **general_backend_v2** (sev 5): Is the strongest backend/cloud evidence visible first? Partly. AWS SDE Intern at the top is the right headline brand, but its single bullet is in progress with no result, and the next bullet a reader hits is a React/Electron UI rebuild. The clearest backend evidence (PostgreSQL/Redis lookup, S3-to-Kinesis/Lambda latency cut, EventBridge-scheduled eval) and the C++ matching engine sit in the lower two-thirds.. *Direction:* Reorder Capital One bullets so a backend bullet leads. Section order can stay (experience before projects is correct for these brands).
- **recruiter_v2** (sev 5): Several bullets put the tool or mechanism before the purpose (Capital One bullet 3, Amazon Leo bullet 3, UMIACS, the third IEX bullet), so the page alternates between very clear bullets and bullets only an engineer can parse.. *Direction:* Apply the same order to every bullet: what problem or user, what was built, then the result. Keep the distinctive nouns (Kinesis, B+ tree, Redis) but put them after the plain-language purpose.
- **skeptic_v2** (sev 5): The 'systems-oriented engineer' story only shows up at the bottom (IEX project). The top half is mostly LLM/workflow tooling (Claude skill, LLM-as-judge, RAG, VLM grasps), so a 7-second skim says 'AI-app builder', not 'backend/systems engineer'.. *Direction:* Within each role, put the most backend/systems bullet first (e.g., the Kinesis latency bullet ahead of the topic-scoring tool bullet at Amazon Leo).
- **recruiter_v2** (sev 4): Bolding is inconsistent. Some results are bold (90%, 65%, 93%, 50.9M, 12.8x, 1.26M events/sec), but equally strong numbers are not (34% latency, 20,000+ visits, 99,122 of 99,123). The bold also skews to the project and Capital One, not AWS.. *Direction:* Choose one bold anchor per role at most and apply it to the headline result of that role (e.g., the 34% latency cut for Amazon Leo, the fill-match figure for IEX), removing bold from secondary numbers.
- **recruiter_v2** (sev 4): 'Amazon Leo' is used as a client name with no hint of what it is, and the employer line 'UMD App Development Contracting (Client: Amazon Leo)' makes it unclear whether this is a club, a university program, or paid work for Amazon.. *Direction:* clarify: what UMD App Development Contracting is (a student contracting group? a university program?), in a few words on the title line, without adding new scope.
- **skeptic_v2** (sev 4): Skills lists items no bullet backs up: 'fine-tuning and evaluation', PyTorch, OpenSearch, SQLAlchemy, API Gateway, CloudWatch, psutil.. *Direction:* Cut skills that cannot be defended for 5 minutes in an interview, or reword 'fine-tuning and evaluation' to match what was actually built (LLM evaluation).
- **skeptic_v2** (sev 4): Three bullets end at intent with no outcome (AWS capacity bounds, UMIACS grasp pipeline, Bedrock judge check), and four use a trailing 'which ...' clause whose referent is grammatically ambiguous.. *Direction:* Vary the sentence shapes; use the 'cut <metric> N% by doing X' form where a real number exists and make sure each 'which' sits directly after the noun it describes.
- **general_backend_v2** (sev 3): Skills lists REST APIs, API Gateway, Node.js, SQLAlchemy and OpenSearch, none of which appear in any bullet.. *Direction:* Keep only skills the candidate can discuss from real work, or ensure the bullets that used them are recognizable (e.g. if the Amazon Leo tool exposes an API, say so).
- **skeptic_v2** (sev 3): Proper nouns appear with no context: 'Tortuga', 'Amazon Leo', 'AnyGrasp', 'React Flow', 'IEX'.. *Direction:* Give each a 2-3 word gloss the first time it appears (e.g., 'Tortuga, a class scheduler'), or drop it where the generic noun does the job.
- **general_backend_v2** (sev 2): Heading 'UMD App Development Contracting (Client: Amazon Leo)' puts a second Amazon name directly under the AWS internship.. *Direction:* Fine as is; it is already honestly scoped.
- **recruiter_v2** (sev 2): The AWS role, the biggest brand on the page and listed first, has one bullet that starts with 'Writing' and carries no outcome. This is accepted as a known gap, but the visual weight of the section is very light compared with Capital One.. *Direction:* No change needed beyond keeping the bullet as clear as it is now. Don't pad it.
- **general_backend_v2** (sev 1): What a backend interviewer would dig into: cache invalidation and freshness for the Redis category tree and the Tortuga cache; why Kinesis + Lambda over S3 staging (ordering, retries, cost) and what the 34% is measured on; how the LLM-as-judge threshold was chosen; the Redshift backtest methodology; and in the IEX project, single-thread vs. multi-thread at 1.26M events/sec, the 1 mismatched fill of 99,123, and why the B+ tree beat the LSM-tree on reads.. *Direction:* No change needed; informational.
