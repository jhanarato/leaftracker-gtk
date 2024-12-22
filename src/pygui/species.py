from enum import Enum, auto

import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject


def on_property_changed(instance, param):
    instance.current_species = True


class SpeciesEditMode(Enum):
    ADD_NEW = auto()
    EDIT_EXISTING = auto()


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_details.ui")
class SpeciesDetailsPage(Adw.NavigationPage):
    __gtype_name__ = "SpeciesDetailsPage"

    reference_display: Adw.EntryRow = Gtk.Template.Child()
    current_scientific_name: Adw.EntryRow = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self._current_species: str | None = None
        self._writer = None

    @GObject.Property(type=str)
    def reference(self) -> str | None:
        return self._current_species

    @reference.setter
    def reference(self, species: str):
        self._current_species = species

    @Gtk.Template.Callback()
    def reference_changed(self, instance, param):
        self.reference_display.set_text(str(self.reference))

    @Gtk.Template.Callback()
    def current_scientific_name_changed(self, instance, param):
        text = self.current_scientific_name.get_text()
        self._writer.write_current_scientific_name(text)

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