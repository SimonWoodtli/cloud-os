Name:           cloud-os-just
Packager:       cloud-os
Vendor:         cloud-os
Version:        0.1.1
Release:        1%{?dist}
Summary:        cloud-os just integration
License:        Apache-2.0
URL:            https://github.com/SimonWoodtli/cloud-os/tree/main/config/build/just

BuildArch:      noarch
Supplements:    just

Source0:        justfile
Source1:        cloud-os-just.sh
Source2:        firstboot
Source3:        recipe.yml
Source4:        cloud-os-desktop.sh
Source5:        feh.desktop

%description
Adds cloud-os just integration for easier setup

%prep
%setup -q -c -T

%build

mkdir -p -m0755  %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
install -Dm755 %{SOURCE1} %{SOURCE2} %{SOURCE4} %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
install -Dm644 %{SOURCE0} %{SOURCE3} %{SOURCE5} %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
install -Dm755 %{SOURCE2} %{buildroot}%{_bindir}/firstboot
mkdir -p -m0755  %{buildroot}%{_sysconfdir}/profile.d
install -Dm755 %{SOURCE1} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d


%files
%dir %attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/justfile
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/recipe.yml
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/feh.desktop
%attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}/cloud-os-just.sh
%attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}/firstboot
%attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}/cloud-os-desktop.sh
%attr(0755,root,root) %{_sysconfdir}/profile.d/cloud-os-just.sh
%attr(0755,root,root) %{_sysconfdir}/profile.d/cloud-os-desktop.sh
%attr(0755,root,root) %{_bindir}/firstboot

%changelog
* Thu Nov 02 2023 Simon D. Woodtli <xnasero@posteo.net> - 0.1.1
- Add custom .desktop file for feh to work with my wrapper script and
  w3m
* Fri Apr 21 2023 Simon D. Woodtli <xnasero@posteo.net> - 0.1.1
- Add firstboot script, justfile with firstboot recipe and recyipe.yml
  with packages to install
* Sun Mar 05 2023 Joshua Stone <joshua.gage.stone@gmail.com> - 0.1
- Add justfile integration
