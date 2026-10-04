# Loop 2 · base · round 05 (3 evaluators)

| dim | mean | min |
|---|---|---|
| impact_clarity | 7.33 | 7 |
| quantification | 7.67 | 7 |
| technical_depth | 8.0 | 8 |
| concision_readability | 7.33 | 7 |
| skim_test | 7.67 | 7 |
| credibility | 7.33 | 7 |
| ats_parseability | 8.67 | 8 |
| visual_layout | 8.0 | 8 |
| domain_fit | 8.0 | 8 |
| human_voice | 7.33 | 7 |
| plain_language | 6.33 | 6 |
| overall | 8.0 | 8 |

**Plain-English restatement (recruiter):** 11/14 bullets understood
**Competitive:** {'general_backend_v2': 'Y', 'recruiter_v2': 'Y', 'skeptic_v2': 'Y'}

## Memory skim (recruiter)
```
{
 "strongest_3": [
  "Amazon Web Services SDE Intern (Fall 2026) - something about EC2 capacity for Redshift",
  "Capital One Software Engineering Intern (Summer 2026) - rebuilt a developer tool, made an AI workflow tool faster",
  "C++ order book / matching engine project replaying real IEX exchange data at over a million events per second"
 ],
 "engineer_type": "Backend / cloud engineer who also does a lot of AI/LLM tooling; has a performance-heavy C++ side project. Reads as a strong generalist with two big-name internships already.",
 "memorable_numbers": [
  "90% of developers preferred it",
  "65% faster",
  "34% latency reduction",
  "50.9M messages",
  "12.8x",
  "1.26M events/sec",
  "110+ member studio",
  "93% satisfactory"
 ],
 "confusing": [
  "What 'Amazon Leo' is and whether this is a real Amazon job or a student contract",
  "The Capital One bullet with the category tree and Redis - couldn't tell what it achieved",
  "The robotics research bullet (AnyGrasp, Open3D) - no idea what was actually built",
  "B+ tree vs LSM-tree line"
 ],
 "skipped": [
  "Most of the Technical Skills section beyond the first two lines",
  "Second half of most Capital One and Amazon Leo bullets",
  "Certification line"
 ],
 "interview_questions": [
  "What exactly are you building at AWS and how far along is it?",
  "What did the 'Claude skill' at Capital One do, and how did you get it 65% faster?",
  "Is the Amazon Leo work in production or still in dev?",
  "How did you verify the order book matched the real exchange?"
 ]
}
```

## Bullet issues (priority = ≥2 evaluators or severity ≥8)

### PRIORITY · 3 evaluators · max sev 7
> Precomputed popular workflows from a 270K+ row PostgreSQL table into a category tree that the Claude skill searches first, with Redis caching full workflows, so lookups rarely touch a database gated by permissions and rate limits
- **general_backend_v2** (sev 4): 'a category tree that the Claude skill searches first' doesn't say what the tree is keyed on or what a lookup is. 'with Redis caching full workflows' is attached without a verb, so the bullet reads as two mechanisms joined by a comma.. *Direction:* Lay out the read path in order, with a verb for each step: tree to find the workflow, Redis to fetch it, database only on a miss. Don't add a hit rate unless one exists.
- **recruiter_v2** (sev 7): Four mechanisms in one sentence (precompute, category tree, Redis cache, gated database) and the payoff is only 'rarely touch a database'. 'Category tree that the Claude skill searches first' and 'database gated by permissions and rate limits' are not restatable by a non-engineer.. *Direction:* Lead with the problem the gated database caused, then the fix in one clause (pre-sorted popular workflows + cache); drop one of the two mechanisms from the sentence or merge this into the 65% bullet if it was part of the same speedup.
- **skeptic_v2** (sev 3): 'with Redis caching full workflows' is an absolute phrase stitched into the middle of the sentence, so the bullet reads as two designs joined together. 'Rarely' is the only outcome word and has no measurement behind it.. *Direction:* Write the two layers as a sequence with their own verbs: the tree answers which workflow, and Redis holds the full workflow body. Keep the closing 'gated by permissions and rate limits' clause.

### PRIORITY · 3 evaluators · max sev 5
> Co-built a research tool that scores and aggregates topics so Amazon Leo’s public-policy staff can see what’s popular, running in dev on AWS Fargate with GitHub Actions CI/CD and AWS CDK infrastructure-as-code ready for production
- **general_backend_v2** (sev 4): The second half is a chain of four technologies ('AWS Fargate with GitHub Actions CI/CD and AWS CDK infrastructure-as-code'), and the first half's 'scores and aggregates topics' doesn't say what is scored or from what data.. *Direction:* Keep the dev/production scoping and one deployment noun that shows ownership (e.g. the CDK infrastructure). Use the freed space to say what the tool scores topics from.
- **recruiter_v2** (sev 5): 'Scores and aggregates topics' is vague (topics of what?), and the second half is a tech list (Fargate, GitHub Actions, CDK) ending in 'running in dev ... ready for production', which tells me it isn't live. 'Amazon Leo' is unexplained, and 'UMD App Development Contracting (Client: Amazon Leo)' makes me unsure whether this is Amazon work or a student club project.. *Direction:* Say what the topics come from in plain words, and move the deployment tech list to Skills or cut it to one clause; keep the honest 'in dev' scoping but put it in plain words.
- **skeptic_v2** (sev 5): 'scores and aggregates topics' leaves out what is scored and from what source. The second half is a deployment-stack list (Fargate, GitHub Actions CI/CD, AWS CDK infrastructure-as-code) that explains no engineering decision. 'Co-built' also leaves the candidate's own share unclear.. *Direction:* Keep the purpose clause ('so public-policy staff can see what's popular'), say what the tool reads, and cut the stack down to whatever the candidate personally set up, or move it to Skills. Honest status wording such as 'deployed to a dev environment' is fine to keep.

### PRIORITY · 3 evaluators · max sev 4
> Writing Java logic that sets the upper and lower bounds on EC2 capacity that Amazon Redshift reserves for operations like patching, balancing availability against cost, and backtesting it
- **general_backend_v2** (sev 4): The sentence ends on a trailing clause, 'and backtesting it', after a comma list ('like patching, balancing availability against cost'). On first read, 'balancing availability against cost' looks like a third item in the 'like patching' list, and 'it' could mean the logic or the bounds.. *Direction:* Put the verbs together and end the 'like patching' example cleanly before giving the goal. For example: 'Writing and backtesting Java logic that sets the upper and lower bounds on EC2 capacity Amazon Redshift reserves for operations like patching, to balance availability against cost'
- **recruiter_v2** (sev 3): 'and backtesting it' dangles at the end, and 'it' is ambiguous (the logic? the bounds?). The core idea is clear but the sentence is built in a way that makes me re-read.. *Direction:* Move the backtesting into the main verb chain, e.g. 'Writing and backtesting Java logic that ...'.
- **skeptic_v2** (sev 3): The participle 'balancing availability against cost' is ambiguous: it could describe the bounds or the candidate. 'and backtesting it' trails at the end, and 'it' could mean the logic or the capacity. The candidate's scope, whether they own the bounds logic or contribute to it, is also unstated.. *Direction:* Turn the trade-off into a purpose clause and make backtesting its own verb. Example shape: 'Writing Java logic that sets how much EC2 capacity Redshift reserves for maintenance such as patching, trading availability against cost, and backtesting it against past usage' (only if 'past usage' is accurate).

### PRIORITY · 3 evaluators · max sev 4
> Reduced end-to-end latency 34% for a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda
- **general_backend_v2** (sev 3): '6,000+ scraped research documents' has no time unit (total, per day, or per run), so the reader can't tell the pipeline's load.. *Direction:* Add the existing scope unit if one exists. Otherwise leave the bullet as it is, since the technique and result are clear.
- **recruiter_v2** (sev 3): 'routing ... to inference' and 'S3 staging hops with Kinesis streams feeding Lambda' are jargon; the result is clear but the how is not restatable.. *Direction:* Replace 'to inference' with 'to the AI model' and describe the change plainly before naming services ('streaming data straight between steps (Kinesis -> Lambda) instead of staging it in S3').
- **skeptic_v2** (sev 4): The bullet gives no absolute latency, so 34% has no baseline. '6,000+ documents' reads as a total corpus, which invites the question of why a stream is needed at batch scale. 'S3 staging hops' is jargon.. *Direction:* Say in plain words what the hops were (each stage wrote to S3 and the next stage read it back) and add the before and after latency if it is known.

### PRIORITY · 2 evaluators · max sev 7
> For a PhD-led robotics project aimed at ICLR, built a pipeline that overlays AnyGrasp's candidate grasps on camera images in Open3D for a vision-language model, then tuned prompts so it favors grasps that avoid hitting the table
- **recruiter_v2** (sev 7): 'AnyGrasp's candidate grasps', 'Open3D' and 'vision-language model' arrive before any plain statement of the goal (helping a robot choose how to pick things up). 'Aimed at ICLR' also invites the question of whether it was submitted or accepted.. *Direction:* Open with the plain goal ('helping a robot arm choose how to grab objects'), then what he built, then the tool names; state the paper status honestly (e.g. 'in preparation for ICLR') if that is accurate.
- **skeptic_v2** (sev 4): The bullet ends with no result or check: 'tuned prompts so it favors grasps that avoid hitting the table' has no evidence that it worked. 'overlays AnyGrasp's candidate grasps on camera images in Open3D for a vision-language model' packs three named components into one clause. 'Tuned prompts' is also the thinnest engineering on the page for a research role.. *Direction:* Describe the pipeline as a plain sequence (generate candidate grasps, draw them on the image, have a vision-language model pick one), and state how success was checked if that is known. Keep 'aimed at ICLR': it is honestly scoped.

### PRIORITY · 2 evaluators · max sev 7
> Implemented B+ tree and LSM-tree backends for the event log and benchmarked them on identical 2M-record workloads, where the B+ tree gave 12.8x the read throughput and 22x faster range queries at the cost of 27% more disk space
- **recruiter_v2** (sev 7): 'B+ tree and LSM-tree backends' and 'range queries' mean nothing to a non-engineer, and the bullet never says why the comparison mattered or what he chose. Three stacked numbers (12.8x, 22x, 27%) compete with each other.. *Direction:* Frame as a decision: 'compared two storage designs for the event log and chose X because ...', keep one headline number (12.8x reads), move the rest to interview material.
- **skeptic_v2** (sev 4): Write throughput, the LSM-tree's usual advantage, is missing for an append-heavy event log, so the comparison looks one-sided. The bullet also doesn't say which backend was chosen, or why an order book's event log needs reads and range queries at all.. *Direction:* Add the reason the event log is read, and complete the trade-off with the write side or name the chosen backend. Cut a number if needed to stay within two lines.

### PRIORITY · 2 evaluators · max sev 6
> Built Redis caching in front of the Prisma ORM queries for Tortuga, the studio’s class scheduler with 20,000+ visits in its first 30 days, to reduce database load and latency
- **general_backend_v2** (sev 4): The bullet ends on intent ('to reduce database load and latency') with no outcome. The 20,000+ visits number describes the product, not the caching work, so it reads as if it measures the change.. *Direction:* Make it clear that 20,000+ visits is the traffic the cache served, e.g. lead with the scheduler and its traffic, then the caching. Or say what the cache keys on so the bullet shows a decision rather than a goal.
- **skeptic_v2** (sev 6): The only number, 20,000+ visits, describes the app and not the cache, and the bullet ends on intent ('to reduce database load and latency') with no outcome. 20K visits a month is roughly 700 a day, which a single Postgres instance handles easily, so the reason for the cache is unclear.. *Direction:* Name the bottleneck the cache fixed before naming Redis and Prisma, and keep the visit count clearly attached to Tortuga rather than to the cache. If no result was measured, describe what gets cached and why it is safe to cache, instead of stating intent.

### PRIORITY · 2 evaluators · max sev 5
> Rebuilt the legacy tool developers use to create test-data workflows as a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation, and 90% of 30+ surveyed developers preferred it
- **general_backend_v2** (sev 5): This is the first Capital One bullet and it is the most frontend one in the role (React, TypeScript, Electron, React Flow), while the two backend bullets beneath it hold the role's stronger systems evidence.. *Direction:* Reorder within the role so the 65% generation-time bullet leads and this one comes last. The text can stay as it is.
- **skeptic_v2** (sev 4): 'a React and TypeScript Electron app with a visual React Flow editor and Jest-tested validation' stacks four technologies and a compound adjective into one phrase. 'Jest-tested validation' is a noun stack nobody says out loud. '90% of 30+' has an open-ended denominator, and 'preferred it' leaves the comparison implied. The bullet also doesn't say whether this was a solo rebuild.. *Direction:* Split purpose from stack: say what the visual editor lets developers do that the old tool didn't, and keep at most React Flow plus Electron in the bullet. Use an exact count, e.g. '27 of 30 surveyed developers preferred it over the old tool', only if those are the real figures.

### PRIORITY · 2 evaluators · max sev 5
> Cut AI workflow generation time 65% to under 15s by replacing a Claude skill's open-ended search with focused sub-skills that call Python tools for workflow search and validation, guided by CloudWatch and OpenSearch latency logs
- **recruiter_v2** (sev 4): Strong result up front, but 'Claude skill's open-ended search with focused sub-skills' is insider vocabulary, and 'guided by CloudWatch and OpenSearch latency logs' is a tech tail that adds length without adding meaning for me.. *Direction:* Rephrase 'Claude skill' as 'AI assistant' (or 'Claude-based assistant') and cut or shorten the latency-logs clause, e.g. '... after profiling showed where time was spent'.
- **skeptic_v2** (sev 5): 'Claude skill' and 'sub-skills' are niche product terms that most recruiters, and many engineers, won't know. The bullet doesn't say what an 'AI workflow' is (it refers back to the test-data workflows in the previous bullet, but never says so). The trailing 'guided by CloudWatch and OpenSearch latency logs' is a dangling modifier that reads as tool-name padding.. *Direction:* Lead with what the AI produces in plain terms, then the change: one broad search replaced by narrow steps that each call a Python tool. If the logs drove the redesign, say what they revealed; otherwise drop the tool names from the end.

### 1 evaluators · max sev 7
> Automated retraining for a production Amazon Bedrock classifier that rates research documents by importance: on an EventBridge schedule a larger LLM grades its ratings, and fine-tuning runs only when the grades shift past a threshold
- **skeptic_v2** (sev 7): Calls the classifier 'production' while the first bullet of the same role says the tool is 'running in dev ... ready for production'. A reader cannot tell what is actually live. The colon also splices a second sentence onto the first, and 'the grades shift past a threshold' doesn't say what shifts: agreement rate, average grade, or drift against a baseline.. *Direction:* Make the deployment status the same in both bullets, then rephrase the trigger as a plain cause and effect with no colon. Example shape: 'Automated retraining for the Bedrock classifier that rates documents by importance: a larger LLM regrades a sample of its ratings each week, and fine-tuning starts only when disagreement passes a threshold' (only if that is what actually happens).

### 1 evaluators · max sev 4
> Building a RAG meal-suggestion feature for the official UMD app, in which GPT-4o mini writes suggestions from scraped recipes found by SentenceBERT vector search in ChromaDB, and internal testers rated 93% of meals satisfactory
- **skeptic_v2** (sev 4): Five technical terms in one relative clause ('RAG ... GPT-4o mini ... scraped recipes found by SentenceBERT vector search in ChromaDB'). 'for the official UMD app' leaves ownership unclear: is TerpLabs contracted by the university, or is this a pitch?. *Direction:* Say the plain idea first ('suggests meals by retrieving similar scraped recipes and having an LLM write the suggestion') and keep at most one or two of the tool names.

### 1 evaluators · max sev 3
> Sustained 1.26M events/sec end-to-end over the full replay, keeping each price level's orders in a std::list FIFO inside a std::map and a hash map from order ID to list iterator for O(1) cancels
- **recruiter_v2** (sev 3): The second half ('std::list FIFO inside a std::map ... list iterator for O(1) cancels') is pure engineer detail; to me it reads as a string of nouns.. *Direction:* Keep the design detail (it is the technique an HM will ask about) but lead the clause with the plain reason, e.g. '... by designing order storage so cancels take constant time (std::list FIFO per price level ...)'.

### 1 evaluators · max sev 2
> Co-founded a 110+ member student product studio that has shipped 5 live products
- **skeptic_v2** (sev 2): This states organizational size, not the candidate's engineering, and doesn't say which of the 5 products they built.. *Direction:* Keep it short, as it is now. Optionally note that Tortuga is one of the 5 so the next bullet connects to it.

## Page-level
- **skeptic_v2** (sev 7): Within the Amazon Leo role, the deployment status contradicts itself: 'running in dev ... ready for production' in bullet 1 and 'a production Amazon Bedrock classifier' in bullet 3.. *Direction:* Choose the accurate status and use the same wording in both bullets.
- **general_backend_v2** (sev 5): The strongest systems evidence on the page, the C++ order book with B+ tree vs LSM backends, sits at the bottom under Projects, below a robotics bullet and a student-studio role.. *Direction:* Consider moving Projects above TerpLabs/UMIACS, or at least leading Capital One with its backend bullets, so the first third of the page shows the backend and performance story. Keep Experience brands at the top.
- **recruiter_v2** (sev 5): The intended 'systems-oriented' story is diluted: the page alternates between cloud pipelines, AI/LLM tooling (Claude skill, Bedrock, RAG, GPT-4o mini, VLM prompts), and the C++ engine, so on a skim it reads as a strong AI-tools/cloud generalist rather than a systems engineer.. *Direction:* Reorder within roles so the infrastructure/performance bullets come first, and consider whether the bold anchors (90%, 65%, 34%, 93%) are the wins that best support the systems story versus 50.9M/1.26M.
- **skeptic_v2** (sev 5): The strongest systems evidence, the IEX order book (50.9M messages, 99,122 of 99,123 fills, 1.26M events/sec), sits at the bottom of the page. The top half is dominated by LLM-orchestration work: Claude skill, Bedrock classifier, VLM prompt tuning, GPT-4o mini RAG.. *Direction:* Without adding facts, put the systems-heavy bullets first within each role (the Kinesis latency bullet before the 'Co-built a research tool' bullet, the Redis/category-tree bullet before or alongside the Claude-skill bullet), and consider tightening the UMIACS and RAG bullets so the order book gets more of the reader's attention.
- **recruiter_v2** (sev 4): Experience header 'UMD App Development Contracting (Client: Amazon Leo)' doesn't tell a recruiter whether this is a company, a university program, or a club.. *Direction:* clarify in the header or title what UMD App Development Contracting is (e.g. university-run contracting program) without adding new scope.
- **general_backend_v2** (sev 3): Jargon that only AI-tooling readers know: 'Claude skill', 'sub-skills', 'AnyGrasp', 'vision-language model', 'RAG'. These appear without a gloss across three roles.. *Direction:* Gloss 'Claude skill' once in plain words the first time it appears (e.g. 'the Claude-based workflow generator's'). Leave the rest.
- **recruiter_v2** (sev 3): Bold metrics are spread across 8 bullets, including softer ones ('90% of 30+ surveyed developers preferred it', '93% of meals satisfactory'), so bold no longer singles out the 2-3 headline wins.. *Direction:* Reserve bold for the 3-4 strongest, hardest numbers and un-bold the survey/preference ones.
- **general_backend_v2** (sev 2): Skills section filler: 'data structures and algorithms', 'Agile', 'Jira' take space without informing a backend reader. Backend items (REST APIs, PostgreSQL, Redis) are mixed with React/Electron under 'Backend & Full-Stack'.. *Direction:* Optionally drop the generic practice terms, or split frontend items onto their own line so the backend line reads as backend.
- **recruiter_v2** (sev 2): The Technical Skills section is six dense lines, partly repeating names already in bullets (Redis, PostgreSQL, Kinesis, Fargate, EventBridge).. *Direction:* Optional: trim duplicates if space is needed for clarifying words elsewhere.
- **skeptic_v2** (sev 2): Several Skills entries appear in no bullet and read as keywords: PyTorch, C, SQLAlchemy, API Gateway, Docker, Jira, Agile, and 'data structures and algorithms'.. *Direction:* Cut the generic practice items. Keep PyTorch and C only if the candidate can discuss real work with them.
- **skeptic_v2** (sev 2): The AWS role, the top brand on the page, has a single present-tense bullet with no result, which visually makes it the lightest entry.. *Direction:* Fix the grammar so the one bullet reads cleanly (see bullet feedback). No new claims are needed.
