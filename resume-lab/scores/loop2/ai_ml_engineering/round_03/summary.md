# Loop 2 · ai_ml_engineering · round 03 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.67 | 7 |
| quantification | 7.67 | 7 |
| technical_depth | 7.67 | 7 |
| concision_readability | 7.67 | 7 |
| skim_test | 7.67 | 7 |
| credibility | 7.67 | 7 |
| ats_parseability | 8.67 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 7.67 | 7 |
| human_voice | 7.33 | 6 |
| plain_language | 6.67 | 6 |
| overall | 7.67 | 7 |

**Plain-English restatement (recruiter):** 10/11 bullets understood
**Competitive:** {'ml_infra_v2': 'Y', 'recruiter_v2': 'Y', 'skeptic_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "Amazon Web Services SDE intern (fall 2026), something about EC2/Redshift capacity",
  "Capital One SWE intern: made an LLM/Claude workflow generator 65% faster",
  "Contract work for Amazon Leo on AWS (Bedrock, Kinesis, 34% latency cut), plus a C++ order book project with 50.9M messages"
 ],
 "engineer_type": "Backend/cloud engineer who builds LLM-powered apps and pipelines on AWS; some C++ systems work on the side",
 "memorable_numbers": [
  "65%",
  "90%",
  "34%",
  "93%",
  "50.9M",
  "20,000+",
  "GPA 3.5",
  "May 2028"
 ],
 "confusing": [
  "What a 'Claude skill' and 'sub-skills' are",
  "What Amazon Leo is (and why a UMD contracting group has it as a client)",
  "The robotics bullet: AnyGrasp, Open3D, 'aimed at ICLR'",
  "'Tortuga' in the TerpLabs section"
 ],
 "skipped": [
  "Technical Skills section beyond the AI/ML line",
  "Most of the UMIACS and TerpLabs bullets",
  "Certification line"
 ],
 "interview_questions": [
  "What did the Claude workflow generator do, and how did you measure that quality didn't drop?",
  "What is Amazon Leo and what was your role versus the rest of the contracting team?",
  "How did you validate your order book against the exchange, and what was the one mismatched fill?",
  "What are you building at AWS right now?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Built an EventBridge-scheduled LLM-as-judge check for a production Amazon Bedrock classifier that rates research documents by importance to trigger fine-tuning only when its grades shift past a threshold
- **ml_infra_v2** (sev 5): This is the strongest ML-infra bullet on the page (scheduled eval gating a retrain), but the sentence has three nested clauses and an ambiguous 'its': it is unclear whether 'its grades' are the judge's grades or the classifier's grades, and 'that rates research documents' could attach to the judge or the classifier. The judge itself is also unvalidated on the page: nothing says what it is compared against.. *Direction:* Split subject and mechanism: state what the classifier does first, then what the judge checks and what crossing the threshold triggers. E.g. 'A production Bedrock classifier rates research documents by importance; built an EventBridge-scheduled LLM-as-judge check that re-grades its outputs and triggers fine-tuning only when [judge vs. classifier disagreement] passes a threshold'.
- **recruiter_v2** (sev 4): 'its grades' is ambiguous (the judge's or the classifier's), and 'EventBridge-scheduled' leads the sentence with a service name instead of the purpose.. *Direction:* Say 'a scheduled check' and let EventBridge sit in Skills or later in the sentence; replace 'its grades' with 'the classifier's ratings' so the trigger is clear.
- **skeptic_v2** (sev 7): The bullet opens on a noun stack, 'EventBridge-scheduled LLM-as-judge check', and the purpose clause 'to trigger fine-tuning' grammatically attaches to the classifier ('a classifier that rates documents ... to trigger fine-tuning'), not to the check he built. 'its grades' could mean the judge's grades or the classifier's grades. There is no outcome, so it reads as a task.. *Direction:* Lead with what the check does in plain words, then the mechanism, and move the scheduler to the end or into Skills. Example shape: 'Built a scheduled LLM-as-judge check that re-grades a production Bedrock document classifier and triggers fine-tuning only when its grades drift past a threshold'

### PRIORITY · 3 evaluators · max sev 6
> Built and prompt-tuned a pipeline for a PhD-led robotics project aimed at ICLR that overlays AnyGrasp's candidate grasps on camera images in Open3D to help a vision-language model pick grasps that avoid hitting the table
- **ml_infra_v2** (sev 5): 'prompt-tuned' is ambiguous (in ML it usually means learned soft prompts, not hand-iterating prompt text), and the bullet has no evaluation or outcome: nothing says whether grasp selection improved or how it was measured. It ends at intent ('to help ... pick grasps').. *Direction:* Replace 'prompt-tuned' with the plain verb that matches what was done (e.g. 'iterated the VLM prompt'); if any evaluation exists, end with it, otherwise state the honest status (e.g. in progress). Consider cutting 'aimed at ICLR' if space is needed - it signals ambition, not result.
- **recruiter_v2** (sev 4): Long single sentence with four proper nouns (ICLR, AnyGrasp, Open3D, vision-language model) before the plain goal arrives at the very end; 'aimed at ICLR' means nothing to most recruiters.. *Direction:* Put the goal first (help a robot's vision-language model choose grasps that avoid the table), then the method (overlaying candidate grasps on camera images). Consider 'targeting a paper at ICLR' so a recruiter recognizes it as a publication effort.
- **skeptic_v2** (sev 6): Garden path: 'a robotics project aimed at ICLR that overlays ...' makes the project, not the pipeline, the thing that overlays. 'aimed at ICLR' name-drops a venue with no submission status. There is no result, and 'Built and prompt-tuned' is two verbs for an unclear split of work.. *Direction:* Put the pipeline's action right after 'pipeline' and move the project context to the end (or into the role line). Cut 'aimed at ICLR' unless a status can be stated.

### PRIORITY · 3 evaluators · max sev 6
> Built Redis caching in front of Tortuga's Prisma ORM queries to reduce database load and latency for a class scheduler that drew 20,000+ visits in its first 30 days
- **ml_infra_v2** (sev 4): 'Tortuga' is never introduced, so the reader can't tell whether it is the class scheduler, a client, or a separate product. The 20,000+ visits number measures the product's traffic, not the caching work; 'reduce database load and latency' is stated as intent with no result.. *Direction:* Name the product once in plain words before the tech (e.g. 'for Tortuga, TerpLabs' class scheduler (20,000+ visits in its first 30 days), put Redis caching in front of Prisma ORM queries to cut database load'), so the traffic number reads as scale context rather than the result.
- **recruiter_v2** (sev 5): 'Tortuga' is never introduced; I don't know whether it is TerpLabs' product, a client, or a library. 'Prisma ORM queries' adds a tech name that doesn't help the reader.. *Direction:* Open with the product: 'For Tortuga, our class scheduler that drew 20,000+ visits in its first 30 days, added Redis caching...'. Prisma can move to Skills.
- **skeptic_v2** (sev 6): 'Tortuga' is never explained (is it the scheduler's name?). The only number, 20,000+ visits, measures the product's traffic, not the caching work, so 'reduce database load and latency' is an unmeasured intent.. *Direction:* Name the product once, plainly, so the visit count reads as context for scale rather than as a result of the caching. Example shape: 'Added Redis caching in front of the Prisma queries for Tortuga, a class scheduler that drew 20,000+ visits in its first 30 days, to cut database load'

### PRIORITY · 3 evaluators · max sev 6
> Rebuilt a legacy test-data workflow tool as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation to make editing smoother, which 90% of 30+ surveyed developers preferred
- **ml_infra_v2** (sev 2): Four framework names in one clause ('React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation'), and 'to make editing smoother' is vague about what was painful before. It is also the least relevant Capital One bullet for an ML-infra target.. *Direction:* Name the old pain in plain words and keep one or two technologies; React Flow and Jest can live in Skills. Fine to keep as the third bullet.
- **recruiter_v2** (sev 3): Four tech names (React, TypeScript, Electron, React Flow, Jest) packed into the middle push the purpose and result to the end; 'make editing smoother' is vague.. *Direction:* Cut to the techs that explain the design (Electron app, visual flow editor) and let Skills carry TypeScript/Jest.
- **skeptic_v2** (sev 6): Five technologies in the middle of the sentence (React, TypeScript, Electron, React Flow, Jest) read as a keyword dump. 'to make editing smoother' is vague. 'which ... preferred' attaches to 'editing smoother' and never says preferred over what.. *Direction:* Keep one or two technologies that explain the design (Electron, the visual flow editor), move the rest to Skills, and state the comparison the 90% refers to.

### PRIORITY · 2 evaluators · max sev 7
> Precomputed popular workflows from a 270K+ row PostgreSQL table into a Redis-cached category tree to keep lookups within the database’s permission and rate limits, which became the Claude skill’s main search tool
- **recruiter_v2** (sev 7): Three abstract nouns in a row ('popular workflows', 'category tree', 'permission and rate limits') with no plain statement of what the user or the AI was looking up and why the database alone could not serve it. 'Permission and rate limits' reads as a constraint I cannot interpret.. *Direction:* Lead with the problem in plain words (the AI tool needed to search X but the database limited how often/what it could query), then the fix (a cached, categorized index of the most-used workflows), then the outcome (became the tool's main search). Drop 'popular' or say what made a workflow popular.
- **skeptic_v2** (sev 6): 'which became' grammatically points to 'permission and rate limits', the nearest noun, not to the category tree. 'Redis-cached category tree' is a noun stack. It is also unclear how precomputing keeps lookups within *permission* limits: rate limits make sense, permissions do not.. *Direction:* Reorder so the result follows its subject directly ('built a cached category tree ... that became the skill's main search tool'), and either explain or drop 'permission'.

### PRIORITY · 2 evaluators · max sev 6
> Co-built a topic-scoring research tool and deployed it to dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK to show Amazon Leo's public-policy staff which research topics are popular
- **ml_infra_v2** (sev 3): The middle of the bullet is a deployment tech list ('AWS Fargate with GitHub Actions CI/CD and AWS CDK') with no decision attached, and 'topic-scoring' is undefined - it is unclear how it relates to the importance classifier in the first bullet of this role.. *Direction:* Lead with what the tool tells policy staff, then the one infra choice the candidate owned; move CDK/GitHub Actions to Skills if they don't explain a decision. Alternatively cut this bullet to give the LLM-as-judge bullet room to breathe.
- **skeptic_v2** (sev 6): Ambiguous ownership: 'Co-built' with no indication of which part was his. The middle is a deployment-stack list (Fargate, GitHub Actions, CI/CD, CDK) that does not explain any engineering decision. 'deployed it to dev' is honest but signals the tool never reached users, and the purpose clause comes last, after the tech dump.. *Direction:* State his piece first and the purpose second. Keep only the deployment tech that matches the part he owned, or cut this bullet so the stronger two Leo bullets stand out.

### PRIORITY · 2 evaluators · max sev 6
> Split a Claude skill into sub-skills backed by Python search and validation tools to stop open-ended model search, which cut LLM workflow generation time 65% to under 15s with no quality loss in stress tests
- **recruiter_v2** (sev 5): 'Claude skill' and 'open-ended model search' are insider terms; the bullet never says what the generated 'workflow' is for or who uses it.. *Direction:* Replace 'to stop open-ended model search' with a plain phrase like 'so the model stopped searching aimlessly', and add a few words naming what the generated workflows are for.
- **skeptic_v2** (sev 6): Structure rule: 'with no quality loss in stress tests' is an extra clause tacked onto the end after the 'which' result. 'Claude skill', 'sub-skills' and 'LLM workflow generation' are not defined, so a non-engineer cannot say what a workflow is or who generates it.. *Direction:* Cut the trailing quality clause, or fold it into the main result so the bullet ends on the metric. Replace 'LLM workflow generation' with a short plain noun for what the model produces.

### PRIORITY · 2 evaluators · max sev 5
> Building RAG meal suggestions for the official UMD app with SentenceBERT vector search in ChromaDB to feed GPT-4o mini real scraped recipes, which internal testers rated satisfactory for 93% of meals
- **ml_infra_v2** (sev 2): The evaluation is end-to-end human satisfaction only; the retrieval step itself has no stated check, and 'feed GPT-4o mini real scraped recipes' does not say why grounding was needed (e.g. to stop invented recipes). The why is implied, not said.. *Direction:* Add the reason in a short clause after 'real scraped recipes' if it is true; do not add retrieval metrics that don't exist.
- **skeptic_v2** (sev 5): 'to feed GPT-4o mini real scraped recipes' is an awkward double object that is hard to say aloud. '93% of meals' is ambiguous (meals, or suggested meals?). 'official UMD app' leaves the relationship unclear: is this a contract, and is it live?. *Direction:* Rephrase the grounding clause as a purpose ('so GPT-4o mini suggests only real scraped recipes') and say '93% of suggestions'.

### 1 evaluators · max sev 5
> Writing backtested Java capacity-planning logic that sets upper and lower bounds on the EC2 capacity Amazon Redshift reserves for patching to balance availability against cost
- **skeptic_v2** (sev 5): 'backtested Java capacity-planning logic' is a noun stack. 'the EC2 capacity Amazon Redshift reserves for patching' is a garden path: 'Redshift reserves' reads as a noun pair until the reader backtracks.. *Direction:* Add the relative pronoun and unstack the adjectives. Example shape: 'Writing Java capacity-planning logic, backtested on past data, that sets bounds on how much EC2 capacity Amazon Redshift holds in reserve for patching, to balance availability against cost'

### 1 evaluators · max sev 3
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **skeptic_v2** (sev 3): Close to the ideal form. The only gaps are the unclear baseline (34% of per-document or per-batch latency?) and whether 6,000+ is a total or a rate.. *Direction:* Optional: add 'per run' or 'per day' if accurate. Otherwise leave as is.

## Page-level
- **ml_infra_v2** (sev 5): Skills lists 'model fine-tuning' under AI/ML, but no bullet shows the candidate fine-tuning a model - the Amazon Leo bullet only triggers fine-tuning.. *Direction:* Cut 'model fine-tuning' from Skills or replace it with what is shown (e.g. fine-tuning triggers / eval gating) unless the candidate actually ran fine-tuning jobs.
- **skeptic_v2** (sev 5): The AI/ML Skills line lists 'model fine-tuning' and 'vision-language models', but no bullet shows him fine-tuning a model (the Leo bullet only triggers fine-tuning) or doing more than prompting a VLM. 'Open3D' is a library, not an AI/ML skill.. *Direction:* Keep only skills the bullets back up, or reword to what he did (e.g., 'fine-tuning triggers/evaluation'). Move Open3D to another line.
- **skeptic_v2** (sev 5): Across the page, three Capital One bullets and two Leo bullets use the 'X to do Y, which Z' frame where 'which' attaches to the nearest noun instead of the intended subject, so the result reads as describing the wrong thing.. *Direction:* On each bullet, check that the noun just before 'which' is the thing that produced the result, and reorder the clauses where it is not.
- **recruiter_v2** (sev 4): Several entities are never explained: 'Amazon Leo', 'Tortuga', 'Claude skill'.. *Direction:* Add a few plain words where each first appears (what the client/product is), without adding new claims.
- **ml_infra_v2** (sev 3): The strongest ML-infra evidence (eval-gated retraining and the 34% Kinesis/Lambda latency cut at Amazon Leo, plus the 65% Claude skill speedup) sits under the 2nd and 3rd roles; the first role is a non-ML Redshift capacity bullet.. *Direction:* Keep reverse-chronological order; make sure the first bullet in each ML-relevant role is the pipeline/eval/latency one (already true at Capital One and Amazon Leo) and keep those bullets the cleanest-reading on the page.
- **recruiter_v2** (sev 3): The top entry (AWS) is a single bullet about Redshift capacity planning, which is not ML work; the strongest LLM/ML-infrastructure evidence (Capital One Claude bullets, Amazon Leo LLM-as-judge and Bedrock pipeline) sits second and third.. *Direction:* Keep chronological order, but make sure the Capital One and Amazon Leo bullets lead with the LLM/ML purpose so the eye picks it up on the second entry.
- **skeptic_v2** (sev 3): Skills list technologies that appear in no bullet: OpenSearch, CloudWatch, X-Ray, Docker, uv. The project header also lists 'Linux perf', but the bullet makes no performance claim.. *Direction:* Trim unevidenced items, or make sure he has a one-sentence story ready for each. Consider dropping 'Linux perf' from the project header.
- **recruiter_v2** (sev 2): Noticeable empty space at the bottom of the page while some bullets run two dense lines.. *Direction:* Slightly increase section spacing or use the room to loosen the densest bullets rather than adding content.
- **skeptic_v2** (sev 2): The bold on '90%' (a developer-preference survey) gives it the same visual weight as the engineering results 65%, 34% and 50.9M.. *Direction:* Consider removing bold from the 90%.
- **ml_infra_v2** (sev 1): 'Open3D' is listed under AI/ML skills alongside LLMs and RAG; it is a 3D point-cloud/geometry library.. *Direction:* Move Open3D to Engineering or drop it from Skills (it already appears in the UMIACS bullet).
- **ml_infra_v2** (sev 1): About a tenth of the page is empty below the Certification line while several bullets wrap tightly.. *Direction:* Use the slack for clarity rather than new content.
