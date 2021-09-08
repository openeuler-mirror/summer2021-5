%global _empty_manifest_terminate_build 0
Name:           python-breathe
Version:        4.29.0
Release:        1
Summary:        Sphinx Doxygen renderer
License:        BSD
URL:            https://github.com/michaeljones/breathe
Source0:        https://files.pythonhosted.org/packages/df/0f/a1946bbc0731ac02ca191b11ca18c634310dd8d37121c5e21b06960e2f28/breathe-4.29.0.tar.gz
BuildArch:      noarch

%description
Breathe is an extension to reStructuredText and Sphinx to be able to read and render Doxygen xml output.

%package -n python3-breathe
Summary:        Sphinx Doxygen renderer
Provides:       python-breathe
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-docutils
BuildRequires:  python3-six

%description -n python3-breathe
Breathe is an extension to reStructuredText and Sphinx to be able to read and render Doxygen xml output.

%package help
Summary:        Sphinx Doxygen renderer
Provides:       python3-breathe-doc
%description help
Breathe is an extension to reStructuredText and Sphinx to be able to read and render Doxygen xml output.

%prep
%autosetup -n breathe-4.29.0 

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

%files -n python3-breathe -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon Aug 23 2021 OpenStack_SIG <openstack@openeuler.org> - 4.29.0-1
- Package update to 4.29.0

* Thu Jan 04 2021 wangxiao <wangxiao65@huawei.com> - 4.26.1-1
- update to 4.26.1 for fix build errors with Sphinx 3.4

* Sat Oct 10 2020 zhanghua <zhanghua40@huawei.com> - 4.22.1-1
- update to 4.22.1 for fix build errors with Sphinx 3.1

* Thu Feb 20 2020 Ling Yang <lingyang2@huawei.com> - 4.11.1-2
- Package init
