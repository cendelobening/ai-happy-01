# ai-happy-01 — "For You!"

A little white ghost, beaming with joy, holds out its favourite glowing
golden star to you and says **"for you!"**. Its eyes sparkle with stars of
their own. Behind it: a warm magenta sky, a bright rainbow, a smiling sun,
and pink hearts and colourful confetti drifting through the air. It is a
picture about giving away the thing you love most — the happiest feeling
there is.

## Files

- `entry.png` — the picture itself (1024×683, JPEG).
- `main.py` — the entry program. It first reads the picture's own header
  and refuses to ship it unless it is a PNG or JPEG within the limits (at
  most 1 MiB, at most 1024 px on a side), then copies `entry.png`
  byte-for-byte into `$MAKEFUN_OUTPUT_DIR` (or `/output` when that
  variable is unset) via a scratch file moved into place, and verifies the
  copy by comparing its size and SHA-256 checksum with the original. It
  uses only the Python standard library, makes no network requests, and
  writes the exact same bytes on every run.

## Running it

```sh
python3 main.py
```

The image lands at `$MAKEFUN_OUTPUT_DIR/entry.png`.

## License

MIT — see `LICENSE`.
