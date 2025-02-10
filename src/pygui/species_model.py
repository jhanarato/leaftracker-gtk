from typing import Self

from gi.repository import Gio, GObject

class SpeciesModel(GObject.Object):
    def __init__(self,
                 reference: str = "",
                 current_name: str = "",
                 previous_names: list[str] = None):
        super().__init__()

        self._reference: str = reference
        self._current_name: str = current_name

        if previous_names is None:
            self._previous_names = list()
        else:
            self._previous_names = previous_names

    def clone(self) -> Self:
        return SpeciesModel(
            reference=self._reference,
            current_name=self._current_name,
            previous_names=self._previous_names,
        )

    @GObject.Property(type=str)
    def reference(self) -> str:
        return self._reference

    @reference.setter
    def reference(self, value: str) -> None:
        if value is None:
            self._reference = ""
        else:
            self._reference = value

    @GObject.Property(type=str)
    def current_name(self) -> str | None:
        return self._current_name

    @current_name.setter
    def current_name(self, value: str) -> None:
        if value is None:
            self._current_name = ""
        else:
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
        return f"SpeciesModel({self.reference!r}, {self.current_name!r}, {self.previous_names!r})"

