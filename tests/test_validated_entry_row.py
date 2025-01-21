import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.validated_entry_row import ValidatedEntryRow

@pytest.fixture
def always_valid() -> ValidatedEntryRow:
    widget = ValidatedEntryRow()
    widget.set_validator(lambda value: True)
    return widget

@pytest.fixture
def always_invalid() -> ValidatedEntryRow:
    widget = ValidatedEntryRow()
    widget.set_validator(lambda value: False)
    return widget

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

    def test_validator_defaults_to_accept_all(self):
        widget = ValidatedEntryRow()
        widget.set_text("some text")
        assert widget.get_show_apply_button()

    def test_valid_text_shows_apply_button(self, always_valid):
        always_valid.set_text("some text")
        assert always_valid.get_show_apply_button()

    def test_invalid_text_hides_apply_button(self, always_invalid):
        always_invalid.set_text("some text")
        assert not always_invalid.get_show_apply_button()

    def test_reset_after_valid_input(self, always_valid):
        always_valid.set_text("some text")
        always_valid.reset()
        assert always_valid.get_text() == ""
        assert always_valid.get_show_apply_button()
