from gi.repository import Gio, Gtk, GObject

from pygui.species_model import SpeciesModel


class TestSpeciesModel:
    def test_reference(self):
        species = SpeciesModel()
        assert species.reference is None
        species.reference = "reference"
        assert species.reference == "reference"

    def test_current_name(self):
        species = SpeciesModel()
        assert species.current_name is None
        species.current_name = "current name"
        assert species.current_name == "current name"

    def test_previous_names(self):
        species = SpeciesModel()
        assert species.previous_names == []
        species.previous_names = ["old name", "older name"]
        assert species.previous_names == ["old name", "older name"]

    def test_append_previous_name(self):
        species = SpeciesModel()
        species.previous_names.append("old name")
        species.previous_names.append("older name")
        assert species.previous_names == ["old name", "older name"]

    def test_add_species_model_to_list_store(self):
        species = SpeciesModel()
        species.current_name = "a name"
        store = Gio.ListStore()
        store.append(species)
        assert store.get_item(0).current_name == "a name"
