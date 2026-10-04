# Loop 2 · base · round 08 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.33 | 7 |
| quantification | 7.67 | 7 |
| technical_depth | 8.33 | 8 |
| concision_readability | 6.67 | 6 |
| skim_test | 8.0 | 8 |
| credibility | 7.67 | 7 |
| ats_parseability | 8.67 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 8.33 | 8 |
| human_voice | 6.67 | 6 |
| plain_language | 6.33 | 6 |
| overall | 8.0 | 8 |

**Plain-English restatement (recruiter):** 12/14 bullets understood
**Competitive:** {'general_backend_v2': 'Y', 'recruiter_v2': 'Y', 'skeptic_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "AWS Software Development Engineer Intern (Redmond), working on EC2 capacity for Redshift",
  "Capital One Software Engineering Intern: rebuilt a developer tool that 90% of surveyed developers preferred, and made an AI workflow tool 65% faster",
  "IEX Order Book & Matching Engine in C++: replayed 50.9M real exchange messages and matched almost every fill"
 ],
 "engineer_type": "Backend/cloud engineer with a lot of AWS and AI-tooling work, plus one serious C++ performance project. Reads as a strong builder across cloud and AI apps; the 'systems' side comes mostly from the order book project.",
 "memorable_numbers": [
  "90% of 30+ developers",
  "65% faster",
  "34% latency",
  "50.9M messages",
  "99,122 of 99,123 fills",
  "12.8x",
  "1.26M events/sec",
  "93% of meals",
  "20,000+ visits",
  "110+ members"
 ],
 "confusing": [
  "'UMD App Development Contracting (Client: Amazon Leo)': is this an Amazon job or a student club? What is Amazon Leo?",
  "'LLM-as-judge check' and 'grades shift past a threshold' in the contracting role",
  "AnyGrasp / Open3D in the research bullet",
  "'B+ tree and LSM-tree backends' and 'std::list FIFOs' in the project"
 ],
 "skipped": [
  "Technical Skills section beyond the first line",
  "UMIACS research bullet",
  "TerpLabs Redis caching bullet",
  "Third order-book bullet"
 ],
 "interview_questions": [
  "What does the AWS capacity-planning logic decide, and how are you checking it against past data?",
  "How did splitting the Claude skill into sub-skills make generation 65% faster?",
  "What was the one fill out of 99,123 that didn't match the exchange, and why?",
  "What is your relationship to Amazon Leo: who employs you and who uses the tool?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Built an EventBridge-scheduled LLM-as-judge check for a production Amazon Bedrock classifier that rates research documents by importance to trigger fine-tuning only when its grades shift past a threshold
- **general_backend_v2** (sev 4): The chain of qualifiers ('for a production ... classifier that rates ... by importance to trigger fine-tuning only when its grades shift') leaves the subject of 'trigger' unclear: is it the classifier or the check? 'grades shift' doesn't say shift relative to what.. *Direction:* Split the bullet into what the check does and what it decides: 'Built a scheduled (EventBridge) LLM-as-judge check on a production Bedrock document classifier that triggers fine-tuning only when its grades drift past a threshold from <baseline>'.
- **recruiter_v2** (sev 7): Three stacked service/technique names ('EventBridge-scheduled LLM-as-judge check', 'production Amazon Bedrock classifier') come before the reader knows what the check does, and 'its grades' is ambiguous: it could refer to the judge or the classifier.. *Direction:* Lead with the plain purpose (a scheduled check that decides when the document classifier needs retraining), then the method (a second model grading its output), and move 'EventBridge' to Skills or the end.
- **skeptic_v2** (sev 7): Two stacked noun phrases ('EventBridge-scheduled LLM-as-judge check', 'production Amazon Bedrock classifier') that nobody says out loud. The tail is also ambiguous: 'to trigger fine-tuning' could attach to the classifier ('rates documents ... to trigger fine-tuning') or to the check, and 'its grades' could be the judge's or the classifier's.. *Direction:* Lead with the plain job in verb form, then the trigger, then the scheduler. Move 'EventBridge' to the end or to Skills. Example shape: 'Built a scheduled check that has an LLM grade our Bedrock document-ranking model and kicks off fine-tuning only when its grades drift past a threshold'.

### PRIORITY · 3 evaluators · max sev 6
> Rebuilt a legacy test-data workflow tool as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation to make editing smoother, which 90% of 30+ surveyed developers preferred
- **general_backend_v2** (sev 4): The middle of the bullet stacks five technologies ('React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation'). '90% ... preferred' doesn't say what they preferred it over.. *Direction:* Keep React Flow, since it explains the visual editor, and leave the rest of the stack to Skills. State the comparison, e.g. '...which 90% of 30+ surveyed developers preferred over the legacy tool'.
- **recruiter_v2** (sev 4): Five technology names in one clause ('React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation') make it read like a stack list rather than a person describing what they built.. *Direction:* Cut 'React and TypeScript' or 'Jest-tested' to Skills; keep 'Electron app' and 'visual editor' since they explain what changed for users.
- **skeptic_v2** (sev 6): Five technologies packed into the middle (React, TypeScript, Electron, React Flow, Jest) read as a parenthetical tech dump without the parentheses. 'to make editing smoother' is vague, and 'preferred' doesn't say over what. 'legacy test-data workflow tool' is a noun stack.. *Direction:* Keep at most 'Electron app with a visual React Flow editor' and move React/TypeScript/Jest to Skills. Say 'preferred it over the old tool'. Replace 'smoother' with the concrete change (e.g. visual editing instead of hand-edited files, if that's the case).

### PRIORITY · 3 evaluators · max sev 6
> Built and prompt-tuned a pipeline for a PhD-led robotics project aimed at ICLR that overlays AnyGrasp’s candidate grasps on camera images in Open3D to help a vision-language model pick grasps that avoid hitting the table
- **general_backend_v2** (sev 3): For a backend reader this is the least relevant bullet, and it has no outcome. It ends at intent ('to help ... pick grasps'), and 'aimed at ICLR' is a submission target, not a result.. *Direction:* Leave it as is if no result exists. If a result does exist, state it. Don't add backend framing that isn't true.
- **recruiter_v2** (sev 4): Long, single-sentence chain ('...aimed at ICLR that overlays AnyGrasp's candidate grasps ... in Open3D to help a vision-language model...'); AnyGrasp and Open3D are opaque tool names mid-sentence.. *Direction:* Lead with the goal (helping a robot's vision-language model choose grips that avoid collisions), then the method; consider moving 'Open3D' to Skills.
- **skeptic_v2** (sev 6): One long chain of relative clauses ('for a project aimed at ICLR that overlays ... to help ... that avoid'). 'that overlays' grammatically attaches to the project or to ICLR, not to the pipeline. 'aimed at ICLR' is a venue name-drop with unclear status (submitted? planned?), and an interviewer will ask. There is no outcome.. *Direction:* Split purpose from venue: put the pipeline's job first (draw candidate grasps onto camera images so a VLM can pick collision-free ones), then 'for a PhD-led project targeting ICLR'. Consider cutting 'in Open3D' to Skills.

### PRIORITY · 3 evaluators · max sev 6
> Built Redis caching in front of Tortuga’s Prisma ORM queries to reduce database load and latency for a class scheduler that drew 20,000+ visits in its first 30 days
- **general_backend_v2** (sev 4): 'Tortuga’s' is an unexplained product name that comes before the reader knows it's a class scheduler. 'to reduce database load and latency' states intent with no measured change, so the only number (20,000+ visits) describes traffic, not the cache.. *Direction:* Introduce the product first ('Tortuga, a class scheduler with 20,000+ visits in its first 30 days'), then the cache and what it cached. If there's no measured result, say what was cached (e.g. which queries) and drop the intent clause.
- **recruiter_v2** (sev 4): 'Tortuga' is never introduced; a reader has to guess it is the class scheduler. 'Prisma ORM queries' adds jargon without explaining the decision.. *Direction:* Name the product first ('Tortuga, a class scheduler that drew 20,000+ visits...'), then the caching; 'Prisma ORM' can move to Skills.
- **skeptic_v2** (sev 6): The only number (20,000+ visits) measures the product's traffic, not the caching work, so it reads as borrowed impact. 'to reduce database load and latency' states an intent with no result. 'Tortuga' is never explained, so the reader has to infer it's the class scheduler.. *Direction:* Name the product once ('Tortuga, a class scheduler with 20,000+ visits in its first month') so the visits are framed as context, not as the cache's result. If no measurement exists, say what the cache keyed on or what it invalidated on instead of an unmeasured 'reduce'.

### PRIORITY · 3 evaluators · max sev 5
> Built the Claude skill’s main search tool by precomputing popular workflows from a 270K+ row PostgreSQL table into a Redis-cached category tree to keep lookups within the database’s permission and rate limits
- **general_backend_v2** (sev 5): The stated reason, 'to keep lookups within the database’s permission and rate limits', is the most confusing clause on the page. It's unclear whether the precomputation avoided rate limiting, worked around restricted access, or both. A backend interviewer will also ask straight away how the cached tree stays fresh.. *Direction:* Name the constraint concretely and say what the tree is keyed on, before the technology. For example: '...so the agent queries a cached tree keyed by <category> and doesn’t hit the shared, rate-limited PostgreSQL table on every lookup'.
- **recruiter_v2** (sev 5): 'Redis-cached category tree' and 'within the database's permission and rate limits' are hard to picture; the bullet doesn't say what the search tool finds or for whom.. *Direction:* Say the problem first (the AI skill couldn't query the 270K-row table directly because of access limits), then the fix (precomputed, cached category tree).
- **skeptic_v2** (sev 5): The mechanism is unclear. 'precomputing popular workflows ... into a category tree' doesn't say what the tree is keyed on, and how a cache keeps lookups 'within the database's permission ... limits' isn't obvious. A cache explains rate limits, not permissions. 'Redis-cached category tree' is a noun stack.. *Direction:* Name the constraint and the design in one sentence without a 'Because ...' preamble, e.g. 'Built ... by precomputing ... so the skill never queried the table directly, keeping it within its access and rate limits'.

### PRIORITY · 3 evaluators · max sev 4
> Cut AI workflow generation time 65% to under 15s by splitting a Claude skill into focused sub-skills that call Python search and validation tools instead of relying on open-ended model search
- **general_backend_v2** (sev 4): 'Claude skill', 'sub-skills' and 'open-ended model search' are terms specific to LLM tooling. A general backend interviewer or recruiter can't picture the before and after.. *Direction:* Describe the change in plain terms: the model stopped searching freely and started calling deterministic Python search and validation tools. Tie 'workflow' back to the tool in the bullet above so the reader knows what was generated.
- **recruiter_v2** (sev 3): 'AI workflow generation' isn't tied back to the test-data tool in bullet one, so the reader isn't sure what is being generated or by whom.. *Direction:* Add a short anchor such as 'test-data workflow generation' so the three Capital One bullets read as one story.
- **skeptic_v2** (sev 3): 'AI workflow generation' doesn't say what a workflow is (it's only explained by the bullet above). 'open-ended model search' is jargon a non-engineer can't restate.. *Direction:* Tie it to the tool above with a few words ('generating test-data workflows with Claude') and replace 'open-ended model search' with 'letting the model search on its own'.

### PRIORITY · 2 evaluators · max sev 7
> Designed the order book with std::list FIFOs per price level in a std::map and an order-ID hash map to make cancels O(1), which ran the full replay at 1.26M events/sec end-to-end
- **recruiter_v2** (sev 7): The first two-thirds is C++ container names ('std::list FIFOs per price level in a std::map'); the only plain outcome is at the very end, and 'O(1)' is jargon to a non-engineer.. *Direction:* Put the goal first (constant-time cancels / fast replay), then the structure in words ('a queue per price level plus a lookup by order ID'); keep 'std::map' only if it explains the choice.
- **skeptic_v2** (sev 6): 'which ran the full replay' has no sensible antecedent: the design, or the cancels, doesn't run a replay; the engine does. The tacked-on 'which' clause links throughput to the cancel design without showing the two are causally connected. 'std::list FIFOs per price level in a std::map' is a dense stack.. *Direction:* Either make throughput the subject ('Replayed the full feed at 1.26M events/sec by ...') or keep the design sentence and drop the dangling 'which'. Spell the structure out in words: 'a FIFO queue per price level, kept in a sorted map, plus a hash map from order ID to its queue position so cancels are O(1)'.

### PRIORITY · 2 evaluators · max sev 6
> Co-built a topic-scoring research tool and deployed it to dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK to show Amazon Leo’s public-policy staff which research topics are popular
- **general_backend_v2** (sev 4): 'Co-built' doesn't say which part the candidate owned. 'deployed it to dev' shows the tool only reached a dev environment, and that sits in the middle of the bullet. The infrastructure list ('Fargate with GitHub Actions CI/CD and AWS CDK') reads as a tech list, not a decision.. *Direction:* Lead with the user and the purpose, then the piece the candidate owned (e.g. 'set up the CDK-defined Fargate deployment and GitHub Actions pipeline'). Keep the honest 'dev' scope, but make it a clause and not the headline.
- **skeptic_v2** (sev 6): 'Co-built' makes ownership unclear: what did Amar build versus a teammate? The middle is a tech list ('AWS Fargate with GitHub Actions CI/CD and AWS CDK') that reads as keywords rather than a decision. 'deployed it to dev' honestly says it isn't in prod, but it lands as an anticlimax after the deployment stack. 'topic-scoring research tool' is a noun stack.. *Direction:* Name Amar's own slice first, keep one infra tool only if it explains a choice, and let Skills carry the rest. Put the audience/purpose before the deployment detail.

### PRIORITY · 2 evaluators · max sev 5
> Writing backtested Java capacity-planning logic that sets upper and lower bounds on the EC2 capacity Amazon Redshift reserves for patching to balance availability against cost
- **general_backend_v2** (sev 5): The phrase 'the EC2 capacity Amazon Redshift reserves for patching' parses two ways on first read: 'reserves' can be read as a noun ('Redshift reserves') until the reader reaches 'for patching'. The top bullet on the page, under the strongest brand, needs a second pass.. *Direction:* Put the system and the purpose first and make 'reserve' unambiguously a verb, e.g. 'Writing backtested Java logic that decides how much EC2 capacity Amazon Redshift should hold back for patching, setting upper and lower bounds to balance availability against cost'.
- **skeptic_v2** (sev 5): 'backtested Java capacity-planning logic' is a noun stack, and 'the EC2 capacity Amazon Redshift reserves for patching' is a reduced relative clause that reads at first as 'EC2 capacity Amazon Redshift' as a compound. 'logic' is vague about what Amar owns (a model? a service? a formula?).. *Direction:* Lead with the problem in plain words: Redshift holds spare EC2 capacity for patching; Amar is writing the Java code that decides how much (upper/lower bounds) and backtesting it on history. Add 'that' in 'the EC2 capacity that Redshift reserves'.

### PRIORITY · 2 evaluators · max sev 5
> Building RAG meal suggestions for the official UMD app with SentenceBERT vector search in ChromaDB to feed GPT-4o mini real scraped recipes, which internal testers rated satisfactory for 93% of meals
- **general_backend_v2** (sev 3): 'to feed GPT-4o mini real scraped recipes' needs a reread: 'real scraped recipes' is the object, but it's easy to read 'GPT-4o mini real' as one phrase. The bullet also stacks three AI terms in a row.. *Direction:* Reorder to put the purpose first: '...so GPT-4o mini suggests meals grounded in real scraped recipes retrieved with SentenceBERT vector search in ChromaDB'.
- **skeptic_v2** (sev 5): 'to feed GPT-4o mini real scraped recipes' is a garden-path phrase (double object, reads as 'feed GPT-4o mini' then 'real scraped recipes'). 'RAG meal suggestions' is a noun stack. 'for 93% of meals' is unclear: meals the model suggested, or dining-hall meals?. *Direction:* Say the purpose in plain words first (suggest meals grounded in real recipes so the model doesn't invent dishes), then the mechanism (SentenceBERT search over scraped recipes), then the 93%. Move ChromaDB to Skills.

### 1 evaluators · max sev 4
> Implemented B+ tree and LSM-tree backends for the engine's event log to compare them on identical 2M-record workloads, which showed the B+ tree giving 12.8x the read throughput and 22x faster range queries for 27% more disk
- **skeptic_v2** (sev 4): Mixes ratio styles ('12.8x the read throughput' vs '22x faster range queries'), and the comparison only reports reads. An LSM tree's main advantage is writes, so a reader wonders whether write results were left out. Why an order-book event log needs either structure isn't stated.. *Direction:* Use one ratio phrasing for both numbers. If write results exist, state the trade-off honestly in place of one of the read numbers; if not, frame it as a read-path comparison.

### 1 evaluators · max sev 3
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **skeptic_v2** (sev 3): '6,000+ scraped research documents' has no time unit (total, per day, per run), so the scale is unanchored. 'S3 staging hops' is jargon.. *Direction:* Add the period if known; say 'intermediate S3 writes' instead of 'staging hops'.

### 1 evaluators · max sev 2
> Co-founded a 110+ member student product studio that has shipped 5 live products
- **recruiter_v2** (sev 2): Pure scale statement with no engineering content; it uses one of three slots in the role.. *Direction:* Fine to keep; optionally fold into the role header line to free attention for the engineering bullets.

## Page-level
- **general_backend_v2** (sev 5): The strongest systems evidence (the C++ order book: 50.9M messages replayed, 99,122/99,123 fills matched, 1.26M events/sec, the B+ tree vs LSM comparison) is last on the page, below the UMIACS robotics bullet and the TerpLabs RAG bullet. The backend and cloud evidence higher up (Postgres to Redis precompute, S3 to Kinesis rewrite, EventBridge drift check) is real but spread out and mixed with LLM and frontend work.. *Direction:* Inside each role, order bullets with the backend or data-path bullet first (e.g. at Capital One, put the PostgreSQL/Redis search-tool bullet above the Electron rewrite). Consider whether UMIACS or TerpLabs should come below Projects for backend-targeted versions.
- **recruiter_v2** (sev 5): The intended 'systems-oriented engineer' identity rests mostly on the IEX order book project, which sits at the bottom of the page; the experience section reads as cloud + AI tooling.. *Direction:* Consider whether the order book project's strongest bullet earns a higher position, or whether experience bullets can name the systems aspect (latency, capacity, caching) first.
- **recruiter_v2** (sev 5): 'UMD App Development Contracting (Client: Amazon Leo)' is an unfamiliar org name next to a famous brand.. *Direction:* clarify in the header what kind of organization this is (e.g. student-run contracting group) and keep the client in parentheses.
- **skeptic_v2** (sev 5): Human voice across the page: about half the bullets lead with a compound noun stack ('backtested Java capacity-planning logic', 'legacy test-data workflow tool', 'topic-scoring research tool', 'EventBridge-scheduled LLM-as-judge check', 'RAG meal suggestions').. *Direction:* Unpack each stack into a verb phrase or a 'that' clause; keep one distinctive noun per bullet.
- **general_backend_v2** (sev 4): Plain-language load is high in the middle of the page: 'Claude skill', 'sub-skills', 'LLM-as-judge', 'Bedrock classifier', 'AnyGrasp', 'Open3D', 'RAG', 'SentenceBERT' all appear within about 12 lines, and most aren't explained.. *Direction:* In each AI bullet, keep the one distinctive noun that explains the engineering. Put the rest into a plain description of what the system does.
- **recruiter_v2** (sev 4): Nearly every bullet fills two full lines and several stack 3-5 product names (React Flow, Jest, EventBridge, Bedrock, Open3D, Prisma).. *Direction:* Move tool names that don't explain a decision to Technical Skills; the Skills section already lists most of them.
- **skeptic_v2** (sev 4): Skills lists tools with no supporting bullet: OpenSearch, SQLAlchemy, API Gateway, CloudWatch, PyTorch, Node.js, Jira, Agile, psutil. 'data structures and algorithms' as a skill is filler.. *Direction:* Cut entries that you can't point to on the page or discuss in depth; drop 'data structures and algorithms' and 'Agile'.
- **general_backend_v2** (sev 3): What a backend interviewer would dig into: (1) Redis category tree: cache key design, refresh and invalidation, and what the 'permission and rate limits' were; (2) S3 to Kinesis: where the 34% came from, and the batching, ordering and retry semantics in Lambda; (3) the 1 fill out of 99,123 that didn't match, and how it was debugged; (4) B+ tree vs LSM: the write-amplification tradeoff behind the '27% more disk'; (5) the Tortuga cache hit rate. Of these, (1) and (5) have the weakest written support.. *Direction:* Clarify the constraint and key in the Capital One search-tool bullet. Say what was cached in the Tortuga bullet. No new metrics are needed.
- **general_backend_v2** (sev 3): No bullet shows API design or service ownership (endpoints, request handling, schemas) even though 'REST APIs' and 'API Gateway' are listed under Skills.. *Direction:* If any existing project (e.g. the Amazon Leo topic-scoring tool or Tortuga) exposed an API the candidate built, name it in that bullet's wording. Otherwise leave it in Skills only and don't invent it.
- **skeptic_v2** (sev 3): Three concurrent college-year roles plus a co-founder role, with one bullet at UMIACS and one at AWS, spread thin evidence across many headers.. *Direction:* No new facts needed; make sure each single-bullet role's bullet states Amar's own deliverable clearly (see AWS and UMIACS bullet feedback).
- **skeptic_v2** (sev 2): Bolding is inconsistent: 90%, 65%, 93%, 50.9M, 12.8x and 1.26M events/sec are bold, but 34% (Kinesis) and 99,122 of 99,123 are not.. *Direction:* Pick one rule (one bold per bullet on the headline result) and apply it consistently. Consider bolding the fill-match instead of 50.9M.
