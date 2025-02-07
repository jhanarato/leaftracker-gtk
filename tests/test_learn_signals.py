import pytest

from gi.repository import Gio, GObject, Gtk


class NoargSignaller(GObject.Object):
    @GObject.Signal
    def noarg_signal(self) -> None:
        pass

def test_noarg_signal():
    called = False

    def handler(instance: NoargSignaller):
        assert isinstance(instance, NoargSignaller)
        nonlocal called
        called = True

    signaller = NoargSignaller()
    signaller.connect("noarg-signal", handler)
    signaller.emit("noarg-signal")

    assert called


class SideEffectSignaller(GObject.Object):
    @GObject.Signal
    def signal_with_side_effect(self) -> None:
        print("A side effect of emit")

def test_signal_with_side_effect(capsys):
    signaller = SideEffectSignaller()
    signaller.emit("signal-with-side-effect")
    captured = capsys.readouterr()
    assert captured.out == "A side effect of emit\n"


class ReturnTypeSignaller(GObject.Object):
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


class ArgumentSignaller(GObject.Object):
    @GObject.Signal(arg_types=(int, str))
    def signal_with_arguments(self, param_one: int, param_two: str) -> None:
        pass


def test_signal_with_arguments():
    argument_one = None
    argument_two = None

    def handler(instance: ArgumentSignaller, param_one: int, param_two: str) -> None:
        assert isinstance(instance, ArgumentSignaller)
        nonlocal argument_one, argument_two
        argument_one = param_one
        argument_two = param_two

    signaller = ArgumentSignaller()
    signaller.connect("signal-with-arguments", handler)
    signaller.emit("signal-with-arguments", 123, "abc")

    assert (argument_one, argument_two) == (123, "abc")


class NotifySignaller(GObject.Object):
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

