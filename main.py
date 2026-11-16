"""Entry for make.fun bounty ai-excited-01 ("Make the AI judge excited").

Copies the entry image (image.jpg, a flying whale over a sunset city)
to /output/entry.png, byte-for-byte. No network, no time, no randomness.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
