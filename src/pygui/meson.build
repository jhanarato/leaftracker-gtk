pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'pygui')

pygui_files = [
  '__init__.py',
  'main.py',
  'list_maker.py',
  'main_window.py',
  'species.py',
]

install_data(pygui_files, install_dir: moduledir)