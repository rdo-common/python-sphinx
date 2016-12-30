%if 0%{?fedora}
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

# At some point, RHEL will need to be in here too
%if 0%{?fedora} && 0%{?fedora} > 24
%global py3_default 1
%else
%global py3_default 0
%endif

%global upstream_name Sphinx

Name:       python-sphinx
Version:    1.5.1
Release:    1%{?dist}
Summary:    Python documentation generator

Group:      Development/Tools

# Unless otherwise noted, the license for code is BSD
# sphinx/util/stemmer.py Public Domain
# sphinx/pycode/pgen2 Python
# jquery (MIT or GPLv2)
License:    BSD and Public Domain and Python and (MIT or GPLv2)
URL:        http://sphinx-doc.org/
Source0:    https://files.pythonhosted.org/packages/source/S/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
Source1:    python2-sphinx
Source2:    python3-sphinx
Source3:    zz-modules-python-sphinx.sh
Source4:    zz-modules-python-sphinx.csh
#Patch0:     Sphinx-1.2.1-mantarget.patch
# Upstream fix for xapian 1.4
# https://github.com/sphinx-doc/sphinx/commit/cf795894b9290c5ab2035ae21535f0a7f4b7107a
Patch1:     python-sphinx-xapian.patch

BuildArch:     noarch
BuildRequires: python2-devel >= 2.4
BuildRequires: python2-babel
BuildRequires: python2-setuptools
BuildRequires: python-docutils
BuildRequires: python-jinja2
BuildRequires: python-pygments >= 2.0
BuildRequires: python-six
BuildRequires: python2-sphinx_rtd_theme
BuildRequires: python2-sphinx-theme-alabaster
BuildRequires: python2-imagesize
BuildRequires: python2-requests
BuildRequires: environment(modules)

# for fixes
BuildRequires: dos2unix

# for testing
BuildRequires: python-nose
BuildRequires: gettext
BuildRequires: texinfo
BuildRequires: graphviz
BuildRequires: python-sqlalchemy
BuildRequires: python2-mock
BuildRequires: python-whoosh
BuildRequires: python2-snowballstemmer
# note: no Python3 xapian binding yet
BuildRequires: xapian-bindings-python
BuildRequires: texlive-collection-fontsrecommended
BuildRequires: texlive-collection-latex
BuildRequires: texlive-dvipng
BuildRequires: texlive-dvisvgm
BuildRequires: texlive-ucs
BuildRequires: tex(cmap.sty)
BuildRequires: tex(ecrm1000.tfm)
BuildRequires: tex(fancybox.sty)
BuildRequires: tex(footnote.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(parskip.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(threeparttable.sty)
BuildRequires: tex(upquote.sty)
BuildRequires: tex(wrapfig.sty)
BuildRequires: tex(capt-of.sty)
BuildRequires: tex(needspace.sty)
BuildRequires: tex(eqparbox.sty)
BuildRequires: tex(amsmath.sty)
BuildRequires: tex(amsthm.sty)
BuildRequires: tex(amssymb.sty)
BuildRequires: tex(amsfonts.sty)
BuildRequires: tex(bm.sty)
BuildRequires: tex(palatino.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(eqparbox.sty)
BuildRequires: tex(atbegshi.sty)
BuildRequires: tex(anyfontsize.sty)
BuildRequires: tex(luatex85.sty)

%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-babel
BuildRequires: python3-setuptools
BuildRequires: python3-docutils
BuildRequires: python3-jinja2
BuildRequires: python3-pygments
BuildRequires: python3-nose
BuildRequires: python3-sqlalchemy
BuildRequires: python3-mock
BuildRequires: python3-whoosh
BuildRequires: python3-snowballstemmer
BuildRequires: python3-six
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-sphinx-theme-alabaster
BuildRequires: python3-imagesize
BuildRequires: python3-requests
%endif # with_python3


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


%package -n    python2-sphinx
Summary:       Python documentation generator
Requires:      python-sphinx-locale = %{version}-%{release}
Requires:      python2-babel
Requires:      python-docutils
Requires:      python-jinja2
Requires:      python-pygments
Requires:      python2-mock
Requires:      python2-snowballstemmer
Requires:      python2-sphinx_rtd_theme
Requires:      python2-six
Requires:      python2-sphinx-theme-alabaster
Requires:      python2-imagesize
Requires:      python2-requests
Requires(posttrans): Lmod
# Needed to get rid of the alternatives config installed in f24 and f25
# versions of the package
Requires(posttrans): /usr/sbin/alternatives
Recommends:    graphviz
Obsoletes:     python-sphinx <= 1.2.3
Obsoletes:     python-sphinxcontrib-napoleon < 0.5
Provides:      python-sphinxcontrib-napoleon = %{version}-%{release}
Obsoletes:     python2-Sphinx <= 1.3.1-4
Provides:      python2-Sphinx = %{version}-%{release}
Provides:      python(Sphinx) = %{version}-%{release}
%{?python_provide:%python_provide python2-sphinx}
Conflicts:     python3-sphinx < %{version}-%{release}

%description -n python2-sphinx
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


%package latex
Summary:       LaTeX builder dependencies for %{name}
Requires:      python(Sphinx) = %{version}-%{release}
Requires:      texlive-collection-fontsrecommended
Requires:      texlive-collection-latex
Requires:      texlive-dvipng
Requires:      texlive-dvisvgm
Requires:      texlive-ucs
Requires:      tex(cmap.sty)
Requires:      tex(ecrm1000.tfm)
Requires:      tex(fancybox.sty)
Requires:      tex(footnote.sty)
Requires:      tex(framed.sty)
Requires:      tex(multirow.sty)
Requires:      tex(parskip.sty)
Requires:      tex(titlesec.sty)
Requires:      tex(threeparttable.sty)
Requires:      tex(upquote.sty)
Requires:      tex(wrapfig.sty)
Requires:      tex(capt-of.sty)
Requires:      tex(needspace.sty)
Requires:      tex(eqparbox.sty)
Requires:      tex(amsmath.sty)
Requires:      tex(amsthm.sty)
Requires:      tex(amssymb.sty)
Requires:      tex(amsfonts.sty)
Requires:      tex(bm.sty)
Requires:      tex(palatino.sty)
Requires:      tex(multirow.sty)
Requires:      tex(eqparbox.sty)
Requires:      tex(atbegshi.sty)
Requires:      tex(anyfontsize.sty)
Requires:      tex(luatex85.sty)
Obsoletes:     python3-sphinx-latex < 1.4.4-2

%description latex
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package pulls in the TeX dependencies needed by Sphinx's LaTeX
builder.


%if 0%{?with_python3}
%package -n python3-sphinx
Summary:       Python documentation generator
Group:         Development/Tools
Requires:      python-sphinx-locale = %{version}-%{release}
Requires:      python3-babel
Requires:      python3-docutils
Requires:      python3-jinja2
Requires:      python3-pygments
Requires:      python3-mock
Requires:      python3-snowballstemmer
Requires:      python3-sphinx_rtd_theme
Requires:      python3-sphinx-theme-alabaster
Requires:      python3-imagesize
Requires:      python3-requests
Requires:      python3-six
Recommends:    graphviz
Requires(posttrans): Lmod
# Needed to get rid of the alternatives config installed in f24 and f25
# versions of the package
Requires(posttrans): /usr/sbin/alternatives
Obsoletes:     python3-sphinxcontrib-napoleon < 0.3.0
Provides:      python3-sphinxcontrib-napoleon = %{version}-%{release}
Provides:      python(Sphinx) = %{version}-%{release}
%{?python_provide:%python_provide python3-sphinx}
Conflicts:     python2-Sphinx < %{version}-%{release}
Conflicts:     python2-sphinx < %{version}-%{release}

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
%endif # with_python3


%package doc
Summary:       Documentation for %{name}
Group:         Documentation
License:       BSD
Requires:      python(Sphinx) = %{version}-%{release}

%description doc
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package contains documentation in reST and HTML formats.


%package locale
Summary:       Locale files for %{name}
Group:         Development/Tools
License:       BSD

%description locale
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

This package contains locale files for Sphinx

%prep
%autosetup -n %{upstream_name}-%{version}%{?prerel} -p1

sed '1d' -i sphinx/pycode/pgen2/token.py

# fix line encoding of bundled jquery.js
dos2unix -k ./sphinx/themes/basic/static/jquery.js

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # with_python3

pushd doc
make html
make man
rm -rf _build/html/.buildinfo
mv _build/html ..
popd


%install
%if 0%{?with_python3}
%py3_install
install -d %{buildroot}%{_libexecdir}/python3-sphinx
for i in sphinx-{apidoc,autogen,build,quickstart}; do
    mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i-%{python3_version}
    ln -s $i-%{python3_version} %{buildroot}%{_bindir}/$i-3
    ln -s %{_bindir}/$i-3 %{buildroot}%{_libexecdir}/python3-sphinx/$i
done
%endif # with_python3

%py2_install
install -d %{buildroot}%{_libexecdir}/python2-sphinx
for i in sphinx-{apidoc,autogen,build,quickstart}; do
    mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i-%{python2_version}
    ln -s $i-%{python2_version} %{buildroot}%{_bindir}/$i-2
    ln -s %{_bindir}/$i-2 %{buildroot}%{_libexecdir}/python2-sphinx/$i
done

pushd doc
# Deliver man pages
install -d %{buildroot}%{_mandir}/man1
for f in _build/man/sphinx-*.1;
do
    ### TODO: these are all the same.  Do we really need to ship them three
    ### times or is it fine to just ship them as e.g. sphinx-build.1
    cp -p $f %{buildroot}%{_mandir}/man1/$(basename $f)
    cp -p $f %{buildroot}%{_mandir}/man1/$(basename $f | sed -e "s|.1$|-%{python2_version}.1|")
    cp -p $f %{buildroot}%{_mandir}/man1/$(basename $f | sed -e "s|.1$|-%{python3_version}.1|")
done

# Remove language files, they're identical to the ones from the
# Python 2 build that will be moved to /usr/share below
find %{buildroot}%{python3_sitelib}/sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -exec rm -rf '{}' \;
popd

# Deliver rst files
rm -rf doc/_build
sed -i 's|python ../sphinx-build.py|/usr/bin/sphinx-build|' doc/Makefile
mv doc reST

# Move language files to /usr/share;
# patch to support this incorporated in 0.6.6
pushd %{buildroot}%{python_sitelib}

for lang in `find sphinx/locale -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f "`;
do
  install -d %{buildroot}%{_datadir}/sphinx/locale/$lang
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.js \
     %{buildroot}%{_datadir}/sphinx/locale/$lang/
  mv sphinx/locale/$lang/LC_MESSAGES/sphinx.mo \
    %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
  rm -rf sphinx/locale/$lang
done
popd

install -d %{buildroot}%{_modulesdir}/python-sphinx
install -m 0644 %{SOURCE1} %{buildroot}%{_modulesdir}/python-sphinx/
sed -i 's|@python2_sphinx_dir@|%{_libexecdir}/python2-sphinx|' %{buildroot}%{_modulesdir}/python-sphinx/python2-sphinx
install -m 0644 %{SOURCE2} %{buildroot}%{_modulesdir}/python-sphinx/
sed -i 's|@python3_sphinx_dir@|%{_libexecdir}/python3-sphinx|' %{buildroot}%{_modulesdir}/python-sphinx/python3-sphinx
install -d %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/profile.d/zz-modules-python-sphinx.sh
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d/zz-modules-python-sphinx.csh

%if %{py3_default}
ln -s python3-sphinx %{buildroot}%{_modulesdir}/python-sphinx/default

# These symlinks establish a default for when a package is first installed (and
# therefore, environment modules is not loaded).  The user can immediately
# switch them by using module swap python-sphinx/python2-sphinx
for filename in sphinx-{build,apidoc,autogen,quickstart} ; do
ln -s %{_libexecdir}/python3-sphinx/$filename %{buildroot}%{_bindir}/$filename
done

%else
ln -s python2-sphinx %{buildroot}%{_modulesdir}/python-sphinx/default

# These symlinks establish a default for when a package is first installed (and
# therefore, environment modules is not loaded).  The user can immediately
# switch them by using module swap python-sphinx/python3-sphinx
for filename in sphinx-{build,apidoc,autogen,quickstart} ; do
ln -s %{_libexecdir}/python2-sphinx/$filename %{buildroot}%{_bindir}/$filename
done

%endif

%find_lang sphinx

# Language files; Since these are javascript, it's not immediately obvious to
# find_lang that they need to be marked with a language.
(cd %{buildroot} && find . -name 'sphinx.js') | sed -e 's|^.||' | sed -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.js$\):%lang(\2) \1\2\3:' \
  >> sphinx.lang


%check
LANG=en_US.UTF-8 make test
%if 0%{?with_python3}
pushd %{py3dir}
LANG=en_US.UTF-8 PYTHON=python3 make test
popd
%endif # with_python3


%pre -n python2-sphinx
# python-sphinx as shipped in an update to f24 and f25 used alternatives.  So
# we need to clean up the alternatives configuration until at least f27
%{_sbindir}/update-alternatives --remove sphinx-build %{_bindir}/sphinx-build-%{python2_version} || :

%if 0%{?with_python3}
%pre -n python3-sphinx
# python-sphinx as shipped in an update to f24 and f25 used alternatives.  So
# we need to clean up the alternatives configuration until at least f27
%{_sbindir}/update-alternatives --remove sphinx-build %{_bindir}/sphinx-build-%{python3_version} || :
%endif # with_python3


%files latex
%license LICENSE

%files locale -f sphinx.lang
%license LICENSE
%dir %{_datadir}/sphinx/
%dir %{_datadir}/sphinx/locale
%dir %{_datadir}/sphinx/locale/*

%files -n python2-sphinx
%license LICENSE
%doc AUTHORS CHANGES EXAMPLES README.rst
%{_bindir}/sphinx-*-2*
%{python2_sitelib}/sphinx/
%{python2_sitelib}/Sphinx-%{version}-py%{python2_version}.egg-info/
%exclude %{_mandir}/man1/sphinx-*-%{python3_version}.1*
%{_mandir}/man1/*
%{_libexecdir}/python2-sphinx/
%{_modulesdir}/python-sphinx/python2-sphinx
%if !%{py3_default}
%{_modulesdir}/python-sphinx/default
%endif
%{_sysconfdir}/profile.d/zz-modules-python-sphinx.sh
%{_sysconfdir}/profile.d/zz-modules-python-sphinx.csh

%if 0%{?with_python3}

%files -n python3-sphinx
%license LICENSE
%doc AUTHORS CHANGES EXAMPLES README.rst
%{_bindir}/sphinx-*-3*
%{_bindir}/sphinx-build
%{_bindir}/sphinx-apidoc
%{_bindir}/sphinx-autogen
%{_bindir}/sphinx-quickstart
%{python3_sitelib}/sphinx/
%{python3_sitelib}/Sphinx-%{version}-py%{python3_version}.egg-info/
%{_mandir}/man1/sphinx-*-%{python3_version}.1*
%{_libexecdir}/python3-sphinx/
%{_modulesdir}/python-sphinx/python3-sphinx
%if %{py3_default}
%{_modulesdir}/python-sphinx/default
%endif
%{_sysconfdir}/profile.d/zz-modules-python-sphinx.sh
%{_sysconfdir}/profile.d/zz-modules-python-sphinx.csh

%endif # with_python3

%files doc
%doc html reST


%changelog
* Fri Dec 30 2016 Orion Poplawski <orion@cora.nwra.com> - 1.5.1-1
- Update to 1.5.1

* Fri Dec 30 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 1.4.9-2
- Remove alternatives.  Alternatives should only be used for a very small
  number of packages (system daemons which also have a compatible command line
  interface).
- Use environment-modules to switch between the python2 and python3 packages
  *but* be aware that no amount of manual switching can get this 100% right.
  The code has to be fixed upstream, not in packaging.

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.4.9-1
- Update to 1.4.9
- Enable python3 tests

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.4.8-3
- Rebuild for Python 3.6
- Disable python3 tests for now

* Thu Oct 6 2016 Avram Lubkin <aviso@fedoraproject.org> - 1.4.8-2
- Added tex(luatex85.sty) dependency to support TexLive 2016

* Thu Oct 6 2016 Avram Lubkin <aviso@fedoraproject.org> - 1.4.8-1
- Update to 1.4.8
- Alternatives fails for scripts sometimes (bz#1382405)

* Sun Sep 4 2016 Avram Lubkin <aviso@fedoraproject.org> - 1.4.6-2
- Alternatives fails for man pages due to existing files

* Fri Sep 2 2016 Avram Lubkin <aviso@fedoraproject.org> - 1.4.6-1
- Update to 1.4.6 (bz#1370810)
- Fix unversioned Obsoletes
- Add alternatives slaves for man pages

* Fri Aug 12 2016 Avram Lubkin <aviso@fedoraproject.org> - 1.4.5-1
- Update to 1.4.5 (bz#1356336)
- Remove Recommends for latex, locale, and doc subpackages (bz#1366624)
- Remove Requires from locale subpackage (bz#1366624)
- Set executable scripts via alternatives  (bz#1321413)
- Change graphviz Requires to Recommends (bz#1366706)

* Sun Jul 03 2016 Avram Lubkin <aviso@fedoraproject.org> - 1.4.4-2
- doc and locale no longer specifically require python2-sphinx
- Colapsed python3-sphinx-latex into python-latex

* Sun Jun 12 2016 Avram Lubkin <aviso@fedoraproject.org> - 1.4.4-1
- Updated to 1.4.4
- Added python-sphinx-locale for common locale files

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 27 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.1-4
- Obsolete napoleon extension, it is now packaged with sphinx (#1286275)
- Rename python2-Sphinx to python2-sphinx
- Add conflicts to disallow parallel installation of different versions,
  which causes file conflicts because of the shared documentation files.

* Wed Nov 25 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.1-3
- Restore using python2 scripts by default (#1285535)

* Wed Nov 25 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.1-2
- Fix requirements of python2- subpackage
- Provide sphinx-*-{3.5,3} symlinks for each script

* Tue Nov 24 2015 Julien Enselme <jujens@jujens.eu> - 1.3.1-1
- Update to 1.3.1 (#1136284)
- Update to new guidelines
- Make the default executable use python3

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 1.2.3-5
- Rebuilt for Python3.5 rebuild
- add patch to reflect that Python3.5 dropped HTMLParserError

* Mon Jul 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.3-4
- Fix line encoding of bundled jquery.js

* Mon Jul 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.3-3
- Re-introduce LaTeX subpackage, solely for pulling in LaTeX dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb  5 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3
- Mark license file with %%license instead of %%doc

* Thu Feb  5 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-10
- Complete LaTeX builder deps (fixes bz#882166)
- Make test output verbose
- Add BRs needed to enable all tests

* Tue Feb  3 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-9
- python3-sphinx package also Provides: python3-sphinx-latex

* Tue Feb  3 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-8
- If a separate LaTeX subpackage is not generated, the main package should have
  a virtual Provides: for it (bz#1187989)

* Tue Jan 27 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-7
- Disable separate LaTeX builder for now (bz#1185574)

* Thu Jan 22 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.2-6
- Split off LaTeX builder into its own subpackages, to remove TeXLive
  dependencies from the main package.
  Thanks to Robert Kuska <rkuska@redhat.com> for feedback
- Clean up python3-sphinx's locale files, they ended up in the python2 package.
  Share the locale files in /usr/share instead

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.2-4
- Don't own the -3 scripts by python 2 package

* Thu May 22 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.2-3
- Add sphinx-*-3 links to scripts
Resolves: #1098109

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-2
- Rebuild for Python 3.4

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 1.2.2-1
- Update to 1.2.2

* Thu Feb 13 2014 Michel Salim <salimma@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar  9 2013 Michel Salim <salimma@fedoraproject.org> - 1.1.3-7
- Fix inheritance_diagram quoting bug, exposed by the newer, stricter dot

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 21 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.3-5
- Fix for use of sphinx's manpage writer with docutils-0.10

* Mon Aug  6 2012 Michel Salim <salimma@fedoraproject.org> - 1.1.3-4
- Rebuild for Python 3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.3-3
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr  5 2012 Michel Salim <salimma@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Sun Feb  5 2012 Michel Salim <salimma@fedoraproject.org> - 1.1.2-5
- Move python3 runtime dependencies to the right subpackage
- Properly exclude python3 binaries

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 Michel Salim <salimma@fedoraproject.org> - 1.1.2-3
- BR on texlive-latex for LaTeX tests

* Thu Dec  8 2011 Michel Salim <salimma@fedoraproject.org> - 1.1.2-2
- Enable python3 subpackage

* Mon Nov 28 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1.2-1
- Update to upstream 1.1.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.7-1
- Update to upstream 1.0.7

* Mon Jan 17 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.6-1
- Update to upstream 1.0.6

* Mon Nov  1 2010 Michel Salim <salimma@fedoraproject.org> - 1.0.4-3
- Fix -doc Makefile to allow regeneration of .rst files

* Mon Nov  1 2010 Michel Salim <salimma@fedoraproject.org> - 1.0.4-2
- Actually include *.js locale files
- Generate manpages

* Fri Sep 17 2010 Michel Salim <salimma@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- Remove BuildRoot and %%clean declarations

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0-0.1.b2.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 31 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-0.2.b2
- Update to 1.0 beta 2
- Fixes problem building html documentation in non-English locales

* Wed May 26 2010 Michel Salim <salimma@fedoraproject.org> - 1.0-0.1.b1
- Update to 1.0 beta 1

* Tue May 25 2010 Michel Salim <salimma@fedoraproject.org> - 0.6.6-1
- Update to 0.6.6

* Fri May 21 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.5-2
- Few minor tweaks to Gareth's spec file update

* Mon May 10 2010 Gareth Armstrong <gareth.armstrong@hp.com> - 0.6.5-1.hp
- Update to 0.6.5
- Initial import of python-sphinx from Fedora Rawhide for use in HP CMS
- Enforce that Sphinx requires Python 2.4 or later via an explicit BR
- Minor tweaks to spec file
- Move language files to %%{_datadir}, idea borrowed from Debian's sphinx
  package
- Deliver man pages for sphinx-build & sphinx-quickstart
- Deliver rst documentation files to reST directory in doc sub-package
- Add %%check section for Python2 and add BR on python-nose

* Wed Jan 13 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4
- Fixes a problem using autodoc with pylons projects.

* Fri Sep  4 2009 Michel Salim <salimma@fedoraproject.org> - 0.6.3-1
- Update to 0.6.3

* Mon Aug 17 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2 -- upstream bugfix requested inside bz#512438

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 05 2009 Luke Macken <lmacken@redhat.com> - 0.6.1-2
- Add a patch to use our own setuptools package

* Fri Apr 17 2009 Michel Salim <salimma@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  2 2009 Michel Salim <salimma@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.5-2
- Rebuild for Python 2.6

* Mon Nov 24 2008 Michel Salim <salimma@fedoraproject.org> - 0.5-1
- Update to 0.5

* Fri Oct 10 2008 Michel Salim <salimma@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3

* Wed Aug 27 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.4.2-1.1
- Fix for EL-5 build.

* Mon Aug 25 2008 Michel Salim <salimma@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Mon May 26 2008 Michel Salim <salimma@fedoraproject.org> - 0.3-1
- Update to 0.3

* Fri May  2 2008 Michel Salim <salimma@fedoraproject.org> - 0.1.61950-3
- Split documentation into subpackage
- Exclude C files (not built by default anyway)

* Wed Apr 16 2008 José Matos <jamatos@fc.up.pt> - 0.1.61950-2
- Build html documentation, include it and include the rst
  documentation.

* Thu Mar 27 2008 Michel Salim <michel.sylvan@gmail.com> 0.1.61950-1
- Initial package
