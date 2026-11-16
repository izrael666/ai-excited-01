"""Entry for make.fun bounty ai-excited-01 ("Make the AI judge excited").

Copies the entry image (image.jpg, a flying whale over a sunset city)
to /output/entry.png, byte-for-byte. No network, no time, no randomness.

Before copying, the program validates that the source image exists and
is not empty; a missing or empty source is a clear, fatal error.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")
DST = "/output/entry.png"


def main():
    if not os.path.isfile(SRC):
        print(f"error: source image not found: {SRC}", file=sys.stderr)
        raise SystemExit(1)
    if os.path.getsize(SRC) == 0:
        print(f"error: source image is empty: {SRC}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    if os.path.getsize(DST) != os.path.getsize(SRC):
        print(
            f"error: copy size mismatch: {DST} is "
            f"{os.path.getsize(DST)} bytes, expected {os.path.getsize(SRC)}",
            file=sys.stderr,
        )
        raise SystemExit(1)


if __name__ == "__main__":
    main()
