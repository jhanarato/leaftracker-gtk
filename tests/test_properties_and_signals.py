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

