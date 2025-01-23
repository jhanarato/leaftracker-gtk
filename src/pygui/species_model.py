import pytest

from gi.repository import Gio, GObject

class SpeciesModel(GObject.Object):
    def __init__(self):
        super().__init__()
        self._reference: str | None = None
        self._current_name: str | None = None

    @GObject.Property(type=str)
    def reference(self) -> str | None:
        return self._reference

    @reference.setter
    def reference(self, value: str):
        self._reference = value

    @GObject.Property(type=str)
    def current_name(self) -> str | None:
        return self._current_name

    @current_name.setter
    def current_name(self, value: str) -> str | None:
        self._current_name = value
