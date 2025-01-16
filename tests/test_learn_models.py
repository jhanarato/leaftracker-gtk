import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk
import pytest

@pytest.fixture
def string_list() -> Gtk.StringList:
    return Gtk.StringList.new(["abc", "def", "hij"])

def test_length(string_list):
    assert len(string_list) == 3