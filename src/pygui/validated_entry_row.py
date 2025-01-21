from collections.abc import Callable

import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk, GObject


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/validated_entry_row.ui")
class ValidatedEntryRow(Adw.EntryRow):
    __gtype_name__ = "ValidatedEntryRow"

    def __init__(self):
        super().__init__()
