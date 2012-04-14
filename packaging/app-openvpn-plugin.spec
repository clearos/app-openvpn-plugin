
Name: app-openvpn-plugin
Epoch: 1
Version: 1.1.0
Release: 1%{dist}
Summary: OpenVPN Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-openvpn-plugin-%{version}.tar.gz
Buildarch: noarch

%description
OpenVPN Policies provide access control for the OpenVPN server app.

%package core
Summary: OpenVPN Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
OpenVPN Policies provide access control for the OpenVPN server app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/openvpn_plugin
cp -r * %{buildroot}/usr/clearos/apps/openvpn_plugin/

install -D -m 0644 packaging/openvpn.php %{buildroot}/var/clearos/accounts/plugins/openvpn.php

%post core
logger -p local6.notice -t installer 'app-openvpn-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/openvpn_plugin/deploy/install ] && /usr/clearos/apps/openvpn_plugin/deploy/install
fi

[ -x /usr/clearos/apps/openvpn_plugin/deploy/upgrade ] && /usr/clearos/apps/openvpn_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-openvpn-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/openvpn_plugin/deploy/uninstall ] && /usr/clearos/apps/openvpn_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/openvpn_plugin/packaging
%exclude /usr/clearos/apps/openvpn_plugin/tests
%dir /usr/clearos/apps/openvpn_plugin
/usr/clearos/apps/openvpn_plugin/deploy
/usr/clearos/apps/openvpn_plugin/language
/usr/clearos/apps/openvpn_plugin/libraries
/var/clearos/accounts/plugins/openvpn.php
