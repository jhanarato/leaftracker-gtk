from gi.repository import Gio
resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetails, SpeciesList


class TestSpeciesDetails():
    def test_get_label_text(self):
        details = SpeciesDetails()
        assert details.get_label_text() == "banged in"

    def test_set_label_text(self):
        details = SpeciesDetails()
        details.set_label_text("banged in new")
        assert details.get_label_text() == "banged in new"


class TestSpeciesList():
    def test_goto_button_callback(self):
        list_page = SpeciesList()
        details_page = SpeciesDetails()
        list_page.set_details_page(details_page)
        list_page.select_species("Acacia saligna")
        list_page.goto_button_clicked()
        assert details_page.get_label_text() == "Acacia saligna"
