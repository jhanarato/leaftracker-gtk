import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk

from .species_details import SpeciesDetails

@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/main_window.ui")
class MainWindow(Adw.ApplicationWindow):
    __gtype_name__ = "MainWindow"

    species_details = SpeciesDetails()

    def __init__(self, application: Adw.Application):
        super().__init__(application=application)
