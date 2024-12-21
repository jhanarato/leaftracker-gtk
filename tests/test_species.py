from gi.repository import Gio, GObject

resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetailsPage


class TestSpeciesDetailsPage:
    def test_set_species_reference(self):
        details = SpeciesDetailsPage()
        details.set_property("reference", "abc")
        assert details.get_property("reference") == "abc"

    def test_set_species_reference_to_none(self):
        details = SpeciesDetailsPage()
        details.set_property("reference", None)
        assert details.get_property("reference") is None

    def test_reference_field_is_updated_when_reference_changed(self):
        details = SpeciesDetailsPage()
        details.set_property("reference", "xyz")
        assert details.reference_display.get_text() == "xyz"

    def test_setting_reference_to_none_shows_missing_message(self):
        details = SpeciesDetailsPage()
        details.set_property("reference", None)
        assert details.reference_display.get_text() == "None"

    def test_changing_bound_property_sets_reference(self, gobject_with_property):
        details_page = SpeciesDetailsPage()
        gobject_with_property.bind_property(
            "prop-a", details_page, "reference",
            GObject.BindingFlags.BIDIRECTIONAL
        )
        gobject_with_property.set_property("prop-a", "cba")
        assert details_page.reference == "cba"


def test_gobject_has_property(gobject_with_property):
    gobject_with_property.set_property("prop-a", "pqr")
    assert gobject_with_property.get_property("prop-a") == "pqr"
