# Add justfile to HOME if it's not already installed

if [[ ! -f "${HOME}/.justfile" && -f /usr/share/cloud-os/cloud-os-just/justfile ]]; then
  cp /usr/share/cloud-os/cloud-os-just/justfile "${HOME}/.justfile"
fi
