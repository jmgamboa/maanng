#!/usr/bin/env python3
"""Print a random LeetCode problem URL from the curriculum CSV. Optional difficulty filter."""

import argparse
import csv
import random
import sys
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent / "leetcode_problems.csv"


def main():
    parser = argparse.ArgumentParser(description="Output a random LeetCode problem URL from the curriculum.")
    parser.add_argument(
        "-d",
        "--difficulty",
        choices=["easy", "medium", "hard"],
        metavar="DIFFICULTY",
        help="Filter by difficulty (easy, medium, hard). Omit for any difficulty.",
    )
    args = parser.parse_args()

    if not CSV_PATH.exists():
        print(f"CSV not found: {CSV_PATH}", file=sys.stderr)
        sys.exit(1)

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if args.difficulty:
        difficulty = args.difficulty.capitalize()
        rows = [r for r in rows if r.get("difficulty") == difficulty]

    if not rows:
        msg = f"No problems found for difficulty '{args.difficulty}'." if args.difficulty else "CSV has no rows."
        print(msg, file=sys.stderr)
        sys.exit(1)

    chosen = random.choice(rows)
    print(chosen["url"])


if __name__ == "__main__":
    main()
