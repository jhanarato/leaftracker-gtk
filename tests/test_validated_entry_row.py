import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.validated_entry_row import ValidatedEntryRow


class Receiver:
    def __init__(self):
        self.received = False

    def callback(self, instance):
        self.received = True


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
        assert widget.is_valid()

    def test_can_use_a_validation_function(self):
        widget = ValidatedEntryRow()
        widget.set_validator(lambda value: True)
        assert widget.is_valid()
        widget.set_validator(lambda value: False)
        assert not widget.is_valid()

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

    def test_clear_after_valid_input(self, always_valid):
        always_valid.set_text("some text")
        always_valid.clear()
        assert always_valid.get_text() == ""
        assert always_valid.get_show_apply_button()

    def test_clear_after_invalid_input(self, always_invalid):
        always_invalid.set_text("some text")
        always_invalid.clear()
        assert always_invalid.get_text() == ""
        assert always_invalid.get_show_apply_button()

    def test_issues_apply_valid_signal_for_valid_input(self, always_valid):
        receiver = Receiver()
        always_valid.connect("apply-valid", receiver.callback)
        always_valid.set_text("some text")
        always_valid.emit("apply")
        assert receiver.received

    def test_does_not_issue_apply_valid_signal_for_invalid_input(self, always_invalid):
        receiver = Receiver()
        always_invalid.connect("apply-valid", receiver.callback)
        always_invalid.set_text("some text")
        always_invalid.emit("apply")
        assert not receiver.received

    def test_validate_acacia_s(self):
        def is_acacia_s(value: str) -> bool:
            return value == "Acacia s"

        widget = ValidatedEntryRow()
        widget.set_validator(is_acacia_s)
        widget.set_text("Acacia s")
        assert widget.is_valid()