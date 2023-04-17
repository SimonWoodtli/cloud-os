#!/usr/bin/bash

set -ouex pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

mkdir -p /tmp/ublue-os/rpmbuild/SOURCES

cp ${SCRIPT_DIR}/{flatpak-user-update.timer,flatpak-user-update.service,10-flatpak-user-update.preset,flatpak-system-update.timer,flatpak-system-update.service,10-flatpak-system-update.preset,rpm-ostreed.conf} /tmp/ublue-os/rpmbuild/SOURCES

rpmbuild -ba \
    --define '_topdir /tmp/ublue-os/rpmbuild' \
    --define '%_tmppath %{_topdir}/tmp' \
    ${SCRIPT_DIR}/ublue-os-update-services.spec
