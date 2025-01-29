import gi
gi.require_version('Adw', '1')
from gi.repository import Adw, Gio

resource = Gio.Resource.load('leaftracker-gtk.gresource')
resource._register()

from pygui.main_window import MainWindow

from behave import *


@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
