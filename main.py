#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes a two-line warning to /output/entry.txt.
Line 1 warns the writer's past self about one specific moment.
Line 2 says why that moment mattered and what changed because of it.
"""

import os
import sys

ENTRY = (
    "Say no when the foreman offers you double pay to cover the night shift at the warehouse on 14 March.\n"
    "The forklift crushes your left hand that night, and the settlement pays for the teaching degree that gets you out of the warehouse for good."
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
