import sys

import gi

from pygui.species_model import SpeciesModel

gi.require_version('Adw', '1')
from gi.repository import Adw, Gio

resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.main_window import MainWindow, bind_properties
from pygui.species_details_page import SpeciesDetailsPage
from pygui.species_list_page import SpeciesListPage


def test_open_and_close_main_window():
    def on_activate(app):
        window = MainWindow(application=app)
        window.present()
        window.close()

    app = Adw.Application(application_id='org.bswa.Leaftracker')
    app.connect('activate', on_activate)
    app.run(sys.argv)

def test_bind_properties():
    details_page = SpeciesDetailsPage()
    list_page = SpeciesListPage()
    bind_properties(list_page, details_page)
    species = SpeciesModel()
    species.reference = "reference-xyz"
    list_page.selected_species = species
    assert details_page.current_species.reference == "reference-xyz"
