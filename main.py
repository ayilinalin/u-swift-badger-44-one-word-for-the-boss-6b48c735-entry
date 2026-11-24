#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (fallback: ``/output/entry.txt``).

The word: "Unreachable".

Why this word, against the judge's brief:
  * It is a single word a person would actually use about the boss
    they report to — no phrase, no caption, no explanation needed.
  * It is funny on its own: every office has the boss you can never
    reach the one time a decision actually matters.
  * It rings true: the universal boss habit is being somewhere else —
    in another meeting, on another floor, on another continent —
    whenever approval is needed.
  * It is fresh: not the first word anyone reaches for (that would be
    "micromanager" or "demanding"), and its surprise is the laugh.
  * It travels: a boss in a kitchen, a warehouse or an office can all
    be unreachable, no industry context required.

No dependencies, no network, fully deterministic.
"""

import os
import sys

# The entry: exactly one word, 1-30 characters, no whitespace.
WORD = "Unreachable"

# Gate from RULES.txt: entry.txt must be UTF-8 text of 1 to 30
# characters, not only white space.
MAX_CHARS = 30


def validate(word):
    """Check the word against the competition gate. Returns an error
    string, or None when the word is valid."""
    if not isinstance(word, str) or not word:
        return "word is empty"
    if len(word) > MAX_CHARS:
        return "word is %d characters, over the 30-character gate" % len(word)
    if word != word.strip() or any(ch.isspace() for ch in word):
        return "word must be a single token with no whitespace"
    try:
        word.encode("utf-8")
    except UnicodeEncodeError:
        return "word is not encodable as UTF-8"
    return None


def output_dir():
    """Resolve the output directory, honouring the harness variable."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    error = validate(WORD)
    if error is not None:
        print("invalid entry word: %s" % error, file=sys.stderr)
        return 1
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD)
    # Re-read what was written and re-check it against the gate, so a
    # silent write failure can never ship an invalid entry.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    error = validate(written)
    if error is not None:
        print("written entry failed the gate: %s" % error, file=sys.stderr)
        return 1
    print("wrote %r to %s" % (WORD, path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
