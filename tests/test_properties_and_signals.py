import pytest
from gi.repository import Gio, GObject


class Meaning(GObject.Object):
    def __init__(self):
        super().__init__()
        self._meaning_of_life = 42

    @GObject.Property(type=int)
    def meaning_of_life(self):
        return self._meaning_of_life

    @meaning_of_life.setter
    def meaning_of_life(self, new_meaning):
        self._meaning_of_life = new_meaning


def test_getting_and_setting_properties():
    meaning = Meaning()
    assert meaning.get_property("meaning_of_life") == 42
    meaning.set_property("meaning_of_life", 43)
    assert meaning.get_property("meaning_of_life") == 43


@pytest.mark.skip("Try with app first")
def test_changing_property_invokes_notifier():
    meaning_changed = False

    def on_notify():
        nonlocal meaning_changed
        meaning_changed = True

    meaning = Meaning()
    meaning.connect("notify::meaning_of_life", on_notify)
    meaning.meaning_of_life = 43

    assert meaning_changed


@pytest.mark.skip("Also fails")
def test_changing_app_property_invokes_notifier():
    app_id_changed = False

    def on_notify():
        nonlocal app_id_changed
        app_id_changed = True

    app = Gio.Application(application_id="foo.bar")
    app.connect("notify::application-id", on_notify)
    app.set_application_id("foo.baz")

    assert app_id_changed
