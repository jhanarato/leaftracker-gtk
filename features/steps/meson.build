pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'features/steps')

steps = [
  'tutorial.py',
]

install_data(steps, install_dir: moduledir)
