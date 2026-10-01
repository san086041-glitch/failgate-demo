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
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1].strip()
            sections.setdefault(current, {})
            continue
        _store(sections, current, line)
    return sections


def _strip_inline_comment(value: str) -> str:
    """Drop a trailing inline comment, keeping '#' that is part of the value.

    A '#' only starts a comment when some non-blank value precedes it and it is
    separated from that value by whitespace, so "#ff0000", "#channel" and
    "https://example.org/page#frag" survive, while "8080  # http" is stripped.
    """
    index = value.find("#")
    if index > 0 and value[:index].strip() and value[index - 1].isspace():
        return value[:index]
    return value


def _store(sections: dict[str, dict[str, str]], section: str | None, line: str) -> None:
    key, sep, value = line.partition("=")
    if not sep:
        raise ValueError(f"expected 'key = value', got {line!r}")
    # 0.3.1: support inline comments ("port = 8080  # http")
    value = _strip_inline_comment(value)
    sections[section][key.strip()] = value.strip()


def get(text: str, section: str, key: str, default: str | None = None) -> str | None:
    return parse(text).get(section, {}).get(key, default)
