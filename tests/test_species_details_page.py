import pytest
from gi.repository import Gio, GLib, Gtk, GObject


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
    def test_on_creation_models_are_initialised(self):
        page = SpeciesDetailsPage()
        assert page.current_species == SpeciesModel()
        assert page.edited_species == SpeciesModel()

    def test_when_current_species_set_to_none_new_species_created(self):
        page = SpeciesDetailsPage()
        page.current_species = None
        assert page.current_species == SpeciesModel()

    def test_set_new_current_species(self):
        page = SpeciesDetailsPage()
        page.current_species = SpeciesModel()
        assert page.current_species == SpeciesModel()

    def test_set_populated_current_species(self, species_data):
        page = SpeciesDetailsPage()
        page.current_species = species_data
        assert page.current_species == species_data.clone()

    def test_when_current_species_set_to_none_edited_species_is_new_species(self):
        page = SpeciesDetailsPage()
        page.current_species = None
        assert page.edited_species == SpeciesModel()

    def test_when_new_current_species_set_to_new_species_edited_is_new_species(self):
        page = SpeciesDetailsPage()
        page.current_species = SpeciesModel()
        assert page.edited_species == SpeciesModel()

    def test_when_current_species_set_to_populated_species_edited_is_same(self, species_data):
        page = SpeciesDetailsPage()
        page.current_species = species_data
        assert page.edited_species == species_data.clone()

    def test_when_reference_is_set_to_none_text_shown_is_empty_string(self):
        page = SpeciesDetailsPage()
        species = SpeciesModel()
        species.reference = None
        assert page.reference_display.get_text() == ""

    def when_current_scientific_name_is_none_text_is_none(self):
        page = SpeciesDetailsPage()
        species = SpeciesModel()
        page.current_species = species
        assert page.current_scientific_name.get_text() == "None"

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

    def test_save_is_not_sensitive_by_default(self):
        page = SpeciesDetailsPage()
        assert not page.save_button.get_sensitive()

    def test_save_is_sensitive_when_current_name_changed(self):
        page = SpeciesDetailsPage()
        page.current_scientific_name.set_text("Eucalyptus rudis")
        assert page.save_button.get_sensitive()

    def test_save_is_not_sensitive_when_current_species_set(self, species_data):
        page = SpeciesDetailsPage()
        page.current_scientific_name.set_text("Eucalyptus rudis")
        assert page.save_button.get_sensitive()
        page.current_species = species_data
        assert not page.save_button.get_sensitive()

    def test_save_is_sensitive_when_previous_name_added(self):
        page = SpeciesDetailsPage()
        assert not page.save_button.get_sensitive()
        page.previous_scientific_names.add_string("Acacia old")
        assert page.save_button.get_sensitive()

    def test_can_add_an_action_group(self):
        page = SpeciesDetailsPage()
        action_group = Gio.SimpleActionGroup()
        page.insert_action_group("species", action_group)

    def test_can_add_save_species_action(self):
        page = SpeciesDetailsPage()
        action_group = Gio.SimpleActionGroup()
        save_action = Gio.SimpleAction(name="save-species")
        action_group.add_action(save_action)
        page.insert_action_group("species", action_group)

    def test_when_save_activated_reference_assigned_to_edited_species(self):
        page = SpeciesDetailsPage()
        page.write_species = lambda species: "reference-ijk"
        page.activate_save_button()
        assert page.edited_species.reference == "reference-ijk"

    def test_current_species_updated_after_saving(self):
        page = SpeciesDetailsPage()
        page.write_species = lambda species: "reference-ijk"
        page.current_scientific_name.set_text("Eucalyptus rudis")
        page.activate_save_button()
        assert page.current_species == page.edited_species
