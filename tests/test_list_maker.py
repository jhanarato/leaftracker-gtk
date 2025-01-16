import pytest
from gi.repository import Gio, Gtk, GObject

resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.list_maker import RemovableRow

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
