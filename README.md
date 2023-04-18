# Cloud-OS

[![License](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](LICENSE)
[![wakatime](https://wakatime.com/badge/user/173067c8-7ded-4cfb-8605-b3032659c00c/project/2500ba3a-f747-4893-b70e-4278332c24fc.svg)](https://wakatime.com/badge/user/173067c8-7ded-4cfb-8605-b3032659c00c/project/2500ba3a-f747-4893-b70e-4278332c24fc)

My personal Linux Fedora Silverblue image with a cloud-native approach. 

This project is possible thanks to the amazing work from [uBlue] 🙏  
I learned a lot from their codebase and used that knowledge to develop my own
offshoot of it.

## Installation

1. verify image: `cosign verify --key cosign.pub ghcr.io/simonwoodtli/cloud-os:latest` (NEED TO figure out if URL can be used for cosign.pub instead of locally safing it)

After installing Silverblue simply rebase to my up to date custom image.  
`sudo rpm-ostree rebase --experimental ostree-unverified-registry:ghcr.io/simonwoodtli/cloud-os:latest` 


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

[uBlue]: <https://github.com/ublue-os>
[workspace]: <https://github.com/SimonWoodtli/workspace>

Related:

* <https://github.com/ublue-os>
