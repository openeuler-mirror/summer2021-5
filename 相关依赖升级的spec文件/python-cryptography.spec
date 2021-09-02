%global srcname cryptography
Name:           python-%{srcname}
Version:        3.4.6
Release:        1
Summary:        PyCA's cryptography library
License:        ASL 2.0 or BSD
URL:            https://cryptography.io/en/latest/  
Source0:        https://files.pythonhosted.org/packages/fa/2d/2154d8cb773064570f48ec0b60258a4522490fcb115a6c7c9423482ca993/cryptography-3.4.6.tar.gz

BuildRequires:  openssl-devel
BuildRequires:  gcc
BuildRequires:  gnupg2

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest 
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pretend
BuildRequires:  python%{python3_pkgversion}-iso8601
BuildRequires:  python%{python3_pkgversion}-cryptography-vectors 
BuildRequires:  python%{python3_pkgversion}-setuptools-rust >= 0.11.3
BuildRequires:  python%{python3_pkgversion}-asn1crypto >= 0.21
BuildRequires:  python%{python3_pkgversion}-hypothesis >= 1.11.4
BuildRequires:  python%{python3_pkgversion}-pytz
BuildRequires:  python%{python3_pkgversion}-idna >= 2.1
BuildRequires:  python%{python3_pkgversion}-six >= 1.4.1
BuildRequires:  python%{python3_pkgversion}-cffi >= 1.7
BuildRequires:  rust
BuildRequires:  cargo

%description
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.


%package     -n python%{python3_pkgversion}-cryptography
Summary:        PyCA's cryptography library

Requires:       openssl-libs
Requires:       python%{python3_pkgversion}-idna >= 2.1
Requires:       python%{python3_pkgversion}-asn1crypto >= 0.21
Requires:       python%{python3_pkgversion}-six >= 1.4.1
Requires:       python%{python3_pkgversion}-cffi >= 1.7

%{?python_provide:%python_provide python%{python3_pkgversion}-cryptography}

%description -n python%{python3_pkgversion}-cryptography
cryptography is a package designed to expose cryptographic primitives and
recipes to Python developers.

%package_help

%prep
%autosetup -n cryptography-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-cryptography
%defattr(-,root,root)
%doc AUTHORS.rst
%license LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitearch}/*
%{python3_sitearch}/cryptography-%{version}-py*.egg-info

%files help
%defattr(-,root,root)
%doc README.rst docs

%changelog
* Tue Jul 27 2021 OpenStack_SIG <openstack@openeuler.org> - 3.4.6-1
- Package update to 3.4.6

* Tue Feb 23 2021 shixuantong <shixuantong@huawei.com> - 3.3.1-2
- fix CVE-2020-36242

* Mon Feb 1 2021 liudabo <liudabo1@huawei.com> - 3.3.1-1
- upgrade version to 3.3.1

* Tue Aug 11 2020 tianwei<tianwei12@huawei.com> -3.0-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:delete python2  

* Thu Jul 23 2020 dingyue<dingyue5@huawei.com> -3.0-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:NA

* Thu Apr 16 2020 chengquan<chengquan3@huawei.com> -2.9-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:upgrade software to v2.9

* Thu Feb 13 2020 openEuler Buildteam <buildteam@openeuler.org> - 2.6.1-1
- Update to 2.6.1

* Tue Oct 22 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3-5
- Package rebuild.

* Sat Oct 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3-4
- Type: enhancement
- ID:   NA
- SUG:  NA
- DESC: fix build failed.

* Sat Sep 14 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3-3
- Package init.
