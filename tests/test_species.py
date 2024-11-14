from gi.repository import Gio
resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetails, SpeciesList


class TestSpeciesDetails():
    def test_start_in_new_species_mode(self):
        page = SpeciesDetails()
        assert page.species_reference == None
