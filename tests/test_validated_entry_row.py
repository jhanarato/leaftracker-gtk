import pytest
from gi.repository import Gio, Gtk, GObject


resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.validated_entry_row import ValidatedEntryRow


class TestValidatedEntryRow:
    def test_create_row(self):
        row = ValidatedEntryRow()