from failgate_demo import parse


def test_value_containing_hash_is_not_truncated() -> None:
    # Regression test for issue #19: since 0.3.1 the inline-comment handling
    # stripped everything from the first '#' onward, so values such as hex
    # colours came back empty.
    assert parse("[theme]\ncolor = #ff0000\n") == {"theme": {"color": "#ff0000"}}
