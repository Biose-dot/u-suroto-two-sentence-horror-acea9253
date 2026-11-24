#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "I heard my own voice calling my name from the basement, though I live alone. When I crept downstairs to look, the voice whispered, 'Don't come down \u2014 I'm already up here.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
