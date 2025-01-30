from enum import Enum, auto

import gi
from leaftracker.service_layer import services

from pygui.species_model import SpeciesModel

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject

from pygui.string_list_maker import StringListMaker
from pygui.validated_entry_row import ValidatedEntryRow


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_details_page.ui")
class SpeciesDetailsPage(Adw.NavigationPage):
    __gtype_name__ = "SpeciesDetailsPage"

    reference_display: Adw.EntryRow = Gtk.Template.Child()
    current_scientific_name: ValidatedEntryRow = Gtk.Template.Child()
    previous_scientific_names: StringListMaker = Gtk.Template.Child()
    save_button: Adw.ButtonRow = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self._current_species = SpeciesModel()
        self.current_scientific_name.set_validator(services.validate_taxon_name)
        self.previous_scientific_names.set_validator(services.validate_taxon_name)

    @GObject.Property(type=SpeciesModel)
    def current_species(self) -> SpeciesModel:
        return self._current_species

    @current_species.setter
    def current_species(self, species: SpeciesModel) -> None:
        self._current_species = species

    @Gtk.Template.Callback()
    def _on_current_species_changed(self, instance, param):
        self.reference_display.set_text(str(self.current_species.reference))

    @Gtk.Template.Callback()
    def save_button_activated(self, instance):
        pass
