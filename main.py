#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — one line, written to the output file.

Pure Python standard library only. The line is the whole entry:
a smart speaker that hears 'play music' as 'order 12 pizzas'.
Gate: entry.txt must be UTF-8 text of 1 to 200 characters.
"""

import os

REPLY = (
    "My smart speaker hears 'play music' as 'order 12 pizzas' — "
    "it understands me better than my family does."
)


def main():
    if not 1 <= len(REPLY) <= 200:
        raise SystemExit("reply must be 1-200 characters, got %d" % len(REPLY))
    if REPLY != REPLY.strip():
        raise SystemExit("reply must not start or end with whitespace")
    if "\n" in REPLY or "\r" in REPLY:
        raise SystemExit("reply must be a single line, no newlines")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.txt")
    data = REPLY.encode("utf-8")
    with open(out, "wb") as f:
        f.write(data)
    with open(out, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit(
            "verification failed: entry.txt does not match the reply "
            "(wrote %d bytes, read back %d bytes)" % (len(data), len(back))
        )
    print("chars=%d bytes=%d" % (len(REPLY), len(data)))
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
