import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.string_list_maker import RemovableRow, StringListMaker, position


class TestRemovableRow:
    def test_emits_remove_signal(self):
        signal_received = False

        def remove_callback(inst):
            nonlocal signal_received
            signal_received = True

        widget = RemovableRow("Row text")
        widget.connect("removed", remove_callback)
        widget.emit("removed")

        assert signal_received

    def test_clicking_remove_button_emits_signal(self):
        signal_received = False

        def remove_callback(inst):
            nonlocal signal_received
            signal_received = True

        widget = RemovableRow("Row text")
        widget.connect("removed", remove_callback)
        widget.click_remove_button()

        assert signal_received

    def test_get_text(self):
        widget = RemovableRow("Row text")
        assert widget.get_text() == "Row text"


class TestStringListMaker:
    def test_can_add_item(self):
        widget = StringListMaker()
        widget.entry_field = "some text"
        widget.click_add_button()
        values = widget.get_values()
        assert values == ["some text"]

    def test_name_field_cleared_after_add(self):
        widget = StringListMaker()
        widget.entry_field = "some text"
        widget.click_add_button()
        assert widget.entry_field == ""

    def test_can_get_list_of_names(self):
        widget = StringListMaker()
        widget.entry_field = "some text"
        widget.click_add_button()
        widget.entry_field = "other text"
        widget.click_add_button()
        assert widget.get_values() == ["some text", "other text"]

    def test_adding_a_duplicate_name_does_not_modify_the_list(self):
        widget = StringListMaker()
        widget.entry_field = "some text"
        widget.click_add_button()
        widget.entry_field = "some text"
        widget.click_add_button()
        assert widget.get_values() == ["some text"]

    def test_position_of_value(self):
        widget = StringListMaker()
        widget.entry_field = "some text"
        widget.click_add_button()
        assert widget.position_of_value("some text") == 0

    def test_remove_value(self):
        widget = StringListMaker()
        widget.entry_field = "some text"
        widget.click_add_button()
        widget.remove_value("some text")
        assert widget.get_values() == []

    def test_item_removed_when_remove_button_clicked(self):
        widget = StringListMaker()
        widget.entry_field = "some text"
        widget.click_add_button()
        widget.click_remove_on_item(0)
        assert widget.get_values() == []


class TestGtkStringListHelpers:
    def test_position_of_value(self):
        string_list = Gtk.StringList.new(["abc", "def", "hij"])
        assert position(string_list, "def") == 1
