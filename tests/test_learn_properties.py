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
    assert meaning.get_property("meaning-of-life") == 42
    meaning.set_property("meaning_of_life", 43)
    assert meaning.get_property("meaning-of-life") == 43


def test_changing_property_invokes_notifier():
    notified = Notification()

    meaning = Meaning()
    meaning.connect("notify::meaning-of-life", notified)
    meaning.set_property("meaning-of-life", 43)

    assert notified.notified
    assert isinstance(notified.instance, Meaning)
    assert isinstance(notified.param, GObject.ParamSpecInt)
    assert notified.param.param_id == 1
    assert notified.param.name == "meaning-of-life"


def test_changing_app_property_invokes_notifier():
    notified = Notification()

    app = Gio.Application(application_id="foo.bar")
    app.connect("notify::application-id", notified)
    app.set_application_id("foo.baz")

    assert isinstance(notified.instance, Gio.Application)
    assert isinstance(notified.param, GObject.ParamSpecString)
    assert notified.param.param_id == 1
    assert notified.param.name == "application-id"
    assert notified.notified


class SelfNotifier(GObject.Object):
    def __init__(self):
        super().__init__()
        self._some_property = 0
        self.notified = False
        self.connect("notify::some-property", self.notify_method)

    @GObject.Property(type=int)
    def some_property(self):
        return self._some_property

    @some_property.setter
    def some_property(self, value):
        self._some_property = value

    def notify_method(self, instance, param):
        self.notified = True


def test_changing_param_invokes_notify_method():
    self_notifier = SelfNotifier()
    assert not self_notifier.notified
    self_notifier.set_property("some-property", 77)
    assert self_notifier.notified


@pytest.mark.skip("Work on method call test first.")
def test_changing_property_calls_callback():
    button = CallbackButton()
    button.string_parameter = "Frosty Fruits"
    assert button.callback_called
