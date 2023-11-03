# Add .desktop files to $HOME if default .desktop file that ships with
# package needs modification.
#
# /usr/share is immutable so:
# If default /usr/share/applications/foo.desktop config files needs
# modification, overwrite it with
# ~/.local/share/applications/foo.desktop which have priority.

# * feh.desktop: exec parameter is not working with my custom feh
#   wrapper script when using `xdg-open`
if [[ ! -f "${HOME}/.local/share/applications/feh.desktop" && -f /usr/share/cloud-os/cloud-os-just/feh.desktop ]]; then
  cp /usr/share/cloud-os/cloud-os-just/feh.desktop "${HOME}/.local/share/applications/feh.desktop"
fi
