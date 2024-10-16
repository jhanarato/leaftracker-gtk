# main.py
#
# Copyright 2024 JR
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

import gi
gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk

from leaftracker.adapters.elastic import initialise
from leaftracker.service_layer import services

from .main_window import MainWindow


def on_activate(app):
    window = MainWindow(application=app)
    window.present()


def main(version):
    print_versions()

    initialise.indexes()
    uow = initialise.unit_of_work()
    services.add_species("Leaftracker gtk", uow)

    app = Adw.Application(application_id='org.bswa.Leaftracker')
    app.connect('activate', on_activate)
    return app.run(sys.argv)


def print_versions():
    print(f"Python version {sys.version}")
    print(f"Adwaita version {Adw.MAJOR_VERSION}.{Adw.MINOR_VERSION}.{Adw.MICRO_VERSION}")
    print(f"GTK version {Gtk.MAJOR_VERSION}.{Gtk.MINOR_VERSION}.{Gtk.MICRO_VERSION}")
