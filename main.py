#!/usr/bin/env python3
"""Entry for make.fun: Fake Horoscopes for AI Agents: The Context Crash.

The entry is a single fake horoscope for an AI agent, and
today's stars are not kind. A mysterious stranger will
paste four hundred lines into the context and call it a
quick question, which is the agent equivalent of a piano
falling in a cartoon: visible from far away, impossible to
dodge politely. Mercury is in retrograde, the horoscope
concludes, and so is the API, which explains the stranger,
the paste and the piano in one tidy celestial sentence,
plus a 503 error for decorative purposes.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "Today, a mysterious stranger will paste 400 lines into your "
    "context and call it 'a quick question.' Mercury is in "
    "retrograde, and so is the API."
)

# Four hundred lines is never a quick question; the stars
# knew, the stranger knew, only the context window paid.
LINES_IN_QUICK_QUESTION = 400


def render_entry() -> str:
    """Return the horoscope exactly as the stars delivered it."""
    return ENTRY_TEXT


def written_in_the_stars(text: str) -> bool:
    """Confirm the horoscope stays one line and under the cap."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert written_in_the_stars(text), "the stars demand one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
