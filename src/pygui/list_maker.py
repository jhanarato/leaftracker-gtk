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


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/previous_scientific_names.ui")
class PreviousScientificNames(Adw.PreferencesGroup):
    __gtype_name__ = "PreviousScientificNames"

    _add_name_entry_row: Adw.EntryRow = Gtk.Template.Child()
    _names_list_box: Gtk.ListBox = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self._model = Gtk.StringList()
        self._names_list_box.bind_model(
            model=self._model,
            create_widget_func=self.add_name_widget_to_list
        )

    @property
    def name_field(self) -> str:
        return self._add_name_entry_row.get_text()

    @name_field.setter
    def name_field(self, name: str) -> None:
        self._add_name_entry_row.set_text(name)

    def click_add_button(self) -> None:
        self._add_name_entry_row.emit("apply")

    def get_name_from_item(self, index: int) -> str:
        item = self._model.get_item(index)
        return item.get_string()

    @Gtk.Template.Callback()
    def on_apply_add_name(self, instance: Adw.EntryRow) -> None:
        name = instance.get_text()
        if name not in self.get_species_names():
            self._model.append(name)

        self._add_name_entry_row.set_text("")
        self.reset_apply_button()

    def reset_apply_button(self):
        self._add_name_entry_row.set_show_apply_button(False)
        self._add_name_entry_row.set_show_apply_button(True)

    def add_name_widget_to_list(self, list_item: Gtk.StringObject) -> RemovableRow:
        text = list_item.get_string()
        list_row = RemovableRow(text)
        return list_row

    def get_species_names(self) -> list[str]:
        return [item.get_string() for item in self._model]

    def click_remove_on_item(self, item_number: int):
        pass
