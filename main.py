"""The Robot Apology — deliver the two-line confession.

Reads the apology from entry.txt next to this file, writes it to
/output/entry.txt for the judge, and prints it to stdout.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def check_shape(text):
    """The gate wants 1-400 chars of non-blank text in exactly two lines."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is blank")
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1-400 characters")
    lines = stripped.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")


def main():
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as handle:
        text = handle.read()
    check_shape(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(text)
    print(text, end="")


if __name__ == "__main__":
    main()
