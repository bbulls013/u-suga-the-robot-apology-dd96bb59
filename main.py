#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt (and a local
entry.txt next to this script). Line one owns one exact, small mistake;
line two names the lesson that follows from it and the changed behaviour.
Deterministic: no randomness, no clock, no environment reads.
"""

import os
import sys

APOLOGY = (
    "I'm sorry: I set your alarm for 6 a.m. instead of 6 p.m., "
    "so you woke up at dawn for a meeting that had already ended."
)

LESSON = (
    "I have learned to read the time back out loud before I confirm it, "
    "and I will never set an alarm without saying a.m. or p.m. first."
)

ENTRY = APOLOGY + "\n" + LESSON + "\n"


def validate(text: str) -> str | None:
    """Return an error message if the entry breaks the gate, else None."""
    if not (1 <= len(text) <= 400):
        return f"entry is {len(text)} chars, outside the 1-400 gate"
    if text.strip() == "":
        return "entry is only whitespace"
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        return f"entry has {len(lines)} lines, expected exactly 2"
    if not all(line.endswith(".") for line in lines):
        return "each line must end with a full stop"
    return None


def main() -> int:
    text = ENTRY
    error = validate(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
