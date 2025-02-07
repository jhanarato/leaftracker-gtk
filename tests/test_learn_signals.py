import pytest

from gi.repository import Gio, GObject, Gtk


class NoargSignaller(GObject.Object):
    def __init__(self):
        super().__init__()

    @GObject.Signal
    def noarg_signal(self) -> None:
        pass

def test_noarg_signal():
    signaller = NoargSignaller()
    signaller.emit("noarg-signal")


class SideEffectSignaller(GObject.Object):
    def __init__(self):
        super().__init__()

    @GObject.Signal
    def signal_with_side_effect(self) -> None:
        print("A side effect of emit")

def test_signal_with_side_effect(capsys):
    signaller = SideEffectSignaller()
    signaller.emit("signal-with-side-effect")
    captured = capsys.readouterr()
    assert captured.out == "A side effect of emit\n"


class ReturnTypeSignaller(GObject.Object):
    def __init__(self):
        super().__init__()

    @GObject.Signal(return_type=bool)
    def signal_with_return_type(self) -> bool:
        pass

def test_signal_with_return_type():
    instance_type = None
    def handler(instance: ReturnTypeSignaller) -> bool:
        nonlocal instance_type
        instance_type = type(instance)
        return True

    signaller = ReturnTypeSignaller()
    signaller.connect("signal-with-return-type", handler)
    signaller.emit("signal-with-return-type")

    assert instance_type == ReturnTypeSignaller


class NotifySignaller(GObject.Object):
    def __init__(self):
        super().__init__()

    @GObject.Property(type=str)
    def static_property(self) -> str:
        return "static property"

    @static_property.setter
    def static_property(self, value: str):
        pass


def test_handle_notify_signal():
    param_passed = None

    def handler(instance, param):
        nonlocal param_passed
        param_passed = param

    signaller = NotifySignaller()
    # Note: static-property is referred to as a "detail"
    signaller.connect("notify::static-property", handler)
    signaller.static_property = "This changes nothing"

    assert isinstance(param_passed, GObject.ParamSpecString)

