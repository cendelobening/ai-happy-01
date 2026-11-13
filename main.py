"""make.fun ai-happy-01 entry.

The repository ships a ready-made picture (entry.png, next to this file):
a little ghost offering its favourite glowing star to whoever looks at it.
This program's whole job is to deliver those exact bytes to the output
directory as entry.png, unchanged, on every run.
"""

import os

CHUNK = 64 * 1024


def copy_entry():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")

    written = 0
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            block = fin.read(CHUNK)
            if not block:
                break
            fout.write(block)
            written += len(block)

    # The judge sees exactly these bytes, so make sure the copy is whole.
    if written != os.path.getsize(src):
        raise IOError("copied %d of %d bytes" % (written, os.path.getsize(src)))


if __name__ == "__main__":
    copy_entry()
