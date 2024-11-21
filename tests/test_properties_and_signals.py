from gi.repository import Gio, GObject


def test_notification_of_property_change():
    app = Gio.Application(application_id="foo.bar")
    assert app.get_property("application_id") == "foo.bar"
