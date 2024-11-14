from gi.repository import Gio
resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from leaftracker_gtk.main import main


def test_run_main_function():
    main(None)
