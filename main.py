"""The One-Line Cat Joke That Lands.

One joke about cats, a single line under 200 characters, written
to /output/entry.txt.

The setup is familiar -- the cat knocks the laptop off the table
and stares -- and the turn is a misdirection: she wasn't being a
jerk, she was peer-reviewing the code, and she rejected it. The
joke works on a fresh angle (the cat as a code reviewer) rather
than a pun anyone has heard before, it says everything in a few
words with no padding after the punchline, and it is the kind of
joke a person retells to a friend the same day.
"""

import os

SETUP = "My cat knocked my laptop off the table, stared at me,"
TURN = "and I realised: she wasn't being a jerk,"
PUNCHLINE = "she was peer-reviewing my code \u2014 and she rejected it."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(setup: str, turn: str, punchline: str) -> str:
    """Join the joke's setup, turn and punchline into one line."""
    parts = [setup.strip(), turn.strip(), punchline.strip()]
    line = " ".join(parts)
    return line


def check_joke(line: str) -> str:
    """Gate the joke the way the sealed scorer does.

    /output/entry.txt must be UTF-8 text of 1 to 200 characters, and
    the brief asks for a single line.
    """
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"joke is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the joke"
    assert "\n" not in line, "the joke must stay on one line"
    return line


def joke_notes(line: str) -> dict:
    """Per-bounty joke check: setup, surprise turn, no padding.

    The judge picks the joke that makes it laugh hardest on the
    first read, so the entry must be a one-line joke about cats with
    a setup and a turn that lands -- a surprise or a misdirection
    rather than a much-heard pun -- and it must end on the
    punchline, with no explanation after it.
    """
    lowered = line.lower()
    assert "cat" in lowered, "the joke must be about a cat"
    assert "laptop" in lowered, "the setup must be concrete"
    assert "peer-reviewing" in lowered, "the turn must be a fresh angle"
    assert "rejected" in lowered, "the punchline must land on the verdict"
    assert line.rstrip().endswith("it."), "nothing may follow the punchline"
    words = line.split()
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_joke(compose(SETUP, TURN, PUNCHLINE))
    notes = joke_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
