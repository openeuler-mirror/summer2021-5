%global pypi_name boto3
Name:                python-%{pypi_name}
Version:             1.17.26
Release:             1
Summary:             The AWS SDK for Python
License:             Apache-2.0
URL:                 https://github.com/boto/boto3
Source0:             https://files.pythonhosted.org/packages/a6/c4/84d6eeee2e3cbde749981557591a9531f97f0fa86866d91e2c2d2de1723c/boto3-1.17.26.tar.gz
BuildArch:           noarch
%description
Boto3 is the Amazon Web Services (AWS) Software Development
Kit (SDK) for Python, which allows Python developers to
write software that makes use of services like Amazon S3
and Amazon EC2.

%package -n          python3-%{pypi_name}
Summary:             The AWS SDK for Python
BuildRequires:       python3-devel python3-setuptools
BuildRequires: python3-s3transfer
BuildRequires: python3-jmespath
BuildRequires: python3-botocore
BuildRequires: python3-nose
BuildRequires: python3-mock
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
Boto3 is the Amazon Web Services (AWS) Software Development
Kit (SDK) for Python, which allows Python developers to
write software that makes use of services like Amazon S3
and Amazon EC2.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
rm -rf tests/integration

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-*.egg-info/

%changelog
* Sun Jul 25 2021 OpenStack_SIG <openstack@openeuler.org> - 1.17.26-1
- update to 1.17.26

* Mon Nov 16 2020 yanan li <liyanan32@huawei.com> - 1.16.17-1
- Package init
