%global _empty_manifest_terminate_build 0
Name:           python-swiftclient
Version:        3.11.1
Release:        1
Summary:        OpenStack Object Storage API Client Library
License:        Apache-2.0
URL:            https://docs.openstack.org/python-swiftclient/latest/
Source0:        https://files.pythonhosted.org/packages/bd/fd/502864fc1312218454646dc6e18fce8cf67c7693c2801f692c4bcffece86/python-swiftclient-3.11.1.tar.gz
BuildArch:      noarch

%description
This is a python client for the Swift API. There’s a Python API (the swiftclient module), and a command-line script (swift).

%package -n python3-swiftclient
Summary:        OpenStack Object Storage API Client Library
Provides:       python-swiftclient

# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-keystoneclient
# Tests running requires
BuildRequires:  python3-coverage
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-mock
BuildRequires:  python3-openstacksdk
BuildRequires:  python3-stestr
BuildRequires:  python3-hacking


%description -n python3-swiftclient
 This is a python client for the Swift API. There’s a Python API (the swiftclient module), and a command-line script (swift).

%package help
Summary:        OpenStack Object Storage API Client Library
Provides:       python3-swiftclient-doc
%description help
 This is a python client for the Swift API. There’s a Python API (the swiftclient module), and a command-line script (swift).

%prep
%autosetup -n python-swiftclient-%{version}

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


%files -n python3-swiftclient -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Jul 27 2021 OpenStack_SIG <openstack@openeuler.org> - 3.11.1-1
- update to 3.11.1

* Sat Jan 30 2021 liusheng <liusheng2048@gmail.com> - 3.10.1-1
- Initial package of python-swiftclient
