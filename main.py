#!/usr/bin/env python3
"""The One-Line Exit — make.fun entry.

Writes one funny single-line resignation letter to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only whitespace, exactly one line.
"""

import os

LINE = (
    "I resign as night-shift lighthouse keeper: six years warning ships "
    "about the rocks, and not once did anyone warn me about this job."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
