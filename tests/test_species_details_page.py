import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species_model import SpeciesModel
from pygui.species_details_page import SpeciesDetailsPage

@pytest.fixture
def species_data() -> SpeciesModel:
    species = SpeciesModel()
    species.reference = "reference-xyz"
    species.current_name = "Acacia saligna"
    species.previous_names = ["Acacia old", "Acacia older"]
    return species

class TestSpeciesDetailsPage:
    def test_species_property(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("current_species", SpeciesModel())
        assert details_page.get_property("current_species") == SpeciesModel()

    def test_setting_current_species_to_none_creates_a_new_species_model(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("current_species", None)
        assert details_page.get_property("current_species") == SpeciesModel()

    def test_when_reference_is_none_it_is_displayed(self):
        details_page = SpeciesDetailsPage()
        species = SpeciesModel()
        species.reference = None
        details_page.set_property("current_species", species)
        assert details_page.reference_display.get_text() == "None"

    def test_when_current_species_set_fields_are_populated(self, species_data):
        page = SpeciesDetailsPage()
        page.current_species = species_data
        assert page.reference_display.get_text() == species_data.reference
        assert page.current_scientific_name.get_text() == species_data.current_name
        assert page.previous_scientific_names.get_values() == species_data.previous_names

    def test_when_current_name_is_changed_the_edited_species_is_updated(self):
        page = SpeciesDetailsPage()
        page.current_scientific_name.set_text("Eucalyptus rudis")
        assert page._edited_species.current_name == "Eucalyptus rudis"

    def test_when_previous_names_are_changed_the_edited_species_is_updated(self):
        page = SpeciesDetailsPage()
        page.previous_scientific_names.add_string("Acacia old")
        page.previous_scientific_names.add_string("Acacia older")
        assert page._edited_species.previous_names == ["Acacia old", "Acacia older"]

    def test_when_current_species_is_set_edited_is_cloned(self, species_data):
        page = SpeciesDetailsPage()

        assert id(page._current_species) != id(page._edited_species)
        assert page._current_species == page._edited_species

        page.current_species = species_data

        assert id(page._current_species) != id(page._edited_species)
        assert page._current_species == page._edited_species

    def test_save_button_is_not_sensitive_by_default(self):
        page = SpeciesDetailsPage()
        assert not page.save_button.get_sensitive()
