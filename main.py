#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "The baby monitor started narrating my daughter's dreams in my voice, three seconds before she dreamed them. Tonight it said, 'She's dreaming of the man in the attic now \u2014 and he just learned how to open doors.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
