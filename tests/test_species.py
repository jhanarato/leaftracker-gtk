from gi.repository import Gio
resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.main_window import MainWindow


def test_set_new_species():
    pass
