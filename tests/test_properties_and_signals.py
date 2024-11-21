from gi.repository import Gio, GObject


def test_getting_and_setting_properties():
    app = Gio.Application(application_id="foo.bar")
    assert app.get_property("application_id") == "foo.bar"
    app.set_property("application_id", "foo.bar.baz")
    assert app.get_property("application_id") == "foo.bar.baz"
