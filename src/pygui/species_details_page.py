from enum import Enum, auto

import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject

from pygui.string_list_maker import StringListMaker

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


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_details_page.ui")
class SpeciesDetailsPage(Adw.NavigationPage):
    __gtype_name__ = "SpeciesDetailsPage"

    reference_display: Adw.EntryRow = Gtk.Template.Child()
    current_scientific_name: Adw.EntryRow = Gtk.Template.Child()
    previous_scientific_names: StringListMaker = Gtk.Template.Child()
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
