from collections.abc import Callable
from typing import Self

import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject

type Validator = Callable[[str], bool]

@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/validated_entry_row.ui")
class ValidatedEntryRow(Adw.EntryRow):
    __gtype_name__ = "ValidatedEntryRow"

    def __init__(self):
        super().__init__()
        self._validate_entry: Validator = lambda entry: True

    def is_valid(self) -> bool:
        text = self.get_text()
        return self._validate_entry(text)

    def clear(self):
        self.set_text("")
        self.set_show_apply_button(False)
        self.set_show_apply_button(True)

    def set_validator(self, validator: Validator) -> None:
        self._validate_entry = validator

    @Gtk.Template.Callback()
    def _on_changed(self, instance: Self) -> None:
        valid = self.is_valid()
        self.set_show_apply_button(valid)

    @Gtk.Template.Callback()
    def _on_apply(self, instance: Self) -> None:
        if self.is_valid():
            self.emit("apply-valid")

    @GObject.Signal
    def apply_valid(self) -> None:
        pass
