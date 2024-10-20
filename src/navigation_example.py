import gi

gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk


@Gtk.Template(resource_path="/org/bswa/Leaftracker/ui/navigation_example.ui")
class NavigationExample(Adw.ApplicationWindow):
    __gtype_name__ = "NavigationExample"


    def __init__(self, application: Adw.Application):
        super().__init__(application=application)