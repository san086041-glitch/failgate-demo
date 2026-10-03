from failgate_demo import config, parse


def test_section_header_with_inline_comment_parses() -> None:
    """A comment after a section header must not be treated as a key/value line."""
    text = "[server]  # main server\nhost = example.org\n"
    assert parse(text) == {"server": {"host": "example.org"}}
    assert config.parse(text) == {"server": {"host": "example.org"}}
