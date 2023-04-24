Name:           cloud-os-dconf
Packager:       cloud-os
Vendor:         cloud-os
Version:        0.1
Release:        1%{?dist}
Summary:        cloud-os dconf settings to customize desktop
License:        Apache-2.0
URL:            https://github.com/SimonWoodtli/cloud-os

BuildArch:      noarch
Supplements:    dconf

Source0:        01-cloud-os
Source1:        dconf-update.service

%description
Adds cloud-os dconf files declaratively for customized Fedora desktop.

%prep
%setup -q -c -T

%build
mkdir -p -m0755 %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
mkdir -p -m0755 %{buildroot}%{_sysconfdir}/dconf/db/local.d %{buildroot}%{_sysconfdir}/systemd/system
install -Dm644 %{SOURCE0} %{SOURCE1} %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
install -Dm644 %{SOURCE0} %{buildroot}%{_sysconfdir}/dconf/db/local.d
install -Dm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/systemd/system

%files
%dir %attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/01-cloud-os
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/dconf-update.service
%attr(0644,root,root) %{_sysconfdir}/dconf/db/local.d/01-cloud-os
%attr(0644,root,root) %{_sysconfdir}/systemd/system/dconf-update.service

%changelog
* Sun Apr 23 2023 Simon D. Woodtli <xnasero@posteo.net> - 0.1
- Add dconf files and systemd service
