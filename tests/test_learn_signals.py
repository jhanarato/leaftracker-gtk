import pytest

from gi.repository import Gio, GObject, Gtk


class Signaller(GObject.Object):
    def __init__(self):
        super().__init__()

    @GObject.Signal
    def noarg_signal(self) -> None:
        pass

class TestSignals:
    def test_noarg_signal(self):
        signaller = Signaller()
        signaller.emit("noarg-signal")