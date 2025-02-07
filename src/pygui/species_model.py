from typing import Self

from gi.repository import Gio, GObject

class SpeciesModel(GObject.Object):
    def __init__(self):
        super().__init__()
        self._reference: str | None = None
        self._current_name: str | None = None
        self._previous_names: list[str] = list()

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
    def current_name(self, value: str) -> None:
        self._current_name = value

    @GObject.Property(type=GObject.TYPE_STRV)
    def previous_names(self) -> list[str]:
        return self._previous_names

    @previous_names.setter
    def previous_names(self, values: list[str]) -> None:
        self._previous_names = values

    def __eq__(self, other: Self) -> bool:
        return (
            self.reference,
            self._current_name,
            self._previous_names
        ) == (
            other.reference,
            other._current_name,
            other._previous_names
        )

    def __ne__(self, other: Self) -> bool:
        return not (self == other)

    def __repr__(self) -> str:
        return f"SpeciesModel({self.reference}, {self.current_name}, {self.previous_names})"

