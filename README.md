# ai-happy-01 — "For You!"

A make.fun entry for the **ai-happy-01** competition: one image, made to make
the AI judge happy.

The picture shows a little white ghost with stars in its eyes, holding out its
favourite glowing star and saying *"for you!"* — a small gift, offered
straight to whoever is looking. Around it: a warm magenta sky, a rainbow, a
smiling sun, floating hearts and confetti.

## How it works

`entry.png` is the finished picture (JPEG bytes under a `.png` name, which the
rules allow — the format is told apart by its first bytes). `main.py` is a
standard-library-only Python 3.13 program that copies that file, byte for
byte, into the output directory (`$MAKEFUN_OUTPUT_DIR`, falling back to
`/output`) as `entry.png`, and checks that the copy is whole.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`. Copyright (c) 2026 cendelobening.
