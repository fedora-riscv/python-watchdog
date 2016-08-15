%global modname watchdog

Name:               python-%{modname}
Version:            0.8.3
Release:            3%{?dist}
Summary:            File system events monitoring

License:            ASL 2.0 and BSD and MIT
URL:                http://pypi.python.org/pypi/%{modname}
Source0:            http://pypi.python.org/packages/source/w/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:          noarch

%description
A Python API and shell utilities to monitor file system events.


%package -n python2-%{modname}
BuildArch:          noarch
BuildRequires:      python2-devel
BuildRequires:      pytest
BuildRequires:      python-pytest-cov
BuildRequires:      python2-pytest-timeout
BuildRequires:      PyYAML >= 3.09
BuildRequires:      python2-argh >= 0.8.1
BuildRequires:      python-pathtools >= 0.1.1
Requires:           PyYAML >= 3.09
Requires:           python2-argh >= 0.8.1
Requires:           python-pathtools >= 0.1.1
Summary:            %{summary}
%{?python_provide:%python_provide python2-%{modname}}

%description -n python2-%{modname}
A Python API and shell utilities to monitor file system events.


%package -n python3-%{modname}
BuildArch:          noarch
BuildRequires:      python3-devel
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-pytest-timeout
BuildRequires:      python3-PyYAML >= 3.09
BuildRequires:      python3-argh >= 0.8.1
BuildRequires:      python3-pathtools >= 0.1.1
Requires:           python3-PyYAML >= 3.09
Requires:           python3-argh >= 0.8.1
Requires:           python3-pathtools >= 0.1.1
Summary:            %{summary}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
A Python API and shell utilities to monitor file system events.


%prep
%setup -q -n %{modname}-%{version}

# Remove all shebangs
find src -name "*.py" | xargs sed -i -e '/^#!\//, 1d'

# Remove +x of the README file
chmod -x README.rst

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
%py3_build
%py2_build


%install
%py3_install
pushd %{buildroot}%{_bindir}
mv watchmedo watchmedo-%{python3_version}
ln -s watchmedo-%{python3_version} watchmedo-3
ln -s watchmedo-%{python3_version} watchmedo-py3
popd

%py2_install
pushd %{buildroot}%{_bindir}
mv watchmedo watchmedo-%{python2_version}
ln -s watchmedo-%{python2_version} watchmedo-2
ln -s watchmedo-%{python2_version} watchmedo
popd


%check
%{__python2} setup.py test
%{__python3} setup.py test


%files -n python2-watchdog
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-%{version}*
%exclude %{_bindir}/watchmedo-*3*
%{_bindir}/watchmedo*


%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*
%{_bindir}/watchmedo-3*


%changelog
* Mon Aug 15 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-3
- Add python-pytest-timeout to BR to launch tests

* Thu Aug 12 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-2
- Add python2-pathtools to BR (was two times in Requires)

* Thu Aug 11 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-1
- Update to 0.8.3
- Correct requires
- Update to follow new Python packaging guidelines
- Always build with Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 22 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.8.2-1
- Update to 0.8.2

* Fri Apr 25 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-4
- Adjust the license tag to ASL2.0 and BSD and MIT

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-3
- Adjust the check for Fedora/RHEL release number for the py3 package

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-2
- Remove all shebang of the python files

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-1
- initial package for Fedora
