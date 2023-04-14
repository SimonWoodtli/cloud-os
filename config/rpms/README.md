# RPMS by ublue.it

These rpms are maintained by ublue, I just copied them out of their [config] repo. Because the project moves fast and too many changes might break my own OS in the future.

> ⚠️ Stil need to figure out how the justfile rpm-package is not present in rpms/ but in build/ all relevant files are present. I think they just did not implement it yet, so I build it myself and put it in my git rpms/ folder.

Wait till i put the just.rpm in rpms/ maybe i can do that simpler

## Extract files from config Image:

1. `echo "FROM alpine:latest
COPY --from=ghcr.io/ublue-os/config:latest . /tmp/config" > /tmp/Containerfile`
1. `docker build -t configImage /tmp/Containerfile`
1. `mkdir /tmp/config`
1. `docker run  --name configContainer configImage`
1. `docker cp configContainer:/tmp/config/ .`

[config]: <https://github.com/ublue-os/config>
