import pytest

from gi.repository import GObject


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
