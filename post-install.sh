#!/bin/sh

set -ouex pipefail

createNewProfile() {
    local dconfdir=/org/gnome/terminal/legacy/profiles:
    local profile_ids=($(dconf list $dconfdir/ | grep ^: |\
                        sed 's/\///g' | sed 's/://g'))
    local profile_name="$1"
    local profile_ids_old="$(dconf read "$dconfdir"/list | tr -d "]")"
    #local profile_id="$(uuidgen)" #use `uuidgen` if brand new needed
    local profile_id="$2"

    [ -z "$profile_ids_old" ] && local profile_ids_old="["  # if there's no `list` key
    [ ${#profile_ids[@]} -gt 0 ] && local delimiter=,  # if the list is empty
    dconf write $dconfdir/list \
        "${profile_ids_old}${delimiter} '$profile_id']"
    dconf write "$dconfdir/:$profile_id"/visible-name "'$profile_name'"
    echo $profile_id
}

systemctl enable rpm-ostreed-automatic.timer
systemctl enable flatpak-system-update.timer

systemctl --global enable flatpak-user-update.timer

cp /usr/share/ublue-os/ublue-os-update-services/rpm-ostreed.conf /etc/rpm-ostreed.conf
## TODO add furter config stuff here, dconf and all that jazz, or maybe
#it's not gonna work then add it to config/build/just and during firstboot add data
systemctl unmask dconf-update.service
systemctl enable dconf-update.service
systemctl enable sshd
fc-cache -f /usr/share/fonts #FIXME not sure if not a folder needs to be specified, gotta test
createNewProfile gruvbox-host eaa70d0f-2bff-4c94-8714-5c8815cf8b0f
createNewProfile gruvbox-workspace 2ea51c17-a89c-4151-af02-925016c2a29a
createNewProfile gruvbox-alpine 4c3035f9-08ef-4956-8cf2-c11fe365d146
sed -i 's/#DefaultTimeoutStopSec.*/DefaultTimeoutStopSec=15s/' /etc/systemd/user.conf
sed -i 's/#DefaultTimeoutStopSec.*/DefaultTimeoutStopSec=15s/' /etc/systemd/system.conf
