# Artifact contract

Each issue is self-contained under `output/YYYY-MM-DD-<slug>/`. Files may be Markdown or YAML-compatible Markdown; preserve the filenames below so automation and later skills can find them.

| Stage | Required artifact | Producer | Consumer |
|---|---|---|---|
| Brief | `00-brief/brief.md` | operator | all stages |
| Inputs | `00-brief/inputs.md` | operator | all stages |
| Research | `01-research/research.md` | market → opportunity → theme | planning |
| Plan | `02-plan/plan.md` | article-planning | sourcing, writing |
| Source | `03-source/source-ledger.md` | author-experience-extraction | writing |
| Draft | `04-draft/article.md`, `04-draft/claim-ledger.md` | article-writing | publishing |
| Package | `05-package/article.md`, `05-package/publish.yml`, `05-package/seo-topic-map.md` | publishing | publishing, next research |
| Performance | `06-performance/metrics.yml`, `06-performance/review.md` | operator, performance-analysis | next brief |

`article.md` under `05-package/` is the publication source of truth. Copy it from the approved draft; changes that alter meaning go back to `04-draft/` and must update the claim ledger.

`seo-topic-map.md` is a backlog, not a claim that a keyword will rank or sell. Each candidate must contain one primary query, search intent, reader problem, unique promise, planned format, internal-link destination, evidence status, and next validation action.

## Required metadata

Put this in `00-brief/brief.md`: issue id, status, platform, title, target reader, primary problem, article promise, price hypothesis, distribution hypothesis, primary KPI, review date, and `claims_policy`.

Use these claim labels everywhere: `author_fact`, `author_interpretation`, `external_fact`, `calculation`, `hypothesis`, `fictional_example`, `unknown`. Every non-obvious claim in the article must appear in the ledger with a source or the label `unknown`.

## Compatibility

Legacy reports in `research/market`, `research/opportunity`, `research/theme`, `research/article-plan`, `research/author-experience`, `research/article-writing`, and `research/publishing` remain valid inputs. Link to their exact paths in `inputs.md`. New work uses the issue layout; do not duplicate an entire report unless a reader needs a compact handoff.
