import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import pytest

@pytest.fixture
def string_list() -> Gtk.StringList:
    return Gtk.StringList.new(["abc", "def", "hij"])


def test_length(string_list):
    assert len(string_list) == 3


def get_position_of_matching_string(string_list: list[str], to_match: str) -> int | None:
    for position, item in enumerate(string_list):
        if item.get_string() == to_match:
            return position
    return None

@pytest.mark.parametrize(
    "value,position",
    [("abc", 0), ("def", 1), ("hij", 2)]
)
def test_get_position_of_matching_string(string_list, value, position):
    assert get_position_of_matching_string(string_list, value) == position
