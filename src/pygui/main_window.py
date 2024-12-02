import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk

from pygui.species import SpeciesDetailsPage, SpeciesList


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/main_window.ui")
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"

    species_details_page: SpeciesDetailsPage = Gtk.Template.Child()
    species_list: SpeciesList = Gtk.Template.Child()

    def __init__(self, application: Adw.Application):
        super().__init__(application=application)
        self.species_list.set_details_page(self.species_details_page)
        self.species_list.select_species("Acacia dentifera")
