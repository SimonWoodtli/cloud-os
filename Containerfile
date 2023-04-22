## MAIN:
ARG IMAGE_NAME="${IMAGE_NAME:-silverblue}"
ARG SOURCE_IMAGE="${SOURCE_IMAGE:-silverblue}"
ARG BASE_IMAGE="quay.io/fedora-ostree-desktops/${SOURCE_IMAGE}"
ARG FEDORA_MAJOR_VERSION="${FEDORA_MAJOR_VERSION:-37}"

FROM ${BASE_IMAGE}:${FEDORA_MAJOR_VERSION} AS builder

ARG IMAGE_NAME="${IMAGE_NAME}"
ARG FEDORA_MAJOR_VERSION="${FEDORA_MAJOR_VERSION}"

ADD config/rpms/ /tmp/rpms
ADD build.sh /tmp/build.sh
ADD post-install.sh /tmp/post-install.sh
ADD packages.json /tmp/packages.json

## install pkgs from containers if needed on host and: (downside none upgradeable via rpm-ostree)
## 1. not yet in Fedora repo
## 2. you need bleeding edge version
## 3. modified binaries/none default compiled binaries
COPY --from=docker.io/mikefarah/yq /usr/bin/yq /usr/bin/yq
COPY --from=cgr.dev/chainguard/cosign:latest /usr/bin/cosign /usr/bin/cosign
##TODO add borderless tmux here

## Already in config/rpms/
#COPY --from=ghcr.io/ublue-os/config:latest /rpms /tmp/rpms

RUN /tmp/build.sh
RUN /tmp/post-install.sh
RUN rm -rf /tmp/* /var/*
RUN ostree container commit
# what is this for?
RUN mkdir -p /var/tmp && chmod -R 1777 /var/tmp

# https://copr.fedorainfracloud.org/coprs/ublue-os/vanilla-first-setup/
# Add Vanilla First Setup, Maybe still need this, it's a wizzard to
# install packages... if so add `vanilla-first-setup` to packages.json
# and activate the copr repo:
#RUN wget https://copr.fedorainfracloud.org/coprs/ublue-os/vanilla-first-setup/repo/fedora-$(rpm -E %fedora)/ublue-os-vanilla-first-setup-fedora-$(rpm -E %fedora).repo -O /etc/yum.repos.d/_copr_ublue-os-vanilla-first-setup.repo

