%global _empty_manifest_terminate_build 0
Name:           python-sphinxcontrib-svg2pdfconverter
Version:        1.1.1
Release:        1
Summary:        Sphinx SVG to PDF converter extension
License:        BSD
URL:            https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter
Source0:        https://files.pythonhosted.org/packages/df/4e/24ce9c8b942562bae7c355aaadb95e9e09428fab6ec8047a27b2299d7245/sphinxcontrib-svg2pdfconverter-1.1.1.tar.gz
BuildArch:      noarch

%description
This extension converts SVG images to PDF in case the builder does not support SVG images natively (e.g. LaTeX).

%package -n python3-sphinxcontrib-svg2pdfconverter
Summary:        Sphinx SVG to PDF converter extension
Provides:       python-sphinxcontrib-svg2pdfconverter

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

BuildRequires:  python3-sphinx



%description -n python3-sphinxcontrib-svg2pdfconverter
This extension converts SVG images to PDF in case the builder does not support SVG images natively (e.g. LaTeX).

%package help
Summary:        Sphinx SVG to PDF converter extension
Provides:       python3-sphinxcontrib-svg2pdfconverter-doc

%description help
This extension converts SVG images to PDF in case the builder does not support SVG images natively (e.g. LaTeX).
%prep
%autosetup -n sphinxcontrib-svg2pdfconverter-%{version}

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



%files -n python3-sphinxcontrib-svg2pdfconverter -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Jul 27 2021 OpenStack_SIG <openstack@openeuler.org> - 1.1.1-1
- update to 1.1.1

* Sat Nov 21 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
