import pytest

from gi.repository import Gio, GObject

class SpeciesModel(GObject.Object):
    def __init__(self):
        super().__init__()
