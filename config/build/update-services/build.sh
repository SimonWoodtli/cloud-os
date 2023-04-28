#!/usr/bin/bash

set -ouex pipefail

declare SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
declare -a FILES=("flatpak-user-update.timer" "flatpak-user-update.service" "10-flatpak-user-update.preset" "flatpak-system-update.timer" "flatpak-system-update.service" "10-flatpak-system-update.preset" "rpm-ostreed.conf")

mkdir -p /tmp/cloud-os/rpmbuild/SOURCES

for file in "${FILES[@]}"; do
  cp "${SCRIPT_DIR}/$file" /tmp/cloud-os/rpmbuild/SOURCES
done

rpmbuild -ba \
    --define '_topdir /tmp/cloud-os/rpmbuild' \
    --define '%_tmppath %{_topdir}/tmp' \
    ${SCRIPT_DIR}/cloud-os-update-services.spec
