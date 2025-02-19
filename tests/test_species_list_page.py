import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()


from pygui.species_model import SpeciesModel
from pygui.species_list_page import SpeciesListPage


class TestSpeciesListPage:
    def test_can_create(self):
        page = SpeciesListPage()

    def test_can_add_a_new_species(self):
        page = SpeciesListPage()
        page.click_add_species()
        new_species = SpeciesModel()
        assert page.selected_species == new_species
