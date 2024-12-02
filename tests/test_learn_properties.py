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


class ObjectA(GObject.Object):
    def __init__(self):
        super().__init__()
        self._property_a = ""

    @GObject.Property(type=str)
    def property_a(self) -> str:
        return self._property_a

    @property_a.setter
    def property_a(self, value: str):
        self._property_a = value


class ObjectB(GObject.Object):
    def __init__(self):
        super().__init__()
        self._property_b = ""

    @GObject.Property(type=str)
    def property_b(self) -> str:
        return self._property_b

    @property_b.setter
    def property_b(self, value: str):
        self._property_b = value


def test_changing_bound_property_propagates():
    object_a = ObjectA()
    object_a.set_property("property-a", "start-value-a")

    object_b = ObjectB()
    object_b.set_property("property-b", "start-value-b")

    object_a.bind_property("property-a", object_b, "property-b", GObject.BindingFlags.BIDIRECTIONAL)

    object_a.set_property("property-a", "value-changed-a")
    assert object_b.get_property("property-b") == "value-changed-a"

    object_b.set_property("property-b", "value-changed-b")
    assert object_a.get_property("property-a") == "value-changed-b"
