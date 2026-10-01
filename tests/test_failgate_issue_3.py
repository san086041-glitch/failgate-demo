"""Regression test for issue #3: unique() must keep first-occurrence order for strings."""

from failgate_demo import unique


def test_unique_keeps_first_occurrence_order_for_strings() -> None:
    # Set-based implementations only *happen* to look ordered for small ints;
    # for strings the iteration order of a set follows hash randomization, so
    # a list with many distinct strings makes the reordering almost certain.
    data = ["b", "a", "b", "c", "a", "d", "e", "c", "f", "g", "h", "i"]
    assert unique(data) == ["b", "a", "c", "d", "e", "f", "g", "h", "i"]

    # The exact example from the issue: the first occurrence of "b" comes first.
    assert unique(["b", "a", "b"]) == ["b", "a"]
