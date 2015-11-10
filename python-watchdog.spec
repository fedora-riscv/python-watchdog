%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%endif

%global modname watchdog

Name:               python-watchdog
Version:            0.8.2
Release:            3%{?dist}
Summary:            File system events monitoring

Group:              Development/Libraries
License:            ASL 2.0 and BSD and MIT
URL:                http://pypi.python.org/pypi/watchdog
Source0:            http://pypi.python.org/packages/source/w/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      pytest
BuildRequires:      python-pytest-cov
BuildRequires:      PyYAML >= 3.09
BuildRequires:      python-argh >= 0.8.1
BuildRequires:      python-pathtools >= 0.1.1

%if 0%{?with_python3}
BuildRequires:      python3-devel
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-PyYAML >= 3.09
BuildRequires:      python3-argh >= 0.8.1
BuildRequires:      python3-pathtools >= 0.1.1
%endif

%description
A Python API and shell utilities to monitor file system events.

%if 0%{?with_python3}
%package -n python3-watchdog
Summary:            Filesystem events monitoring
Group:              Development/Libraries

%description -n python3-watchdog
A Python API and shell utilities to monitor file system events.

%endif

%prep
%setup -q -n %{modname}-%{version}

# Remove all shebangs
find src -name "*.py" | xargs sed -i -e '/^#!\//, 1d'

# Remove +x of the README file
chmod -x README.rst

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
mv %{buildroot}/%{_bindir}/watchmedo %{buildroot}/%{_bindir}/watchmedo-py3
popd
%endif
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%check
# Tests are no currently included in the releases
# https://github.com/gorakhargosh/watchdog/pull/232

#%{__python2} setup.py test
#%if 0%{?with_python3}
#pushd %{py3dir}
#%{__python3} setup.py test
#popd
#%endif

%files
%doc README.rst LICENSE
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{modname}-%{version}*
%{_bindir}/watchmedo

%if 0%{?with_python3}
%files -n python3-watchdog
%doc README.rst LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*
%{_bindir}/watchmedo-py3

%endif

%changelog
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
