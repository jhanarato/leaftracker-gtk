import pytest
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GObject


callback_template = """\
<interface>
    <template class="CallbackWidget" parent="GtkBox">
        <signal name="notify::custom-property" handler="property_changed"/>
    </template>
</interface>
"""


@Gtk.Template(string=callback_template)
class CallbackWidget(Gtk.Box):
    __gtype_name__ = "CallbackWidget"

    def __init__(self):
        super().__init__()
        self._custom_property_value = 0
        self._callback_called = False

    @GObject.Property(type=int)
    def custom_property(self) -> int:
        return self._custom_property_value

    @custom_property.setter
    def custom_property(self, new_value: int) -> None:
        self._custom_property_value = new_value

    @property
    def callback_called(self) -> bool:
        return self._callback_called

    @Gtk.Template.Callback()
    def property_changed(self, *args):
        self._callback_called = True


def test_changing_property_calls_callback():
    button = CallbackWidget()
    button.custom_property = 1
    assert button.callback_called is True
