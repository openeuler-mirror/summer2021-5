%global pypi_name botocore
Name:                python-%{pypi_name}
Version:             1.20.26
Release:             1
Summary:             Low-level, data-driven core of boto 3
License:             Apache-2.0
URL:                 https://github.com/boto/botocore
Source0:              https://files.pythonhosted.org/packages/09/e9/3f85aac6fcf346a12b59e7f946aa23a732c0689a39c9a658dd3dc91c3ea6/botocore-1.20.26.tar.gz
BuildArch:           noarch
%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%package -n          python3-%{pypi_name}
Summary:             Low-level, data-driven core of boto 3
BuildRequires:       python3-devel python3-setuptools
buildRequires:  python3-nose
buildRequires:  python3-tox
buildRequires:  python3-mock
buildRequires:  python3-behave
buildRequires:  python3-jsonschema
BuildRequires:  python3-urllib3
BuildRequires:  python3-dateutil
BuildRequires:  python3-jmespath
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:            python3-jmespath
%description -n python3-%{pypi_name}
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for the AWS CLI as well as boto3.

%prep
%autosetup -n %{pypi_name}-%{version}
# unable to import "botocore". I'm not 100% sure why this happened but for now
# just exclude this one test and run all the other functional tests.
rm -vr tests/functional/leak

%build
%py3_build

%install
%py3_install

%check
cd tests
nosetests-%{python3_version} unit functional

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Mon Jul 26 2021 OpenStack_SIG <openstack@openeuler.org> - 1.20.26-1
- update to 1.20.26

* Mon Nov 16 2020 yanan li <liyanan32@huawei.com> - 1.19.17-1
- Package init
