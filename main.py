#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

One dry, petty note from a smart fridge to its owner, written to
/output/entry.txt for the make.fun judge heat. Pure standard library,
fully deterministic: the same single line on every run.
"""

import os

NOTE = "You opened me 14 times today, ate nothing, and closed the door like I was the problem."


def main() -> None:
    """Write the fridge's note to the harness output path."""
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(out_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(NOTE)


if __name__ == "__main__":
    main()
