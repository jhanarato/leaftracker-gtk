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

    def test_can_give_action_a_handler(self):
        called = False

        def handler(action, parameter):
            nonlocal called
            called = True

        save_action = Gio.SimpleAction(name="save-species", parameter_type=GLib.VariantType("s"))
        save_action.connect("activate", handler)
        save_action.emit("activate", GLib.Variant.new_string("wheetbix"))

        assert called
