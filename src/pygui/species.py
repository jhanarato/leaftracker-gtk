import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/species_details.ui")
class SpeciesDetails(Adw.NavigationPage):
    __gtype_name__ = "SpeciesDetails"



    def __init__(self):
        super().__init__()
        self._species_reference = None

    @property
    def species_reference(self) -> str | None:
        return self._species_reference

    def select_species(self, reference: str) -> None:
        self._species_reference = reference

    def get_label_text(self) -> str:
        return "ui defined label"


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
        self._details_page.select_species(reference)

    @Gtk.Template.Callback()
    def goto_button_clicked(self, *args):
        self.select_species("callback_set_reference")
