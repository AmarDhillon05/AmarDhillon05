import re, sys
sys.path.insert(0, "tools")
from texparse import match_brace
NEW = {
"aws_sde.redshift": r"Researching and implementing Java-based utilization optimizations for Amazon Redshift",
"capital_one.ui_overhaul": r"Overhauled the legacy UI of a test data workflow creator using React + Electron with TypeScript workflow validation backed by Jest testing and a React-Flow editor, receiving \textbf{90\%} satisfaction compared to the legacy tool",
"capital_one.search_index": r"Engineered a precomputed tree-style workflow search index to minimize database queries under access constraints, distilling popular workflows from a \textbf{270K+ row} PostgreSQL table with Python + SQLAlchemy, backed by Redis caching",
"capital_one.claude_skill": r"Developed a Claude skill for workflow generation using sub-skill decomposition and Python functions for workflow search and validation, guided by CloudWatch + OpenSearch latency logs, cutting generation time \textbf{65\%} to under 15 seconds",
"amazon_contract.leo_deploy": r"Deployed an Amazon Leo space topic research utility adopted into Leo's ecosystem through Docker + AWS Fargate and GitHub Actions CI/CD, with AWS CDK (TypeScript) infrastructure so new engineers can contribute",
"amazon_contract.kinesis_pipeline": r"Achieved a \textbf{34\%} speedup on a pipeline routing 6,000+ scraped research documents for inference by implementing Kinesis streams feeding Lambda processors, with API Gateway fronting for app integration",
"amazon_contract.bedrock_finetune": r"Integrated automated fine-tuning of an AWS Bedrock source relevancy model through EventBridge cron triggers with decision gates to avoid redundant retraining, with X-Ray tracing and SNS failure alerts",
"umiacs.phystwin": r"Developing automated training for PhysTwin, a physics-based digital twin, with a PhD research team targeting an ICLR submission",
"umiacs.grasp_vlm": r"Built a Python pipeline linking AnyGrasp multi-camera grasp candidates to Open3D overlay views consumed by a Qwen3-VL-8B VLM, enabling researchers to isolate scene components",
"umiacs.env_setup": r"Cut research-environment setup time \textbf{30\%} via uv dependency pinning and Docker, with psutil timing and memory monitoring and Pytest unit testing for identifying bottlenecks",
"terplabs.studio": r"Co-founded and scaled a \textbf{110+ member} campus product studio shipping 5 live products, organizing teams through agile practices",
"terplabs.tortuga": r"Sustained \textbf{20,000+ visits} in the first 30 days of Tortuga, a class scheduler, through developing Prisma-based SQL querying with Redis query caching to reduce database load and latency",
"terplabs.rag_meal": r"Building a RAG meal suggestion feature for the official UMD app using GPT-4o mini over ChromaDB + SentenceBERT vector search on scraped recipes, achieving \textbf{93\%} meal satisfaction on internal test users",
"iex.order_book": r"Implemented a C++ order book simulation on historical IEX data, with a contract-based plug-and-play design for evaluating multiple approaches with enforced correctness",
"iex.lfu_storage": r"Wrote paginated hash-based storage for live order book data with in-memory LFU caching for frequently requested tickers, evaluated for drift against IEX's historical book data",
"iex.lsm_vs_btree": r"Designed and benchmarked a time-based adaptive LSM storage against B+ tree storage for simulation logs, testing throughput and latency via rdtscp timing and hardware utilization via Linux perf",
}
src = open(sys.argv[1]).read(); out = []; i = 0; done = set()
for m in re.finditer(r"%\s*fact:\s*(\S+)", src):
    fid = m.group(1)
    if fid not in NEW: continue
    k = src.index(r"\resumeItem{", m.end()) + len(r"\resumeItem")
    j = match_brace(src, k)
    out.append(src[i:k+1]); out.append(NEW[fid]); i = j; done.add(fid)
out.append(src[i:])
assert done == set(NEW), set(NEW) - done
open(sys.argv[2], "w").write("".join(out))
