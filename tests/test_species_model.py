from pygui.species_model import SpeciesModel


class TestSpeciesModel:
    def test_when_created_reference_is_none(self):
        species = SpeciesModel()
        assert species.reference is None

    def test_can_set_reference(self):
        species = SpeciesModel()
        species.reference = "reference"
        assert species.reference == "reference"