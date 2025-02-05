import pytest

from gi.repository import Gio, GObject, Gtk


class Signaller(GObject.Object):
    def __init__(self):
        super().__init__()

    @GObject.Signal
    def noarg_signal(self) -> None:
        pass

    @GObject.Signal
    def signal_with_side_effect(self) -> None:
        print("A side effect of emit")


class TestSignals:
    def test_noarg_signal(self):
        signaller = Signaller()
        signaller.emit("noarg-signal")

    def test_signal_with_side_effect(self, capsys):
        signaller = Signaller()
        signaller.emit("signal-with-side-effect")
        captured = capsys.readouterr()
        assert captured.out == "A side effect of emit\n"
