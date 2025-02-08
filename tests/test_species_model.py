from gi.repository import Gio, Gtk, GObject

from pygui.species_model import SpeciesModel

class TestSpeciesModel:
    def test_reference_empty_string_when_created(self):
        species = SpeciesModel()
        assert species.reference == ""

    def test_set_reference_property(self):
        species = SpeciesModel()
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

    def test_equality_when_created(self):
        species_a = SpeciesModel()
        species_b = SpeciesModel()
        assert species_a == species_b
        assert species_b == species_a

    def test_equality_with_reference(self):
        species_a = SpeciesModel()
        species_b = SpeciesModel()
        species_a.reference = "abc"
        species_b.reference = "abc"
        assert species_a == species_b
        assert species_b == species_a

    def test_equality_with_current_name(self):
        species_a = SpeciesModel()
        species_b = SpeciesModel()
        species_a.current_name = "Acacia saligna"
        species_b.current_name = "Acacia saligna"
        assert species_a == species_b
        assert species_b == species_a

    def test_equality_with_previous_names(self):
        species_a = SpeciesModel()
        species_b = SpeciesModel()
        species_a.previous_names = ["Acacia old", "Acacia older"]
        species_b.previous_names = ["Acacia old", "Acacia older"]
        assert species_a == species_b
        assert species_b == species_a

    def test_inequality(self):
        species_a = SpeciesModel()
        species_b = SpeciesModel()
        assert (species_a == species_b)
        assert not (species_a != species_b)

    def test_init_sets_properties(self):
        species = SpeciesModel(
            reference="ref123",
            current_name="Acacia saligna",
            previous_names=["Acacia old", "Acacia older"],
        )

        assert f"{species!r}" == "SpeciesModel('ref123', 'Acacia saligna', ['Acacia old', 'Acacia older'])"

    def test_clone(self):
        species = SpeciesModel(
            reference="ref123",
            current_name="Acacia saligna",
            previous_names=["Acacia old", "Acacia older"],
        )

        species_clone = species.clone()

        assert id(species) != id(species_clone)
        assert species == species_clone
