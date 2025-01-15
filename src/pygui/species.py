from enum import Enum, auto

import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject

from leaftracker.adapters.elastic.initialise import unit_of_work
from leaftracker.service_layer import services


class SpeciesEditMode(Enum):
    ADD_NEW = auto()
    EDIT_EXISTING = auto()

class SpeciesWriter:
    def __init__(self):
        self.reference: str | None = None

    def write_current_scientific_name(self, name: str) -> None:
        uow = unit_of_work()
        self.reference = services.add_species(name, uow)


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/removable_row.ui")
class RemovableRow(Adw.PreferencesRow):
    __gtype_name__ = "RemovableRow"

    _text : Gtk.Label = Gtk.Template.Child()
    _remove_button : Gtk.Label = Gtk.Template.Child()

    def __init__(self, text: str):
        super().__init__()
        self._text.set_text(text)

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


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_details.ui")
class SpeciesDetailsPage(Adw.NavigationPage):
    __gtype_name__ = "SpeciesDetailsPage"

    reference_display: Adw.EntryRow = Gtk.Template.Child()
    current_scientific_name: Adw.EntryRow = Gtk.Template.Child()
    save_button: Adw.ButtonRow = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self._current_species: str | None = None
        self._writer = SpeciesWriter()

    @GObject.Property(type=str)
    def reference(self) -> str | None:
        return self._current_species

    @reference.setter
    def reference(self, species: str) -> None:
        self._current_species = species

    @Gtk.Template.Callback()
    def reference_changed(self, instance, param):
        self.reference_display.set_text(str(self.reference))

    @Gtk.Template.Callback()
    def save_button_activated(self, instance):
        text = self.current_scientific_name.get_text()
        self._writer.write_current_scientific_name(text)
        self.reference = self._writer.reference

    def mode(self) -> SpeciesEditMode:
        if self.reference is None:
            return SpeciesEditMode.ADD_NEW
        else:
            return SpeciesEditMode.EDIT_EXISTING

    def set_writer(self, writer):
        self._writer = writer


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_list.ui")
class SpeciesListPage(Adw.NavigationPage):
    __gtype_name__ = "SpeciesListPage"

    def __init__(self):
        super().__init__()

    @Gtk.Template.Callback()
    def goto_button_clicked(self, *args):
        print("Clicked")