#!/usr/bin/env python3
"""ATS keyword coverage of a resume against real job postings.

usage: ats_score.py <resume.pdf|.txt> <variant> [--json out.json]
       variant = general_backend | infra_distributed | systems_quant | ai_ml_engineering

1. Keyword weights: document frequency of each VOCAB term across corpus/jds/<variant>.jsonl
   (infra also pools general_backend postings; its own board set is small).
   must-have = in >= 25% of postings, nice-to-have = 10-25%.
2. Claimable = the term (or its evidence regex) appears in resume/facts.yaml, i.e. Amar can
   honestly list it. Missing non-claimable terms are reported but never count against him.
3. The resume is read as plain pdftotext output (what an ATS ingests).
Soft skills (communication, collaboration) are not scored: they are shown through content, not keywords.
Target: >= 90% of claimable must-haves present.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# canonical: (regex matched in JDs and resume, evidence regex in facts.yaml or None = same regex)
VOCAB = {
    "Python": (r"\bpython\b", None), "Java": (r"\bjava\b(?!script)", None), "C++": (r"c\+\+", None),
    "C": (r"\bC\b(?![+#])", None), "Go": (r"\bgo(lang)?\b(?=[ ,/)])", r"\bgolang\b"), "Rust": (r"\brust\b", None),
    "TypeScript": (r"typescript", None), "JavaScript": (r"javascript", None), "SQL": (r"\bsql\b", None),
    "Bash": (r"\bbash\b|shell script", None), "Kotlin": (r"kotlin", None), "Scala": (r"\bscala\b", None),
    "React": (r"\breact\b", None), "Node.js": (r"node\.?js", None), "GraphQL": (r"graphql", None),
    "REST APIs": (r"\brest(ful)?\b|\bapis?\b", r"rest apis|api gateway|\bapi\b"),
    "PostgreSQL": (r"postgres", None), "Redis": (r"\bredis\b", None), "NoSQL": (r"nosql|mongodb|dynamodb", r"mongodb"),
    "databases": (r"databases?\b|\bdbms\b", r"postgres|database|\bdb\b"),
    "AWS": (r"\baws\b|amazon web services", None), "GCP / Azure": (r"\bgcp\b|google cloud|azure", None),
    "cloud": (r"\bcloud\b", r"\baws\b"), "Docker": (r"docker|container", r"docker"),
    "Kubernetes": (r"kubernetes|\bk8s\b", None), "Terraform": (r"terraform", None),
    "infrastructure as code": (r"infrastructure.as.code|\biac\b|terraform|cloudformation|\bcdk\b", r"\bcdk\b|cloudformation"),
    "CI/CD": (r"ci/cd|continuous (integration|delivery|deployment)|github actions|jenkins", r"github actions|codedeploy"),
    "Linux": (r"\blinux\b|unix", None), "Git": (r"\bgit\b|github", None),
    "Kafka / streaming": (r"kafka|kinesis|stream(ing)? (data|processing)|event.driven", r"kinesis"),
    "data pipelines / ETL": (r"data pipelines?|\betl\b|pipelines?", r"pipeline"),
    "distributed systems": (r"distributed (systems?|computing)", r"distributed"),
    "microservices": (r"microservices?", None), "serverless": (r"serverless|\blambda\b", r"lambda"),
    "caching": (r"cach(e|ing)", r"redis|cach"),
    # stricter evidence (loop 2 review): "scaled a studio" is not technical scalability; nothing in the
    # facts is a system-design claim. Both stay listed but not claimable.
    "scalability": (r"scal(able|ability|e)\b", r"scalab"),
    "performance optimization": (r"performance|latency|throughput|optimi[sz]", r"latency|throughput|perf\b"),
    "low latency": (r"low.latency|latency.sensitive", r"latency|ns/event|µs"),
    "data structures & algorithms": (r"data structures?|algorithms?", r"order book|b\+ tree|skip list|hash map|std::map"),
    "object-oriented design": (r"object.oriented|\booo?p\b|\bood\b", None),
    "concurrency / multithreading": (r"concurren|multi.?thread|parallel", None),
    "networking": (r"\bnetwork(ing|s)?\b|tcp|udp", None), "operating systems": (r"operating systems?|kernel", None),
    "unit testing": (r"unit test|testing|test.driven|\btdd\b", r"pytest|jest|test"),
    "debugging": (r"debug", r"profil|diagnos|bottleneck"),
    "monitoring / observability": (r"monitor|observab|logging|metrics", r"cloudwatch|x-ray|logs"),
    "system design": (r"system design|design (and|&) (build|implement)|architect", r"system design"),
    "machine learning": (r"machine learning|\bml\b", r"model|fine-tun|classif"),
    "LLMs": (r"\bllms?\b|large language model|generative ai|genai", r"\bllm|claude|gpt"),
    "RAG / retrieval": (r"\brag\b|retrieval|vector (db|database|search)|embedding", r"\brag\b|chromadb|sentencebert"),
    "model fine-tuning / evaluation": (r"fine.tun|evaluat|evals?\b", r"fine-tun|eval"),
    "PyTorch": (r"pytorch", None), "TensorFlow": (r"tensorflow", None), "CUDA": (r"\bcuda\b", None),
    "prompt engineering": (r"prompt", r"prompt"), "agents": (r"\bagent(s|ic)?\b", r"agent|claude skill|sub-skill"),
    "full stack": (r"full.?stack|front.?end", r"react|electron"), "backend": (r"back.?end|server.side", r"postgres|api|lambda"),
    "developer tools": (r"developer (tools|tooling|productivity|experience)|internal tools", r"developer|workflow builder|tool"),
    "agile": (r"\bagile\b|scrum", r"agile|jira"), "code review": (r"code review", None),
    "storage engines": (r"storage|database internals|query engine", r"b\+ tree|lsm"),
    "benchmarking / profiling": (r"benchmark|profil", r"benchmark|perf\b|psutil"),
    "probability / statistics": (r"statistic|probabilit", r"statistics"),
    "trading / market data": (r"trading|market data|exchange|order", r"order book|iex|exchange"),
}


def text_of(p: Path) -> str:
    if p.suffix == ".pdf":
        return subprocess.run(["pdftotext", str(p), "-"], capture_output=True, text=True).stdout
    return p.read_text()


def score(resume_text: str, variant: str):
    files = [variant] + (["general_backend"] if variant == "infra_distributed" else [])
    jds = [json.loads(l) for f in files for l in open(ROOT / f"corpus/jds/{f}.jsonl")]
    facts = (ROOT / "resume/facts.yaml").read_text()
    rows = []
    for kw, (rx, ev) in VOCAB.items():
        flags = 0 if kw == "C" else re.I
        df = sum(bool(re.search(rx, j["title"] + "\n" + j["text"], flags)) for j in jds) / len(jds)
        tier = "must" if df >= 0.25 else "nice" if df >= 0.10 else None
        if not tier:
            continue
        claimable = bool(re.search(ev or rx, facts, flags))
        present = bool(re.search(rx, resume_text, flags))
        rows.append({"keyword": kw, "df": round(df, 2), "tier": tier, "claimable": claimable, "present": present})
    def cov(t):
        c = [r for r in rows if r["tier"] == t and r["claimable"]]
        return (sum(r["present"] for r in c) / len(c)) if c else 1.0, c
    must, mc = cov("must")
    nice, nc = cov("nice")
    return {"variant": variant, "n_postings": len(jds), "must_coverage": round(must, 3), "nice_coverage": round(nice, 3),
            "missing_claimable": [r["keyword"] for r in sorted(mc + nc, key=lambda r: -r["df"]) if not r["present"]],
            "not_claimable": [r["keyword"] for r in rows if not r["claimable"]], "rows": rows}


def main():
    res = score(text_of(Path(sys.argv[1])), sys.argv[2])
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(res, indent=2))
    print(f"ats[{res['variant']}, {res['n_postings']} postings]: must {res['must_coverage']:.0%}, nice {res['nice_coverage']:.0%}")
    if res["missing_claimable"]:
        print("  missing (claimable): " + ", ".join(res["missing_claimable"]))
    print("  not claimable (ignored): " + ", ".join(res["not_claimable"]))
    sys.exit(0 if res["must_coverage"] >= 0.9 else 1)


if __name__ == "__main__":
    main()
