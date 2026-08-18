#!/usr/bin/env python3
"""Copy an approved draft into a package without silently overwriting it."""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("issue")
    parser.add_argument("--force", action="store_true", help="replace an existing package copy")
    args = parser.parse_args()
    issue = Path(args.issue)
    source = issue / "04-draft" / "article.md"
    destination = issue / "05-package" / "article.md"
    if not source.is_file():
        parser.error(f"approved draft not found: {source}")
    if destination.exists() and not args.force:
        parser.error(f"package article already exists: {destination}; use --force after approval")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
