from gi.repository import Gio, GObject

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
        assert species.previous_names is None
        species.previous_names = ["old name", "older name"]
        assert species.previous_names == ["old name", "older name"]