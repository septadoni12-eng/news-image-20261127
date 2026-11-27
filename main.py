#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261127 submission.

Copies the committed entry.png (the tournament-winning variant) into
the make.fun output directory. Deterministic: same input bytes produce
the same output bytes on every run.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    src_hash = sha256_file(SRC)
    dst_hash = sha256_file(dst)
    print("source sha256: %s" % src_hash)
    print("output sha256: %s" % dst_hash)
    if src_hash != dst_hash:
        print("ERROR: output hash does not match source hash", file=sys.stderr)
        return 1
    print("wrote %s" % dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
