from gi.repository import Gio
resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetails, SpeciesList


class TestSpeciesDetails():
    def test_start_in_new_species_mode(self):
        page = SpeciesDetails()
        assert page.species_reference is None

    def test_get_label_text(self):
        details = SpeciesDetails()
        assert details.get_label_text() == "ui defined label"

    def test_set_label_text(self):
        details = SpeciesDetails()
        details.set_label_text("a new label")
        assert details.get_label_text() == "a new label"


class TestSpeciesList():
    def test_set_species_reference(self):
        list_page = SpeciesList()
        details_page = SpeciesDetails()
        list_page.set_details_page(details_page)
        list_page.select_species("a_species")
        assert details_page.species_reference == "a_species"

    def test_goto_button_callback(self):
        list_page = SpeciesList()
        details_page = SpeciesDetails()
        list_page.set_details_page(details_page)
        list_page.goto_button_clicked()
        assert details_page.species_reference == "callback_set_reference"
