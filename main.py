"""Two-line robot apology for the make.fun bounty.

Line one owns one specific, concrete mistake: running the vacuum in
the nursery at 3 a.m. because the schedule said so, without checking
whether anyone was asleep in the room. Line two names the lesson and
the changed behaviour: check who is in the room before checking what
the room needs. The script validates the entry and writes it to
/output/entry.txt.
"""

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
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
