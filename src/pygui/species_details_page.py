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
        self.update_save_sensitivity()

    @GObject.Property(type=SpeciesModel)
    def current_species(self) -> SpeciesModel:
        return self._current_species

    @current_species.setter
    def current_species(self, species: SpeciesModel) -> None:
        if species is None:
            self._current_species = SpeciesModel()
            self._edited_species = SpeciesModel()
        else:
            self._current_species = species
            self._edited_species = species.clone()

    @GObject.Property(type=SpeciesModel)
    def edited_species(self) -> SpeciesModel:
        return self._edited_species

    @Gtk.Template.Callback()
    def _on_current_species_changed(self, instance, param):
        self.set_fields_to_current_species_values()

    def set_fields_to_current_species_values(self):
        self.reference_display.set_text(self.current_species.reference)
        self.current_scientific_name.set_text(self.current_species.current_name)
        for previous_name in self.current_species.previous_names:
            self.previous_scientific_names.add_string(previous_name)

    @Gtk.Template.Callback()
    def _on_current_scientific_name_edited(self, instance, param):
        self.edited_species.current_name = self.current_scientific_name.get_text()
        self.update_save_sensitivity()

    @Gtk.Template.Callback()
    def _on_previous_scientific_name_edited(self, instance):
        self.edited_species.previous_names = self.previous_scientific_names.get_values()
        self.update_save_sensitivity()

    @Gtk.Template.Callback()
    def _on_save_button_activated(self, instance):
        reference = self.write_species(self._edited_species)
        self._edited_species.reference = reference
        self.current_species = self.edited_species.clone()

    def write_species(self, species: SpeciesModel) -> str:
        return ""

    def update_save_sensitivity(self) -> None:
        self.save_button.set_sensitive(self.is_modified())

    def is_modified(self) -> bool:
        return (self.current_species != self.edited_species)

    def activate_save_button(self):
        self.save_button.emit("activated")
