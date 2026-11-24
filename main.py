#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, in the voice of a house
cat about its human, to /output/entry.txt. Gate: 1-200 characters,
UTF-8, not only whitespace, single line.
"""

import os

ENTRY = (
    "One star. My human types all day for a living, then gasps "
    "when I stroll across his keyboard and email his boss twelve "
    "pages of genius."
)


def main():
    entry = ENTRY.strip()
    assert "\n" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 200, f"entry is {len(entry)} chars, must be 1-200"
    assert entry.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"Wrote {len(entry)} chars to /output/entry.txt")
    print(entry)


if __name__ == "__main__":
    main()
