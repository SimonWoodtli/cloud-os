Name:           ublue-os-update-services
Packager:       ublue-os
Vendor:         ublue-os
Version:        0.1
Release:        1%{?dist}
Summary:        ublue-os auto-update services
License:        MIT
URL:            https://github.com/ublue-os/config

BuildArch:      noarch
Supplements:    update-services

Source0:        flatpak-user-update.timer
Source1:        flatpak-user-update.service
Source2:        10-flatpak-user-update.preset
Source3:        flatpak-system-update.timer
Source4:        flatpak-system-update.service
Source5:        10-flatpak-system-update.preset
Source6:        rpm-ostreed.conf

%description
Adds ublue-os auto-uppdate services integration for easier setup

%prep
%setup -q -c -T

%build
mkdir -p -m0755 %{buildroot}%{_datadir}/%{VENDOR}/%{NAME} %{buildroot}%{_userunitdir} %{buildroot}%{_userpresetdir} %{buildroot}%{_unitdir} %{buildroot}%{_presetdir} %{buildroot}%{_sysconfdir}
install -Dm644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}
install -Dm644 %{SOURCE0} %{SOURCE1} %{buildroot}%{_userunitdir}
install -Dm644 %{SOURCE2} %{buildroot}%{_userpresetdir}
install -Dm644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE5} %{buildroot}%{_presetdir}
#install -Dm644 %{SOURCE6} %{buildroot}%{_sysconfdir}

%files
%dir %attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/flatpak-user-update.timer
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/flatpak-user-update.service
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/10-flatpak-user-update.preset
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/flatpak-system-update.timer
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/flatpak-system-update.service
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/10-flatpak-system-update.preset
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/rpm-ostreed.conf
%attr(0644,root,root) %{_userunitdir}/flatpak-user-update.timer
%attr(0644,root,root) %{_userunitdir}/flatpak-user-update.service
%attr(0644,root,root) %{_userpresetdir}/10-flatpak-user-update.preset
%attr(0644,root,root) %{_unitdir}/flatpak-system-update.timer
%attr(0644,root,root) %{_unitdir}/flatpak-system-update.service
%attr(0644,root,root) %{_presetdir}/10-flatpak-system-update.preset
#%attr(0644,root,root) %{_sysconfdir}/rpm-ostreed.conf

%changelog
* Mon Apr 17 2023 Simon D. Woodtli <xnasero@posteo.net> - 0.1
- Add update-services integration
