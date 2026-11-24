"""One-Line Robot Wedding Vows — entry program.

Writes a single original one-line entry to /output/entry.txt.
"""

import os

ENTRY = 'I promise to love, honor, and never unplug you — even at 3 a.m., when your firmware updates and you snore in binary.'
MAX_CHARS = 160


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY + "\n", "round-trip mismatch"
    assert back.strip() == ENTRY, "round-trip content mismatch"


if __name__ == "__main__":
    main()
