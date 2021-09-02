Name:           python-coverage
Version:        5.5
Release:        1
Summary:        Code coverage measurement for Python

License:        Apache-2.0
URL:            https://coverage.readthedocs.io/en/coverage-%{version}/
Source0:        https://pypi.python.org/packages/source/c/coverage/coverage-%{version}.tar.gz

BuildRequires:  gcc

%description
Coverage.py measures code coverage, typically during test execution. It uses the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are executable, and which have been executed.

%package -n     python3-coverage
Summary:        Code coverage measurement for Python 3
BuildRequires:  python3-devel python3-setuptools
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-coverage}
Provides:       bundled(js-jquery) = 1.11.1 bundled(js-jquery-debounce) = 1.1
Provides:       bundled(js-jquery-hotkeys) = 0.8 bundled(js-jquery-tablesorter)
Provides:       bundled(js-jquery-isonscreen) = 1.2.0
Obsoletes:      platform-python-coverage < %{version}-%{release}

%description -n python3-coverage
Coverage.py is a tool for measuring code coverage of Python 3 programs. It monitors
your program, noting which parts of the code have been executed, then analyzes the
source to identify code that could have been executed but was not.

%prep
%autosetup -n coverage-%{version} -p1
sed -i 's/\r//g' README.rst
find . -type f ! -perm 0644 -exec chmod 0644 \{\} \;

%build
%py3_build

%install
%py3_install
mv %{buildroot}/%{_bindir}/coverage %{buildroot}/%{_bindir}/python3-coverage

find %{buildroot}/%{_bindir} -type f -name "coverage*" -delete

pushd %{buildroot}%{_bindir}
ln -s python3-coverage coverage3 
ln -s python3-coverage coverage-%{python3_version}
popd

%files -n python3-coverage
%doc README.rst
%license NOTICE.txt LICENSE.txt
%{_bindir}/coverage-%{python3_version}
%{_bindir}/coverage3
%{_bindir}/python3-coverage
%{python3_sitearch}/coverage/
%{python3_sitearch}/coverage-%{version}-py?.?.egg-info/

%changelog
* Sun Jul 25 2021 OpenStack_SIG <openstack@openeuler.org> - 5.5-1
- Package update to 5.5.1

* Sat Jan 30 2021 xihaochen <xihaochen@huawei.com> - 5.4-1
- Type:requirements                                                                                                                                  
- Id:NA
- SUG:NA
- DESC:update python-coverage to 5.4

* Thu Oct 29 2020 gaihuiying <gaihuiying1@huawei.com> - 5.2-2
- Type:requirement
- ID:NA
- SUG:NA
- DESC:remove python2

* Tue Jul 28 2020 liulong <liulong20@huawei.com> - 5.2-1
- Type:requirement
- ID:NA
- SUG:NA
- DESC:update coverage version to 5.2

* Sat Oct 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 4.5.3-1
- Package Init
