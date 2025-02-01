import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib, Gio


button_ui = """\
    <interface>
      <template class="TheButton" parent="GtkButton">
      </template>
    </interface>
    """

@Gtk.Template(string=button_ui)
class TheButton(Gtk.Button):
    __gtype_name__ = "TheButton"


class TestSimpleAction:
    def test_activate_with_no_parameters(self):
        action_name = None

        def callback(action, _):
            nonlocal action_name
            action_name = action.get_name()

        simple_action = Gio.SimpleAction(name="simple")
        simple_action.connect("activate", callback)

        assert action_name is None
        simple_action.activate()
        assert action_name == "simple"
