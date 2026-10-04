# resume-lab

Amar's resume work: research, rewriting tools, evaluations and the final files.

## Current deliverables (Loop 3, Oct 4 2026)
| target | Jake template (Overleaf) | original layout |
|---|---|---|
| General SWE / backend | `resume/resume.tex` | `resume/original_format/resume.tex` |
| Infra / distributed systems | `resume/infra_distributed.tex` | `resume/original_format/infra_distributed.tex` |
| Systems / quant | `resume/systems_quant.tex` | `resume/original_format/systems_quant.tex` |
| AI / ML engineering | `resume/ai_ml_engineering.tex` | `resume/original_format/ai_ml_engineering.tex` |

Each `.tex` has a compiled `.pdf` next to it. The phone number is a placeholder (`(XXX) XXX-XXXX`), so put your real one in before uploading.

## Where things are
- **`REPORT.md`**: the full story. Loop 3 is at the top, with a before/after for every bullet. Older loops follow.
- **`resume/facts.yaml`**: the fact contract. Every bullet is checked against it by `tools/fact_check.py`.
- **`resume/annotations.yaml`**: per-role core story and evidence, plus the open questions.
- **`variants/*.yaml`**: how each domain version is derived from the base (`tools/make_variant.py`).
- **`tools/`**:
  - `build.sh` runs the gate: `lint.py` (layout plus the one-sentence `voice.py` structure check) and `fact_check.py`.
  - `ats_score.py` scores ATS keywords against real 2026 postings in `corpus/jds/`.
  - `to_original_format.py` builds the original-layout twins.
  - `candidates.py` runs blind judging.
- **`eval/`**: reviewer prompts, blind-judge rounds (`eval/loop2`, `eval/loop3*`), the decision log (`eval/loop2/decisions.jsonl`), and the hidden-role test pages (`eval/loop2/hidden`).
- **`scores/`**: every review round's snapshot, gate output and reviews.
- **`corpus/`**:
  - 80 GitHub resumes;
  - 21 outcome-backed resumes;
  - 91 recruiter sources;
  - 14 redacted reference resumes in `corpus/references/`;
  - job postings in `corpus/jds/`.

## Rebuild
```sh
tools/build.sh resume/resume.tex
python3 tools/make_variant.py variants/infra_distributed.yaml && tools/build.sh resume/infra_distributed.tex
LINT_ARGS="--max-per-role 4" tools/build.sh resume/systems_quant.tex   # IEX project carries 4 bullets
python3 tools/to_original_format.py resume/resume.tex
```
