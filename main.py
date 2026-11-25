"""One-line missed-deadline excuse.

Writes line.txt (the entry: one sentence, 1-200 characters) to
/output/entry.txt byte for byte, exactly as the bounty requires.

MAKEFUN_OUTPUT_DIR, when set, stands in for /output so the entry can
be tested locally without touching the real output directory.

The program refuses to write anything that would fail the gate:
it checks the source is valid UTF-8, 1-200 characters, a single line,
and not only white space, then verifies the written copy byte for byte.

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_FILE = HERE / "line.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"

MAX_CHARS = 200


def load_entry() -> tuple[bytes, str]:
    raw = SOURCE_FILE.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"line.txt is not valid UTF-8: {exc}") from exc
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, allowed 1-{MAX_CHARS}"
        )
    if text.startswith("\ufeff"):
        raise ValueError("entry must not start with a UTF-8 byte order mark")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no line breaks")
    return raw, text


def main() -> None:
    raw, text = load_entry()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(raw)

    written = OUTPUT_FILE.read_bytes()
    if written != raw:
        raise ValueError(
            f"written copy differs from line.txt: wrote {len(written)} "
            f"bytes, source is {len(raw)} bytes"
        )
    print(
        f"wrote {OUTPUT_FILE} "
        f"({len(raw)} bytes, {len(text)} characters, 1 line)"
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
