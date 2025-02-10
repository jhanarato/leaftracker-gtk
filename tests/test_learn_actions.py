import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib, Gio


button_ui = """\
    <interface>
      <template class="TheButton" parent="GtkButton">
        <signal name="clicked" handler="on_button_clicked"/>
        <property name="action-name">say.cheese</property>
      </template>
    </interface>
    """

@Gtk.Template(string=button_ui)
class TheButton(Gtk.Button):
    __gtype_name__ = "TheButton"

    @Gtk.Template.Callback()
    def on_button_clicked(self, instance):
        pass


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
        save_action.activate(GLib.Variant.new_string("wheetbix"))

        assert called

    def test_give_button_an_action(self, capsys):
        button = TheButton()
        button_actions = Gio.SimpleActionGroup()
        button.insert_action_group("say", button_actions)
        cheese_action = Gio.SimpleAction(name="cheese")
        button_actions.add_action(cheese_action)
        cheese_action.connect("activate", lambda action, _: print("cheese", end=""))
        button.emit("clicked")
        captured = capsys.readouterr()
        assert captured.out == "cheese"
