#!/usr/bin/env python3
"""Two Lines to Your Past Self — writes the entry to /output/entry.txt.

Stdlib only, no network, deterministic output: the same two lines every run.
"""
import os

ENTRY = (
    "Don't send that 2 a.m. text to Maya from the kitchen floor \u2014 put the phone down and go to sleep.\n"
    "Because you didn't send it, she never read the words you couldn't take back — and ten years later, she still calls you first.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
