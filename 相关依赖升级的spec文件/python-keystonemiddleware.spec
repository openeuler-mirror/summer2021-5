%global _empty_manifest_terminate_build 0
Name:           python-keystonemiddleware
Version:        9.2.0
Release:        1
Summary:        Middleware for OpenStack Identity
License:        Apache-2.0
URL:            https://docs.openstack.org/keystonemiddleware/latest/
Source0:        https://tarballs.openstack.org/keystonemiddleware/keystonemiddleware-%{version}.tar.gz
BuildArch:      noarch
%description
OpenStack Identity API (Keystone) This package contains middleware modules
designed to provide authentication and authorization features to web services

%package -n python3-keystonemiddleware
Summary:        Middleware for OpenStack Identity
Provides:       python-keystonemiddleware
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-webob
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-oslo-cache
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-context
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-oslo-log
BuildRequires:  python3-oslo-serialization
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-pycadf
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-oslo-messaging
# Tests running requires
BuildRequires:  python3-webtest
BuildRequires:  python3-bandit
BuildRequires:  python3-coverage
BuildRequires:  python3-cryptography
BuildRequires:  python3-fixtures
BuildRequires:  python3-flake8-docstrings
BuildRequires:  python3-hacking
BuildRequires:  python3-oslo-messaging
BuildRequires:  python3-oslotest
BuildRequires:  python3-memcached
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore
BuildRequires:  python3-testresources
BuildRequires:  python3-testtools

%description -n python3-keystonemiddleware
Middleware for the OpenStack Identity API.

%package help
Summary:        Middleware for OpenStack Identity
Provides:       python3-keystonemiddleware-doc
%description help
OpenStack Identity API (Keystone) This package contains middleware modules
designed to provide authentication and authorization features to web services

%prep
%autosetup -n keystonemiddleware-%{version} -p1

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


%files -n python3-keystonemiddleware -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Sat Jul 17 2021 OpenStack_SIG <openstack@openeuler.org>
- Upgrade to 9.2.0

* Thu Jan 07 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
