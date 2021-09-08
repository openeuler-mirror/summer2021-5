%global _empty_manifest_terminate_build 0
Name:           python-pyeclib
Version:        1.3.1
Release:        1
Summary:        Python interface to erasure codes
License:        BSD
URL:            http://git.openstack.org/cgit/openstack/pyeclib/
Source0:        https://files.pythonhosted.org/packages/bf/87/bfec569d085a8b0c5b197687ed5514d394787c6027b3776458056d87b06a/pyeclib-1.3.1.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  liberasurecode-devel 

%description
This library provides a simple Python interface for implementing erasure
codes. A number of back-end implementations is supported either directly
or through the C interface liberasurecode.

%package -n python3-pyeclib
Summary: This library provides a simple Python interface for implementing erasure codes. 
Provides:       python-pyeclib
Requires:       liberasurecode 

%description -n python3-pyeclib
This is v0.9 of PyECLib. This library provides a simple Python interface for implementing erasure codes and is known to work with Python v2.6, 2.7 and 3.x.


%prep
%autosetup -n pyeclib-%{version}

%build
%py3_build

%install
%py3_install


%check
%{__python3} setup.py test

%files -n python3-pyeclib

%{python3_sitearch}/pyeclib*



%changelog
* Sat Jul 31 2021 OpenStack_SIG <openstack@openeuler.org> - 1.3.1-1
- Package init