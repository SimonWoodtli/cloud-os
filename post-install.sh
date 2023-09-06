#!/bin/sh

set -ouex pipefail

systemctl enable rpm-ostreed-automatic.timer
systemctl enable flatpak-system-update.timer
systemctl --global enable flatpak-user-update.timer
cp /usr/share/cloud-os/cloud-os-update-services/rpm-ostreed.conf /etc/rpm-ostreed.conf
## TODO add furter config stuff here, dconf and all that jazz, or maybe
#it's not gonna work then add it to config/build/just and during firstboot add data
systemctl unmask dconf-update.service
systemctl enable dconf-update.service
systemctl enable sshd
systemctl enable pcscd
systemctl enable ydotool
fc-cache -f /usr/share/fonts #FIXME not sure if not a folder needs to be specified, gotta test
sed -i 's/#DefaultTimeoutStopSec.*/DefaultTimeoutStopSec=15s/' /etc/systemd/user.conf
sed -i 's/#DefaultTimeoutStopSec.*/DefaultTimeoutStopSec=15s/' /etc/systemd/system.conf
