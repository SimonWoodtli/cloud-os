#!/usr/bin/bash

set -ouex pipefail

declare SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

mkdir -p /tmp/cloud-os/rpmbuild/SOURCES

cp ${SCRIPT_DIR}/{01-cloud-os,user,dconf-update.service} /tmp/cloud-os/rpmbuild/SOURCES

rpmbuild -ba \
    --define '_topdir /tmp/cloud-os/rpmbuild' \
    --define '%_tmppath %{_topdir}/tmp' \
    ${SCRIPT_DIR}/cloud-os-dconf.spec
