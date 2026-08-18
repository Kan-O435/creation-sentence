#!/usr/bin/env python3
"""Validate the portable issue contract without third-party dependencies."""
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = (
    "00-brief/brief.md", "00-brief/inputs.md", "01-research/research.md",
    "02-plan/plan.md", "03-source/source-ledger.md", "04-draft/article.md",
    "04-draft/claim-ledger.md", "05-package/publish.yml", "05-package/seo-topic-map.md",
    "06-performance/metrics.yml", "06-performance/review.md",
)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("issue")
    args = parser.parse_args()
    issue = Path(args.issue)
    errors, warnings = [], []
    if not issue.is_dir():
        errors.append(f"not an issue directory: {issue}")
    for relative in REQUIRED:
        path = issue / relative
        if not path.is_file():
            errors.append(f"missing: {relative}")
    brief = issue / "00-brief/brief.md"
    if brief.is_file():
        text = brief.read_text(encoding="utf-8")
        for field in ("issue_id:", "status:", "target_reader:", "article_promise:", "claims_policy:"):
            if field not in text:
                errors.append(f"brief missing field: {field}")
    article = issue / "04-draft/article.md"
    if article.is_file() and len(article.read_text(encoding="utf-8").strip()) < 200:
        warnings.append("draft is still a placeholder or extremely short")
    ledger = issue / "04-draft/claim-ledger.md"
    if ledger.is_file() and "|" not in ledger.read_text(encoding="utf-8"):
        warnings.append("claim ledger has no table")
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")
    if not errors:
        print(f"OK: {issue}")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
