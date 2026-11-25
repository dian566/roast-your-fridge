#!/usr/bin/env python3
"""One-line fridge roast for make.fun."""

# The roast is the twist: the fridge light acts surprised every time
# the door opens — and the owner is just as surprised to be back.

import os

ROAST = "The fridge light comes on every time I open the door, like it's surprised I came back — honestly, so am I."


def file_roast() -> None:
    """Write the roast to /output/entry.txt, nothing else."""
    if len(ROAST) > 200 or not ROAST.strip() or "\n" in ROAST:
        raise ValueError("roast must be a single non-empty line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    # Read back: the entry must be exactly the roast, no trailing newline.
    if open("/output/entry.txt", encoding="utf-8").read() != ROAST:
        raise ValueError("entry.txt does not match the roast exactly")


if __name__ == "__main__":  # run it
    file_roast()
