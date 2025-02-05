pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'pygui_tests')

pygui_tests = [
  'conftest.py',
  'test_main_window.py',
  'test_learn_actions.py',
  'test_learn_models.py',
  'test_learn_properties.py',
  'test_learn_signals.py',
  'test_learn_templates.py',
  'test_string_list_maker.py',
  'test_species_details_page.py',
  'test_species_list_page.py',
  'test_species_model.py',
  'test_validated_entry_row.py',
  'pytest.ini'
]

install_data(pygui_tests, install_dir: moduledir)
