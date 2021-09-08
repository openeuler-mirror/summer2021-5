%global _empty_manifest_terminate_build 0
Name:           python-greenlet
Version:        1.0.0
Release:        1
Summary:        Lightweight in-process concurrent programming
License:        Python-2.0 and MIT
URL:            https://greenlet.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/92/be/878cc5314fa5aadce33e68738c1a24debe317605196bdfc2049e66bc9c30/greenlet-1.0.0.tar.gz

%description
Greenlets are lightweight coroutines for in-process concurrent programming.

%package -n python3-greenlet
Summary:        Lightweight in-process concurrent programming
Provides:       python-greenlet

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-cffi
BuildRequires:  gcc-c++
BuildRequires:  gdb

Requires:       python3-sphinx

%description -n python3-greenlet
Greenlets are lightweight coroutines for in-process concurrent programming.

%package help
Summary:        Lightweight in-process concurrent programming
Provides:       python3-greenlet-doc
%description help
Greenlets are lightweight coroutines for in-process concurrent programming.

%prep
%autosetup -n greenlet-%{version} -p1


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

%files -n python3-greenlet -f filelist.lst
%dir %{python3_sitearch}/*
%{_includedir}/python%{python3_version}*/greenlet/


%files help -f doclist.lst
%{_docdir}/*





%changelog
* Tue Jul 27 2021 OpenStack_SIG <openstack@openeuler.org> - 1.0.0-1
- updata to 1.0.0

* Fri Jan 22 2021 zhangy1317 <zhangy1317@foxmail.com> -0.4.15
- update to 0.4.15

* Thu Oct 29 2020 tianwei <tianwei12@huawei.com> - 0.4.14-4
- delete python2 require

* Tue Sep 8 2020 liuweibo <liuweibo10@huawei.com> - 0.4.14-3
- Fix Source0

* Mon Dec 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.4.14-2
- Package init
