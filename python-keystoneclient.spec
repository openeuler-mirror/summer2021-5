%global _empty_manifest_terminate_build 0
Name:           python-keystoneclient
Version:        4.2.0
Release:        1
Summary:        Client Library for OpenStack Identity
License:        Apache-2.0
URL:            https://docs.openstack.org/python-keystoneclient/latest/
Source0:        https://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-%{version}.tar.gz
BuildArch:      noarch
%description
This is a client for the OpenStack Identity API, implemented by the Keystone team; it contains a Python API (the
keystoneclient module) for OpenStack's Identity Service.

%package -n python3-keystoneclient
Summary:        Client Library for OpenStack Identity
Provides:       python-keystoneclient
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-debtcollector
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-stevedore
# General requires
Requires:       python3-debtcollector
Requires:       python3-keystoneauth1
Requires:       python3-oslo-config
Requires:       python3-oslo-i18n
Requires:       python3-oslo-serialization
Requires:       python3-oslo-utils
Requires:       python3-pbr
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-stevedore
%description -n python3-keystoneclient
This is a client for the OpenStack Identity API, implemented by the Keystone team; it contains a Python API (the
keystoneclient module) for OpenStack's Identity Service.

%package help
Summary:        Client Library for OpenStack Identity
Provides:       python3-keystoneclient-doc
%description help
This is a client for the OpenStack Identity API, implemented by the Keystone team; it contains a Python API (the
keystoneclient module) for OpenStack's Identity Service.

%prep
%autosetup -n python-keystoneclient-%{version}
rm -rf {test-,}requirements.txt
%build
%py3_build

%install
%py3_install

install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .


%files -n python3-keystoneclient -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*



%changelog
* Sun Jul 25 2021 OpenStack_SIG <openstack@openeuler.org> - 4.2.0-1
- update to 4.2.0

* Thu Jan 21 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
