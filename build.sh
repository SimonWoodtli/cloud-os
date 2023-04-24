#!/bin/sh

set -ouex pipefail

RELEASE="$(rpm -E %fedora)"

INCLUDED_PACKAGES=($(jq -r ".include | sort | unique[]" /tmp/packages.json))
EXCLUDED_PACKAGES=($(jq -r ".exclude | sort | unique[]" /tmp/packages.json))

## Check if excluded packages are actually installed, if so add them to array
if [[ "${#EXCLUDED_PACKAGES[@]}" -gt 0 ]]; then
    EXCLUDED_PACKAGES=($(rpm -qa --queryformat='%{NAME} ' ${EXCLUDED_PACKAGES[@]}))
fi

## Add third party repo, just for building the image to install neccesary
## packages. After the build is finished third party repo is removed so
## on a live system you don't have the repo activated.
wget -P /tmp/rpms \
    https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-${RELEASE}.noarch.rpm \
    https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-${RELEASE}.noarch.rpm

## fix rpm install cannot overwrite existing files (can't force update it)
## either this or rmv profile/user from rpm package and just filter
## strings with sed here
rm /etc/dconf/profile/user

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
