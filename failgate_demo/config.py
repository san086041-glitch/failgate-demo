"""Parse INI-style text.

    # comment
    name = demo          <- keys before the first section belong to "DEFAULT"
    [server]
    host = example.org
    port = 8080          # inline comments are stripped (0.3.1)
"""

from __future__ import annotations

DEFAULT = "DEFAULT"


def parse(text: str) -> dict[str, dict[str, str]]:
    """Return {section: {key: value}}. Keys before the first section go to DEFAULT."""
    sections: dict[str, dict[str, str]] = {}
    current = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith(("#", ";")):
            continue
        # 0.3.1: strip inline comments before classifying the line, so that a
        # comment after a section header ("[server]  # main") is not mistaken
        # for a key/value line.
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1].strip()
            sections.setdefault(current, {})
            continue
        _store(sections, current, line)
    return sections


def _store(sections: dict[str, dict[str, str]], section: str | None, line: str) -> None:
    key, sep, value = line.partition("=")
    if not sep:
        raise ValueError(f"expected 'key = value', got {line!r}")
    # 0.3.1: support inline comments ("port = 8080  # http")
    value = value.split("#", 1)[0]
    sections[section][key.strip()] = value.strip()


def get(text: str, section: str, key: str, default: str | None = None) -> str | None:
    return parse(text).get(section, {}).get(key, default)
