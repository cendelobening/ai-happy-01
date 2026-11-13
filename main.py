"""ai-happy-01 entry runner.

Copies the bundled picture (entry.png, sitting next to this file) into the
output directory and checks that the copy arrived intact.

The picture itself is the entry: a little ghost offering its favourite star.
This script does nothing creative at run time on purpose -- it just delivers
the exact same bytes every time, so the judge always sees the same image.

Usage: python3 main.py
Output: $MAKEFUN_OUTPUT_DIR/entry.png (falls back to /output/entry.png)
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / SOURCE_NAME

    shutil.copyfile(source, target)

    # The copy is only good if it is byte-for-byte identical to the source.
    if target.stat().st_size != source.stat().st_size:
        print("copy failed: size mismatch", file=sys.stderr)
        return 1
    if _sha256(target) != _sha256(source):
        print("copy failed: checksum mismatch", file=sys.stderr)
        return 1

    print(f"wrote {target} ({target.stat().st_size} bytes, sha256 OK)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
