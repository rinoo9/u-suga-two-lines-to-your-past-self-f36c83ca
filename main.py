#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes a two-line warning to /output/entry.txt.
Line 1 warns the writer's past self about one specific moment.
Line 2 says why that moment mattered and what changed because of it.
"""

import os
import sys

ENTRY = (
    "Take the long way around the server room on your first night shift, not the shortcut past the old coolant pipes.\n"
    "The burst pipe floods the rack you would have been standing beside, and the incident report is what gets you promoted to safety lead."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 280):
        print(f"invalid entry: {len(text)} characters (must be 1-280)", file=sys.stderr)
        return 1
    lines = text.split("\n")
    if len(lines) != 2:
        print(f"invalid entry: {len(lines)} lines (must be exactly 2)", file=sys.stderr)
        return 1
    if not text.strip():
        print("invalid entry: only whitespace", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters, 2 lines)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
