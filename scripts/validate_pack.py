#!/usr/bin/env python3
"""Validate a FlowBoost share package before ZIP creation."""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.cwd()
MAX_FILES = 200
MAX_SIZE_MB = 10

ALLOW_EXTS = {".md", ".py", ".sh", ".json", ".txt"}
BLOCK_NAMES = {".git", "__pycache__", ".DS_Store"}


def main() -> int:
    files = [p for p in ROOT.rglob("*") if p.is_file()]
    count = 0
    total = 0
    problems = []

    for p in files:
        rel = p.relative_to(ROOT)
        if any(part in BLOCK_NAMES for part in rel.parts):
            problems.append(f"blocked path: {rel}")
            continue
        if p.suffix not in ALLOW_EXTS:
            problems.append(f"unexpected extension: {rel}")
        count += 1
        total += p.stat().st_size

    size_mb = total / (1024 * 1024)
    if count > MAX_FILES:
        problems.append(f"file count too high: {count}")
    if size_mb > MAX_SIZE_MB:
        problems.append(f"package too large: {size_mb:.2f}MB")

    if problems:
        print("Validation failed:")
        for item in problems[:50]:
            print(f"- {item}")
        return 1

    print(f"OK: {count} files, {size_mb:.2f}MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
