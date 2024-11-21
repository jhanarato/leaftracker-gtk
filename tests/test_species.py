import pytest
from gi.repository import Gio, GObject
resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetails, SpeciesList


class TestSpeciesDetails():
    def test_bang_in_species_reference(self):
        details = SpeciesDetails()
        details.set_banged_in("banged in new")
        assert details.get_banged_in() == "banged in new"

    def test_set_species_reference_via_property(self):
        details = SpeciesDetails()
        details.set_property("species_property", "species_reference")
        assert details.get_property("species_property") == "species_reference"

    def test_property_can_be_none(self):
        details = SpeciesDetails()
        details.set_property("species_property", None)
        assert details.get_property("species_property") is None

    def test_notify_when_property_changes(self):
        details = SpeciesDetails()
        details.set_property("species_property", "species_id")
        details.emit("notify::species_property", GObject.ParamSpecString())
        assert details.property_changed()


class TestSpeciesList():
    def test_goto_button_callback(self):
        list_page = SpeciesList()
        details_page = SpeciesDetails()
        list_page.set_details_page(details_page)
        list_page.select_species("Acacia saligna")
        list_page.goto_button_clicked()
        assert details_page.get_banged_in() == "Acacia saligna"
