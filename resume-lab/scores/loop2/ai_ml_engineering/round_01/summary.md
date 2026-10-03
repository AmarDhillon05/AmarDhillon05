# Loop 2 · ai_ml_engineering · round 01 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.0 | 7 |
| quantification | 6.67 | 6 |
| technical_depth | 7.67 | 7 |
| concision_readability | 7.33 | 7 |
| skim_test | 7.0 | 7 |
| credibility | 7.67 | 7 |
| ats_parseability | 8.0 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 7.0 | 7 |
| human_voice | 7.0 | 6 |
| plain_language | 6.67 | 6 |
| overall | 7.67 | 7 |

**Plain-English restatement (recruiter):** 10/11 bullets understood
**Competitive:** {'ml_infra_v2': 'Y', 'recruiter_v2': 'Y', 'skeptic_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "Amazon Web Services SDE Intern (Redmond), something about Redshift capacity planning in Java",
  "Capital One SWE Intern: made an LLM/Claude workflow tool 65% faster",
  "Side project: C++ stock-exchange order book that matched real IEX data almost perfectly (99,122 of 99,123)"
 ],
 "engineer_type": "Backend / cloud engineer who builds LLM-powered tools on AWS; lots of AWS service names, some ML, plus one low-level C++ project",
 "memorable_numbers": [
  "65% faster",
  "90% of developers preferred it",
  "34% latency",
  "93% satisfactory meals",
  "50.9M messages",
  "99,122 of 99,123",
  "20,000+ visits",
  "GPA 3.5"
 ],
 "confusing": [
  "What 'Amazon Leo' is and why a UMD student contracting group has Amazon as a client",
  "'Claude skill' / 'sub-skills' - not a term I know",
  "Four roles marked Present at the same time as a Redmond internship",
  "The robotics bullet: AnyGrasp, Open3D - could not tell what the result was"
 ],
 "skipped": [
  "Most of the Technical Skills block (read only the AI/ML line label)",
  "Second half of the long Capital One and Amazon Leo bullets",
  "Certification line",
  "TerpLabs Tortuga caching bullet"
 ],
 "interview_questions": [
  "Walk me through what the Capital One LLM tool does for developers and why it was slow before",
  "What is Amazon Leo and what was your role on that contract team?",
  "How did you decide when the classifier should retrain?",
  "What did the vision-language model do in the robotics project, and did it get better?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Because the 270K+ row PostgreSQL workflow table had strict access limits, precomputed popular workflows into a category tree that the Claude skill searches first, with Redis caching full workflows to cut database queries
- **ml_infra_v2** (sev 3): Opening with 'Because' delays the verb to the second clause, and 'strict access limits' is ambiguous (rate limits, permissions, query quotas?).. *Direction:* Lead with the action: 'Precomputed popular workflows into a category tree the Claude skill searches first ... because the 270K+ row table was [rate-limited/quota-limited]'.
- **recruiter_v2** (sev 7): Opens with a 20-word 'Because...' clause about table size and access limits, so the action ('precomputed popular workflows') arrives mid-line and the bullet ends on 'cut database queries' without telling me what the user of the tool gained.. *Direction:* Lead with what was built and for whom, then the constraint as a short reason; if it contributed to the 65% speedup, say so by merging or cross-referencing rather than adding a new number. e.g. 'Gave the Claude skill a fast first lookup: a precomputed category tree of popular workflows plus a Redis cache, since the 270K+ row PostgreSQL table had strict access limits'
- **skeptic_v2** (sev 4): The action arrives only after a long 'Because...' clause, and the sentence has no subject ('Because X, precomputed...'). 'strict access limits' is ambiguous: rate limits, query quotas, or permissions? 'category tree' and the 'with Redis caching...' tail are two separate designs stitched into one sentence.. *Direction:* Lead with the action and put the constraint after it, e.g. 'Precomputed popular workflows into a category tree the Claude skill searches first, because the 270K+ row PostgreSQL table had [kind of] limits, and cached full workflows in Redis'

### PRIORITY · 3 evaluators · max sev 6
> For a PhD-led robotics project aimed at ICLR, built a pipeline that overlays AnyGrasp's candidate grasps on camera images in Open3D for a vision-language model, then tuned prompts so the model picks the right grasp more often
- **ml_infra_v2** (sev 6): The bullet ends on 'tuned prompts so the model picks the right grasp more often'. That is a prompt-only outcome with no stated evaluation: 'more often' has no comparison set, no trial count, and no definition of 'right grasp'. For an ML infra reader this is exactly the pattern that reads as hype, and it is the only bullet on the page under a 'Machine Learning Research' title.. *Direction:* Put the weight on the pipeline design (turning 3D grasp candidates into a visual multiple-choice for the VLM). If an evaluation set or success rate exists, name it; if not, replace 'more often' with the concrete method used to compare prompt variants, or end at the pipeline.
- **recruiter_v2** (sev 5): Three unfamiliar names in a row ('AnyGrasp's candidate grasps', 'Open3D', 'vision-language model') before I know the goal, and the result 'more often' is unmeasured.. *Direction:* State the goal in plain words first (helping a vision-language model choose where a robot arm should grab an object), then the method; drop 'in Open3D' to Skills if space is needed.
- **skeptic_v2** (sev 5): 'picks the right grasp more often' is the only result, and it is unquantified and unanchored. 'tuned prompts' is the thinnest kind of ML contribution and sits next to 'ICLR', which raises expectations.. *Direction:* If a measured improvement exists, state it. If not, say how success was judged (e.g. on a held-out set of scenes) or soften 'aimed at ICLR' so the venue doesn't outrun the result.

### PRIORITY · 3 evaluators · max sev 5
> Built Redis caching in front of the Prisma ORM queries for Tortuga, the studio's class scheduler with 20,000+ visits in its first 30 days, to reduce database load and latency
- **ml_infra_v2** (sev 4): Ends on intent ('to reduce database load and latency') with no observed effect, and the 20,000+ visits number describes the product's traffic, not the caching work.. *Direction:* If a measured effect exists, end on it. If not, either name what was cached and why (which queries were hot) so the design choice carries the bullet, or cut it to give the RAG bullet more room.
- **recruiter_v2** (sev 3): 'the studio's' is unclear (TerpLabs is never called a studio), and 'to reduce database load and latency' is intent with no outcome; the 20,000+ number describes the app, not this work.. *Direction:* Introduce Tortuga first as the product ('Tortuga, TerpLabs' class scheduler with 20,000+ visits in its first 30 days'), then the caching; replace 'the studio's' with the company name.
- **skeptic_v2** (sev 5): The only number, 20,000+ visits, belongs to the product, not to the caching work, and the caching outcome is stated only as intent ('to reduce'). 'the studio' is undefined: the role header says TerpLabs, and the page never calls it a studio.. *Direction:* If Amar built Tortuga, lead with that and let the 20,000 visits be its result, with caching as the supporting detail. If he only added the cache, keep the traffic as context and say plainly that it was preventive. Replace 'the studio’s' with 'TerpLabs’'.

### PRIORITY · 3 evaluators · max sev 5
> Building capacity planning for Amazon Redshift maintenance like patching: Java logic that sets upper and lower bounds on reserved EC2 capacity to balance availability against cost, validated by backtesting
- **ml_infra_v2** (sev 3): 'Java logic' after the colon is a noun phrase that hides what the logic is based on (forecasting, historical usage, rules), and 'maintenance like patching' reads awkwardly.. *Direction:* Rephrase as a full sentence that names the technique: 'Building Java logic that sets upper and lower bounds on reserved EC2 capacity for Redshift maintenance (e.g. patching) from [input], balancing availability against cost; validating it by backtesting'.
- **recruiter_v2** (sev 4): The colon after 'patching' turns the second half into a noun phrase ('Java logic that sets...') rather than a sentence, and 'Building capacity planning' is vague as a verb phrase. It is the top bullet under the biggest brand but is the least AI/ML-related item on the page.. *Direction:* Rephrase as one sentence with a real verb ('Writing Java logic that sets...'); keep it short since it is a 2-month-in role. Ordering is chronological so leave it, but keep it to one tight line-and-a-half.
- **skeptic_v2** (sev 5): The colon splits the bullet into a heading and a verbless fragment ('Java logic that sets...'), which nobody would say aloud. 'Building capacity planning' doesn't say whether he owns the whole capacity-planning effort or one component of it. 'maintenance like patching' reads as a typo for 'such as patching'.. *Direction:* Make it one sentence with a verb and a clear owner: what he is writing, what it decides, and why. Drop the colon. e.g. 'Writing the Java logic that sets upper and lower bounds on reserved EC2 capacity for Redshift maintenance such as patching, trading availability against cost, and checking it with backtests'

### PRIORITY · 3 evaluators · max sev 4
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **ml_infra_v2** (sev 4): '34%' has no absolute baseline, and '6,000+ scraped research documents' has no time unit (per day? per run? total corpus?).. *Direction:* Keep the mechanism (S3 staging hops replaced by Kinesis to Lambda), which is strong. Add the absolute latency and the time unit for the document count if known, e.g. 'from X to Y per document'.
- **recruiter_v2** (sev 3): 'S3 staging hops with Kinesis streams feeding Lambda' is three AWS service names in a row; a non-engineer only gets 'changed how data moves'. Fine for an engineer, but 'staging hops' is jargon.. *Direction:* Rephrase the method in plain words with the service names kept, e.g. 'by streaming documents through Kinesis to Lambda instead of writing each step to S3'.
- **skeptic_v2** (sev 4): '6,000+ scraped research documents' has no time unit: per day, per run, or total? The 34% has no absolute baseline (seconds? minutes?).. *Direction:* Add the existing unit or baseline only if it exists. Otherwise leave as is. The mechanism phrase is good.

### PRIORITY · 3 evaluators · max sev 4
> Deployed a space-topic research tool for Amazon Leo's public-policy team and set it up for handoff with AWS CDK infrastructure-as-code and GitHub Actions CI/CD, so Leo engineers new to the project now maintain it on AWS Fargate
- **ml_infra_v2** (sev 3): 'space-topic research tool' doesn't say what the tool does for the policy team, so the reader can't connect it to the classifier and pipeline bullets above.. *Direction:* Replace 'space-topic research tool' with a short functional description, and trim 'infrastructure-as-code' since CDK already implies it.
- **recruiter_v2** (sev 4): Five tooling names (AWS CDK, infrastructure-as-code, GitHub Actions, CI/CD, Fargate) carry most of the bullet; 'space-topic research tool' does not tell me what the tool does for the policy team.. *Direction:* Say what the tool does, then the handoff outcome; keep one or two infrastructure names and let Skills carry the rest.
- **skeptic_v2** (sev 4): 'space-topic research tool' is a noun stack that doesn't say what the tool does. The bullet then lists CDK, infrastructure-as-code, GitHub Actions, CI/CD and Fargate, so it reads mostly as deployment keywords. 'AWS Fargate' at the very end adds nothing to the handoff story.. *Direction:* Say in a few plain words what the tool does. Keep CDK and CI/CD as the reason the handoff worked, and cut or move 'on AWS Fargate'.

### PRIORITY · 2 evaluators · max sev 6
> Cut LLM workflow generation time 65% to under 15s by splitting one large Claude skill into smaller sub-skills that call Python tools for search and validation, and output quality held in repeated stress-test runs
- **ml_infra_v2** (sev 4): 'Claude skill' and 'sub-skills' are vendor-specific terms that many ML/platform readers and most recruiters won't recognize as an agent/tool-use decomposition. The link between splitting and speed (smaller context per call? fewer tokens? parallel calls?) is also left implicit.. *Direction:* Gloss 'Claude skill' once in plain words (e.g. 'one large Claude agent prompt (skill)'), and name the reason the split was faster in a short clause. The quality phrase can stay as is.
- **skeptic_v2** (sev 6): Three problems. (1) 'LLM workflow generation' is undefined here; the reader only learns in the third bullet that a 'workflow' is a test-data workflow. (2) The tail 'and output quality held in repeated stress-test runs' is a separate clause bolted on with 'and', with a new subject and no verb tying it to Amar. (3) The mechanism is unclear: the bullet never says why smaller sub-skills are faster (less context per call? parallel calls? fewer retries?).. *Direction:* Name the output in plain words before the tech. Give the cause of the speedup in a few words. Turn the quality tail into a subordinate phrase, e.g. '...without losing output quality across repeated stress tests'

### PRIORITY · 2 evaluators · max sev 4
> Automated retraining for a production Amazon Bedrock classifier that rates research documents by importance: on an EventBridge schedule a larger LLM grades its ratings, and fine-tuning runs only when the grades shift past a threshold
- **ml_infra_v2** (sev 4): This is the best ML infra evidence on the page (scheduled LLM-as-judge evaluation gating fine-tuning), but 'the grades shift past a threshold' doesn't say what the shift is measured against, and the bullet has no outcome.. *Direction:* Keep the structure. Swap 'the grades shift past a threshold' for the specific quantity being thresholded (e.g. 'agreement with the judge drops below a set level'), using only true details.
- **skeptic_v2** (sev 4): 'production Amazon Bedrock classifier that rates research documents by importance' is a long noun stack. Bedrock is a hosting service, not a model, so 'Bedrock classifier' invites the question 'what model is it?' The colon again splits the sentence into claim and explanation.. *Direction:* Split the noun stack into a sentence: say what the model does in plain words, then the trigger logic, with no colon. e.g. 'Automated retraining for a production LLM on Bedrock that rates research documents by importance, so a larger LLM grades its ratings on a schedule and fine-tuning runs only when those grades drift past a threshold'

### 1 evaluators · max sev 4
> Building a RAG meal-suggestion feature for the official UMD app, in which GPT-4o mini writes suggestions from scraped recipes found by SentenceBERT vector search in ChromaDB, and internal testers rated 93% of meals satisfactory
- **skeptic_v2** (sev 4): 'for the official UMD app' is a large scope claim, but 'Building' plus 'internal testers' suggests it hasn't shipped, and the bullet doesn't say so. The middle chains GPT-4o mini, SentenceBERT and ChromaDB in one clause ('in which...found by...in...'). The bolded 93% has no tester count.. *Direction:* State the status plainly (e.g. 'in internal testing'). Shorten the retrieval chain to one plain phrase, such as 'retrieves similar recipes with embeddings', and keep model names in Skills. Consider unbolding 93%.

### 1 evaluators · max sev 3
> Rebuilt the legacy tool developers use to create test-data workflows as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation, and 90% of 30+ surveyed developers preferred it
- **skeptic_v2** (sev 3): The middle is a tech run: React, TypeScript, Electron, React Flow and Jest, with React named twice. Only 'visual React Flow editor' explains a design choice. 'preferred it' leaves out the comparison (presumably over the legacy tool).. *Direction:* Keep 'visual editor' and the survey result. Move React/TypeScript/Electron/Jest to Skills or reduce them to one framing noun, e.g. '...as an Electron app with a visual drag-and-drop editor; 90% of 30+ surveyed developers preferred it to the old tool'

## Page-level
- **recruiter_v2** (sev 5): The AI/ML story is spread across five roles and starts with a non-ML AWS capacity bullet; there is no single place where 'LLM applications / ML infrastructure engineer' jumps out in the first 7 seconds.. *Direction:* Keep chronological order but make the first bullet of each role its most AI-relevant one; within the Amazon Leo role the retraining bullet is already first, which is good.
- **skeptic_v2** (sev 5): The 'ML infrastructure' half of the intended profile rests on one bullet (judge-triggered retraining on Bedrock). The rest of the AI/ML evidence is LLM-API orchestration: Claude sub-skills, prompt tuning, and RAG with GPT-4o mini.. *Direction:* Bring forward the ML-infrastructure parts that already exist: the retraining trigger, the Kinesis inference pipeline, and the judge-based evaluation. Describe them as infrastructure decisions rather than LLM features.
- **ml_infra_v2** (sev 4): The strongest ML infra evidence (evaluation-gated retraining, Kinesis latency cut) sits in the third role, under a non-ML-sounding company heading 'UMD App Development Contracting'. The two roles above it open with capacity planning and an LLM-latency bullet.. *Direction:* Keep chronological order, but make sure the '(Client: Amazon Leo)' heading line and the retraining bullet are what the eye lands on: the retraining bullet is already first in its role. Consider tightening the AWS and Capital One bullets so that section starts higher on the page.
- **ml_infra_v2** (sev 4): Across the AI bullets, evaluation is mostly qualitative ('output quality held', 'picks the right grasp more often', '93% satisfactory'). Mechanisms are well named, but only the Bedrock bullet describes an evaluation loop, and none states an eval set or baseline.. *Direction:* Without inventing metrics, describe the evaluation mechanism that existed (who or what judged, what it was compared against) in the bullets where it's known, starting with UMIACS and the Bedrock gate.
- **recruiter_v2** (sev 4): 'Amazon Leo' and 'UMD App Development Contracting' are unexplained; a recruiter may not know Amazon Leo is an Amazon program, so the client brand does not land.. *Direction:* Clarify in a few words what Amazon Leo is (e.g. a parenthetical on first mention) without adding new scope.
- **skeptic_v2** (sev 4): The Skills section carries terms the bullets don't support: 'model fine-tuning' (only via Bedrock), 'OpenSearch', 'CloudWatch, X-Ray', 'Docker', 'uv', plus generic filler such as 'data structures and algorithms' and 'object-oriented design'. 'Open3D' sits under AI/ML.. *Direction:* Cut the generic items ('data structures and algorithms', 'object-oriented design'). Keep only the unsupported tools he can discuss in depth, and move Open3D out of AI/ML.
- **skeptic_v2** (sev 4): 'UMD App Development Contracting (Client: Amazon Leo)' doesn't say what kind of organization this is (student club, university program, or his own contracting), so ownership and employer are ambiguous.. *Direction:* Clarify the organization type in the header in a few words, without adding scope.
- **skeptic_v2** (sev 4): Three bullets use the colon/'Because' construction or stitch a second clause on with ', and' (AWS, the first Capital One bullet, Bedrock retraining, TerpLabs RAG). Read in a row, the pattern sounds generated rather than spoken.. *Direction:* Rewrite each as one subject-verb-object sentence with the result in a trailing clause. Avoid colons inside bullets.
- **recruiter_v2** (sev 3): Several bullets use stacked tech names as the main content ('React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation'; 'AWS CDK infrastructure-as-code and GitHub Actions CI/CD').. *Direction:* Keep the one tool that explains the design choice in each bullet and leave the rest to Skills.
- **skeptic_v2** (sev 3): 'Claude skill' / 'sub-skills' is product-specific jargon that many recruiters and engineers outside Anthropic's ecosystem won't recognize.. *Direction:* On first use, add a two- or three-word gloss (e.g. 'Claude skill (agent instructions plus tools)'), or describe it as an LLM agent with tools.
- **ml_infra_v2** (sev 2): Skills 'AI/ML' line mixes in 'Open3D' (a 3D geometry library) and 'prompt engineering', and uses 'Claude skills' as a skill term.. *Direction:* Move Open3D out of the AI/ML line; consider dropping 'prompt engineering' since the bullets already show it in context.
- **recruiter_v2** (sev 2): Bold is used only on numbers (65%, 90%, 34%, 93%, 50.9M) but not on the IEX 99,122 of 99,123 result, which is the most memorable number on the page.. *Direction:* Consider moving the bold from '50.9M' to '99,122 of 99,123 fills'.
