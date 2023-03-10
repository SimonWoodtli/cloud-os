# Silverblue-OS

My personal Linux Fedora Silverblue image with a cloud-native approach. 

## Installation

After installing Silverblue simply rebase to my up to date custom image.  
`rpm-ostree rebase fedora:fedora/36/x86_64/silverblue` (need to update this
once image is done)

## Features

* Reliable, atomic updates with built in rollback
* Reduces time to configure Linux on a fresh install drastically
* Ships with flatpak, flathub only
* Ships with distrobox
* Ships with my terminal-centric [workspace]
* Ships with Qemu/Virt-Manager or VMware (not sure yet)
* Auto updates the base Fedora image and the my additional packages on a daily
  basis.
* Hosted on ghcr.io

[workspace]: <https://github.com/SimonWoodtli/workspace>


Related:

* <https://github.com/ublue-os>
