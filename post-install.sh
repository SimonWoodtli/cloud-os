#!/bin/sh

set -ouex pipefail

systemctl enable rpm-ostreed-automatic.timer
systemctl enable flatpak-system-update.timer

systemctl --global enable flatpak-user-update.timer

cp /usr/share/ublue-os/ublue-os-update-services/rpm-ostreed.conf /etc/rpm-ostreed.conf
## TODO add furter config stuff here, dconf and all that jazz
