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