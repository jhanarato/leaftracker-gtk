import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species_model import SpeciesModel
from pygui.species_details_page import SpeciesDetailsPage
from pygui.species_list_page import SpeciesListPage


class TestSpeciesDetailsPage:
    def test_species_property(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("current_species", SpeciesModel())
        assert details_page.get_property("current_species") == SpeciesModel()

    def test_can_set_species_property_to_none(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("current_species", None)
        assert details_page.get_property("current_species") is None

    def test_when_reference_is_none_it_is_displayed(self):
        details_page = SpeciesDetailsPage()
        species = SpeciesModel()
        species.reference = None
        details_page.set_property("current_species", species)
        assert details_page.reference_display.get_text() == "None"

    def test_when_current_species_set_fields_are_populated(self):
        page = SpeciesDetailsPage()
        species = SpeciesModel()
        species.reference = "reference-xyz"
        species.current_name = "Acacia saligna"
        species.previous_names = ["Acacia old", "Acacia older"]
        page.current_species = species
        assert page.reference_display.get_text() == "reference-xyz"
        assert page.current_scientific_name.get_text() == "Acacia saligna"
        assert page.previous_scientific_names.get_values() == ["Acacia old", "Acacia older"]
