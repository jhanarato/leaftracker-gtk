pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'leaftracker_gtk')
gnome = import('gnome')

gnome.compile_resources('leaftracker-gtk',
  'leaftracker_gtk.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'leaftracker-gtk.in',
  output: 'leaftracker-gtk',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

leaftracker_gtk_sources = [
  '__init__.py',
  'main.py',
  'window_test.py',
  'backend.py',
]

install_data(leaftracker_gtk_sources, install_dir: moduledir)
