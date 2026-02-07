#!/usr/bin/env python3
"""Parse curriculum markdown files and build a CSV of LeetCode problems."""

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Curriculum dir -> pattern name for CSV
CURRICULA = {
    "Array-and-Hashmaps": "Array and Hashmaps",
    "BinarySearch": "Binary Search",
    "Intervals": "Intervals",
    "PrefixSum": "Prefix Sum",
    "Sliding-Window": "Sliding Window",
    "Stacks": "Stacks",
    "Trees": "Trees",
    "TwoPointers": "Two Pointers",
}

# Map curriculum dir to its main markdown file (some have different names)
CURRICULUM_FILES = {
    "Array-and-Hashmaps": "ArrayAndHashmaps.md",
    "BinarySearch": "BinarySearch.md",
    "Intervals": "Intervals.md",
    "PrefixSum": "PrefixSum.md",
    "Sliding-Window": "SlidingWIndow.md",
    "Stacks": "Stacks.md",
    "Trees": "Trees.md",
    "TwoPointers": "TwoPointer.md",
}

URL_PATTERN = re.compile(
    r"https?://(?:leetcode\.com|neetcode\.io)/problems/([^\s\)\]\"]+?)(?:\s|$|\)|\]|\")"
)


def normalize_url(line: str) -> str | None:
    """Extract problem URL from a line; return None if it's a submission or invalid."""
    m = re.search(r"(https?://(?:leetcode\.com|neetcode\.io)/problems/[^\s\)\]\"]+)", line)
    if not m:
        return None
    url = m.group(1).rstrip("/")
    if "/submissions/" in url:
        return None
    # Strip query string for neetcode for consistency, but keep base URL
    if "?" in url:
        url = url.split("?")[0]
    return url


def parse_file(dirname: str, filepath: Path) -> list[tuple[str, str, str]]:
    """Parse one curriculum file. Returns list of (url, difficulty, pattern)."""
    pattern = CURRICULA[dirname]
    rows: list[tuple[str, str, str]] = []
    current_difficulty = "Easy"  # default until we see a section

    text = filepath.read_text()
    for line in text.splitlines():
        line_stripped = line.strip()
        if line_stripped.startswith("## Easy"):
            current_difficulty = "Easy"
            continue
        if line_stripped.startswith("## Medium"):
            current_difficulty = "Medium"
            continue
        if line_stripped.startswith("## Hard") or line_stripped.startswith("### Hard"):
            current_difficulty = "Hard"
            continue
        url = normalize_url(line)
        if url:
            rows.append((url, current_difficulty, pattern))
    return rows


def main():
    all_rows: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str]] = set()  # (url, pattern) to avoid dupes within same file

    for dirname, pattern in CURRICULA.items():
        filename = CURRICULUM_FILES.get(dirname)
        if not filename:
            continue
        filepath = ROOT / dirname / filename
        if not filepath.exists():
            continue
        for url, difficulty, pat in parse_file(dirname, filepath):
            key = (url, pat)
            if key in seen:
                continue
            seen.add(key)
            all_rows.append((url, difficulty, pat))

    out_path = Path(__file__).resolve().parent / "leetcode_problems.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["url", "difficulty", "pattern"])
        w.writerows(all_rows)

    print(f"Wrote {len(all_rows)} problems to {out_path}")


if __name__ == "__main__":
    main()
