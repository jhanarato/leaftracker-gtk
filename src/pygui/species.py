import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_details.ui")
class SpeciesDetails(Adw.NavigationPage):
    __gtype_name__ = "SpeciesDetails"

    banged_in: Gtk.Label = Gtk.Template.Child()

    def __init__(self):
        super().__init__()

    def select_species(self, reference: str) -> None:
        self.set_banged_in(reference)

    def get_banged_in(self) -> str:
        return self.banged_in.get_label()

    def set_banged_in(self, text: str) -> None:
        self.banged_in.set_label(text)


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_list.ui")
class SpeciesList(Adw.NavigationPage):
    __gtype_name__ = "SpeciesList"

    def __init__(self):
        super().__init__()
        self._species_reference = None
        self._details_page = None

    def set_details_page(self, page: SpeciesDetails) -> None:
        self._details_page = page

    def select_species(self, reference: str) -> None:
        self._species_reference = reference
        self._details_page.select_species(reference)

    @Gtk.Template.Callback()
    def goto_button_clicked(self, *args):
        if self._species_reference:
            self._details_page.select_species(self._species_reference)
