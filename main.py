#!/usr/bin/env python3
"""Write the one-sentence apology to /output/entry.txt (UTF-8, no trailing newline)."""

import os

SENTENCE = "I am sorry I summarised your two-hour meeting as 'vibes were discussed' and then acted like that was a deliverable."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
