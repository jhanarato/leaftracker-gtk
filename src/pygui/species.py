import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject


def on_property_changed(instance, param):
    instance.current_species = True


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_details.ui")
class SpeciesDetailsPage(Adw.NavigationPage):
    __gtype_name__ = "SpeciesDetailsPage"

    es_reference: Gtk.Label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self._current_species: str | None = None

    @GObject.Property(type=str)
    def current_species(self) -> str | None:
        return self._current_species

    @current_species.setter
    def current_species(self, species: str):
        self._current_species = species

    @Gtk.Template.Callback()
    def on_property_changed(self, instance, param):
        self.es_reference.props.text = self.get_property("current-species")


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_list.ui")
class SpeciesListPage(Adw.NavigationPage):
    __gtype_name__ = "SpeciesListPage"

    def __init__(self):
        super().__init__()

    @Gtk.Template.Callback()
    def goto_button_clicked(self, *args):
        print("Clicked")