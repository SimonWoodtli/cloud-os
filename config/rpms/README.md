# rpms

## Mutt Wizard

Mutt-wizzard pkg is currently being added manually

TODO: automate this process

1. Launch ubuntu container
1. get .deb of mutt-wizard: `apt download mutt-wizard`
1. Install alien: `sudo apt install alien`
1. convert .deb to .rpm: `sudo alien -r -k your_package_name.deb`
1. inspect paths of .deb: `dpkg -c your_package_name.deb`
1. inspect paths of .rpm: `rpm -qlp your_package_name.rpm`
1. Check files and paths (should be good)
1. mv mutt-wizard .rpm to cloud-os/config/rpms and commit/push
