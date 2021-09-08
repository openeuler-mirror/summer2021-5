%global _empty_manifest_terminate_build 0
Name:           python-setuptools-rust
Version:        0.12.1
Release:        1
Summary:        Setuptools Rust extension plugin
License:        MIT
URL:            https://github.com/PyO3/setuptools-rust
Source0:        https://files.pythonhosted.org/packages/12/22/6ba3031e7cbd6eb002e13ffc7397e136df95813b6a2bd71ece52a8f89613/setuptools-rust-0.12.1.tar.gz
BuildArch:      noarch
%description
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%package -n python3-setuptools-rust
Summary:        Setuptools Rust extension plugin
Provides:       python-setuptools-rust
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-semantic_version
BuildRequires:  python3-toml
BuildRequires:  python3-setuptools_scm
Requires:       python3-setuptools
Requires:       python3-semantic_version
Requires:       python3-toml
%description -n python3-setuptools-rust
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.
%package help
Summary:        Setuptools Rust extension plugin
Provides:       python3-setuptools-rust-doc
%description help
Setuptools helpers for Rust Python extensions. Compile and distribute Python
extensions written in Rust as easily as if they were written in C.

%prep
%autosetup -n setuptools-rust-0.12.1 

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

%files -n python3-setuptools-rust -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Sat Aug 14 2021 OpenStack_SIG <openstack@openeuler.org> - 0.12.1-1
- Initial package.
