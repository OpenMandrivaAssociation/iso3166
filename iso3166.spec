%global srcname iso3166
%global common_summary Self-contained ISO 3166-1 country definitions
%global common_description ISO 3166-1 defines two-letter, three-letter, and three-digit country\
codes. python-iso3166 is a self-contained module that converts between these\
codes and the corresponding country name.

Name:           python-%{srcname}
Version:	2.0.2
Release:	1
Summary:        %{common_summary}

License:        MIT
URL:            https://github.com/deactivated/python-iso3166/
Source0:	https://files.pythonhosted.org/packages/2c/2b/803db3a6e2f4041cc4e9553d3b27d81fa8938acc0ea4f86f00cc5416d5af/iso3166-2.0.2.tar.gz

BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python)
BuildRequires:  python2dist(setuptools)
BuildRequires:  python3dist(setuptools)
BuildArch:      noarch
Provides:       python3-%{srcname}
%{?python_provide:%python_provide python3-%{srcname}}

%description
%{common_description}

%package -n python2-%{srcname}
Summary:        %{common_summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py_build

%install
%py2_install
%py_install

%files -n python2-%{srcname}
%doc CHANGES README.rst
%license LICENSE.txt
%{python2_sitelib}/*

%files
%doc CHANGES README.rst
%license LICENSE.txt
%{python_sitelib}/*
