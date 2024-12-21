import pytest
from gi.repository import Gio, GObject

resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetailsPage, SpeciesEditMode


@pytest.fixture
def details_page() -> SpeciesDetailsPage:
    return SpeciesDetailsPage()


class TestSpeciesDetailsPage:
    def test_set_species_reference(self, details_page):
        details_page.set_property("reference", "abc")
        assert details_page.get_property("reference") == "abc"

    def test_set_species_reference_to_none(self, details_page):
        details_page.set_property("reference", None)
        assert details_page.get_property("reference") is None

    def test_reference_display_is_updated_when_reference_changed(self, details_page):
        details_page.set_property("reference", "xyz")
        assert details_page.reference_display.get_text() == "xyz"

    def test_setting_reference_to_none_shows_missing_message(self, details_page):
        details_page.set_property("reference", None)
        assert details_page.reference_display.get_text() == "None"

    def test_changing_bound_property_sets_reference(self, details_page, gobject_with_property):
        gobject_with_property.bind_property(
            source_property="prop-a",
            target=details_page,
            target_property="reference",
            flags=GObject.BindingFlags.BIDIRECTIONAL
        )
        gobject_with_property.set_property("prop-a", "cba")
        assert details_page.reference == "cba"

    def test_starts_in_add_new_mode(self, details_page):
        assert details_page.mode() == SpeciesEditMode.ADD_NEW

    def test_switches_mode_to_edit_existing(self, details_page):
        details_page.set_property("reference", "a reference")
        assert details_page.mode() == SpeciesEditMode.EDIT_EXISTING

    def test_switches_mode_to_add_new(self, details_page):
        details_page.set_property("reference", "a reference")
        details_page.set_property("reference", None)
        assert details_page.mode() == SpeciesEditMode.ADD_NEW

