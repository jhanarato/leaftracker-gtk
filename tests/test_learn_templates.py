import pytest
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, GObject

template_defining_property = """\
<interface>
    <template class="WidgetWithTemplateDefinedProperty" parent="GtkBox">
        <property name="template-defined-property">1</property>
    </template>
</interface>
"""


@Gtk.Template(string=template_defining_property)
class WidgetWithTemplateDefinedProperty(Gtk.Box):
    # This needs to match the template, the class name doesn't
    __gtype_name__ = "WidgetWithTemplateDefinedProperty"


def test_cannot_define_property_in_template():
    widget = WidgetWithTemplateDefinedProperty()
    with pytest.raises(TypeError, match="does not have property `template-defined-property'"):
        widget.set_property("template-defined-property", 1)


callback_template = """\
<interface>
    <template class="CallbackWidget" parent="GtkBox">
        <signal name="notify::custom-parameter" handler="parameter_changed"  swapped="no" />
    </template>
</interface>
"""


@Gtk.Template(string=callback_template)
class CallbackWidget(Gtk.Box):
    __gtype_name__ = "CallbackWidget"

    def __init__(self):
        super().__init__()
        self._custom_parameter_value = 0
        self._callback_called = False

    @GObject.Property(type=int)
    def custom_parameter(self) -> int:
        return self._custom_parameter_value

    @custom_parameter.setter
    def custom_parameter(self, new_value: int) -> None:
        self._custom_parameter_value = new_value

    @property
    def callback_called(self) -> bool:
        return self._callback_called

    @Gtk.Template.Callback()
    def parameter_changed(self, *args):
        self._callback_called = True


def test_changing_property_calls_callback():
    button = CallbackWidget()
    button.custom_parameter = 1
    assert button.callback_called is True
