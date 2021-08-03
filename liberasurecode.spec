Name:           liberasurecode
Version:        1.6.2
Release:        1
Summary:        Erasure Code API library written in C with pluggable backends
License:        BSD and CRC32
URL:            https://bitbucket.org/tsg-/liberasurecode/
Source0:        %{name}-%{version}.tar.gz
Patch2:         liberasurecode-1.6.2-docs.patch
Patch3:         liberasurecode-1.6.2-ldtest.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  zlib-devel

%description
An API library for Erasure Code, written in C. It provides a number
of pluggable backends, such as Intel ISA-L library.

%package doc
Summary:        Documentation for %{name}

%description doc
The documentation for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch2 -p1
%patch3 -p1

%build
autoreconf -i -v
%configure --disable-static --disable-mmi
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make V=1 %{?_smp_mflags}

%check
make test

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_datadir}/doc -type f -exec chmod a-x {} ';'

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_libdir}/*.so
%{_libdir}/*.so.*

%files doc
%{_datadir}/doc/liberasurecode/html/*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/erasurecode-1.pc


%changelog
* Sun Aug 15 2021 OpenStack_SIG <openstack@openeuler.org> - 1.6.2-1
- Initial release
