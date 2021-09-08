%global _empty_manifest_terminate_build 0
Name:           python-os-api-ref
Version:        2.1.0
Release:        1
Summary:        Sphinx Extensions to support API reference sites in OpenStack
License:        Apache-2.0
URL:            https://docs.openstack.org/os-api-ref/latest/
Source0:        https://files.pythonhosted.org/packages/a9/35/e8c15cec076cbff90262b22b446486950c5f57c0197a1d8697969a13a246/os-api-ref-2.1.0.tar.gz
BuildArch:      noarch
%description
Sphinx Extensions to support API reference sites in OpenStack

%package -n python3-os-api-ref
Summary:        Sphinx Extensions to support API reference sites in OpenStack
Provides:       python-os-api-ref

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

BuildRequires:  python3-pyyaml
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-six
BuildRequires:  python3-sphinx

%description -n python3-os-api-ref
Sphinx Extensions to support API reference sites in OpenStack

%package help
Summary:        Sphinx Extensions to support API reference sites in OpenStack
Provides:       python3-os-api-ref-doc
%description help
Sphinx Extensions to support API reference sites in OpenStack

%prep
%autosetup -n os-api-ref-%{version}
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


%files -n python3-os-api-ref -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Sat Jul 31 2021 OpenStack_SIG <openstack@openeuler.org> - 2.1.0-1
- Package init
