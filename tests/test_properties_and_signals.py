import pytest
from gi.repository import Gio, GObject


class Notification():
    def __init__(self):
        self.notified = False
        self.instance = None
        self.param = None

    def __call__(self, instance, param):
        self.instance = instance
        self.param = param
        self.notified = True


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


@pytest.mark.skip("Have to figure out how parameter notifications work")
def test_changing_property_invokes_notifier():
    notified = Notification()

    meaning = Meaning()
    meaning.connect("notify::meaning_of_life", notified)
    meaning.meaning_of_life = 43

    assert notified.notified


def test_changing_app_property_invokes_notifier():
    notified = Notification()

    app = Gio.Application(application_id="foo.bar")
    app.connect("notify::application-id", notified)
    app.set_application_id("foo.baz")

    assert isinstance(notified.instance, Gio.Application)
    assert isinstance(notified.param, GObject.ParamSpecString)
    assert notified.param.name == "application-id"
    assert notified.notified
