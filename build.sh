#!/bin/sh

set -ouex pipefail

RELEASE="$(rpm -E %fedora)"

INCLUDED_PACKAGES=($(jq -r ".include | sort | unique[]" /tmp/packages.json))
EXCLUDED_PACKAGES=($(jq -r ".exclude | sort | unique[]" /tmp/packages.json))

## Check if excluded packages are actually installed, if so add them to array
if [[ "${#EXCLUDED_PACKAGES[@]}" -gt 0 ]]; then
    EXCLUDED_PACKAGES=($(rpm -qa --queryformat='%{NAME} ' ${EXCLUDED_PACKAGES[@]}))
fi

# Removing Filtered Flathub Repository
#/usr/bin/flatpak remote-delete flathub --force || exit 1
# Enabling Flathub Repository
/usr/bin/flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo || exit 1
# Replacing Fedora Flatpaks with Flathub Ones (this may take a while)"
/usr/bin/flatpak install --user --noninteractive org.gnome.Platform//43
/usr/bin/flatpak install --user --noninteractive --reinstall flathub $(flatpak list --app-runtime=org.fedoraproject.Platform --columns=application | tail -n +1 ) || exit 1
# Removing all preinstalled Flatpaks
/usr/bin/flatpak remove --system --noninteractive --all || exit 1
# Removing Fedora Flatpak Repository
/usr/bin/flatpak remote-delete fedora --force || exit 1

## this might be needed for firstboot
#/usr/bin/systemctl --user enable --now flatpak-user-update.timer 

## Add third party repo, just for building the image to install neccesary
## packages. After the build is finished third party repo is removed so
## on a live system you don't have the repo activated.
wget -P /tmp/rpms \
    https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-${RELEASE}.noarch.rpm \
    https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-${RELEASE}.noarch.rpm

rpm-ostree install \
    /tmp/rpms/*.rpm \
    fedora-repos-archive

##TODO add flatpaks here
if [[ "${#INCLUDED_PACKAGES[@]}" -gt 0 && "${#EXCLUDED_PACKAGES[@]}" -eq 0 ]]; then
    rpm-ostree install \
        ${INCLUDED_PACKAGES[@]}

elif [[ "${#INCLUDED_PACKAGES[@]}" -eq 0 && "${#EXCLUDED_PACKAGES[@]}" -gt 0 ]]; then
    rpm-ostree override remove \
        ${EXCLUDED_PACKAGES[@]}

elif [[ "${#INCLUDED_PACKAGES[@]}" -gt 0 && "${#EXCLUDED_PACKAGES[@]}" -gt 0 ]]; then
    rpm-ostree override remove \
        ${EXCLUDED_PACKAGES[@]} \
        $(printf -- "--install=%s " ${INCLUDED_PACKAGES[@]})

else
    echo "No packages to install."

fi

