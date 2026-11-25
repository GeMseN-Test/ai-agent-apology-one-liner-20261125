#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry.

One line an AI agent sends its human right after accidentally
pushing something it should not have pushed. The line is 149
characters, under the 160-character limit.

The program writes exactly that one line to /output/entry.txt.
Deterministic: no randomness, no network, no trailing newline.
"""

import os

LINE = "I pushed your private diary to the public repo at 3 AM \u2014 it already has 400 stars, and someone just forked the chapter about your boss. Sweet dreams."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
