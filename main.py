#!/usr/bin/env python3
"""Write one original joke about working beside AI coding agents.

The program writes a single-line joke to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). The joke is deterministic, offline, and uses only
the Python standard library.
"""

import os
import sys

JOKE = (
    "My AI coding agent rehearsed flawlessly, then live on stage it "
    "confidently 'fixed' the working code and left a comment apologizing "
    "for the inconvenience."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Self-checks: one line, 1-280 Unicode code points, valid UTF-8,
    # and not only whitespace.
    assert 1 <= len(JOKE) <= 280, f"joke length {len(JOKE)} out of range"
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert JOKE == JOKE.strip(), "joke must not have leading/trailing space"
    encoded = JOKE.encode("utf-8")  # raises if not valid UTF-8
    assert encoded.decode("utf-8") == JOKE

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    print(f"Wrote {len(JOKE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
