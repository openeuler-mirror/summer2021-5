%global _empty_manifest_terminate_build 0
Name:           python-eventlet
Version:        0.30.2
Release:        1
Summary:        Highly concurrent networking library
License:        MIT License
URL:            http://eventlet.net
Source0:        https://files.pythonhosted.org/packages/23/db/8ff5a9dec5ff016d5836254b676d507c2180d8838d7e545277d938896913/eventlet-0.30.2.tar.gz
BuildArch:      noarch

%description
Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.

%package -n python3-eventlet
Summary:        Highly concurrent networking library
Provides:       python-eventlet
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-dns
BuildRequires:  python3-greenlet
BuildRequires:  python3-six
# General requires
Requires:       python3-dns
Requires:       python3-greenlet
Requires:       python3-six

%description -n python3-eventlet
Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.

%package help
Summary:        Highly concurrent networking library
Provides:       python3-eventlet-doc

%description help
Eventlet is a concurrent networking library for Python that allows you to change how you run your code, not how you write it.

%prep
%autosetup -n eventlet-0.30.2 -S git

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


%files -n python3-eventlet -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon Jul 26 2021 OpenStack_SIG <openstack@openeuler.org> - 0.30.2-1
- update to 0.30.2

* Fri Jan 15 2021 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated

* Thu Mar 12 2020 zoushuangshuang <zoushuangshuang@huawei.com> - 0.23.0-3
- Package init

