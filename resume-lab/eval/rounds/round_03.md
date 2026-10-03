# Round 03 → v4/v5 decisions

**Panel result on v3:**
- Overall 8.0, with all five reviewers at 8.
- impact_clarity and quantification were at 7.
- Credibility was 7.6, up from 6.8.

## v4: wording consensus (≥2 reviewers each), then blind-judged (5/8 new wins)
- Contract heading changed to "(Client: Amazon Leo)".
- Skills: AWS row renamed "Cloud (AWS)"; React/Electron moved to "Web & Data".
- Studio: dropped "run with Jira and GitHub" (filler, flagged by 4/5).
- Search index now leads with "Precomputed".
- Leo and Bedrock bullets tightened.
- Redshift: "Writing Java to tune…" fixes the "Java-based bounds" misreading.
- Order-book and Tortuga wording reverted to the judge-preferred versions.

## v5: candidate facts (Amar, Oct 3)
- **PhysTwin correction:** the work was *not* automated training. It is the AnyGrasp → Open3D overlay → VLM input pipeline, plus prompt tuning.
  - Removed the inaccurate "Developing automated training" bullet and marked it superseded in facts.yaml.
  - Merged the context into the pipeline bullet.
- **Kinesis:** the bullet now says what was replaced: S3 staging hops (scraper → S3 → Lambda → S3).
- **IEX:** real metrics were added, with the verbatim source in `resume/sources/iex_metrics_2026-10.md`. The bullets now show:
  - replay correctness: 50.9M messages and 99,122/99,123 fills
  - the B+ tree vs LSM benchmark: 12.8× read throughput and 22× range summaries for 27% more disk
  - throughput: 1.26M events/s
- New accepted risk: `env_setup_baseline`, because no baseline exists for the 30%.

## Tooling
- Reviewer ATS text now comes from plain `pdftotext`. Layout mode had inserted blank lines inside wrapped bullets, which the ATS reviewer flagged. Plain mode keeps each bullet together, which is closer to real parsers.
- `fact_check.py` now rejects facts marked superseded.
