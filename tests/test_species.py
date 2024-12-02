import pytest
from gi.repository import Gio, GObject
resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetailsPage, SpeciesListPage


class TestSpeciesDetailsPage:
    def test_bang_in_species_reference(self):
        details = SpeciesDetailsPage()
        details.set_banged_in("banged in new")
        assert details.get_banged_in() == "banged in new"

    def test_set_species_reference_via_property(self):
        details = SpeciesDetailsPage()
        details.set_property("current-species", "species_reference")
        assert details.get_property("current-species") == "species_reference"

    def test_property_can_be_none(self):
        details = SpeciesDetailsPage()
        details.set_property("current-species", None)
        assert details.get_property("current-species") is None

    def test_notify_when_property_changes(self):
        details = SpeciesDetailsPage()
        details.set_property("current-species", "species_id")
        assert details.property_changed()
