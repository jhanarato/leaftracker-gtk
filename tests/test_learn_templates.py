import pytest
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

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



@pytest.mark.skip("Work on other test first.")
def test_changing_property_calls_callback():
    button = CallbackButton()
    button.string_parameter = "Frosty Fruits"
    assert button.callback_called