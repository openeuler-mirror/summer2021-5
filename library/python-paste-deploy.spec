%global _empty_manifest_terminate_build 0
Name:           python-PasteDeploy
Version:        2.1.1
Release:        1
Summary:        Load, configure, and compose WSGI applications and servers
License:        MIT
URL:            https://pylonsproject.org/
Source0:        https://files.pythonhosted.org/packages/3f/98/179626030d6b3f04e4471aae01f1eae7539347fa7bb8f1228ea4ed600054/PasteDeploy-2.1.1.tar.gz
BuildArch:      noarch

%description
This tool provides code to load WSGI applications and servers from URIs. These URIs can refer to Python eggs for INI-style configuration files. Paste Script provides commands to serve applications based on this configuration file.

%package -n python3-paste-deploy
Summary:        Load, configure, and compose WSGI applications and servers
Provides:       python-paste-deploy

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-pytest

Requires:       python3-paste
Requires:       python3-sphinx
Requires:       python3-pylons-sphinx-themes
Requires:       python3-pytest

%description -n python3-paste-deploy
This tool provides code to load WSGI applications and servers from URIs. These URIs can refer to Python eggs for INI-style configuration files. Paste Script provides commands to serve applications based on this configuration file.

%package help
Summary:        Load, configure, and compose WSGI applications and servers
Provides:       python3-paste-deploy-doc

%description help
This tool provides code to load WSGI applications and servers from URIs. These URIs can refer to Python eggs for INI-style configuration files. Paste Script provides commands to serve applications based on this configuration file.

%prep
%autosetup -n PasteDeploy-%{version}

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
pytest

%files -n python3-paste-deploy -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Jul 27 2021 OpenStack_SIG <openstack@openeuler.org> - 2.1.1-1
- updata to 2.1.1

* Thu Jul 16 2020 yanglongkang <yanglongkang@huawei.com> - 2.1.0-1
- update package to 2.1.0

* Fri Feb 14 2020 Ruijun Ge <geruijun@huawei.com> - 1.5.2-18
- init package
