import sys

import gi
gi.require_version('Adw', '1')
from gi.repository import Adw, Gio

resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.main_window import MainWindow


def test_open_and_close_main_window():
    def on_activate(app):
        window = MainWindow(application=app)
        window.present()
        window.close()

    app = Adw.Application(application_id='org.bswa.Leaftracker')
    app.connect('activate', on_activate)
    app.run(sys.argv)
