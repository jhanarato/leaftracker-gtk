from collections.abc import Callable
from typing import Self

import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/validated_entry_row.ui")
class ValidatedEntryRow(Adw.EntryRow):
    __gtype_name__ = "ValidatedEntryRow"

    def __init__(self):
        super().__init__()
        self._validate_entry: Callable[[str], bool] = lambda entry: True

    def entry_is_valid(self) -> bool:
        text = self.get_text()
        return self._validate_entry(text)

    def reset(self):
        self.set_text("")
        self.set_show_apply_button(False)
        self.set_show_apply_button(True)

    def set_validator(self, validator: Callable[[str], bool]):
        self._validate_entry = validator

    @Gtk.Template.Callback()
    def _on_changed(self, instance: Self) -> None:
        text = self.get_text()
        valid = self._validate_entry(text)
        self.set_show_apply_button(valid)
