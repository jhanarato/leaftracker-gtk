import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.list_maker import RemovableRow, PreviousScientificNames


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


class TestPreviousScientificNames:
    def test_can_add_name(self):
        widget = PreviousScientificNames()
        widget.name_field = "Acacia saligna"
        widget.click_add_button()
        name = widget.get_name_from_item(0)
        assert name == "Acacia saligna"

    def test_name_field_cleared_after_add(self):
        widget = PreviousScientificNames()
        widget.name_field = "Acacia saligna"
        widget.click_add_button()
        assert widget.name_field == ""

    def test_can_get_list_of_names(self):
        widget = PreviousScientificNames()
        widget.name_field = "Acacia abc"
        widget.click_add_button()
        widget.name_field = "Acacia xyz"
        widget.click_add_button()
        assert widget.get_species_names() == ["Acacia abc", "Acacia xyz"]

    def test_adding_a_duplicate_name_does_not_modify_the_list(self):
        widget = PreviousScientificNames()
        widget.name_field = "Acacia saligna"
        widget.click_add_button()
        widget.name_field = "Acacia saligna"
        widget.click_add_button()
        assert widget.get_species_names() == ["Acacia saligna"]