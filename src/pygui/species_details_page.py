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
        self._edited_species = SpeciesModel()
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
        # Note that we can set the property to None, but we shouldn't.
        if self.current_species is None:
            return

        self.show_reference()
        self.show_current_species()
        self.show_previous_names()

    @Gtk.Template.Callback()
    def _on_edited(self, instance, param):
        self._edited_species.current_name = self.current_scientific_name.get_text()

    def show_reference(self) -> None:
        reference = str(self.current_species.reference)
        self.reference_display.set_text(reference)

    def show_current_species(self) -> None:
        current_name = str(self.current_species.current_name)
        self.current_scientific_name.set_text(current_name)

    def show_previous_names(self) -> None:
        for previous_name in self.current_species.previous_names:
            self.previous_scientific_names.add_string(previous_name)

    @Gtk.Template.Callback()
    def save_button_activated(self, instance):
        pass
