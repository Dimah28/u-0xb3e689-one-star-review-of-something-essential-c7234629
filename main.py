#!/usr/bin/env python3
"""Write one deadpan one-star review of sleep, an everyday essential.

Deterministic, stdlib only, no network. Writes /output/entry.txt.
"""

import os

ENTRY = (
    "One star for sleep. I hand it eight hours a night and it returns me tired, "
    "stiff, and late, like a hotel that charges full price for a room it never cleaned."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
