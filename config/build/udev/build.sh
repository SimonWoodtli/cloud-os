#!/usr/bin/bash

set -ouex pipefail

declare SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
declare -a FILES_GAME_DEVICES=("71-8bitdo-controllers.rules" "71-alpha_imaging_technology_co-vr.rules" "71-astro_gaming-controllers.rules" "71-betop-controllers.rules" "71-hori-controllers.rules" "71-htc-vr.rules" "71-logitech-controllers.rules" "71-mad_catz-controllers.rules" "71-microsoft-controllers.rules" "71-nacon-controllers.rules" "71-nintendo-controllers.rules" "71-nvidia-controllers.rules" "71-pdp-controllers.rules" "71-personal_communication_systems_inc-controllers.rules" "71-powera-controllers.rules" "71-razer-controllers.rules" "71-sony-controllers.rules" "71-sony-vr.rules" "71-valve-controllers.rules" "71-valve-vr.rules" "71-zeroplus_technology_corporation-controllers.rules")
declare -a FILES_GENERAL=("60-openrgb.rules" "70-titan-key.rules" "70-u2f.rules" "80-wooting.rules")

mkdir -p /tmp/ublue-os/rpmbuild/SOURCES

for file in "${FILES_GAME_DEVICES[@]}"; do
  cp "${SCRIPT_DIR}/game-devices/$file" /tmp/ublue-os/rpmbuild/SOURCES
done
for file in "${FILES_GENERAL[@]}"; do
  cp "${SCRIPT_DIR}/general/$file" /tmp/ublue-os/rpmbuild/SOURCES
done

rpmbuild -ba \
    --define '_topdir /tmp/ublue-os/rpmbuild' \
    --define '%_tmppath %{_topdir}/tmp' \
    ${SCRIPT_DIR}/ublue-os-udev.spec
