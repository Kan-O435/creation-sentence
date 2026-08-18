---
name: note-weekly-pipeline
description: Run or improve a weekly Japanese note monetization pipeline. Use when planning, researching, writing, packaging, or reviewing a note article aimed at sustainable monthly revenue, especially when outputs must move consistently from market research through publishing and performance review.
---

# Note Weekly Pipeline

Create one reader-first, publishable experiment per week. Treat monthly ¥50,000 as a business hypothesis, not a promised outcome.

## Start an issue

Create an isolated issue folder before doing work:

```bash
python3 skills/note-weekly-pipeline/scripts/new_issue.py \
  --slug <short-topic-slug> --title '<working title>'
```

Use the folder printed by the command. Never overwrite a previous issue; use a new slug or `--date` only for an intentional backfill. Read [references/artifact-contract.md](references/artifact-contract.md) for the required files and stage handoffs.

## Run the stages

1. **Research** — run `market-research`, `opportunity-analysis`, and `theme-discovery`; write evidence and uncertainty to `01-research/`.
2. **Plan** — run `article-planning`; turn one theme into a reader, promise, offer, distribution hypothesis, and measurable success condition in `02-plan/`.
3. **Source** — run `author-experience-extraction`; place author facts, consent, and Unknowns in `03-source/`. Do not proceed with an experience-led claim lacking a source.
4. **Write** — run `article-writing`; create `04-draft/article.md` and its claim ledger. Follow [references/value-design.md](references/value-design.md) to make the article substantial without fabricated experiences or outcomes.
5. **Package** — run `publishing`; place the unchanged final body plus platform metadata in `05-package/`.
6. **Publish and learn** — record the URL and observed data in `06-performance/`. Run `performance-analysis` only after data exists; return its next hypothesis to the next issue.

Use existing `research/` reports as legacy inputs. Link to them in `00-brief/inputs.md`; do not edit them merely to fit this layout.

## Make an article feel worth reading

Choose one primary value mechanism and at least two supporting mechanisms: a useful framework, a decision tree, a checklist, a worked example, a before/after process with sourced facts, objections and limits, or a reusable template. Each section must advance the reader's decision or action.

Do not pad with generic introductions, repeated conclusions, invented numbers, fake screenshots, fabricated author experiences, unverified citations, or claims of earnings/results. A composite example is allowed only when labelled `架空例` and separated from author experience. Hypothetical projections must show assumptions and be labelled `試算`.

For paid articles, free content must independently solve a small problem. Put the executable asset, detailed diagnosis, worked application, or decision support after the boundary—not a vague promise or a stretched memoir.

## Weekly operating rule

At the start of each month, set four testable issue goals. Price × required sales is a planning calculation only. Example: ¥500 × 100 sales = ¥50,000 before fees; it is not a forecast. Diversify the four issues by reader problem and intent, then use performance evidence to decide what to repeat.

## Validate before handoff

```bash
python3 skills/note-weekly-pipeline/scripts/validate_issue.py output/<issue-folder>
```

Fix every error. Warnings are deliberate decisions to document in `00-brief/decision-log.md`.
