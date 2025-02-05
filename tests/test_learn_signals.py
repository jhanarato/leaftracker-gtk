import pytest

from gi.repository import Gio, GObject, Gtk


class Signaller(GObject.Object):
    def __init__(self):
        super().__init__()

    @GObject.Signal
    def noarg_signal(self) -> None:
        pass

    @GObject.Signal
    def print_signal(self) -> None:
        print("A side effect of emit")


class TestSignals:
    def test_noarg_signal(self):
        signaller = Signaller()
        signaller.emit("noarg-signal")

    def test_print_signal(self, capsys):
        signaller = Signaller()
        signaller.emit("print-signal")
        captured = capsys.readouterr()
        assert captured.out == "A side effect of emit\n"
