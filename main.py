#!/usr/bin/env python3
"""Draft entry writer for the two-sentence horror bounty (v1)."""

import os

ENTRY = "The old radio in the attic only ever played one song, and tonight it was playing my voice. I went upstairs to unplug it, and the voice on the stairs behind me said I was already too late."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
