import gi


gi.require_version('Adw', '1')
from gi.repository import Adw, GObject, Gtk

from pygui.species_list_page import SpeciesListPage
from pygui.species_details_page import SpeciesDetailsPage


def bind_properties(list_page: SpeciesListPage, details_page: SpeciesDetailsPage):
    details_page.bind_property(
        source_property="current_species",
        target=list_page,
        target_property="selected_species",
        flags=GObject.BindingFlags.BIDIRECTIONAL
    )


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/main_window.ui")
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"

    species_details_page: SpeciesDetailsPage = Gtk.Template.Child()
    species_list_page: SpeciesListPage = Gtk.Template.Child()

    def __init__(self, application: Adw.Application):
        super().__init__(application=application)
        bind_properties(self.species_list_page, self.species_details_page)
