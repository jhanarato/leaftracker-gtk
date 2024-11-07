flatpak-builder --force-clean --user --install builddir org.bswa.Leaftracker.json
flatpak run --command=pytest --cwd=/app/share/leaftracker-gtk/leaftracker_gtk_tests --devel org.bswa.Leaftracker