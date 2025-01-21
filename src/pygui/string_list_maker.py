import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject


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
    _add_item_row: Adw.EntryRow = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self._model = Gtk.StringList()
        self._list_box.bind_model(
            model=self._model,
            create_widget_func=self.add_name_widget_to_list
        )

        self._list_row.set_visible(False)

    def click_add_button(self) -> None:
        self._add_item_row.emit("apply")

    @property
    def entry_field(self) -> str:
        return self._add_item_row.get_text()

    @entry_field.setter
    def entry_field(self, name: str) -> None:
        self._add_item_row.set_text(name)

    def reset_entry_field(self):
        self._add_item_row.set_text("")
        self._add_item_row.set_show_apply_button(False)
        self._add_item_row.set_show_apply_button(True)

    @Gtk.Template.Callback()
    def _on_apply_add_item(self, instance: Adw.EntryRow) -> None:
        name = instance.get_text()
        if name not in self.get_values():
            self._model.append(name)
        self.reset_entry_field()

    def get_values(self) -> list[str]:
        return [item.get_string() for item in self._model]

    def add_name_widget_to_list(self, list_item: Gtk.StringObject) -> RemovableRow:
        text = list_item.get_string()
        list_row = RemovableRow(text)
        list_row.connect("removed", self._on_remove_button_clicked)
        return list_row

    def _on_remove_button_clicked(self, item: RemovableRow):
        value = item.get_text()
        remove(self._model, value)

    def click_remove_on_item(self, item_number: int):
        """ Method required only for testing """
        item: RemovableRow = self._list_box.get_row_at_index(item_number)
        item.click_remove_button()

    def list_row_is_visible(self):
        """ Method required only for testing """
        return self._list_row.get_visible()
