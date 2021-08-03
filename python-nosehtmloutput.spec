%global _empty_manifest_terminate_build 0
Name:           python-nosehtmloutput
Version:        0.0.7
Release:        1
Summary:        Nose plugin to produce test results in html.
License:        Apache-2.0
URL:            https://git.openstack.org/cgit/openstack-infra/nose-html-output
Source0:        https://files.pythonhosted.org/packages/07/77/d13a9e64bd65f36a0d7c52634ede2b81c7f29957362df6de364e8376955c/nosehtmloutput-0.0.7.tar.gz
BuildArch:      noarch
%description
Nose plugin that generates a nice html test report.

%package -n python3-nosehtmloutput
Summary:        Nose plugin to produce test results in html.
Provides:       python-nosehtmloutput

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip

BuildRequires:  python3-nose
BuildRequires:  python3-six


%description -n python3-nosehtmloutput
Nose plugin that generates a nice html test report.

%package help
Summary:        Nose plugin to produce test results in html.
Provides:       python3-nosehtmloutput-doc
%description help
Nose plugin that generates a nice html test report.

%prep
%autosetup -n nosehtmloutput-%{version}

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



%files -n python3-nosehtmloutput -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Sat Jul 31 2021 OpenStack_SIG <openstack@openeuler.org> - 0.0.7-1
- Package init