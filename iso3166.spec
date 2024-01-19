%global srcname iso3166
%global common_summary Self-contained ISO 3166-1 country definitions
%global common_description ISO 3166-1 defines two-letter, three-letter, and three-digit country\
codes. python-iso3166 is a self-contained module that converts between these\
codes and the corresponding country name.

Name:           python-%{srcname}
Version:	2.1.1
Release:	1
Summary:        %{common_summary}

License:        MIT
URL:            https://github.com/deactivated/python-iso3166/
Source0:	https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildArch:      noarch
Provides:       python3-%{srcname}
%{?python_provide:%python_provide python3-%{srcname}}

%description
%{common_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py_build

%install
%py_install

%files
%doc CHANGES README.rst
%license LICENSE.txt
%{python_sitelib}/*
