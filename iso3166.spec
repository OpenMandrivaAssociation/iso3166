%global srcname iso3166
%global common_summary Self-contained ISO 3166-1 country definitions
%global common_description ISO 3166-1 defines two-letter, three-letter, and three-digit country\
codes. python-iso3166 is a self-contained module that converts between these\
codes and the corresponding country name.

Name:           python-%{srcname}
Version:	1.0
Release:        2
Summary:        %{common_summary}

License:        MIT
URL:            https://github.com/deactivated/python-iso3166/
Source0:	https://files.pythonhosted.org/packages/0e/ae/0b4ee6f5f3f197b1508f21044f8b18508bc04dd4bc1be98d57d7c720330f/iso3166-1.0.tar.gz

BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3egg(setuptools)
BuildRequires:  pythonegg(setuptools)
BuildArch:      noarch

%description
%{common_description}


%package -n python2-%{srcname}
Summary:        %{common_summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{common_description}


%package -n python3-%{srcname}
Summary:        %{common_summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
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


%files -n python3-%{srcname}
%doc CHANGES README.rst
%license LICENSE.txt
%{python_sitelib}/*
