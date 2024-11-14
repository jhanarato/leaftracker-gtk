build:
	flatpak-builder --force-clean --user --install builddir org.bswa.Leaftracker.json

test: build
	flatpak run --command=pytest --cwd=/app/share/leaftracker-gtk/pygui_tests --devel org.bswa.Leaftracker

run:
	flatpak run org.bswa.Leaftracker

shell:
	flatpak run --command=sh --cwd=/app/share/leaftracker-gtk/ --devel org.bswa.Leaftracker