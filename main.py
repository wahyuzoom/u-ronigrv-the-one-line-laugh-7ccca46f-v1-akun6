#!/usr/bin/env python3
"""The One-Line Laugh — one-line entry.

Writes a single funny sentence (at most 200 characters) to
/output/entry.txt: an everyday truth with a surprise at the end.

Stdlib only, offline, deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

# The line: a to-do list, a breakup, and no explanation needed.
# Counted at 52 characters — inside the 1..200 window.
LINE = "My to-do list and I have agreed to see other people."


def output_dir() -> Path:
    """Where the grader expects the entry file.

    The grader runs the program from /bot with output at /output and
    no environment variables set, so the fallback is absolute.
    """
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    """Write the line to entry.txt."""
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


# Guard: only run when executed directly.
if __name__ == "__main__":
    main()
