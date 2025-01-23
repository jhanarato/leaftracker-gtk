import pytest

from gi.repository import Gio, GObject

class SpeciesModel(GObject.Object):
    def __init__(self):
        super().__init__()
        self._reference: str | None = None

    @GObject.Property(type=str)
    def reference(self) -> str | None:
        return self._reference

    @reference.setter
    def reference(self, value: str):
        self._reference = value
