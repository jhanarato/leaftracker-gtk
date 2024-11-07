pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'leaftracker_gtk_tests')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

leaftracker_gtk_tests = [
  'test_example.py',
  'pytest.ini'
]

install_data(leaftracker_gtk_tests, install_dir: moduledir)
