from collections.abc import Callable

import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject

from pygui.validated_entry_row import ValidatedEntryRow, Validator

@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/removable_row.ui")
class RemovableRow(Adw.PreferencesRow):
    __gtype_name__ = "RemovableRow"

    _text : Gtk.Label = Gtk.Template.Child()
    _remove_button : Gtk.Label = Gtk.Template.Child()

    def __init__(self, text: str):
        super().__init__()
        self._text.set_text(text)

    def get_text(self) -> str:
        return self._text.get_text()

    @GObject.Signal
    def removed(self) -> None:
        pass

    def click_remove_button(self) -> None:
        self._remove_button.emit("clicked")

    @Gtk.Template.Callback()
    def _on_remove_button_clicked(self, instance: Gtk.Button):
        self.emit("removed")


def position(string_list: Gtk.StringList, value: str) -> int | None:
    for i, item in enumerate(string_list):
        if item.get_string() == value:
            return i
    return None


def remove(string_list: Gtk.StringList, value: str) -> None:
    p = position(string_list, value)
    if p is not None:
        string_list.remove(p)


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/string_list_maker.ui")
class StringListMaker(Adw.PreferencesGroup):
    __gtype_name__ = "StringListMaker"

    _list_row: Adw.PreferencesRow = Gtk.Template.Child()
    _list_box: Gtk.ListBox = Gtk.Template.Child()
    _add_item_row: ValidatedEntryRow = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self._model = Gtk.StringList()
        self._list_box.bind_model(
            model=self._model,
            create_widget_func=self.create_removable_row
        )

        self._list_row.set_visible(False)

        self._model.connect("items_changed", self._on_string_list_changed)

    @property
    def entry_field(self) -> str:
        return self._add_item_row.get_text()

    @entry_field.setter
    def entry_field(self, name: str) -> None:
        self._add_item_row.set_text(name)

    @GObject.Signal
    def list_changed(self) -> None:
        pass

    @Gtk.Template.Callback()
    def _on_apply_valid_add_item(self, instance: ValidatedEntryRow) -> None:
        text = instance.get_text()
        if text not in self.get_values():
            self.add_string(text)
        self._add_item_row.clear()

    def _on_string_list_changed(self, instance, foo, bar, baz):
        # foo, bar and baz are integers, what they mean I don't know.
        self.emit("list-changed")

    def add_string(self, value: str) -> None:
        self._model.append(value)
        self._list_row.set_visible(True)

    def get_values(self) -> list[str]:
        return [item.get_string() for item in self._model]

    def create_removable_row(self, list_item: Gtk.StringObject) -> RemovableRow:
        text = list_item.get_string()
        list_row = RemovableRow(text)
        list_row.connect("removed", self._on_remove_button_clicked)
        return list_row

    def _on_remove_button_clicked(self, item: RemovableRow):
        value = item.get_text()
        remove(self._model, value)
        if self._model.get_n_items() == 0:
            self._list_row.set_visible(False)

    def list_row_is_visible(self):
        return self._list_row.get_visible()

    def set_validator(self, validator: Validator):
        self._add_item_row.set_validator(validator)

    def click_add_button(self) -> None:
        """ Method required only for testing """
        self._add_item_row.emit("apply")

    def click_remove_on_item(self, item_number: int):
        """ Method required only for testing """
        item: RemovableRow = self._list_box.get_row_at_index(item_number)
        item.click_remove_button()

