import pytest

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gio, GLib, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species_model import SpeciesModel


class GObjectWithProperty(GObject.Object):
    def __init__(self):
        super().__init__()
        self._prop_a = ""

    @GObject.Property(type=str)
    def prop_a(self):
        return self._prop_a

    @prop_a.setter
    def prop_a(self, new_value):
        self._prop_a = new_value


@pytest.fixture
def gobject_with_property():
    return GObjectWithProperty()


@pytest.fixture
def species_data() -> SpeciesModel:
    species = SpeciesModel()
    species.reference = "reference-xyz"
    species.current_name = "Acacia saligna"
    species.previous_names = ["Acacia old", "Acacia older"]
    return species