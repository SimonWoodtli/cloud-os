Name:           cloud-os-udev-rules
Packager:       cloud-os
Vendor:         cloud-os
Version:        0.1
Release:        1%{?dist}
Summary:        cloud-os udev rules
License:        Apache-2.0
URL:            https://github.com/SimonWoodtli/cloud-os/tree/main/config

BuildArch:      noarch
Supplements:    udev-rules
## game-devices: https://codeberg.org/fabiscafe/game-devices-udev
Source0:        71-8bitdo-controllers.rules
Source1:        71-alpha_imaging_technology_co-vr.rules
Source2:        71-astro_gaming-controllers.rules
Source3:        71-betop-controllers.rules
Source4:        71-hori-controllers.rules
Source5:        71-htc-vr.rules
Source6:        71-logitech-controllers.rules
Source7:        71-mad_catz-controllers.rules
Source8:        71-microsoft-controllers.rules
Source9:        71-nacon-controllers.rules
Source10:       71-nintendo-controllers.rules
Source11:       71-nvidia-controllers.rules
Source12:       71-pdp-controllers.rules
Source13:       71-personal_communication_systems_inc-controllers.rules
Source14:       71-powera-controllers.rules
Source15:       71-razer-controllers.rules
Source16:       71-sony-controllers.rules
Source17:       71-sony-vr.rules
Source18:       71-valve-controllers.rules
Source19:       71-valve-vr.rules
Source20:       71-zeroplus_technology_corporation-controllers.rules
## general
Source21:       60-openrgb.rules
Source22:       70-titan-key.rules
Source23:       70-u2f.rules
Source24:       80-wooting.rules

%description
Adds cloud-os udev-rules integration for easier setup

%prep
%setup -q -c -T

%build
mkdir -p -m0755 %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}/game-devices %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}/general %{buildroot}%{_udevrulesdir}
install -Dm644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}/game-devices
install -Dm644 %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{buildroot}%{_datadir}/%{VENDOR}/%{NAME}/general 
install -Dm644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE16} %{SOURCE17} %{SOURCE18} %{SOURCE19} %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{buildroot}%{_udevrulesdir}

%files
%dir %attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices
%dir %attr(0755,root,root) %{_datadir}/%{VENDOR}/%{NAME}/general
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-8bitdo-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-alpha_imaging_technology_co-vr.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-astro_gaming-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-betop-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-hori-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-htc-vr.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-logitech-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-mad_catz-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-microsoft-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-nacon-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-nintendo-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-nvidia-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-pdp-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-personal_communication_systems_inc-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-powera-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-razer-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-sony-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-sony-vr.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-valve-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-valve-vr.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/game-devices/71-zeroplus_technology_corporation-controllers.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/general/60-openrgb.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/general/70-titan-key.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/general/70-u2f.rules
%attr(0644,root,root) %{_datadir}/%{VENDOR}/%{NAME}/general/80-wooting.rules
%attr(0644,root,root) %{_udevrulesdir}/71-8bitdo-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-alpha_imaging_technology_co-vr.rules
%attr(0644,root,root) %{_udevrulesdir}/71-astro_gaming-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-betop-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-hori-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-htc-vr.rules
%attr(0644,root,root) %{_udevrulesdir}/71-logitech-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-mad_catz-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-microsoft-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-nacon-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-nintendo-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-nvidia-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-pdp-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-personal_communication_systems_inc-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-powera-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-razer-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-sony-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-sony-vr.rules
%attr(0644,root,root) %{_udevrulesdir}/71-valve-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/71-valve-vr.rules
%attr(0644,root,root) %{_udevrulesdir}/71-zeroplus_technology_corporation-controllers.rules
%attr(0644,root,root) %{_udevrulesdir}/60-openrgb.rules
%attr(0644,root,root) %{_udevrulesdir}/70-titan-key.rules
%attr(0644,root,root) %{_udevrulesdir}/70-u2f.rules
%attr(0644,root,root) %{_udevrulesdir}/80-wooting.rules

%changelog
* Tue Apr 18 2023 Simon D. Woodtli <xnasero@posteo.net> - 0.1
- Add udev-rules integration
