pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'pygui_tests')

pygui_tests = [
  'conftest.py',
  'test_main.py',
  'test_learn_models.py',
  'test_learn_properties.py',
  'test_learn_templates.py',
  'test_list_maker.py',
  'test_species_details_page.py',
  'pytest.ini'
]

install_data(pygui_tests, install_dir: moduledir)
