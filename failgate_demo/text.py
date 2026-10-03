from __future__ import annotations

import unicodedata


def _ascii(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def slugify(text: str, sep: str = "-") -> str:
    """Lowercase ASCII words joined by `sep`: "Hello, World!" -> "hello-world"."""
    text = _ascii(text).lower()
    # 0.3.0: replaced the regex with a faster character loop
    out: list[str] = []
    for ch in text:
        if ch.isalnum():
            out.append(ch)
        elif out and out[-1] != sep:
            out.append(sep)
    return "".join(out).strip(sep)
