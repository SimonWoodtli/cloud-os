Name:           ublue-os-just
Packager:       ublue-os
Vendor:         ublue-os
Version:        0.1.1
Release:        1%{?dist}
Summary:        ublue-os just integration
License:        MIT
URL:            https://github.com/ublue-os/config

BuildArch:      noarch
Supplements:    just

Source0:        justfile
Source1:        ublue-os-just.sh
Source2:        firstboot
Source3:        recipe.yml

%description
Adds ublue-os just integration for easier setup

%prep
%setup -q -c -T

%build

mkdir -p -m0755  %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
install -Dm755 %{SOURCE1} %{SOURCE2} %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
install -Dm644 %{SOURCE0} %{SOURCE3} %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
install -Dm755 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/ublue-os-just.sh
install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/firstboot

%files
%dir %attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/justfile
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/recipe.yml
%attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}/ublue-os-just.sh
%attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}/firstboot
%attr(0755,root,root) %{_sysconfdir}/profile.d/ublue-os-just.sh
%attr(0755,root,root) %{_bindir}/firstboot

%changelog
* Fri Apr 21 2023 Simon D. Woodtli <xnasero@posteo.net> - 0.1.1
- Add firstboot script, justfile with firstboot recipe and recyipe.yml
  with packages to install
* Sun Mar 05 2023 Joshua Stone <joshua.gage.stone@gmail.com> - 0.1
- Add justfile integration
