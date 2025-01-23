pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'pygui')

pygui_files = [
  '__init__.py',
  'main.py',
  'main_window.py',
  'species_list_page.py',
  'species_details_page.py',
  'species_model.py',
  'string_list_maker.py',
  'validated_entry_row.py',
]

install_data(pygui_files, install_dir: moduledir)