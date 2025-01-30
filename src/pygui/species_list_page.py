from enum import Enum, auto

import gi

from pygui.species_model import SpeciesModel

gi.require_version('Adw', '1')
from gi.repository import Adw, GObject, Gtk


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_list_page.ui")
class SpeciesListPage(Adw.NavigationPage):
    __gtype_name__ = "SpeciesListPage"

    def __init__(self):
        super().__init__()
        self._selected_species = SpeciesModel()

    @Gtk.Template.Callback()
    def goto_button_clicked(self, *args):
        print("Clicked")

    def click_add_species(self):
        pass

    @Gtk.Template.Callback()
    def _on_add_species_clicked(self, *args):
        self.selected_species = SpeciesModel()

    @GObject.Property(type=SpeciesModel)
    def selected_species(self) -> SpeciesModel:
        return self._selected_species

    @selected_species.setter
    def selected_species(self, selected: SpeciesModel) -> None:
        self._selected_species = selected
