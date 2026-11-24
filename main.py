"""Copy the entry image to the grader output directory.

No network, no randomness: every run writes the same bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    # The grader runs this in a sandbox with /output writable; locally the
    # output directory can be overridden with MAKEFUN_OUTPUT_DIR.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
