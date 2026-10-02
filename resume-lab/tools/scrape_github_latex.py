#!/usr/bin/env python3
"""
scrape_github_latex.py -- build a structured corpus of public LaTeX resumes from GitHub.

Pipeline
--------
1. Inputs: a candidates file (one ``owner/repo [preferred/path.tex]`` per line, '#' comments allowed),
   explicit repo URLs on the command line, and/or a GitHub repository-search query
   (``--query``; uses the unauthenticated REST search endpoint, 10 req/min).
2. Each repo is shallow-cloned (``git clone --depth 50 --filter=blob:limit=2m --no-checkout``) into
   ``--workdir`` (default /tmp/claude-0/gh_corpus) -- never into this repo.
3. All ``.tex`` files at HEAD are scored as "resume-like" (Jake Gutierrez macros such as
   ``\\resumeSubheading``/``\\resumeItem``, or Experience/Education sections + itemize). ``\\input``/``\\include``
   files are inlined (recursively, within the repo). One resume is chosen per repo: the preferred path if
   given, otherwise the most recently modified resume-like file (ties -> shorter path / name contains
   "resume"). Last-modified date = ``git log -1 --format=%cI -- <file and its \\input files>`` (max).
4. Filters (each rejection is recorded with a reason):
   - placeholder template text ("Lorem", "Jake Ryan", "Southwestern University", "Your Name", "John Doe",
     "Jane Doe", "123-456-7890", "First Last", ...);
   - tool / AI-tailoring repos (repo name matches tailor|builder|agent|pipeline|generator|optimi[sz]er|ats-|
     autoapply|job-app...), and repos with > 25 resume-like .tex files (mass-generated variants);
   - last_modified < --min-date (default 2024-01-01);
   - non-English (share of common English stop-words among tokens too low, or many non-ASCII letters);
   - senior: > 5 years of full-time (non-intern) experience, or earliest full-time year more than 6 years
     before the file date; also academic CVs (>= 8 publication-like items and no industry roles);
   - too few bullets (< 6) or near-duplicate of an already-kept resume (bullet-set Jaccard >= 0.5, or same
     hashed identity line) -- forks/copies.
5. Extraction (brace-matching parser, not regexes over nested braces):
   - document body between ``\\begin{document}`` and ``\\end{document}``, comments stripped;
   - sections from ``\\section``/``\\section*``/``\\cvsection``/``\\sectiontitle``-style commands;
   - roles from ``\\resumeSubheading{a}{b}{c}{d}`` (title vs company decided by title keywords),
     ``\\resumeSubSubheading{title}{date}``, ``\\resumeProjectHeading{name}{date}``, ``\\cventry``;
   - bullets from ``\\resumeItem{...}``, ``\\resumeSubItem{title}{text}``, and bare ``\\item ...`` (text runs
     to the next ``\\item``/``\\end{itemize}``/``\\resume*`` macro at brace depth 0); bullets are only taken
     in experience/project/research/leadership-type sections (not Skills/Education/Coursework);
   - LaTeX -> plain text with a recursive token walker; ``\\textbf{..}``, ``{\\bf ..}``, ``{\\bfseries ..}``
     contents are recorded as bold phrases; ``\\href{url}{text}`` -> text; math is flattened
     (``$\\sim$``->~, ``\\times``->x, ``\\%``->%); emails/phones/URLs are scrubbed from any stored text.
6. Anonymisation: no names, e-mails or phones are written. ``id`` = sha1(repo + path)[:12]. The source repo
   URL is kept (public provenance), as requested by the corpus spec.

Tagging heuristics (bullet level)
---------------------------------
- ``leading_verb``: first alphabetic token, lower-cased.
- ``metric_types`` (regexes, see METRIC_PATTERNS):
    percent: ``\\d+%``/"percent"/"pp"; money: ``$\\d``, "USD", "\\d+k ARR", "revenue/cost ... \\d";
    time: number + (ms|µs|ns|s|sec|seconds|minutes|hours|days|weeks|months) or "latency ... \\d";
    scale: number with K/M/B suffix, "million"/"billion", GB/TB/PB, QPS/RPS/"req/s", "\\d+x" multipliers;
    count: any other standalone integer >= 2 that is not a year (19xx/20xx) or a version (e.g. Python 3).
  ``has_metric`` = any metric type present.
- ``techs``: case-insensitive word-boundary matches against TECH_VOCAB (canonical spellings).
- ``has_context`` (states the why/problem): purpose clauses "to <goal verb>" (reduce, improve, enable,
  support, automate, eliminate, ...), "in order to", "so that", "enabling", "allowing", "addressing",
  "because", "due to", "previously", "bottleneck", "pain point", "manual(ly)", "replacing".
- ``has_result`` (states the outcome): "resulting in", "leading to", "which (reduced|improved|...)",
  ", (reducing|improving|cutting|increasing|saving|boosting|achieving|enabling) ...", "from X to Y",
  "by \\d", "adopted by", "used by", "serving", "won", or a metric co-occurring with an outcome verb
  (reduced, increased, improved, decreased, cut, saved, boosted, accelerated, achieved, eliminated...).
- ``domain`` per bullet: keyword scores per domain (DOMAIN_KEYWORDS) over the bullet text plus a 0.5x
  weight of the role header text; company tier "quant" adds to quant_hft; argmax, ties/no hits ->
  role-level domain -> "general_swe".
- ``company_tier``: quant | faang_bign | top_startup | other_industry | academic | project, via the
  name lists TIER_QUANT / TIER_FAANG / TIER_TOP_STARTUP and university/lab keywords.

Resume level
------------
- intern: expected/end graduation year (max 20xx in Education section) > file year, or == file year and the
  file was last modified before June, and no post-graduation full-time role.
- new_grad: graduated (or graduating) with <= 1.5 years full-time experience.
- early_career: 1.5 - 5 years full-time. (> 5 -> rejected as senior.)

Usage
-----
    python3 tools/scrape_github_latex.py --candidates corpus/raw/github_candidates.txt \
        --out-resumes corpus/github_resumes.jsonl --out-bullets corpus/github_bullets.jsonl \
        --report corpus/raw/github_scrape_report.json
    python3 tools/scrape_github_latex.py --query 'resume language:TeX pushed:>2025-01-01' --max-repos 60 ...
    python3 tools/scrape_github_latex.py https://github.com/owner/repo ...
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from collections import Counter

# --------------------------------------------------------------------------------------------------
# Vocabularies
# --------------------------------------------------------------------------------------------------
DOMAINS = ["general_swe", "startup_fullstack", "backend_distributed", "cloud_infra_sre",
           "ai_ml_engineering", "ml_research_robotics", "quant_hft", "data_engineering",
           "embedded_systems"]

TIER_QUANT = ["jane street", "citadel", "hudson river", "hrt", "two sigma", "jump trading", "optiver",
              "imc trading", "imc ", "drw", "susquehanna", "sig ", "akuna", "d. e. shaw", "de shaw",
              "d.e. shaw", "tower research", "five rings", "virtu", "millennium", "point72", "cubist",
              "radix", "xtx", "old mission", "belvedere", "headlands", "squarepoint", "bridgewater",
              "renaissance technologies", "aqr", "flow traders", "chicago trading", "wolverine", "vatic", "pdt partners",
              "hap capital", "geneva trading", "peak6", "qube", "g-research", "maven securities",
              "alphagrep", "quadeye", "graviton", "transmarket", "valkyrie", "teza"]
TIER_FAANG = ["google", "alphabet", "deepmind", "meta", "facebook", "instagram", "amazon", "aws",
              "apple", "microsoft", "netflix", "nvidia", "linkedin", "youtube", "waymo", "oracle",
              "ibm", "intel", "salesforce", "adobe", "uber", "bloomberg", "tiktok", "bytedance",
              "qualcomm", "amd", "cisco", "vmware", "samsung", "x (twitter)", "twitter"]
TIER_TOP_STARTUP = ["stripe", "databricks", "openai", "anthropic", "scale ai", "palantir", "ramp",
                    "figma", "notion", "airbnb", "lyft", "snowflake", "coinbase", "robinhood", "plaid",
                    "rippling", "brex", "anduril", "spacex", "tesla", "cloudflare", "datadog", "snap",
                    "pinterest", "roblox", "doordash", "instacart", "shopify", "discord", "vercel",
                    "perplexity", "cohere", "mistral", "xai", "cruise", "duolingo", "atlassian",
                    "mongodb", "confluent", "hashicorp", "retool", "verkada", "samsara", "asana",
                    "dropbox", "twitch", "reddit", "spotify", "palo alto networks", "crowdstrike",
                    "affirm", "chime", "gusto", "faire", "benchling", "flexport", "nuro", "zoox",
                    "aurora", "skydio", "applied intuition", "modal", "replit", "cursor", "anysphere",
                    "hugging face", "together ai", "glean", "harvey", "cognition", "sierra", "mercor",
                    "neuralink", "supabase", "linear", "warp", "pinecone", "weights & biases",
                    "jane", "capital one", "goldman sachs", "jpmorgan", "j.p. morgan", "morgan stanley"]
# banks are not "top-tier" for SWE signal purposes; remove them from the top-startup list
_NOT_TOP = {"jane", "capital one", "goldman sachs", "jpmorgan", "j.p. morgan", "morgan stanley"}
TIER_TOP_STARTUP = [c for c in TIER_TOP_STARTUP if c not in _NOT_TOP]
# a smaller "FAANG/Big-N" core used for top_tier_signal (oracle/ibm/intel/cisco etc. don't count)
TOP_TIER_BIGN = ["google", "alphabet", "deepmind", "meta", "facebook", "instagram", "amazon", "aws",
                 "apple", "microsoft", "netflix", "nvidia", "linkedin", "youtube", "waymo", "uber",
                 "bloomberg", "tiktok", "bytedance", "salesforce", "adobe"]
ACADEMIC_KW = ["university", "college", "institute", "lab", "laboratory", "school of", "research group",
               "nsf", "reu", "faculty", "professor", "polytechnic"]

TECH_VOCAB = [
    "Python", "Java", "C++", "C#", "Go", "Golang", "Rust", "TypeScript", "JavaScript", "Kotlin", "Swift",
    "Scala", "Ruby", "PHP", "SQL", "PostgreSQL", "MySQL", "SQLite", "MongoDB", "Redis", "DynamoDB",
    "Cassandra", "Elasticsearch", "Kafka", "RabbitMQ", "gRPC", "GraphQL", "REST", "React", "Next.js",
    "Vue", "Angular", "Svelte", "Node.js", "Express", "Django", "Flask", "FastAPI", "Spring", "Spring Boot",
    "Rails", ".NET", "AWS", "GCP", "Azure", "Lambda", "S3", "EC2", "ECS", "EKS", "Docker", "Kubernetes",
    "Terraform", "Helm", "Ansible", "Jenkins", "GitHub Actions", "CI/CD", "Prometheus", "Grafana",
    "Datadog", "Spark", "PySpark", "Airflow", "dbt", "Snowflake", "BigQuery", "Hadoop", "Flink", "Pandas",
    "NumPy", "PyTorch", "TensorFlow", "JAX", "Keras", "scikit-learn", "Hugging Face", "LangChain",
    "LlamaIndex", "OpenAI", "LLM", "RAG", "CUDA", "Triton", "ONNX", "TensorRT", "vLLM", "OpenCV", "ROS",
    "ROS2", "MATLAB", "Simulink", "Verilog", "SystemVerilog", "VHDL", "FPGA", "RTOS", "FreeRTOS", "STM32",
    "Arduino", "Raspberry Pi", "Linux", "Bash", "Git", "Unity", "Unreal", "Flutter", "React Native",
    "iOS", "Android", "Tailwind", "Firebase", "Supabase", "Vercel", "Figma", "Selenium", "Playwright",
    "Jest", "pytest", "OCaml", "Haskell", "Zig", "WebAssembly", "WebSockets", "Nginx", "Celery", "Pydantic",
    "Postgres", "Prisma", "Kubeflow", "MLflow", "Ray", "Databricks", "Tableau", "Power BI", "Excel",
    "C", "Assembly", "LLVM", "MPI", "OpenMP", "SIMD", "Protobuf", "Bazel", "CMake", "Pinecone", "FAISS",
    "LangGraph", "Streamlit", "Vite", "Redux", "Electron", "Three.js", "WebGL", "Solidity", "Zookeeper",
]

DOMAIN_KEYWORDS = {
    "quant_hft": ["trading", "trader", "market data", "order book", "orderbook", "hft", "exchange connect",
                  "alpha", "backtest", "options pricing", "quant", "low-latency", "low latency",
                  "market making", "market-making", "pnl", "p&l", "futures", "equities", "tick data",
                  "derivatives", "risk model", "order execution", "fix protocol", "volatility", "kdb",
                  "signals", "strategies", "hedg"],
    "ml_research_robotics": ["research", "paper", "publication", "robot", "ros", "slam", "reinforcement",
                             "perception", "neurips", "icml", "iclr", "cvpr", "arxiv", "lab", "thesis",
                             "manipulation", "autonomous", "navigation", "lidar", "control policy",
                             "simulation", "benchmark", "ablation", "first-author", "co-author", "drone"],
    "ai_ml_engineering": ["llm", "rag", "pytorch", "tensorflow", "model", "fine-tun", "finetun",
                          "inference", "embedding", "agent", "transformer", "machine learning", "ml ",
                          "gpt", "langchain", "vector", "prompt", "classifier", "neural", "deep learning",
                          "nlp", "computer vision", "recommendation", "training", "evaluation", "ai ",
                          "genai", "generative", "diffusion", "cuda", "gpu", "hugging face", "openai"],
    "cloud_infra_sre": ["kubernetes", "terraform", "infrastructure", "ci/cd", "sre", "observability",
                        "prometheus", "grafana", "on-call", "deployment", "docker", "helm", "reliability",
                        "uptime", "incident", "monitoring", "cloud", "aws", "gcp", "azure", "devops",
                        "provision", "autoscal", "cluster", "container", "ansible", "jenkins", "github actions"],
    "backend_distributed": ["distributed", "microservice", "kafka", "grpc", "throughput", "consensus",
                            "raft", "database", "cache", "caching", "redis", "scalab", "api", "backend",
                            "concurrency", "rpc", "sharding", "replication", "queue", "storage", "latency",
                            "service", "endpoint", "postgres", "sql", "server", "rest"],
    "data_engineering": ["etl", "elt", "pipeline", "spark", "airflow", "dbt", "snowflake", "warehouse",
                         "bigquery", "data lake", "databricks", "ingestion", "batch", "streaming",
                         "schema", "data quality", "dashboard", "analytics", "tableau", "pandas"],
    "embedded_systems": ["firmware", "microcontroller", "mcu", "stm32", "rtos", "embedded", "fpga",
                         "verilog", "pcb", "can bus", "i2c", "spi", "uart", "cortex", "arduino",
                         "sensor", "hardware", "driver", "bare-metal", "bootloader", "asic", "rtl",
                         "soc", "vhdl", "systemverilog", "oscilloscope", "esp32"],
    "startup_fullstack": ["react", "next.js", "frontend", "front-end", "full-stack", "full stack",
                          "fullstack", "typescript", "node", "ui", "ux", "startup", "founding", "mobile",
                          "flutter", "react native", "web app", "landing page", "tailwind", "customers",
                          "users", "mvp", "product", "ios", "android", "stripe", "supabase", "firebase"],
}

PLACEHOLDERS = ["lorem ipsum", "jake ryan", "southwestern university", "your name", "john doe",
                "jane doe", "123-456-7890", "first last", "firstname lastname", "your.email",
                "youremail", "name@example", "your university", "company name", "insert ",
                "electronics and computer systems", "simple paintball", "gitlytics"]

TOOL_REPO_RE = re.compile(r"(tailor|builder|agent|pipeline|generator|optimi[sz]er|(^|[-_])ats[-_]|"
                          r"auto[-_]?apply|job[-_]?app|resumere|jobpilot|career-ops|hirepilot|"
                          r"resume-ai|resumo|refiner|template)", re.I)
SKIP_PATH_RE = re.compile(r"(^|/)(sample|samples|example|examples|fixture|fixtures|test|tests|"
                          r"templates?|node_modules|vendor|seeds)(/|$)|(sample|example|template|"
                          r"fixture|cover[-_ ]?letter|coverletter)[^/]*\.tex$", re.I)

EXP_SEC_RE = re.compile(r"experience|employment|work|project|research|leadership|activit|"
                        r"involvement|extracurricular|internship|engineering|professional|open source|"
                        r"hackathon|teaching", re.I)
NONBULLET_SEC_RE = re.compile(r"skill|education|coursework|course|award|honou?r|certif|interest|"
                              r"language|summary|objective|profile|publication|reference|contact", re.I)
TITLE_KW_RE = re.compile(r"\b(engineer|engineering|intern|internship|developer|researcher|research|"
                         r"assistant|analyst|scientist|lead|manager|founder|co-founder|cofounder|"
                         r"fellow|associate|consultant|swe|sde|mle|programmer|architect|trader|"
                         r"student|member|officer|president|director|tutor|ta\b|co-op|coop)", re.I)
INTERN_RE = re.compile(r"\b(intern|internship|co-?op|research assistant|undergraduate|student|"
                       r"teaching assistant|\bta\b|fellow|apprentice|extern|reu|summer analyst|"
                       r"part-time|volunteer|tutor)", re.I)

MONTHS = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug",
                                          "sep", "oct", "nov", "dec"])}

# --------------------------------------------------------------------------------------------------
# Brace-matching LaTeX helpers
# --------------------------------------------------------------------------------------------------

def strip_comments(tex: str) -> str:
    out = []
    for line in tex.splitlines():
        i, cut = 0, None
        while i < len(line):
            c = line[i]
            if c == "\\":
                i += 2
                continue
            if c == "%":
                cut = i
                break
            i += 1
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)


def skip_ws(s: str, i: int) -> int:
    while i < len(s) and s[i] in " \t\r\n":
        i += 1
    return i


def read_group(s: str, i: int, open_ch="{", close_ch="}"):
    """s[i] must be open_ch. Returns (content, index_after_close). Handles nesting and escapes."""
    assert s[i] == open_ch
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


def read_args(s: str, i: int, n: int, allow_optional=True):
    """Read up to n mandatory brace args after position i (skipping whitespace and [optional] args)."""
    args = []
    j = i
    while len(args) < n:
        k = skip_ws(s, j)
        if k < len(s) and s[k] == "[" and allow_optional:
            _, k = read_group(s, k, "[", "]")
            j = k
            continue
        if k < len(s) and s[k] == "{":
            a, j = read_group(s, k)
            args.append(a)
        else:
            break
    return args, j


CMD_RE = re.compile(r"\\([A-Za-z@]+\*?|.)")

BOLD_CMDS = {"textbf", "mathbf", "bfseries", "bf", "textsc"}  # textsc treated as emphasis-ish? no:
BOLD_CMDS = {"textbf", "mathbf"}
BOLD_DECLS = {"bf", "bfseries"}
DROP_WITH_ARGS = {"vspace": 1, "vspace*": 1, "hspace": 1, "hspace*": 1, "color": 1, "textcolor": 1,
                  "fontsize": 2, "setlength": 2, "addtolength": 2, "url": 1, "includegraphics": 1,
                  "faIcon": 1, "label": 1, "ref": 1, "cite": 1, "rule": 2, "raisebox": 1,
                  "definecolor": 3, "phantom": 1, "hyperlink": 1, "newline": 0}
SYMBOLS = {"%": "%", "$": "$", "&": "&", "_": "_", "#": "#", "{": "{", "}": "}", "~": "~", ",": " ",
           ";": " ", " ": " ", "\\": " ", "-": "", "/": "", "'": "", "`": "", '"': ""}
WORD_CMDS = {"sim": "~", "textasciitilde": "~", "times": "x", "approx": "~", "geq": ">=", "ge": ">=",
             "leq": "<=", "le": "<=", "rightarrow": "->", "to": "->", "Rightarrow": "=>", "uparrow": "↑",
             "downarrow": "↓", "pm": "±", "mu": "µ", "cdot": "·", "textbar": "|", "ldots": "...",
             "dots": "...", "textendash": "–", "textemdash": "—", "LaTeX": "LaTeX", "TeX": "TeX",
             "textdollar": "$", "textpercent": "%", "cpp": "C++", "CC": "C++", "Cpp": "C++",
             "textgreater": ">", "textless": "<", "infty": "∞", "checkmark": "", "bullet": "",
             "quad": " ", "qquad": " ", "item": " ", "linebreak": " ", "newline": " ", "par": " ",
             "%": "%", "textquotesingle": "'", "degree": "°", "Delta": "Δ", "alpha": "α", "beta": "β",
             "lambda": "λ", "sigma": "σ", "theta": "θ", "log": "log", "S": "§", "textregistered": "®",
             "texttrademark": "™", "copyright": "©", "ampersand": "&", "plus": "+", "uparrow": "↑"}


def latex_to_text(s: str, bold_out=None, _in_bold=False) -> str:
    """Recursive LaTeX -> plain text. Appends bold phrases (plain text) to bold_out."""
    out = []
    i = 0
    n = len(s)
    in_bold_decl = _in_bold
    while i < n:
        c = s[i]
        if c == "\\":
            m = CMD_RE.match(s, i)
            if not m:
                i += 1
                continue
            name = m.group(1)
            i = m.end()
            if not name[0].isalpha() and name[0] != "@":
                out.append(SYMBOLS.get(name, ""))
                continue
            if name in BOLD_CMDS:
                args, i = read_args(s, i, 1)
                if args:
                    sub_bold = []
                    t = latex_to_text(args[0], sub_bold, True)
                    if bold_out is not None and t.strip() and not _in_bold:
                        bold_out.append(norm_ws(t))
                    out.append(t)
                continue
            if name in BOLD_DECLS:
                # {\bf text} -- rest of current group is bold
                rest = latex_to_text(s[i:], None, True)
                if bold_out is not None and rest.strip() and not _in_bold:
                    bold_out.append(norm_ws(rest))
                out.append(rest)
                return "".join(out)
            if name in ("href",):
                args, i = read_args(s, i, 2)
                if len(args) == 2:
                    out.append(latex_to_text(args[1], bold_out, in_bold_decl))
                continue
            if name in DROP_WITH_ARGS:
                _, i = read_args(s, i, DROP_WITH_ARGS[name])
                continue
            if name in ("begin", "end"):
                args, i = read_args(s, i, 1, allow_optional=False)
                if name == "begin" and args and args[0] in ("tabular", "tabular*", "tabularx"):
                    _, i = read_args(s, i, 2 if args[0] != "tabular" else 1)
                continue
            if name in WORD_CMDS:
                out.append(WORD_CMDS[name])
                # swallow an empty {} after word commands
                k = skip_ws(s, i)
                if s[k:k + 2] == "{}":
                    i = k + 2
                continue
            # generic command: drop name, keep the text of its brace args
            k = skip_ws(s, i) if False else i
            while k < n and s[k] in "[{":
                if s[k] == "[":
                    _, k = read_group(s, k, "[", "]")
                    continue
                a, k = read_group(s, k)
                out.append(latex_to_text(a, bold_out, in_bold_decl))
            i = k
            continue
        if c == "{":
            a, i = read_group(s, i)
            out.append(latex_to_text(a, bold_out, in_bold_decl))
            continue
        if c == "}":
            i += 1
            continue
        if c == "$":
            i += 1
            continue
        if c == "~":
            out.append(" ")
            i += 1
            continue
        if c == "^" or c == "_":
            i += 1
            continue
        if c == "&":
            out.append(" ")
            i += 1
            continue
        out.append(c)
        i += 1
    txt = "".join(out)
    txt = txt.replace("---", "—").replace("--", "–").replace("``", '"').replace("''", '"')
    return txt


def norm_ws(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_RE = re.compile(r"(\+?\d[\d\s().-]{8,}\d)")
URL_RE = re.compile(r"(https?://\S+|www\.\S+|github\.com/\S+|linkedin\.com/\S+)", re.I)


def scrub(t: str) -> str:
    t = EMAIL_RE.sub("[email]", t)
    t = URL_RE.sub("[url]", t)
    t = PHONE_RE.sub(lambda m: m.group(0) if not re.search(r"\d{3}.*\d{3}.*\d{4}", m.group(0)) else "[phone]", t)
    return t

# --------------------------------------------------------------------------------------------------
# Git helpers
# --------------------------------------------------------------------------------------------------

def run(cmd, cwd=None, timeout=120):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
                       errors="replace")
    return r.returncode, r.stdout, r.stderr


def clone(repo: str, workdir: str) -> str | None:
    dest = os.path.join(workdir, repo.replace("/", "__"))
    if os.path.isdir(os.path.join(dest, ".git")):
        return dest
    url = f"https://github.com/{repo}.git"
    code, _, err = run(["git", "clone", "-q", "--depth", "50", "--filter=blob:limit=2m", "--no-checkout",
                        url, dest], timeout=180)
    if code != 0:
        return None
    return dest


def git_show(dest: str, path: str) -> str | None:
    code, out, _ = run(["git", "show", f"HEAD:{path}"], cwd=dest)
    return out if code == 0 else None


def _shallow_set(dest: str):
    f = os.path.join(dest, ".git", "shallow")
    return set(open(f).read().split()) if os.path.exists(f) else set()


def git_date(dest: str, paths) -> str | None:
    """Last commit date touching any of `paths`. If that commit is the shallow-clone boundary (i.e. the
    file was not changed within the fetched history, so the boundary commit would be mis-reported as
    the last change), deepen the clone (up to full history) and retry."""
    for attempt in range(3):
        code, out, _ = run(["git", "log", "-1", "--format=%H %cI", "--"] + list(paths), cwd=dest)
        if code != 0 or not out.strip():
            return None
        h, d = out.split()
        if h not in _shallow_set(dest):
            return d
        if attempt == 0:
            run(["git", "fetch", "-q", "--deepen=500", "--filter=blob:limit=2m"], cwd=dest, timeout=300)
        else:
            run(["git", "fetch", "-q", "--unshallow", "--filter=blob:limit=2m"], cwd=dest, timeout=600)
    return None  # could not establish a reliable date

# --------------------------------------------------------------------------------------------------
# Resume detection / inlining
# --------------------------------------------------------------------------------------------------
INPUT_RE = re.compile(r"\\(input|include|subfile)\s*\{([^}]+)\}")


def inline_inputs(dest, path, text, all_files, depth=0, used=None):
    used = used if used is not None else [path]
    if depth > 4:
        return text, used
    base = os.path.dirname(path)

    def repl(m):
        target = m.group(2).strip()
        cands = [os.path.normpath(os.path.join(base, target)), os.path.normpath(target)]
        cands = cands + [c + ".tex" for c in cands]
        for c in cands:
            if c in all_files:
                sub = git_show(dest, c)
                if sub is None:
                    return ""
                used.append(c)
                sub, _ = inline_inputs(dest, c, strip_comments(sub), all_files, depth + 1, used)
                return sub
        return ""
    return INPUT_RE.sub(repl, text), used


def resume_score(tex: str) -> int:
    s = 0
    for k in ("\\resumeSubheading", "\\resumeItem", "\\resumeProjectHeading", "\\resumeSubHeadingListStart"):
        if k in tex:
            s += 3
    low = tex.lower()
    for k in ("experience", "education", "projects", "skills"):
        if re.search(r"\\(sub)?section\*?\{[^}]*" + k, low) or ("{" + k) in low:
            s += 1
    if "\\item" in tex:
        s += 1
    if "\\documentclass" in tex:
        s += 1
    return s

# --------------------------------------------------------------------------------------------------
# Body parsing
# --------------------------------------------------------------------------------------------------
SECTION_CMDS = {"section", "section*", "cvsection", "sectiontitle", "resumeSection", "mysection",
                "Section", "newsection", "headingSection", "sectionTitle", "cvSection", "rSection"}
SUBHEAD4 = {"resumeSubheading", "resumeSubHeading", "resumeSubheadingContinue", "resumeQuadHeading",
            "resumeSubheadingWithLink", "experienceHeading", "jobentry", "cventry", "resumeEntry",
            "resumeExperience", "resumeTrioHeading", "resumeHeading"}
SUBSUB = {"resumeSubSubheading", "resumeSubSubHeading", "resumeQuadHeadingChild", "resumeSubheadingRole"}
PROJHEAD = {"resumeProjectHeading", "resumeProject", "projectHeading", "resumeProjectHeadingWithLink",
            "resumeProjectHeadingTwo", "projectentry"}
ITEM1 = {"resumeItem", "resumeitem", "resumeBullet", "bulletItem", "resumeItemNH", "cvitem"}
ITEM2 = {"resumeSubItem", "resumeItemWithTitle"}


DATE_ARG_RE = re.compile(r"(19|20)\d\d|present|current|expected|summer|fall|spring|winter|"
                         r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s", re.I)
LOC_RE = re.compile(r"^(remote|hybrid|onsite)\b|^[A-Z][A-Za-z .'-]+,\s*(?:[A-Z]{2}|[A-Z][a-z]+)\b(?:,\s*\w+)?$|"
                    r"^(USA|Canada|India|UK|United States|Singapore)$", re.I)


def classify_head(args_plain):
    """Return (company, title, dates) from a k-arg subheading (Jake: company, location, title, dates;
    many forks swap title/company or drop location). Arg roles are decided by content, not position."""
    a = [x for x in args_plain]
    dates, title, company = "", "", ""
    used = set()
    for idx, x in enumerate(a):
        if x and DATE_ARG_RE.search(x) and len(x) < 45 and not TITLE_KW_RE.search(x):
            dates, _ = x, used.add(idx)
            break
    rest = [(i, x) for i, x in enumerate(a) if i not in used and x]
    # Jake order preference: title is arg 2 when it looks like a title, else arg 0
    order = sorted(rest, key=lambda t: (t[0] != 2, t[0]))
    for i, x in order:
        if TITLE_KW_RE.search(x) and len(x) < 120:
            title = x
            used.add(i)
            break
    def bad_company(x):
        return ((LOC_RE.search(x) and len(x) < 40) or x.count(",") >= 3 or
                (DATE_ARG_RE.search(x) and len(x) < 30) or
                (TITLE_KW_RE.search(x) and not re.search(r"\b(inc|llc|ltd|corp|labs?|technologies|"
                                                          r"capital|group|university|institute)\b", x, re.I)))
    for i, x in rest:
        if i in used or bad_company(x):
            continue
        company = x
        used.add(i)
        break
    if not title:
        for i, x in rest:
            if i not in used and not (LOC_RE.search(x) and len(x) < 40):
                title = x
                break
    return clean_company(company), norm_ws(title), norm_ws(dates)


def clean_company(c: str) -> str:
    c = norm_ws(c)
    m = re.search(r"\b(?:at|@)\s+(.+)$", c)
    if m and TITLE_KW_RE.search(c[:m.start()]):
        c = m.group(1)
    c = re.split(r"\s+[|—–]\s+|\s+-\s+|\s*\|\s*", c)[0]
    c = re.sub(r",\s*[A-Z][a-zA-Z .]+,?\s*(?:[A-Z]{2}|USA|Canada|Remote)?$", "", c) if c.count(",") >= 1 \
        and len(c) > 25 else c
    return c.strip(" ,;:")


NEWCMD_RE = re.compile(r"\\(?:re)?newcommand\*?\s*\{?\\([A-Za-z@]+)\}?\s*(?:\[(\d)\])?")


def user_macros(tex: str):
    """Detect bullet macros defined in the preamble: 1- or 2-arg commands whose body emits \\item (or
    wraps an already-known bullet macro) and that are not heading macros. Known macro names are
    re-assigned by their actual arity (e.g. Jake's 1-arg \\resumeSubItem vs sb2nov's 2-arg one)."""
    defs = []
    for m in NEWCMD_RE.finditer(tex):
        name, k = m.group(1), int(m.group(2) or 0)
        j = skip_ws(tex, m.end())
        if j >= len(tex) or tex[j] != "{":
            continue
        body, _ = read_group(tex, j)
        defs.append((name, k, body))
    item1, item2 = set(), set()
    heads = {}
    for name, k, body in defs:
        if 2 <= k <= 6 and ("tabular" in body or "hfill" in body) and name not in ITEM1 | ITEM2:
            heads[name] = k
    known = set(ITEM1 | ITEM2)
    for _ in range(2):  # two passes for wrappers of wrappers
        for name, k, body in defs:
            if name in SUBHEAD4 | SUBSUB | PROJHEAD or name in heads or "tabular" in body or k not in (1, 2):
                continue
            if "\\item" in body or any("\\" + kn in body for kn in known | item1 | item2):
                (item1 if k == 1 else item2).add(name)
    return item1, item2, heads


def parse_body(tex: str):
    u1, u2, heads = user_macros(tex)
    for h in SUBHEAD4:
        heads.setdefault(h, 4)
    for h in SUBSUB | PROJHEAD:
        heads.pop(h, None)
    item1 = (ITEM1 - u2) | u1
    item2 = (ITEM2 - u1) | u2
    m = re.search(r"\\begin\{document\}", tex)
    body = tex[m.end():] if m else tex
    m2 = re.search(r"\\end\{document\}", body)
    body = body[:m2.start()] if m2 else body

    sections = []           # list of section heading strings (plain)
    roles = []              # dicts: section, company, title, dates, kind
    bullets = []            # dicts: section, role_idx, raw
    cur_sec = None
    cur_role = None
    i, n = 0, len(body)
    while i < n:
        c = body[i]
        if c != "\\":
            i += 1
            continue
        m = CMD_RE.match(body, i)
        if not m:
            i += 1
            continue
        name = m.group(1)
        j = m.end()
        if name in item1:
            args, j = read_args(body, j, 1)
            if args:
                bullets.append({"section": cur_sec, "role_idx": cur_role, "raw": args[0]})
            i = j
            continue
        if name in item2:
            args, j = read_args(body, j, 2)
            if args:
                bullets.append({"section": cur_sec, "role_idx": cur_role,
                                "raw": ("\\textbf{" + args[0] + "}: " + args[1]) if len(args) == 2 else args[0]})
            i = j
            continue
        if name in ("textbf", "bf", "bfseries", "large", "Large") and cur_sec and EXP_SEC_RE.search(cur_sec):
            # generic (non-Jake) heading: \textbf{Company} \hfill dates \\ \textit{Title} ... before a list
            stop = re.compile(r"\\begin\{(?:itemize|enumerate|zitemize)\}|\\item\b|\\resumeItemListStart|"
                              r"\\(?:sub)?section")
            mm = stop.search(body, j)
            end = mm.start() if mm else n
            seg = body[i:end]
            if len(seg) < 600 and re.search(r"(?:19|20)\d\d|present", seg, re.I):
                plain = norm_ws(latex_to_text(seg))
                bold = []
                latex_to_text(seg, bold)
                first = bold[0] if bold else plain
                rest = norm_ws(plain.replace(first, "", 1))
                dm = re.search(r"((?:[A-Z][a-z]{2,8}\.?\s*)?(?:19|20)\d\d\s*(?:[-–—]+|to)?\s*"
                               r"(?:(?:[A-Z][a-z]{2,8}\.?\s*)?(?:19|20)\d\d|[Pp]resent|[Cc]urrent)?)", plain)
                dates = dm.group(1) if dm else ""
                rest_nd = norm_ws(rest.replace(dates, ""))
                if TITLE_KW_RE.search(first) and not TITLE_KW_RE.search(rest_nd[:60]):
                    title, company = first, rest_nd
                else:
                    company, title = first, rest_nd
                kind = "project" if re.search(r"project", cur_sec, re.I) else "role"
                roles.append({"section": cur_sec, "company": clean_company(company)[:80], "title": title[:100],
                              "dates": dates, "kind": kind, "header": plain[:200]})
                cur_role = len(roles) - 1
                i = end
                continue
        if name in SECTION_CMDS or name.rstrip("*") in SECTION_CMDS:
            args, j = read_args(body, j, 1)
            if args:
                cur_sec = norm_ws(latex_to_text(args[0]))
                sections.append(cur_sec)
                cur_role = None
            i = j
            continue
        if name in heads:
            args, j = read_args(body, j, heads[name])
            plain = [norm_ws(latex_to_text(a)) for a in args]
            company, title, dates = classify_head(plain)
            kind = "project" if (cur_sec and re.search(r"project", cur_sec, re.I)
                                 and not re.search(r"experience", cur_sec, re.I)) else "role"
            roles.append({"section": cur_sec, "company": company if kind == "role" else "",
                          "title": title if kind == "role" else (plain[0] if plain else ""),
                          "dates": dates, "kind": kind, "header": " ".join(plain)})
            cur_role = len(roles) - 1
            i = j
            continue
        if name in SUBSUB:
            args, j = read_args(body, j, 2)
            plain = [norm_ws(latex_to_text(a)) for a in args]
            comp = roles[cur_role]["company"] if cur_role is not None else ""
            roles.append({"section": cur_sec, "company": comp, "title": plain[0] if plain else "",
                          "dates": plain[1] if len(plain) > 1 else "", "kind": "role",
                          "header": " ".join(plain) + " " + comp})
            cur_role = len(roles) - 1
            i = j
            continue
        if name in PROJHEAD:
            args, j = read_args(body, j, 2)
            plain = [norm_ws(latex_to_text(a)) for a in args]
            title = plain[0] if plain else ""
            roles.append({"section": cur_sec, "company": "", "title": title.split("|")[0].strip(),
                          "dates": plain[1] if len(plain) > 1 else "", "kind": "project",
                          "header": " ".join(plain)})
            cur_role = len(roles) - 1
            i = j
            continue
        if name == "item":
            # optional [label]
            k = skip_ws(body, j)
            if k < n and body[k] == "[":
                _, k = read_group(body, k, "[", "]")
            start = k
            depth = 0
            while k < n:
                ch = body[k]
                if ch == "\\":
                    mm = CMD_RE.match(body, k)
                    if not mm:
                        k += 1
                        continue
                    nm = mm.group(1)
                    if depth == 0 and (nm == "item" or nm == "end" or nm.startswith("resume")
                                       or nm in SECTION_CMDS or nm == "begin"):
                        break
                    k = mm.end()
                    continue
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    if depth == 0:
                        break
                    depth -= 1
                k += 1
            raw = body[start:k]
            if raw.strip():
                bullets.append({"section": cur_sec, "role_idx": cur_role, "raw": raw})
            i = k
            continue
        i = j
    return sections, roles, bullets

# --------------------------------------------------------------------------------------------------
# Tagging heuristics
# --------------------------------------------------------------------------------------------------
YEAR_RE = re.compile(r"\b(19[5-9]\d|20[0-4]\d)\b")
NUM_RE = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?![\w.]*\d)")
METRIC_PATTERNS = {
    "percent": re.compile(r"\d\s*%|\bpercent\b|\d+\s*pp\b|\bbps\b", re.I),
    "money": re.compile(r"\$\s?\d|\bUSD\b|\d+\s?[kKmMbB]\+?\s*(?:ARR|MRR|revenue|in revenue|savings)|"
                        r"(?:revenue|cost|savings|saved|funding|raised|budget)\D{0,25}\d", re.I),
    "time": re.compile(r"\d+(?:\.\d+)?\+?\s*(?:ms|µs|us|ns|s|sec|secs|seconds?|mins?|minutes?|hrs?|hours?|"
                       r"days?|weeks?|months?)\b|latency\D{0,20}\d|\d+\s*x\s*faster", re.I),
    "scale": re.compile(r"\d+(?:\.\d+)?\s?[kKmMbB]\+?(?![a-zA-Z])|\b(?:million|billion|thousand)s?\b|"
                        r"\d+\s?(?:GB|TB|PB|MB)\b|\b(?:QPS|RPS|TPS)\b|req(?:uests)?/s|\d+(?:\.\d+)?\s?[xX]\b|"
                        r"\d+\s?(?:k|K)\+", re.I),
}
OUTCOME_VERBS = r"(reduc|increas|improv|decreas|cut|sav|boost|accelerat|achiev|eliminat|lower|rais|" \
                r"grew|grow|speed|sped|doubl|tripl|halv|shrank|shrink|minimi[sz]|maximi[sz]|enabl|won|" \
                r"generat|drove|driv)"
RESULT_RE = re.compile(r"resulting in|leading to|which (?:reduced|improved|increased|cut|saved|enabled|"
                       r"allowed|led)|,\s*(?:reducing|improving|cutting|increasing|saving|boosting|"
                       r"achieving|enabling|lowering|decreasing|eliminating|accelerating|doubling|"
                       r"speeding|raising|driving|yielding)|\bfrom\s+\S+\s+to\s+\S+|\bby\s+~?\$?\d|"
                       r"adopted by|used by|serving|\bwon\b|placed|awarded|achiev|outperform|"
                       r"\bsaving\b|\bsaved\b", re.I)
CONTEXT_RE = re.compile(r"\bto\s+(?:reduce|improve|enable|support|automate|eliminate|streamline|"
                        r"accelerate|ensure|prevent|help|allow|increase|decrease|cut|speed|replace|"
                        r"address|resolve|identify|detect|provide|facilitate|unblock|scale|minimi[sz]e|"
                        r"maximi[sz]e|optimi[sz]e|empower|simplify|power|handle|serve|track|monitor|"
                        r"centrali[sz]e|standardi[sz]e|consolidate|lower|boost|predict|capture|avoid|"
                        r"mitigate|surface|give|let)\b|in order to|so that|\benabling\b|\ballowing\b|"
                        r"\baddressing\b|\bbecause\b|\bdue to\b|\bpreviously\b|\bbottleneck|pain point|"
                        r"\bmanual(?:ly)?\b|\breplacing\b|\bfor (?:\d|the|a|an|internal|external|over)\b"
                        r"[^,.;]{0,40}(?:team|users|customers|clients|engineers|analysts|traders|"
                        r"researchers|students)", re.I)


def metric_types(t: str):
    found = [k for k, rx in METRIC_PATTERNS.items() if rx.search(t)]
    # count: any standalone integer >= 2 that's not a year/version and not already explained
    tt = YEAR_RE.sub(" ", t)
    tt = re.sub(r"\b(?:python|java|c\+\+|ros|html|css|es|ipv|python3|v)\s?\d+(?:\.\d+)*", " ", tt, flags=re.I)
    tt = re.sub(r"\b\d+(?:st|nd|rd|th)\b", " ", tt)
    tt = re.sub(r"\b[A-Za-z]+\d+[A-Za-z0-9]*\b|\b\d+[A-Za-z]{2,}\w*\b", " ", tt)  # S3, EC2, 3D, 5G..
    nums = [x for x in NUM_RE.findall(tt)]
    for x in nums:
        try:
            v = float(x.replace(",", ""))
        except ValueError:
            continue
        if v >= 2 and not found:
            found.append("count")
            break
        if v >= 2 and "count" not in found and not any(k in found for k in ("percent", "money", "time", "scale")):
            found.append("count")
            break
    return [k for k in ["percent", "count", "time", "money", "scale"] if k in found]


def techs_in(t: str):
    out = []
    for tech in TECH_VOCAB:
        if tech in ("C", "Go", "REST", "Ray", "Excel", "Git", "Spring", "Express", "Vue", "S3", "LLM", "RAG"):
            pat = r"(?<![\w+#.-])" + re.escape(tech) + r"(?![\w+#])"
            if re.search(pat, t):  # case-sensitive for ambiguous short names
                if tech == "C" and re.search(r"\bC\s*(?:\+\+|#)", t) and not re.search(r"\bC(?![+#\w])", t):
                    continue
                out.append(tech)
        else:
            pat = r"(?<![\w])" + re.escape(tech) + r"(?![\w])" if tech[-1].isalnum() else \
                r"(?<![\w])" + re.escape(tech)
            if re.search(pat, t, re.I):
                out.append(tech)
    canon = {"Golang": "Go", "Postgres": "PostgreSQL", "Spring Boot": "Spring", "ROS2": "ROS"}
    res = []
    for x in out:
        x = canon.get(x, x)
        if x not in res:
            res.append(x)
    return res


def company_tier(company: str, kind: str, section: str | None) -> str:
    if kind == "project" or (section and re.search(r"project", section, re.I) and not company):
        return "project"
    lc = " " + company.lower() + " "
    if any(re.search(r"(?<![a-z])" + re.escape(q.strip()) + r"(?![a-z])", lc) for q in TIER_QUANT):
        return "quant"
    if any(re.search(r"(?<![a-z])" + re.escape(q) + r"(?![a-z])", lc) for q in TIER_FAANG):
        return "faang_bign"
    if any(re.search(r"(?<![a-z])" + re.escape(q) + r"(?![a-z])", lc) for q in TIER_TOP_STARTUP):
        return "top_startup"
    if any(k in lc for k in ACADEMIC_KW):
        return "academic"
    return "other_industry" if company else "unknown"


NOT_EMPLOYER_RE = re.compile(r"developer (student )?groups?|student|club|society|hackathon|major league hacking|"
                             r"\bmlh\b|fellowship program|ambassador|competition|olympiad|challenge", re.I)


def is_top_tier(company: str) -> bool:
    if NOT_EMPLOYER_RE.search(company):
        return False
    lc = " " + company.lower() + " "
    lists = TIER_QUANT + TOP_TIER_BIGN + TIER_TOP_STARTUP
    return any(re.search(r"(?<![a-z])" + re.escape(q.strip()) + r"(?![a-z])", lc) for q in lists)


def domain_scores(text: str, weight=1.0, scores=None):
    scores = scores if scores is not None else Counter()
    low = " " + text.lower() + " "
    for d, rx in _DOMAIN_RX.items():
        hits = len(rx.findall(low))
        if hits:
            scores[d] += weight * hits
    return scores


# keywords match at a word start (so stems like "scalab"/"fine-tun" work, but "lab" != "label")
_DOMAIN_RX = {d: re.compile(r"(?<![a-z0-9])(?:" + "|".join(re.escape(k.strip()) for k in kws) + r")"
                            + r"(?:[a-z0-9-]*)", re.I)
              for d, kws in DOMAIN_KEYWORDS.items()}


def pick_domain(scores: Counter, fallback="general_swe") -> str:
    if not scores:
        return fallback
    (d1, s1), *rest = scores.most_common()
    if rest and rest[0][1] == s1:
        return fallback if fallback in (d1, rest[0][0]) else d1
    return d1 if s1 >= 1 else fallback

# --------------------------------------------------------------------------------------------------
# Level / seniority
# --------------------------------------------------------------------------------------------------

def parse_years(dates: str):
    yrs = [int(y) for y in re.findall(r"(?:19|20)\d\d", dates)]
    present = bool(re.search(r"present|current|now|ongoing", dates, re.I))
    return yrs, present


def estimate_level(tex_plain_edu: str, roles, file_dt: dt.datetime):
    fy = file_dt.year
    grad_years = [int(y) for y in re.findall(r"20[0-4]\d", tex_plain_edu)]
    grad = max(grad_years) if grad_years else None
    if re.search(r"present|expected|anticipated|candidate for|in progress|ongoing|current", tex_plain_edu, re.I) \
            and (grad is None or grad <= fy):
        grad = fy + 1  # still enrolled at file date (e.g. "2022 - Present", "Expected ...")
    ft_years = 0.0
    earliest_ft = None
    for r in roles:
        if r["kind"] != "role" or not r["dates"]:
            continue
        title_hdr = r["title"] + " " + r["header"]
        if INTERN_RE.search(title_hdr) or (r["section"] and re.search(r"research|leadership|activit|"
                                                                     r"volunteer|extracurricular|teach",
                                                                     r["section"], re.I)):
            continue
        yrs, present = parse_years(r["dates"])
        if not yrs:
            continue
        start = min(yrs)
        end = fy if present else max(yrs)
        if grad and end <= grad and not present:
            continue  # part-time role during school
        if grad and start < grad:
            start = grad
        ft_years += max(0.25, end - start)
        earliest_ft = start if earliest_ft is None else min(earliest_ft, start)
    student = grad is not None and (grad > fy or (grad == fy and file_dt.month < 6))
    if student and ft_years < 1:
        level = "intern"
    elif ft_years <= 1.5:
        level = "new_grad"
    elif ft_years <= 5:
        level = "early_career"
    else:
        level = "senior"
    if earliest_ft and fy - earliest_ft > 6:
        level = "senior"
    return level, grad, round(ft_years, 2)

# --------------------------------------------------------------------------------------------------
# Main per-repo processing
# --------------------------------------------------------------------------------------------------
STOP = set("the and to of in a for with on using by from that as at an is was were into via across "
           "over this which their our it be".split())


def english_ok(text: str) -> bool:
    toks = re.findall(r"[A-Za-zÀ-ÿ]+", text.lower())
    if len(toks) < 80:
        return False
    stop = sum(1 for t in toks if t in STOP)
    nonascii = sum(1 for ch in text if ord(ch) > 127 and ch.isalpha())
    return stop / len(toks) > 0.06 and nonascii < 0.03 * len(text)


def process_repo(repo: str, preferred: str | None, workdir: str, min_date: dt.datetime):
    rec = {"repo": repo, "status": "rejected", "reason": None}
    if TOOL_REPO_RE.search(repo.split("/")[1]):
        rec["reason"] = "tool_or_template_repo"
        return rec, None
    dest = clone(repo, workdir)
    if not dest:
        rec["reason"] = "clone_failed"
        return rec, None
    code, out, _ = run(["git", "ls-tree", "-r", "--name-only", "HEAD"], cwd=dest)
    files = set(out.splitlines())
    texs = [f for f in files if f.lower().endswith(".tex") and not SKIP_PATH_RE.search(f)]
    if not texs:
        rec["reason"] = "no_tex"
        return rec, None
    scored = []
    for f in texs:
        raw = git_show(dest, f)
        if raw is None or "\\documentclass" not in raw:
            continue  # only root documents; \input fragments are inlined below
        text, used = inline_inputs(dest, f, strip_comments(raw), files)
        if resume_score(text) >= 5:
            scored.append((f, text, used))
    if not scored:
        rec["reason"] = "no_resume_like_tex"
        return rec, None
    if len(scored) > 60:
        # very large sets of near-identical variants: restrict date lookups to the 60 newest-named
        scored = sorted(scored, key=lambda x: x[0])[-60:]
    cands = []
    for f, text, used in scored:
        d = git_date(dest, used)
        cands.append((f, text, used, d))
    if preferred and any(c[0] == preferred for c in cands):
        chosen = [c for c in cands if c[0] == preferred][0]
    else:
        def key(c):
            nm = os.path.basename(c[0]).lower()
            bonus = 1 if ("resume" in nm or nm == "main.tex" or "cv" in nm) else 0
            ver = [int(x) for x in re.findall(r"\d+", c[0])][-3:]
            return (c[3] or "", ver, bonus, -len(c[0]))
        chosen = sorted(cands, key=key, reverse=True)[0]
    path, text, used, date = chosen
    rec.update({"file_path": path, "last_modified": date, "n_resume_tex": len(scored)})
    if not date:
        rec["reason"] = "no_date"
        return rec, None
    file_dt = dt.datetime.fromisoformat(date)
    if file_dt.replace(tzinfo=None) < min_date:
        rec["reason"] = "too_old"
        return rec, None
    low = text.lower()
    for ph in PLACEHOLDERS:
        if ph in low:
            rec["reason"] = f"placeholder:{ph.strip()}"
            return rec, None
    sections, roles, bullets = parse_body(text)
    plain_all = norm_ws(latex_to_text(text[text.find("\\begin{document}"):] if "\\begin{document}" in text else text))
    if not english_ok(plain_all):
        rec["reason"] = "non_english_or_too_short"
        return rec, None
    # identity hash (never stored in output; used only for dedup)
    hm = re.search(r"\\(?:Huge|huge|LARGE|Large)\s*[^}]*?([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z.]+){1,3})", text)
    ident = hashlib.sha1((hm.group(1) if hm else repo).lower().encode()).hexdigest()
    emails = EMAIL_RE.findall(plain_all)
    if emails:
        ident = hashlib.sha1(emails[0].lower().encode()).hexdigest()
    # Education text for grad year
    edu_text = ""
    m = re.search(r"\\section\*?\{\s*education\s*\}(.*?)(\\section|\Z)", text, re.S | re.I)
    if m:
        edu_text = latex_to_text(m.group(1))
    else:
        m = re.search(r"education(.{0,600})", plain_all, re.I | re.S)
        edu_text = m.group(1) if m else ""
    for r in roles:
        r["is_edu"] = bool(r["section"] and NONBULLET_SEC_RE.search(r["section"])
                           and not EXP_SEC_RE.search(r["section"]))
    work_roles = [r for r in roles if not r["is_edu"]]
    level, grad, ft_years = estimate_level(edu_text, work_roles, file_dt)
    pubs = len(re.findall(r"\b(?:NeurIPS|ICML|ICLR|CVPR|ICCV|ECCV|ACL|EMNLP|AAAI|IJCAI|arXiv|"
                          r"Proceedings|Journal|Conference)\b", plain_all))
    industry_roles = [r for r in work_roles if r["kind"] == "role" and company_tier(r["company"], "role", r["section"])
                      in ("quant", "faang_bign", "top_startup", "other_industry")]
    if level == "senior":
        rec["reason"] = f"senior(ft_years={ft_years})"
        return rec, None
    if pubs >= 8 and not industry_roles:
        rec["reason"] = "academic_cv"
        return rec, None

    # Build bullets
    out_bullets = []
    role_dom_scores = {}
    for b in bullets:
        sec = b["section"] or ""
        if NONBULLET_SEC_RE.search(sec) and not EXP_SEC_RE.search(sec):
            continue
        if not EXP_SEC_RE.search(sec) and b["role_idx"] is None:
            continue
        bold = []
        t = norm_ws(latex_to_text(b["raw"], bold))
        t = scrub(t)
        if len(t) < 25 or len(t.split()) < 5:
            continue
        b["text"], b["bold"] = t, [scrub(x) for x in bold if len(x) > 1]
        out_bullets.append(b)
    # drop exact duplicate bullets (conditional \\if branches / repeated \\input of the same section)
    seen_txt, dedup = set(), []
    for b in out_bullets:
        key = b["text"].lower()
        if key not in seen_txt:
            seen_txt.add(key)
            dedup.append(b)
    n_dupes = len(out_bullets) - len(dedup)
    out_bullets = dedup
    if len(out_bullets) < 6:
        rec["reason"] = f"too_few_bullets({len(out_bullets)})"
        return rec, None

    rid = hashlib.sha1(f"{repo}:{path}".encode()).hexdigest()[:12]
    rows = []
    companies, top = [], False
    for r in roles:
        if r["is_edu"]:
            r["tier"] = "academic"
            continue
        if r["kind"] == "role" and r["company"]:
            tier = company_tier(r["company"], "role", r["section"])
            r["tier"] = tier
            if tier != "academic" and r["company"] not in companies:
                companies.append(scrub(r["company"]))
            if r["section"] and re.search(r"experience|employment|work|intern|professional|industry",
                                          r["section"], re.I) and is_top_tier(r["company"]):
                top = True
            elif is_top_tier(r["company"]) and (INTERN_RE.search(r["title"]) or
                                                TITLE_KW_RE.search(r["title"])):
                top = True
        else:
            r["tier"] = company_tier(r.get("company", ""), r["kind"], r["section"])
    dom_counter = Counter()
    for b in out_bullets:
        role = roles[b["role_idx"]] if b["role_idx"] is not None else None
        sc = Counter()
        domain_scores(b["text"], 1.0, sc)
        if role:
            domain_scores(role["header"], 0.5, sc)
            if role.get("tier") == "quant":
                sc["quant_hft"] += 2
            if role.get("tier") == "academic" and re.search(r"research", role["header"], re.I):
                sc["ml_research_robotics"] += 1
        dom = pick_domain(sc)
        dom_counter[dom] += 1
        mt = metric_types(b["text"])
        words = b["text"].split()
        # skip a short "Label:" prefix (e.g. "Data Pipeline: Built ...") when finding the leading verb
        body_txt = re.sub(r"^[^:]{2,40}:\s+", "", b["text"]) if re.match(r"^[^:]{2,40}:\s+[A-Z]", b["text"]) \
            else b["text"]
        lv = re.match(r"[A-Za-z][A-Za-z-]*", body_txt)
        rows.append({
            "resume_id": rid,
            "role_title": scrub(role["title"]) if role else None,
            "company_tier": role.get("tier") if role else "unknown",
            "domain": dom,
            "last_modified": date,
            "text": b["text"],
            "bold_phrases": b["bold"],
            "chars": len(b["text"]),
            "words": len(words),
            "leading_verb": lv.group(0).lower() if lv else None,
            "has_metric": bool(mt),
            "metric_types": mt,
            "techs": techs_in(b["text"]),
            "has_context": bool(CONTEXT_RE.search(b["text"])),
            "has_result": bool(RESULT_RE.search(b["text"]) or
                               (mt and re.search(OUTCOME_VERBS, b["text"], re.I))),
        })
    total = sum(dom_counter.values())
    n_quant_rows = sum(1 for r in rows if r["company_tier"] == "quant")
    domains = [d for d, c in dom_counter.most_common() if c / total >= 0.2][:3] or [dom_counter.most_common(1)[0][0]]
    if n_quant_rows >= 2 and "quant_hft" not in domains:
        domains = (domains + ["quant_hft"])[:4]
    uniq_ratio = len(out_bullets) / (len(out_bullets) + n_dupes)
    n_pages = max(1.0, round(len(plain_all) * uniq_ratio / 3800 * 2) / 2)
    if "\\newpage" in text or "\\clearpage" in text:
        n_pages = max(n_pages, 2.0)
    notes = []
    if any(k in text for k in ("\\resumeSubheading", "\\resumeItem")):
        notes.append("jake_template_family")
    if len(scored) > 1:
        notes.append(f"{len(scored)} resume-like .tex in repo; picked most recent")
    if len(scored) > 15:
        notes.append("many variants (per-application/versioned)")
    if grad:
        notes.append(f"grad_year={grad}")
    notes.append(f"ft_years~{ft_years}")
    if n_dupes:
        notes.append(f"{n_dupes} duplicate bullets removed (conditional/duplicated inputs)")
    resume_row = {
        "id": rid,
        "source_url": f"https://github.com/{repo}",
        "file_path": path,
        "last_modified": date,
        "level": level,
        "companies": companies,
        "top_tier_signal": top,
        "domains": domains,
        "section_order": [scrub(s) for s in sections],
        "n_bullets": len(rows),
        "page_estimate": n_pages,
        "notes": "; ".join(notes),
    }
    n_ind = sum(1 for r in work_roles if r.get("tier") in ("quant", "faang_bign", "top_startup", "other_industry"))
    metric_rate = sum(r["has_metric"] for r in rows) / len(rows)
    quality = (3.0 * top + 3.0 * metric_rate + min(n_ind, 3) * 0.75
               + (1.0 if file_dt.year >= 2026 else 0.5 if file_dt.year == 2025 else 0.0)
               + 0.5 * (sum(r["has_result"] for r in rows) / len(rows))
               - (1.0 if sum(r["company_tier"] == "project" for r in rows) / len(rows) > 0.7 else 0.0))
    rec.update({"status": "kept", "reason": None, "id": rid, "quality": round(quality, 3),
                "n_industry_roles": n_ind, "metric_rate": round(metric_rate, 3)})
    return rec, {"resume": resume_row, "bullets": rows, "ident": ident, "quality": quality,
                 "n_ind": n_ind, "metric_rate": metric_rate,
                 "bullet_set": {re.sub(r"\W+", " ", r["text"].lower())[:60] for r in rows}}


def search_repos(query: str, max_repos: int):
    out = []
    page = 1
    while len(out) < max_repos and page <= 10:
        url = ("https://api.github.com/search/repositories?" +
               urllib.parse.urlencode({"q": query, "sort": "updated", "per_page": 100, "page": page}))
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                                                   "User-Agent": "resume-lab-scraper"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)
        except Exception as e:  # noqa: BLE001
            print(f"[search] failed: {e}", file=sys.stderr)
            break
        items = data.get("items", [])
        if not items:
            break
        out += [it["full_name"] for it in items]
        page += 1
    return out[:max_repos]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repos", nargs="*", help="repo URLs or owner/repo")
    ap.add_argument("--candidates", help="file with owner/repo [path] per line")
    ap.add_argument("--query", help="GitHub repository search query")
    ap.add_argument("--max-repos", type=int, default=100)
    ap.add_argument("--workdir", default="/tmp/claude-0/gh_corpus")
    ap.add_argument("--min-date", default="2024-01-01")
    ap.add_argument("--out-resumes", default="corpus/github_resumes.jsonl")
    ap.add_argument("--out-bullets", default="corpus/github_bullets.jsonl")
    ap.add_argument("--report", default=None)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--max-keep", type=int, default=80, help="max resumes kept after quality ranking")
    ap.add_argument("--domain-quota", type=int, default=4,
                    help="min resumes per primary domain (if available) before best-first fill")
    a = ap.parse_args()

    os.makedirs(a.workdir, exist_ok=True)
    targets = []
    for r in a.repos:
        m = re.search(r"github\.com/([^/]+/[^/#?]+)", r)
        targets.append(((m.group(1) if m else r).removesuffix(".git"), None))
    if a.candidates:
        for line in open(a.candidates):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 1)
            targets.append((parts[0], parts[1] if len(parts) > 1 else None))
    if a.query:
        targets += [(r, None) for r in search_repos(a.query, a.max_repos)]
    seen, uniq = set(), []
    for t in targets:
        if t[0].lower() not in seen:
            seen.add(t[0].lower())
            uniq.append(t)
    min_date = dt.datetime.fromisoformat(a.min_date)

    results = []
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        futs = {ex.submit(process_repo, r, p, a.workdir, min_date): r for r, p in uniq}
        for f in cf.as_completed(futs):
            try:
                results.append(f.result())
            except Exception as e:  # noqa: BLE001
                results.append(({"repo": futs[f], "status": "rejected", "reason": f"error:{e!r}"[:200]}, None))
    results.sort(key=lambda x: x[0]["repo"].lower())

    # dedup (forks / copies of the same person's resume)
    kept, idents, report = [], set(), []
    for rec, data in results:
        if data:
            dup = data["ident"] in idents
            if not dup:
                for k in kept:
                    inter = len(k["bullet_set"] & data["bullet_set"])
                    if inter / max(1, len(k["bullet_set"] | data["bullet_set"])) >= 0.5:
                        dup = True
                        break
            if dup:
                rec.update({"status": "rejected", "reason": "duplicate_of_kept_resume"})
                data = None
            else:
                idents.add(data["ident"])
                kept.append(data)
        report.append(rec)

    # quality selection: hard floor, then best-first with per-domain coverage quota
    pool = [k for k in kept if k["n_ind"] >= 1 and (k["metric_rate"] >= 0.25 or k["resume"]["top_tier_signal"])]
    floor_rejects = [k for k in kept if k not in pool]
    pool.sort(key=lambda k: k["quality"], reverse=True)
    chosen, quota = [], a.domain_quota
    for d in DOMAINS:  # guarantee coverage of every domain tag (primary domain)
        for k in [k for k in pool if k["resume"]["domains"][0] == d and k not in chosen][:quota]:
            chosen.append(k)
    for k in pool:
        if len(chosen) >= a.max_keep:
            break
        if k not in chosen:
            chosen.append(k)
    chosen_ids = {k["resume"]["id"] for k in chosen}
    for rec in report:
        if rec.get("status") == "kept" and rec.get("id") not in chosen_ids:
            fl = any(k["resume"]["id"] == rec["id"] for k in floor_rejects)
            rec.update({"status": "rejected",
                        "reason": "quality_floor(no_industry_role, or metric_rate<0.25 without top-tier role)" if fl
                        else "below_quality_cutoff"})
    kept = chosen

    with open(a.out_resumes, "w") as fr, open(a.out_bullets, "w") as fb:
        for k in sorted(kept, key=lambda d: d["resume"]["last_modified"], reverse=True):
            fr.write(json.dumps(k["resume"], ensure_ascii=False) + "\n")
            for b in k["bullets"]:
                fb.write(json.dumps(b, ensure_ascii=False) + "\n")
    if a.report:
        with open(a.report, "w") as f:
            json.dump(report, f, indent=1)
    reasons = Counter((r["reason"] or "kept").split("(")[0].split(":")[0] for r in report)
    print(f"targets={len(uniq)} kept={len(kept)} bullets={sum(len(k['bullets']) for k in kept)}")
    print(dict(reasons))


if __name__ == "__main__":
    main()
