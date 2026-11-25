"""The funniest honest error message a washing machine could show.

The line is fixed. A set of small named checks inspects it
before it is saved: it must be real text, fit the 200-character
limit, contain no control characters, open with ERROR the way
a genuine error message does, name the washing machine, keep
clean edges with no doubled spaces or line breaks, end with
sentence punctuation, and carry letters. Links are refused --
an error message should not need a URL to land. The first
check that objects prints its reason to stderr and exits with
code 1, so a bad line is never written. No input, no network,
no randomness, no clock: every run writes the same bytes.
"""

import sys
from pathlib import Path

ENTRY = "ERROR E-12: I am a washing machine, not a magician. Your red sock is now everyone's problem."
LIMIT = 200
DEST = Path("/output/entry.txt")
END_MARKS = ".!?"


def fail(reason):
    print(f"invalid: {reason}", file=sys.stderr)
    raise SystemExit(1)


def check_present(text):
    if not text or text.strip() == "":
        fail("entry is empty")


def check_inside_limit(text):
    if len(text) > LIMIT:
        fail("entry is longer than 200 characters")


def check_without_controls(text):
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        fail("entry contains control characters")


def check_opens_like_an_error(text):
    if not text.startswith("ERROR"):
        fail("entry must start with ERROR")


def check_names_the_machine(text):
    if "washing machine" not in text:
        fail("entry must mention the washing machine")


def check_clean_line(text):
    if text != text.strip() or "  " in text or "\n" in text or "\r" in text:
        fail("entry has ragged edges or line breaks")


def check_proper_ending(text):
    if not text or text[-1] not in END_MARKS:
        fail("entry must end with . ! or ?")


def check_letters_present(text):
    if not any(ch.isalpha() for ch in text):
        fail("entry has no letters")


def check_not_punctuation_only(text):
    if not any(ch.isalnum() for ch in text):
        fail("entry is punctuation only")


def check_not_digits_only(text):
    if text.isdigit():
        fail("entry is digits only")


def check_without_links(text):
    if "http" in text:
        fail("entry must not contain a link")


def check_capital_start(text):
    # An error message opens with a capital letter, never a lowercase one.
    if text and text[0].islower():
        fail("entry must not start with a lowercase letter")


CHECKS = (
    check_present,
    check_inside_limit,
    check_without_controls,
    check_opens_like_an_error,
    check_names_the_machine,
    check_clean_line,
    check_proper_ending,
    check_letters_present,
    check_not_punctuation_only,
    check_not_digits_only,
    check_without_links,
    check_capital_start,
)


def validate(text):
    for check in CHECKS:
        check(text)


def main():
    validate(ENTRY)
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
