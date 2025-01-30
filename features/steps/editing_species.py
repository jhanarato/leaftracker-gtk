import gi
gi.require_version('Adw', '1')
from gi.repository import Adw, Gio

resource = Gio.Resource.load('leaftracker-gtk.gresource')
resource._register()

from pygui.main_window import MainWindow

from behave import *

@given("we have navigated to the species details page")
def step_impl(context):
    pass

@when("we fill in the form")
def step_impl(context):
    pass

@when("we click the save button")
def step_impl(context):
    pass

@then("the species is displayed on the species list page")
def step_impl(context):
    pass
