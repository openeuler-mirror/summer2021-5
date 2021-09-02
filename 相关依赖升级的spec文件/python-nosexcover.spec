%global _empty_manifest_terminate_build 0
Name:           python-nosexcover
Version:        1.0.11
Release:        1
Summary:        Extends nose.plugins.cover to add Cobertura-style XML reports
License:        BSD
URL:            http://github.com/cmheisel/nose-xcover/
Source0:        https://files.pythonhosted.org/packages/11/b3/2b9e812eb9cb7e60bbfff0a1f581bf411d5b55156e211a4e3580560c8902/nosexcover-1.0.11.tar.gz
BuildArch:      noarch
%description
A companion to the built-in nose.plugins.cover, this plugin will write out an XML coverage report to a file named coverage.xml.

%package -n python3-nosexcover
Summary:        Extends nose.plugins.cover to add Cobertura-style XML reports
Provides:       python-nosexcover

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-coverage
BuildRequires:  python3-nose
%description -n python3-nosexcover
A companion to the built-in nose.plugins.cover, this plugin will write out an XML coverage report to a file named coverage.xml.

%package help
Summary:        Extends nose.plugins.cover to add Cobertura-style XML reports
Provides:       python3-nosexcover-doc
%description help


%prep
%autosetup -n nosexcover-%{version}

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

%check
%{__python3} setup.py test

%files -n python3-nosexcover -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Sat Jul 31 2021 OpenStack_SIG <openstack@openeuler.org> - 1.0.11-1
- Package init