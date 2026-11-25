#!/usr/bin/env python3
"""A one-line roast of my fridge, written for a make.fun bounty.

The joke is the light: it acts surprised every single time."""


import pathlib

LINE = "The fridge light comes on every time I open the door, like it's surprised I came back — honestly, so am I."
OUT = pathlib.Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if "\n" in text or not text or len(text) > 200:
        raise ValueError("entry must be a single line of 1-200 characters")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    if OUT.read_text(encoding="utf-8") != text:
        raise ValueError("entry.txt does not contain the roast exactly")


if __name__ == "__main__":
    main()
