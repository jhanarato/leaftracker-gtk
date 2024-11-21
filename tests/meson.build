pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'pygui_tests')

pygui_tests = [
  'test_main.py',
  'test_properties_and_signals.py',
  'test_species.py',
  'pytest.ini'
]

install_data(pygui_tests, install_dir: moduledir)
