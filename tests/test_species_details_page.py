import pytest
from gi.repository import Gio, Gtk, GObject

resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species_model import SpeciesModel
from pygui.species_details_page import SpeciesDetailsPage


class TestSpeciesDetailsPage:
    def test_set_species_reference(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("reference", "abc")
        assert details_page.get_property("reference") == "abc"

    def test_set_species_reference_to_none(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("reference", None)
        assert details_page.get_property("reference") is None

    def test_reference_display_is_updated_when_reference_changed(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("reference", "xyz")
        assert details_page.reference_display.get_text() == "xyz"

    def test_setting_reference_to_none_shows_missing_message(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("reference", None)
        assert details_page.reference_display.get_text() == "None"

    def test_changing_bound_property_sets_reference(self, gobject_with_property):
        details_page = SpeciesDetailsPage()
        gobject_with_property.bind_property(
            source_property="prop-a",
            target=details_page,
            target_property="reference",
            flags=GObject.BindingFlags.BIDIRECTIONAL
        )
        gobject_with_property.set_property("prop-a", "cba")
        assert details_page.reference == "cba"

    def test_species_property(self):
        details_page = SpeciesDetailsPage()
        details_page.set_property("current_species", SpeciesModel())
        assert details_page.get_property("current_species") == SpeciesModel()

    def test_reference_display_updated_when_current_species_changed(self):
        page = SpeciesDetailsPage()
        species = SpeciesModel()
        species.reference = "reference-xyz"
        page.current_species = species
        assert page.reference_display.get_text() == "reference-xyz"
        