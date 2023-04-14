# Cloud-OS

[![License](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](LICENSE)
[![wakatime](https://wakatime.com/badge/user/173067c8-7ded-4cfb-8605-b3032659c00c/project/2500ba3a-f747-4893-b70e-4278332c24fc.svg)](https://wakatime.com/badge/user/173067c8-7ded-4cfb-8605-b3032659c00c/project/2500ba3a-f747-4893-b70e-4278332c24fc)

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

![Alt](https://repobeats.axiom.co/api/embed/fa9e3f63018894aee1a032e23926a68beb110808.svg "Repobeats analytics image")

[workspace]: <https://github.com/SimonWoodtli/workspace>

Related:

* <https://github.com/ublue-os>
