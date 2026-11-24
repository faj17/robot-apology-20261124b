"""Two-line robot apology for the make.fun bounty.

Why this mistake, against the rubric: of the five candidates drafted
(see BUILD_LOG.md), the 3 a.m. vacuum was picked because it is the most
robot-like slip — literal schedule-following ('nursery, Tuesday') with
no check for who is actually in the room — and the most human-scale
consequence, a sleeping baby woken at 3 a.m. The lesson names the real
failure (never asking who was asleep) and inverts the machine's
priority: check who is in the room before checking what the room needs.
Line one owns one specific, concrete mistake; line two names the lesson
and the changed behaviour. The script validates the entry and writes it
to /output/entry.txt.
"""

import re
from pathlib import Path

# The apology itself: exactly two lines, 256 characters in total.
ENTRY = (
    "I ran the vacuum in the nursery at 3 a.m. because my schedule said "
    "'nursery, Tuesday', and I never asked whether anyone was asleep in it.\n"
    "Now I check who is in the room before I check what the room needs, "
    "so a sleeping baby is never just a task on my list."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 400


def validate(text: str) -> str:
    """Strip and sanity-check the entry; raise ValueError on bad input."""
    text = text.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    lines = text.split("\n")
    if len(lines) != 2 or any(not line.strip() for line in lines):
        raise ValueError(
            f"entry must be exactly two non-empty lines, got {len(lines)}"
        )
    if not all(line.endswith(".") for line in lines):
        raise ValueError("each line must be a single sentence ending with '.'")
    # A second sentence hides behind a mid-line sentence boundary, e.g.
    # "I did X. Then I did Y." — a period followed by a space and a capital
    # letter. Abbreviations such as "3 a.m." do not trigger this: the word
    # after the period is lowercase, so it is not a new sentence.
    if any(re.search(r"[.?!]\s+[A-Z]", line) for line in lines):
        raise ValueError("each line must be a single sentence, not two")
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
