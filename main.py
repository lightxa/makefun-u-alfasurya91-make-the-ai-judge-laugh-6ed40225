"""Make the AI Judge Laugh: one line about office life.

The entry is a single deadpan joke: a meeting called to fix too many
meetings, which runs over and spawns one more. One concrete incident,
one counted detail (14 weekly meetings, a 15th booked), no explanation.
The program writes the line to /output/entry.txt and self-checks the
kit's gate before exiting: UTF-8, one line, 1 to 200 characters.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

JOKE = (
    "My boss called a meeting about our 14 weekly meetings. "
    "It ran over, so we booked a 15th."
)


def main() -> None:
    """Write the joke and verify it passes the kit's gate."""
    line = JOKE.strip()
    assert line, "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == line, "round-trip mismatch"
    assert 1 <= len(written) <= 200, "written entry must be 1 to 200 characters"
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
