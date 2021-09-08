Name:       python-sphinx
Version:    3.5.2
Release:    1
Epoch:      1
Summary:    Python documentation generator
License:    BSD and MIT 
URL:        http://sphinx-doc.org/
Source0:    https://files.pythonhosted.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
Patch1:     sphinx-test_theming.diff

BuildArch:     noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-babel
BuildRequires: python3-docutils
BuildRequires: python3-imagesize
BuildRequires: python3-jinja2
BuildRequires: python3-packaging
BuildRequires: python3-pygments
BuildRequires: python3-requests
BuildRequires: python3-sphinxcontrib-applehelp
BuildRequires: python3-sphinxcontrib-devhelp
BuildRequires: python3-sphinxcontrib-htmlhelp
BuildRequires: python3-sphinxcontrib-jsmath
BuildRequires: python3-sphinxcontrib-qthelp
BuildRequires: python3-sphinxcontrib-serializinghtml
BuildRequires: python3-sphinx-theme-alabaster

BuildRequires: dos2unix

BuildRequires: python3-test
BuildRequires: python3-html5lib
BuildRequires: python3-mock
BuildRequires: python3-pytest
BuildRequires: python3-snowballstemmer

BuildRequires: gettext
BuildRequires: graphviz
BuildRequires: texinfo


%description
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.

%package -n python3-sphinx
Summary:Python documentation generator

Requires:      python-sphinx-locale = %{?epoch}:%{version}-%{release}
Requires:      python3-babel python3-docutils python3-jinja2 python3-pygments
Requires:      python3-snowballstemmer python3-sphinx_rtd_theme python3-sphinx-theme-alabaster
Requires:      python3-imagesize python3-requests python3-six python3-packaging
Requires:      environment(modules) python3-sphinxcontrib-websupport python3-mock
Requires(pre): /usr/sbin/alternatives
Recommends:    graphviz ImageMagick

Obsoletes:     python3-sphinxcontrib-napoleon < 0.3.0
Provides:      python3-sphinxcontrib-napoleon = %{?epoch}:%{version}-%{release}
Provides:      python(Sphinx) = %{?epoch}:%{version}-%{release}
Conflicts:     python2-Sphinx < %{?epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-sphinx}


%description -n python3-sphinx
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

Sphinx uses reStructuredText as its markup language, and many of its
strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.

Although it is still under constant development, the following
features are already present, work fine and can be seen "in action" in
the Python docs:

    * Output formats: HTML (including Windows HTML Help) and LaTeX,
      for printable PDF versions
    * Extensive cross-references: semantic markup and automatic links
      for functions, classes, glossary terms and similar pieces of
      information
    * Hierarchical structure: easy definition of a document tree, with
      automatic links to siblings, parents and children
    * Automatic indices: general index as well as a module index
    * Code handling: automatic highlighting using the Pygments highlighter
    * Various extensions are available, e.g. for automatic testing of
      snippets and inclusion of appropriately formatted docstrings.

%package  help
Summary:Documentation for %{name}
Requires:      python(Sphinx) = %{?epoch}:%{version}-%{release}
Provides:      python-sphinx-doc python-sphinx-latex
Obsoletes:     python-sphinx-doc < %{?epoch}:%{version}-%{release}
Obsoletes:     python-sphinx-latex < %{?epoch}:%{version}-%{release}

%description   help
This package contains help documentation in reST and HTML formats.

%package   locale
Summary:Locale files for python-sphinx

%description   locale
This package contains locale files for Sphinx.

%prep
%autosetup -n Sphinx-%{version} -p1

dos2unix -k ./sphinx/themes/basic/static/jquery.js

%build
%py3_build

export PYTHONPATH=$PWD
pushd doc
export SPHINXBUILD="%{__python3} ../sphinx/cmd/build.py"
make html SPHINXBUILD="$SPHINXBUILD"
make man SPHINXBUILD="$SPHINXBUILD"
rm -rf _build/html/.buildinfo
mv _build/html ..
popd


%install
%py3_install

# For backwards compatibility. Remove around Fedora 33 (with care)
install -d %{buildroot}%{_libexecdir}/python3-sphinx
for i in sphinx-{apidoc,autogen,build,quickstart}; do
    ln -s %{_bindir}/$i %{buildroot}%{_bindir}/$i-%{python3_version}
    ln -s %{_bindir}/$i %{buildroot}%{_bindir}/$i-3
    ln -s %{_bindir}/$i %{buildroot}%{_libexecdir}/python3-sphinx/$i
done

rm -f %{buildroot}%{python3_sitelib}/sphinx/locale/.DS_Store
rm -rf %{buildroot}%{python3_sitelib}/sphinx/locale/.tx

pushd doc
install -d %{buildroot}%{_mandir}/man1
for f in _build/man/sphinx-*.1;
do
    cp -p $f %{buildroot}%{_mandir}/man1/$(basename $f)
done
popd

rm -rf doc/_build
sed -i 's|python ../sphinx-build.py|/usr/bin/sphinx-build|' doc/Makefile
mv doc reST
rm reST/make.bat

pushd %{buildroot}%{python3_sitelib}

for lang in `find sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/sphinx/locale/$lang
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.js \
     %{buildroot}%{_datadir}/sphinx/locale/$lang/
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.mo \
    %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
  rm -rf sphinx/locale/$lang
done
popd

mkdir %{buildroot}%{python3_sitelib}/sphinxcontrib

%find_lang sphinx

(cd %{buildroot} && find . -name 'sphinx.js') | sed -e 's|^.||' | sed -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.js$\):%lang(\2) \1\2\3:' \
  >> sphinx.lang


%if %{with tests}
%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PATH=%{buildroot}%{_bindir}:$PATH
%endif

%files locale -f sphinx.lang
%license LICENSE
%dir %{_datadir}/sphinx/
%dir %{_datadir}/sphinx/locale
%dir %{_datadir}/sphinx/locale/*

%files -n python3-sphinx -f sphinx.lang
%license LICENSE
%doc AUTHORS CHANGES EXAMPLES README.rst
%{_bindir}/sphinx-*
%{python3_sitelib}/sphinx/
%dir %{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/Sphinx-%{version}-py%{python3_version}.egg-info/
%{_libexecdir}/python3-sphinx/

%files help
%doc html reST
%{_mandir}/man1/*

%changelog
* Tue Jul 27 2021 OpenStack_SIG <openstack@openeuler.org> - 3.5.2-1
- update to 3.5.2

* Wed Jan 13 2021 SimpleUpdate Robot <tc@openeuler.org> - 3.4.3-1
- Upgrade to version 3.4.3

* Wed Aug 5  2020 tianwei <tianwei12@huawei.com> - 3.1.2-2
- add package locale and help

* Fri Jul 31 2020 tianwei <tianwei12@huawei.com> - 3.1.2-1
- Package update to 3.1.2

* Thu Feb 20 2020 Lijin Yang <yanglijin@huawei.com> - 1:1.7.6-6
- delete useless files

* Thu Feb 20 2020 Lijin Yang <yanglijin@huawei.com> - 1:1.7.6-5
- Type: enhancement
- ID: NA
- SUG: NA
- DESC: make sphinx-build enable

* Thu Nov 14 2019 Lijin Yang <yanglijin@huawei.com> - 1:1.7.6-4
- init package
