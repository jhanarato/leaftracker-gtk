import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.validated_entry_row import ValidatedEntryRow


class TestValidatedEntryRow:
    def test_entry_is_valid_by_default(self):
        widget = ValidatedEntryRow()
        assert widget.entry_is_valid()

    def test_can_use_a_validation_function(self):
        widget = ValidatedEntryRow()
        widget.set_validator(lambda value: True)
        assert widget.entry_is_valid()
        widget.set_validator(lambda value: False)
        assert not widget.entry_is_valid()

    def test_valid_text_shows_apply_button(self):
        widget = ValidatedEntryRow()
        widget.set_validator(lambda value: True)
        widget.set_text("some text")
        assert widget.get_show_apply_button()

    def test_invalid_text_hides_apply_button(self):
        widget = ValidatedEntryRow()
        widget.set_validator(lambda value: False)
        widget.set_text("some text")
        assert not widget.get_show_apply_button()