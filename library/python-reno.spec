%global _empty_manifest_terminate_build 0
Name:           python-reno
Version:        3.3.0
Release:        1
Summary:        RElease NOtes manager
License:        Apache-2.0
URL:            https://docs.openstack.org/reno/latest/
Source0:        https://files.pythonhosted.org/packages/0a/bb/9a121ddb86e5cec94d9336653fc1ecb33f27e151e64f4eb9274d968b81e2/reno-3.3.0.tar.gz
BuildArch:      noarch
%description
Reno is a release notes manager designed with high throughput in mind, supporting fast distributed development teams without introducing additional development processes. Our goal is to encourage detailed and accurate release notes for every release.

%package -n python3-reno
Summary:        RElease NOtes manager
Provides:       python-reno
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-pyyaml
BuildRequires:  python3-dulwich
BuildRequires:  python3-packaging
BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx
# Tests running requires
BuildRequires:  python3-coverage
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-subunit
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools

%description -n python3-reno
 Reno is a release notes manager designed with high throughput in mind, supporting fast distributed development teams without introducing additional development processes. Our goal is to encourage detailed and accurate release notes for every release.

%package help
Summary:        RElease NOtes manager
Provides:       python3-reno-doc
%description help
 Reno is a release notes manager designed with high throughput in mind, supporting fast distributed development teams without introducing additional development processes. Our goal is to encourage detailed and accurate release notes for every release.

%prep
%autosetup -n reno-3.3.0 

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


%files -n python3-reno -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon Jul 26 2021 OpenStack_SIG <openstack@openeuler.org> - 3.3.0-1
- update to 3.3.0

* Thu Nov 19 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
