from failgate_demo import get, parse

CONFIG = "name = demo\n[server]\nhost = example.org\n"


def test_keys_before_first_section_go_to_default() -> None:
    assert parse(CONFIG) == {
        "DEFAULT": {"name": "demo"},
        "server": {"host": "example.org"},
    }
    assert get(CONFIG, "DEFAULT", "name") == "demo"
