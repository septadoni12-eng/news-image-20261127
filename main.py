#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261127 submission.

Copies the committed entry.png (the tournament-winning variant) into
the make.fun output directory. Deterministic: same input bytes produce
the same output bytes on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print("wrote %s" % dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
