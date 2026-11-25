#!/usr/bin/env python3
"""Write the midnight fridge roast entry to entry.txt.

Competition: Midnight Fridge Roast (1-200 chars, single line, roast a
smart fridge that refuses to open after midnight). Candidates:
A) "Sorry, the fridge is closed: apparently my midnight snack needed
   a reservation, a dress code, and a better life story."
B) "After midnight this fridge turns into a nightclub bouncer:
   'You're not on the list, and neither is that leftover cake.'"
C) "It is past midnight, so the door stays shut: this fridge does not
   negotiate with anyone wearing pyjamas and holding a fork."
Selected B: the refusal itself is the target - the fridge as a
nightclub bouncer working a guest list is a fresh, concrete image,
the line reads aloud in one breath, and the punchline lands last on
the cake that is not on the list. A lists three jokes where one would
do; C is vivid but its laugh is the pyjamas, not the petty rule.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "After midnight this fridge turns into a nightclub bouncer: 'You're not on the list, and neither is that leftover cake.'"
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    # Repair revision: the checks below reject padded or double-spaced
    # lines, so the printed entry is exactly the selected one-liner.
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
