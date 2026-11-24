#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes the entry text (no trailing newline, nothing else) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Exactly two sentences; the second reframes the first — the comfort of a speaker that says goodnight becomes dread when it speaks unplugged, in a dead voice — and the horror is implied, never explained.
"""
import os

ENTRY = "I finally taught my smart speaker to say goodnight back, and now it does, every night, without being asked. Tonight it whispered goodnight from inside the walls, in my dead mother's voice, before I had even plugged it in."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
