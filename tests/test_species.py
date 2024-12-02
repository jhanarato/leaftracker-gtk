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
        details.set_property("species-property", "species_reference")
        assert details.get_property("species_property") == "species_reference"

    def test_property_can_be_none(self):
        details = SpeciesDetailsPage()
        details.set_property("species-property", None)
        assert details.get_property("species-property") is None

    def test_notify_when_property_changes(self):
        details = SpeciesDetailsPage()
        details.set_property("species-property", "species_id")
        assert details.property_changed()


class TestSpeciesListPage:
    def test_goto_button_callback(self):
        list_page = SpeciesListPage()
        details_page = SpeciesDetailsPage()
        list_page.set_details_page(details_page)
        list_page.select_species("Acacia saligna")
        list_page.goto_button_clicked()
        assert details_page.get_banged_in() == "Acacia saligna"
