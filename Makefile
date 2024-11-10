build:
	flatpak-builder --force-clean --user --install builddir org.bswa.Leaftracker.json

test: build
	flatpak run --command=pytest --cwd=/app/share/leaftracker-gtk/leaftracker_gtk_tests --devel org.bswa.Leaftracker

run:
	flatpak run org.bswa.Leaftracker