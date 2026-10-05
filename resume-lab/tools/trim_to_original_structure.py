"""Rewrite bullets of a resume .tex by fact id (source: the loop-1 round-01 resume).

usage: trim_to_original_structure.py <in.tex> <out.tex> [--round01-fixes]
Default: Amar's original sentence structure, trimmed to the first-rewrite content, with the
details learned later (Oct 2026) added back in.
--round01-fixes: the raw first-rewrite wording with the same later details applied.
A value may be (new_fact_id, text) to retag a bullet, e.g. the IEX bullets now carry metrics.
"""
import re, sys
sys.path.insert(0, "tools")
from texparse import match_brace

IEX_HEADING = (r"\textbf{IEX Matching Engine Simulation} $|$ \textit{C++, STL, POSIX}", r"\textbf{IEX Order Book \& Matching Engine} $|$ \textit{C++17, STL, POSIX, Linux perf}")

NEW = {
"aws_sde.redshift": r"Researching and implementing Java-based capacity optimizations for Amazon Redshift, backtesting upper and lower bounds on the EC2 capacity reserved for patching to balance availability against cost",
"capital_one.ui_overhaul": r"Overhauled the legacy UI of a test data workflow creator using React + Electron with TypeScript workflow validation backed by Jest testing and a React-Flow editor, preferred over the legacy tool by \textbf{90\%} of 30+ surveyed developers",
"capital_one.search_index": r"Engineered a precomputed tree-style workflow search index as the Claude skill's main search tool, distilling popular workflows from a \textbf{270K+ row} PostgreSQL table with Python + SQLAlchemy and Redis caching to stay within database permission and rate limits",
"capital_one.claude_skill": r"Developed a Claude skill for workflow generation using sub-skill decomposition and Python functions for workflow search and validation, guided by CloudWatch + OpenSearch latency logs, cutting generation time \textbf{65\%} to under 15 seconds",
"amazon_contract.leo_deploy": r"Deployed an Amazon Leo topic-scoring research utility that shows public-policy staff which space topics are popular, through Docker + AWS Fargate and GitHub Actions CI/CD with AWS CDK (TypeScript) production infrastructure",
"amazon_contract.kinesis_pipeline": r"Achieved a \textbf{34\%} end-to-end latency reduction on a pipeline routing 6,000+ scraped research documents for inference by replacing S3 staging hops with Kinesis streams feeding Lambda processors, with API Gateway fronting for app integration",
"amazon_contract.bedrock_finetune": r"Integrated production fine-tuning of an AWS Bedrock document-importance model through EventBridge cron triggers with an LLM-as-judge decision gate to avoid redundant retraining, with X-Ray tracing and SNS failure alerts",
"umiacs.phystwin": ("umiacs.phystwin", r"Developing VLM-based robot grasp selection for PhysTwin, a physics-based digital twin, with a PhD research team targeting ICLR"),
"umiacs.grasp_vlm": r"Built a Python pipeline linking AnyGrasp multi-camera grasp candidates to Open3D overlay views consumed by a Qwen3-VL-8B VLM, isolating scene components, and tuned its prompts to pick grasps that avoid hitting the table",
"umiacs.env_setup": r"Cut research-environment setup time \textbf{30\%} via uv dependency pinning and Docker, with psutil timing and memory monitoring and Pytest unit testing for identifying bottlenecks",
"terplabs.studio": r"Co-founded and scaled a \textbf{110+ member} campus product studio shipping 5 live products, organizing teams with Jira and GitHub through agile practices",
"terplabs.tortuga": r"Sustained \textbf{20,000+ visits} without crashing in the first 30 days of Tortuga, a class scheduler, through rewriting Prisma-based SQL queries with Redis query caching to take load off compute",
"terplabs.rag_meal": r"Building a RAG meal suggestion feature for the official UMD app using GPT-4o mini over ChromaDB + SentenceBERT vector search on scraped recipes, achieving \textbf{93\%} meal satisfaction on internal test users",
"iex.order_book": ("iex.replay_correctness", r"Implemented a C++17 order book and matching engine on historical IEX data, replaying \textbf{50.9M} real exchange messages with no resync and matching 99,122 of 99,123 fills and 100\% of top-of-book prices"),
"iex.lfu_storage": ("iex.throughput+iex.data_structures", r"Designed the order book with std::map price levels of FIFO queues and an order-ID hash map for O(1) cancels, sustaining \textbf{1.26M} events/sec end-to-end over the full replay"),
"iex.lsm_vs_btree": ("iex.storage_benchmark", r"Designed and benchmarked LSM-tree and B+ tree storage for simulation logs on identical 2M-record workloads, with the B+ tree giving \textbf{12.8x} read throughput and 22x faster range queries for 27\% more disk"),
}

ROUND01_FIXES = {
"aws_sde.redshift": r"Writing Java policies that set upper/lower bounds on the EC2 capacity Amazon Redshift reserves for patching, backtested to balance availability against cost",
"capital_one.ui_overhaul": r"Rebuilt the legacy UI of a test-data workflow builder in React, Electron, and TypeScript, adding Jest-tested workflow validation and a React-Flow editor; preferred by \textbf{90\%} of 30+ surveyed developers",
"capital_one.search_index": r"Built a precomputed tree-style workflow search index, the Claude skill's main search tool, distilling popular workflows from a \textbf{270K+ row} PostgreSQL table via Python/SQLAlchemy and Redis within DB permission and rate limits",
"amazon_contract.leo_deploy": r"Shipped an Amazon Leo topic-scoring research tool showing public-policy staff which space topics are popular, on Docker + AWS Fargate via GitHub Actions, with AWS CDK (TypeScript) production infrastructure",
"amazon_contract.kinesis_pipeline": r"Cut end-to-end latency \textbf{34\%} on a pipeline routing 6,000+ scraped research documents to inference by replacing S3 staging hops with Kinesis streams feeding Lambda, exposed to the app via API Gateway",
"amazon_contract.bedrock_finetune": r"Automated production fine-tuning of an AWS Bedrock document-importance model with EventBridge cron triggers and an LLM-as-judge gate that skips redundant retraining; added X-Ray tracing and SNS failure alerts",
"umiacs.phystwin": ("umiacs.phystwin", r"Developing VLM-based robot grasp selection for PhysTwin, a physics-based digital twin, with a PhD team targeting ICLR"),
"umiacs.grasp_vlm": r"Engineered a Python pipeline rendering AnyGrasp multi-camera grasp candidates as Open3D overlays for a Qwen3-VL-8B vision-language model, and tuned its prompts to pick grasps that avoid hitting the table",
"terplabs.studio": r"Co-founded and scaled a \textbf{110+ member} campus product studio shipping 5 live products, run as agile teams with Jira and GitHub",
"terplabs.tortuga": r"Developed Prisma-based SQL querying with Redis query caching for Tortuga, a class scheduler, taking load off compute so it handled \textbf{20,000+ visits} in its first 30 days without crashing",
"iex.order_book": ("iex.replay_correctness", r"Built a C++17 order book and matching engine that replayed \textbf{50.9M} real IEX messages with no resync, matching 99,122 of 99,123 fills and 100\% of top-of-book prices"),
"iex.lfu_storage": ("iex.throughput+iex.data_structures", r"Sustained \textbf{1.26M} events/sec end-to-end with std::map price levels of FIFO queues and an order-ID hash map for O(1) cancels"),
"iex.lsm_vs_btree": ("iex.storage_benchmark", r"Benchmarked B+ tree vs LSM-tree storage for simulation logs on identical 2M-record workloads; the B+ tree gave \textbf{12.8x} read throughput and 22x faster range queries for 27\% more disk"),
}

if len(sys.argv) > 3 and sys.argv[3] == "--round01-fixes":
    NEW = ROUND01_FIXES
src = open(sys.argv[1]).read().replace(*IEX_HEADING)
out = []; i = 0; done = set()
for m in re.finditer(r"%\s*fact:\s*(\S+)", src):
    fid = m.group(1)
    if fid not in NEW: continue
    val = NEW[fid]
    new_id, text = val if isinstance(val, tuple) else (fid, val)
    k = src.index(r"\resumeItem{", m.end()) + len(r"\resumeItem")
    j = match_brace(src, k)
    out.append(src[i:m.start()]); out.append(f"% fact: {new_id}")
    out.append(src[m.end():k + 1]); out.append(text); i = j; done.add(fid)
out.append(src[i:])
assert done == set(NEW), set(NEW) - done
open(sys.argv[2], "w").write("".join(out))
