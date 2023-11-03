# Cloud-OS

[![License](https://img.shields.io/badge/license-Apache2-brightgreen.svg)](LICENSE)
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/cloud-os)](https://artifacthub.io/packages/search?repo=cloud-os)
[![wakatime](https://wakatime.com/badge/user/173067c8-7ded-4cfb-8605-b3032659c00c/project/2500ba3a-f747-4893-b70e-4278332c24fc.svg)](https://wakatime.com/badge/user/173067c8-7ded-4cfb-8605-b3032659c00c/project/2500ba3a-f747-4893-b70e-4278332c24fc)

My personal Linux Fedora Silverblue image with a cloud-native approach.

## Installation

1. Verify image:

```
cosign verify --key https://raw.githubusercontent.com/SimonWoodtli/cloud-os/main/cosign.pub ghcr.io/simonwoodtli/cloud-os:latest
```

2. Install [Fedora Silverblue][silverblue] and boot it up
3. Rebase to cloud-os and reboot

```
sudo rpm-ostree rebase --experimental ostree-unverified-registry:ghcr.io/simonwoodtli/cloud-os:latest
systemctl reboot
```

4. Setup cloud-os

```
just firstboot
```

## Features

* Reliable, atomic updates with built in rollback
* Reduces time to configure Linux on a fresh install drastically
* Ships with flatpak, flathub only
* Ships with distrobox
* Ships with my terminal-centric Alpine Linux [workspace]
* Ships with Qemu/Virt-Manager
* Auto updates the base Fedora image and the my additional packages on a daily
  basis
* Hosted on ghcr.io

![Alt](https://repobeats.axiom.co/api/embed/fa9e3f63018894aee1a032e23926a68beb110808.svg "Repobeats analytics image")

[workspace]: <https://github.com/SimonWoodtli/workspace-alpine>
[silverblue]: <https://fedoraproject.org/silverblue/download/>

Related:

* <https://github.com/ublue-os>
