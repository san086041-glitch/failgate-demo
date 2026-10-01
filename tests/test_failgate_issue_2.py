"""Regression test for issue #2: slugify must collapse runs of separators.

A run of spaces and punctuation should become a single separator (0.2.x
behaviour: ``slugify("Hello,  World!") == "hello-world"``).
"""

from failgate_demo import slugify


def test_punctuation_and_spaces_collapse_to_single_separator() -> None:
    assert slugify("Hello,  World!") == "hello-world"
