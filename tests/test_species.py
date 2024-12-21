from gi.repository import Gio

resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetailsPage


class TestSpeciesDetailsPage:
    def test_set_species_reference_via_property(self):
        details = SpeciesDetailsPage()
        details.set_property("reference", "abc")
        assert details.get_property("reference") == "abc"

    def test_property_can_be_none(self):
        details = SpeciesDetailsPage()
        details.set_property("reference", None)
        assert details.get_property("reference") is None

    def test_changing_reference_property_sets_label(self):
        details = SpeciesDetailsPage()
        details.set_property("reference", "xyz")
        assert details.es_reference.get_text() == "xyz"

    def test_setting_reference_to_none_shows_missing_message(self):
        details = SpeciesDetailsPage()
        details.set_property("reference", None)
        assert details.es_reference.get_text() == "None"


def test_conftest_is_available(fixture_xyz):
    assert fixture_xyz == 1
