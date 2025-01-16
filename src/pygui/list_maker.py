import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/removable_row.ui")
class RemovableRow(Adw.PreferencesRow):
    __gtype_name__ = "RemovableRow"

    _text : Gtk.Label = Gtk.Template.Child()
    _remove_button : Gtk.Label = Gtk.Template.Child()

    def __init__(self, text: str):
        super().__init__()
        self._text.set_text(text)

    def get_text(self) -> str:
        return self._text.get_text()

    @GObject.Signal
    def removed(self) -> None:
        pass

    def click_remove_button(self) -> None:
        self._remove_button.emit("clicked")

    @Gtk.Template.Callback()
    def _on_remove_button_clicked(self, instance: Gtk.Button):
        self.emit("removed")