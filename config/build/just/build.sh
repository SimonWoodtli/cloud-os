#!/usr/bin/bash

set -ouex pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

mkdir -p /tmp/cloud-os/rpmbuild/SOURCES

cp ${SCRIPT_DIR}/{justfile,cloud-os-just.sh,firstboot,recipe.yml,cloud-os-desktop.sh,feh.desktop} /tmp/cloud-os/rpmbuild/SOURCES

rpmbuild -ba \
    --define '_topdir /tmp/cloud-os/rpmbuild' \
    --define '%_tmppath %{_topdir}/tmp' \
    ${SCRIPT_DIR}/cloud-os-just.spec
