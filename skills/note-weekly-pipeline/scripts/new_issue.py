#!/usr/bin/env python3
"""Create a non-destructive, self-contained weekly note issue."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re


STAGES = (
    "00-brief", "01-research", "02-plan", "03-source",
    "04-draft", "05-package", "06-performance",
)


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("--slug must contain ASCII letters or numbers")
    return slug


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--output-root", default="output")
    args = parser.parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        parser.error("--date must be YYYY-MM-DD")
    try:
        slug = safe_slug(args.slug)
    except ValueError as exc:
        parser.error(str(exc))

    issue = Path(args.output_root) / f"{args.date}-{slug}"
    if issue.exists():
        parser.error(f"issue already exists: {issue}; choose another slug")
    for stage in STAGES:
        (issue / stage).mkdir(parents=True)
    issue_id = issue.name
    write_if_missing(issue / "00-brief" / "brief.md", f"""# {args.title}

- issue_id: {issue_id}
- status: brief
- platform: note
- target_reader: TODO
- primary_problem: TODO
- article_promise: TODO
- price_hypothesis: TODO
- distribution_hypothesis: TODO
- primary_kpi: purchases
- review_date: TODO
- claims_policy: sourced facts; labelled hypotheses; no fabricated experience/results
""")
    write_if_missing(issue / "00-brief" / "inputs.md", "# Inputs\n\n- TODO: link legacy `research/` reports and author-approved material.\n")
    write_if_missing(issue / "00-brief" / "decision-log.md", "# Decision log\n\n| Date | Decision | Evidence / reason | Owner |\n|---|---|---|---|\n")
    write_if_missing(issue / "01-research" / "research.md", "# Research handoff\n\n## Evidence\n\n## Opportunity\n\n## Theme decision\n")
    write_if_missing(issue / "02-plan" / "plan.md", "# Article plan\n\n## Reader and promise\n\n## Offer and paywall\n\n## Distribution and measurement\n")
    write_if_missing(issue / "03-source" / "source-ledger.md", "# Source ledger\n\n| ID | Claim label | Source / consent | Safe wording |\n|---|---|---|---|\n")
    write_if_missing(issue / "04-draft" / "article.md", f"# {args.title}\n\n<!-- Write the approved draft here. -->\n")
    write_if_missing(issue / "04-draft" / "claim-ledger.md", "# Claim ledger\n\n| Article section | Claim | Label | Source / calculation | Status |\n|---|---|---|---|---|\n")
    write_if_missing(issue / "05-package" / "publish.yml", "platform: note\nstatus: draft\narticle_source: ../04-draft/article.md\nprice: null\ntags: []\npublished_url: null\n")
    write_if_missing(issue / "06-performance" / "metrics.yml", "observed_at: null\nviews: null\nlikes: null\npurchases: null\nrevenue_jpy: null\nsource: null\n")
    write_if_missing(issue / "06-performance" / "review.md", "# Performance review\n\nRun after sufficient observation; distinguish observed data, calculations, and hypotheses.\n")
    print(issue)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
