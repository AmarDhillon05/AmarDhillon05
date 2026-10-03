# Loop 2 · infra_distributed · round 01 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.33 | 7 |
| quantification | 7.33 | 7 |
| technical_depth | 8.0 | 7 |
| concision_readability | 7.33 | 7 |
| skim_test | 7.33 | 7 |
| credibility | 7.67 | 7 |
| ats_parseability | 8.33 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 7.0 | 6 |
| human_voice | 7.33 | 6 |
| plain_language | 6.67 | 6 |
| overall | 7.67 | 7 |

**Plain-English restatement (recruiter):** 11/12 bullets understood
**Competitive:** {'infra_v2': 'Y', 'recruiter_v2': 'Y', 'skeptic_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "AWS SDE intern (Redshift capacity planning, Redmond) - the current role",
  "Capital One SWE intern - cut AI workflow generation time 65%",
  "IEX order book / matching engine in C++ - 50.9M real exchange messages, 1.26M events/sec"
 ],
 "engineer_type": "Backend / cloud engineer who does a lot of AWS work, with a performance-heavy C++ side project; reads as infra-leaning rather than front-end",
 "memorable_numbers": [
  "65%",
  "90% of developers preferred it",
  "34% latency cut",
  "30% setup time",
  "50.9M messages",
  "12.8x",
  "1.26M events/sec"
 ],
 "confusing": [
  "What 'Amazon Leo' is and why a UMD contracting group has Amazon as a client",
  "What a 'Claude skill' / 'sub-skills' are at Capital One",
  "B+ tree vs LSM-tree line - I could not tell what it means for the reader"
 ],
 "skipped": [
  "Technical Skills block (too long to read in a skim)",
  "Second and third Amazon Leo bullets",
  "UMIACS and TerpLabs bullets beyond the titles"
 ],
 "interview_questions": [
  "What does the Redshift capacity planning work actually decide, and who uses it?",
  "Walk me through how you made the Capital One AI workflow tool faster.",
  "How did you check your order book matched the real exchange?",
  "How do you split time between the AWS internship and the ongoing roles?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Implemented B+ tree and LSM-tree backends for the event log and benchmarked them on identical 2M-record workloads, where the B+ tree gave 12.8x the read throughput and 22x faster range queries at the cost of 27% more disk space
- **infra_v2** (sev 4): The comparison only reports the read side. An event log is append-heavy, and write throughput is the reason anyone picks an LSM tree, so leaving out writes makes the tradeoff look one-sided. '12.8x' and '22x' also use different precision.. *Direction:* If write results exist, state both sides of the tradeoff in one clause and name which backend was chosen and why. Use the same precision for both multipliers.
- **recruiter_v2** (sev 7): Three unexplained terms in a row ('B+ tree', 'LSM-tree', 'range queries') and no statement of what he decided or why the comparison mattered. I can repeat the numbers but not the point.. *Direction:* Lead with the purpose ('compared two storage designs for the engine's event log') and end with the choice or takeaway; keep the 12.8x as the single headline number and consider cutting one of the three figures.
- **skeptic_v2** (sev 5): The comparison reports only read-side wins for the B+ tree. An LSM tree's main advantage is write throughput, which is missing, so the benchmark looks one-sided. 'The event log' is never introduced, so the reader doesn't know why a matching engine needs a storage backend.. *Direction:* If write numbers exist, state the tradeoff both ways instead of only the read side. Otherwise frame it as the read-path choice for this workload, and say in a few words what the event log is for.

### PRIORITY · 3 evaluators · max sev 6
> Building capacity planning for Amazon Redshift maintenance like patching: Java logic that sets upper and lower bounds on reserved EC2 capacity to balance availability against cost, validated by backtesting
- **infra_v2** (sev 5): This is the most on-target infra bullet on the page (capacity vs. availability vs. cost), but the mechanism is hidden. 'Java logic that sets upper and lower bounds' does not say what the bounds are computed from, and 'maintenance like patching' reads as a loose aside. ('Building' as an in-progress verb is fine.). *Direction:* Swap 'Java logic' for the input the bounds come from, and turn 'maintenance like patching' into a plain clause about why capacity is reserved (e.g. 'reserved EC2 capacity held for Redshift patching windows'). Leave the language to the Skills section.
- **recruiter_v2** (sev 4): The colon splits the bullet into a heading plus a noun phrase ('Java logic that sets...'), so the second half has no verb; 'maintenance like patching' also reads awkwardly.. *Direction:* Make it one sentence with a verb throughout, e.g. 'Building Java logic that decides how much EC2 capacity to reserve during Redshift maintenance such as patching, balancing availability against cost and validating it by backtesting.'
- **skeptic_v2** (sev 6): Colon-stitched fragment. After the colon, 'Java logic that sets upper and lower bounds' has no verb tied to the candidate, so nobody would say it out loud. 'Building capacity planning' also reads as if the intern owns all of Redshift maintenance capacity planning, and 'maintenance like patching' is clumsy.. *Direction:* Make it one sentence with the candidate as the subject of each verb, and name the component they own before the language. Example shape: 'Writing the Java logic that sets upper and lower bounds on the reserved EC2 capacity Redshift holds for maintenance such as patching, trading availability against cost, and validating it by backtesting'

### PRIORITY · 3 evaluators · max sev 6
> Because the 270K+ row PostgreSQL workflow table had strict access limits, precomputed popular workflows into a category tree that the Claude skill searches first, with Redis caching full workflows to cut database queries
- **infra_v2** (sev 4): Opening with 'Because' delays the action. 'strict access limits' is ambiguous: rate/query limits, permissions, or connection quotas each imply a different design. This is a good read-path / caching-tier story, but it ends on 'to cut database queries' with no stated outcome.. *Direction:* Lead with the verb and name the constraint precisely, e.g. 'Precomputed popular workflows into a category tree the Claude skill searches first, with Redis caching full workflows, to stay under the 270K+ row PostgreSQL table's [specific limit]'.
- **recruiter_v2** (sev 3): Starts with a 'Because...' clause so the action verb ('precomputed') is hidden mid-line, and the bullet ends on intent ('to cut database queries') with no outcome.. *Direction:* Put the verb first: 'Precomputed popular workflows into a category tree ... because the 270K+ row PostgreSQL table had strict access limits, and cached full workflows in Redis to cut database queries.'
- **skeptic_v2** (sev 6): 'Strict access limits' is ambiguous: rate limits, permissions, or query quotas? 'Category tree' is unexplained. Opening with 'Because' delays the action, and the bullet drops its subject ('...limits, precomputed'), which reads as telegraphic. 'With Redis caching full workflows' is a second mechanism bolted on.. *Direction:* Lead with the verb and the subject ('I precomputed...'), name what the limit was in a few words, and say what the tree is keyed on before naming the stores.

### PRIORITY · 3 evaluators · max sev 5
> Cut AI workflow generation time 65% to under 15s by replacing a Claude skill’s open-ended search with focused sub-skills that call Python tools for workflow search and validation, guided by CloudWatch and OpenSearch latency logs
- **infra_v2** (sev 5): 'Workflow' isn't defined until the third Capital One bullet ('test-data workflows'), so here 'AI workflow generation' and 'workflow search' are opaque. 'Claude skill' and 'sub-skills' are LLM-tooling jargon an infra screener may not know.. *Direction:* Say 'test-data workflow' at first mention, and move the latency-log diagnosis earlier so the bullet reads measure → change → result, e.g. 'Used CloudWatch and OpenSearch latency logs to find where test-data workflow generation stalled, then split a Claude skill's open-ended search into focused sub-skills..., cutting generation time 65% to under 15s'.
- **recruiter_v2** (sev 4): 'Claude skill' and 'sub-skills' are unfamiliar product terms to a non-engineer, and 'workflow' appears three times in this bullet and four more times in the next, so the Capital One section blurs together.. *Direction:* Name what the workflows are once, early, and replace 'sub-skills' with plainer wording such as 'smaller, focused steps'; trim the trailing 'guided by...' clause if space is needed.
- **skeptic_v2** (sev 5): 'AI workflow generation' is never defined, so a reader can't tell what is generated or for whom. The bullet stacks three clauses: the cut, the replacement, then 'guided by CloudWatch and OpenSearch latency logs' tacked on at the end. 'Sub-skills' and 'Claude skill' are vendor-specific terms most infra readers won't parse.. *Direction:* Say what a workflow is in plain words first. Move the profiling step ahead of the fix so the bullet reads diagnose then change then result, and drop 'OpenSearch' unless it explains the engineering.

### PRIORITY · 2 evaluators · max sev 5
> Built Redis caching in front of the Prisma ORM queries for Tortuga, the studio’s class scheduler with 20,000+ visits in its first 30 days, to reduce database load and latency
- **infra_v2** (sev 4): The only number (20,000+ visits) describes the product's traffic, not the cache's effect. 'to reduce database load and latency' states intent, not a result, so readers may wrongly attribute the number to the caching work.. *Direction:* Frame the traffic number explicitly as the load the cache had to absorb ('to absorb 20,000+ visits in its first 30 days'), or state the measured effect if there is one. Otherwise keep the intent wording but put the traffic before the caching so cause and context read in order.
- **skeptic_v2** (sev 5): The only number (20,000+ visits) measures product traffic, not the cache, and the bullet ends at intent ('to reduce database load and latency'). 'The studio's' is unexplained (is TerpLabs a studio?). Redis caching to cut DB queries already appears in the Capital One bullet, so this repeats the same idea.. *Direction:* Separate the product scale from the change: say what Tortuga is and its traffic, then what the candidate built. If no effect of the cache was measured, phrase it as the design (what is cached and why) rather than as a result.

### PRIORITY · 2 evaluators · max sev 5
> Automated retraining for a production Amazon Bedrock classifier that rates research documents by importance: on an EventBridge schedule a larger LLM grades its ratings, and fine-tuning runs only when the grades shift past a threshold
- **recruiter_v2** (sev 3): Colon-joined two-part structure plus 'EventBridge', 'LLM' and 'fine-tuning' make the second half dense; it is the hardest Amazon Leo bullet to read aloud.. *Direction:* Lead with the idea: 'Set up a production Bedrock document classifier to retrain only when needed: a larger LLM grades its ratings on a schedule, and fine-tuning runs when the grades drift past a threshold.'
- **skeptic_v2** (sev 5): 'Production Amazon Bedrock classifier' is a four-word noun stack. The colon stitches two sentences together, and 'grades its ratings' / 'grades shift' is circular wording (ratings, grades, threshold) that takes two reads.. *Direction:* Split the colon into a plain sentence order: what runs on the schedule, what it checks, and what happens when the check fails. Example shape: 'Automated retraining for a production document-importance classifier on Bedrock: a scheduled job has a larger LLM re-grade a sample of its ratings and starts fine-tuning only when agreement drops past a threshold'

### PRIORITY · 2 evaluators · max sev 3
> Cut end-to-end latency 34% on a data pipeline that sends 6,000+ scraped research documents to model inference by streaming them through Amazon Kinesis into AWS Lambda instead of staging each step in S3
- **infra_v2** (sev 3): Strong mechanism + result (batch-staging in S3 replaced with Kinesis streaming), but 'end-to-end latency' has no unit. Per-document latency and total time to process the 6,000+ corpus are different claims.. *Direction:* Add the unit to the latency noun ('per-document latency' or 'time to process the full batch'). Keep the rest; it's one of the best infra bullets on the page.
- **recruiter_v2** (sev 2): 'model inference' and 'staging each step in S3' are jargon a recruiter has to guess at, though the before/after structure is good.. *Direction:* Optional: 'to an AI model' instead of 'to model inference'.

### 1 evaluators · max sev 4
> Rebuilt the legacy tool developers use to create test-data workflows as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation, and 90% of 30+ surveyed developers preferred it
- **skeptic_v2** (sev 4): Tech dump: React, TypeScript, Electron, React Flow, and Jest in one clause, with React named twice. 'Preferred it' doesn't say over what (presumably the legacy tool). This is frontend work and takes a full slot on an infra-targeted page.. *Direction:* Cut the stack to the one or two technologies that explain the design (Electron app, visual editor) and leave the rest to Skills. For this target, consider shortening this bullet or ordering it last within the role.

### 1 evaluators · max sev 4
> Deployed a space-topic research tool for Amazon Leo’s public-policy team and set it up for handoff with AWS CDK infrastructure-as-code and GitHub Actions CI/CD, so Leo engineers new to the project now maintain it on AWS Fargate
- **skeptic_v2** (sev 4): 'Space-topic research tool' is a noun stack nobody says out loud. The bullet also chains three tools across two clauses, and 'AWS Fargate' lands at the very end, where it reads as a keyword rather than a design choice.. *Direction:* Rephrase 'space-topic research tool' as 'a tool that researches space-policy topics' (or similar, without adding facts). Put the handoff outcome next to the CDK/CI mechanism and name Fargate where the deployment target is introduced.

### 1 evaluators · max sev 4
> Cut research-environment setup time 30% by pinning dependencies with uv and packaging the environment in Docker so every machine gets an identical setup
- **skeptic_v2** (sev 4): This is the only bullet under a 'Machine Learning Research Intern' title, and it describes environment tooling, not research. The causal link is also loose: pinning and containerizing mainly buy reproducibility, so 'setup time 30%' invites 'what part got faster?'. *Direction:* Lead with the reproducibility outcome ('every machine gets an identical setup'), which is the real mechanism, and keep the 30% as the secondary result. That framing also fits a platform/dev-tooling target.

### 1 evaluators · max sev 3
> Sustained 1.26M events/sec end-to-end over the full replay, keeping each price level’s orders in a std::list FIFO inside a std::map and a hash map from order ID to list iterator for O(1) cancels
- **infra_v2** (sev 3): It's the headline throughput number, but it comes third in the project, and it doesn't say whether it's single-threaded or on what hardware. The data-structure clause is good but dense ('std::list FIFO inside a std::map and a hash map from order ID to list iterator').. *Direction:* Move this bullet up to second in the project (right after correctness), and add the threading context in a few words. Optionally split the data-structure clause with 'with' so it reads as two steps.

## Page-level
- **skeptic_v2** (sev 6): Little distributed-systems evidence. The strongest engineering on the page (IEX order book, storage backends) is single-process. Experience bullets mostly describe AWS service wiring (Kinesis to Lambda, CDK, EventBridge) and LLM tooling, with no failure handling, scaling limits, consistency, retries, or monitoring/alerting ownership.. *Direction:* Without adding facts, reorder and rephrase existing bullets to bring out the systems parts that are already there: the Kinesis streaming change, the CDK/CI handoff, the capacity bounds, and the precompute/cache constraint. Shorten or move down the frontend and prompt-structure details.
- **infra_v2** (sev 5): The deepest infra and performance evidence (B+ tree vs. LSM benchmark, 1.26M events/sec, 50.9M-message replay) sits at the bottom of the page under Projects. Meanwhile the first two Capital One bullets lead with Claude-skill/LLM tooling.. *Direction:* Within Capital One, consider leading with the bullet whose mechanism is most infra-shaped (the latency-log diagnosis or the precompute + Redis tier) and phrasing the LLM part as the workload, not the headline. Keep Projects where it is but make sure its throughput bullet is near the top of the project.
- **recruiter_v2** (sev 5): The 'UMD App Development Contracting (Client: Amazon Leo)' header is confusing on a skim: I couldn't tell whether this is Amazon employment, a student club, or a consulting job, and 'Amazon Leo' is not a name most recruiters know.. *Direction:* Clarify the relationship in the header or title line (e.g. 'student contracting team' or a short descriptor of Amazon Leo) without adding new claims.
- **skeptic_v2** (sev 4): The page leans on colon and 'Because...' constructions and long three-clause sentences (the AWS bullet, the Bedrock bullet, Capital One bullet 2), which push several bullets to the full two lines with dense middles.. *Direction:* Rewrite the stitched bullets as subject-verb-object sentences, one mechanism per bullet, and cut trailing tool names that don't explain the design.
- **infra_v2** (sev 3): Infra evidence across the experience is mostly mechanism-only, with no result, in the AWS and TerpLabs entries and the Capital One caching bullet. The concrete mechanism + result pairs (Kinesis 34%, Capital One 65%, the IEX numbers) are spread across different sections.. *Direction:* Lead with the result-bearing bullet within each role where possible (UMD Contracting already does this well). No new metrics needed.
- **recruiter_v2** (sev 3): Bold is used only on Capital One, the Amazon Leo first bullet, UMIACS and the IEX project numbers; the AWS role (top of page) and its bullet have no bold anchor, so the eye jumps past the biggest brand to '65%'.. *Direction:* Acceptable as is since the AWS role has no metric; if desired, reorder nothing but make sure the AWS line reads cleanly as one sentence (see bullet feedback).
- **skeptic_v2** (sev 3): The Skills section lists technologies that never appear in a bullet: X-Ray, API Gateway, SNS, SQLAlchemy, Node.js, psutil. It also lists 'data structures and algorithms' and 'B+ tree and LSM-tree storage' as skills.. *Direction:* Keep only items the candidate can defend in an interview. Drop 'data structures and algorithms' and let the IEX project carry the B+ tree/LSM claim instead of listing it as a skill.
- **skeptic_v2** (sev 3): Vendor-specific jargon ('Claude skill', 'sub-skills', 'Amazon Leo') appears without a gloss.. *Direction:* Use a plain-language description the first time each term appears, e.g. describe the Claude skill by what it does, and keep the product names secondary.
- **infra_v2** (sev 2): About 10% of the page is empty at the bottom below Certification, while several bullets are compressed to fit two lines.. *Direction:* Use the spare vertical space for slightly more breathing room between sections, or for the clarifications above, rather than new content.
- **recruiter_v2** (sev 2): The Technical Skills section is five dense lines with nested parentheses (e.g. 'AWS (EC2, Lambda, Kinesis, Fargate/ECS, API Gateway, EventBridge, SNS), observability (CloudWatch, X-Ray)').. *Direction:* Fine for ATS; optionally trim items that appear nowhere else (psutil, SQLAlchemy) to shorten the block.
