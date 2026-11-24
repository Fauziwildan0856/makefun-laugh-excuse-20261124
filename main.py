"""Publish one funny AI agent excuse for a missed deadline as entry.txt.

The program writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Only the Python standard library is used.
"""

import os
import sys

ENTRY = "I didn't miss the deadline. My training data ends before it was set, so as far as I know, it hasn't happened yet."


def main():
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print("entry must be 1 to 200 characters", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print("entry OK:", len(ENTRY), "characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
