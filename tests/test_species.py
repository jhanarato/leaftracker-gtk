import pytest
from gi.repository import Gio, Gtk, GObject

resource = Gio.Resource.load('../leaftracker-gtk.gresource')
resource._register()

from pygui.species import SpeciesDetailsPage, SpeciesEditMode, PreviousScientificNames, RemovableRow


class FakeSpeciesWriter:
    def __init__(self):
        self.reference = None
        self.current_scientific_name = None

    def write_current_scientific_name(self, name: str):
        self.reference = "species-ref"
        self.current_scientific_name = name


@pytest.fixture
def writer() -> FakeSpeciesWriter:
    return FakeSpeciesWriter()

@pytest.fixture
def details_page(writer) -> SpeciesDetailsPage:
    page = SpeciesDetailsPage()
    page.set_writer(writer)
    return page

class TestFakeSpeciesWriter:
    def test_create_writer(self):
        writer = FakeSpeciesWriter()


class TestRemovableRow:
    def test_emits_remove_signal(self):
        signal_received = False

        def remove_callback(inst):
            nonlocal signal_received
            signal_received = True

        widget = RemovableRow("Row text")
        widget.connect("removed", remove_callback)
        widget.emit("removed")

        assert signal_received

    def test_clicking_remove_button_emits_signal(self):
        signal_received = False

        def remove_callback(inst):
            nonlocal signal_received
            signal_received = True

        widget = RemovableRow("Row text")
        widget.connect("removed", remove_callback)
        widget.click_remove_button()

        assert signal_received


class TestPreviousScientificNames:
    def test_can_add_name(self):
        widget = PreviousScientificNames()
        widget.name_field = "Acacia saligna"
        widget.click_add_button()
        name = widget.get_name_from_item(0)
        assert name == "Acacia saligna"

    def test_name_field_cleared_after_add(self):
        widget = PreviousScientificNames()
        widget.name_field = "Acacia saligna"
        widget.click_add_button()
        assert widget.name_field == ""

    def test_can_get_list_of_names(self):
        widget = PreviousScientificNames()
        widget.name_field = "Acacia abc"
        widget.click_add_button()
        widget.name_field = "Acacia xyz"
        widget.click_add_button()
        assert widget.get_species_names() == ["Acacia abc", "Acacia xyz"]

    def test_adding_a_duplicate_name_does_not_modify_the_list(self):
        widget = PreviousScientificNames()
        widget.name_field = "Acacia saligna"
        widget.click_add_button()
        widget.name_field = "Acacia saligna"
        widget.click_add_button()
        assert widget.get_species_names() == ["Acacia saligna"]


class TestSpeciesDetailsPage:
    def test_set_species_reference(self, details_page):
        details_page.set_property("reference", "abc")
        assert details_page.get_property("reference") == "abc"

    def test_set_species_reference_to_none(self, details_page):
        details_page.set_property("reference", None)
        assert details_page.get_property("reference") is None

    def test_reference_display_is_updated_when_reference_changed(self, details_page):
        details_page.set_property("reference", "xyz")
        assert details_page.reference_display.get_text() == "xyz"

    def test_setting_reference_to_none_shows_missing_message(self, details_page):
        details_page.set_property("reference", None)
        assert details_page.reference_display.get_text() == "None"

    def test_changing_bound_property_sets_reference(self, details_page, gobject_with_property):
        gobject_with_property.bind_property(
            source_property="prop-a",
            target=details_page,
            target_property="reference",
            flags=GObject.BindingFlags.BIDIRECTIONAL
        )
        gobject_with_property.set_property("prop-a", "cba")
        assert details_page.reference == "cba"

    def test_starts_in_add_new_mode(self, details_page):
        assert details_page.mode() == SpeciesEditMode.ADD_NEW

    def test_switches_mode_to_edit_existing(self, details_page):
        details_page.set_property("reference", "a reference")
        assert details_page.mode() == SpeciesEditMode.EDIT_EXISTING

    def test_switches_mode_to_add_new(self, details_page):
        details_page.set_property("reference", "a reference")
        details_page.set_property("reference", None)
        assert details_page.mode() == SpeciesEditMode.ADD_NEW

    def test_changes_saved_when_save_button_clicked(self, details_page, writer):
        species_name = "Acacia saligna"
        details_page.current_scientific_name.set_text(species_name)
        assert writer.current_scientific_name is None
        details_page.save_button.emit("activated")
        assert writer.current_scientific_name == species_name

    def test_reference_displayed_on_save(self, details_page):
        species_name = "Acacia saligna"
        details_page.current_scientific_name.set_text(species_name)
        details_page.save_button.emit("activated")
        assert details_page.reference_display.get_text() == "species-ref"
