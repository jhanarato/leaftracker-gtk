pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'features')

features = [
  'tutorial.feature',
]

install_data(features, install_dir: moduledir)

subdir('steps')