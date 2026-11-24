#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "The photo on my wall showed me sleeping, dated last night, though I live alone. This morning there was a new one, dated tonight."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
