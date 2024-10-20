import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_details.ui")
class SpeciesDetails(Adw.NavigationPage):
    __gtype_name__ = "SpeciesDetails"
