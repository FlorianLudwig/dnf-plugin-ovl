Name:    dnf-plugin-ovl
Version: 0.0.1
Release: 1%{?dist}
Summary: GNU Hello
URL:     https://github.com/FlorianLudwig/dnf-plugin-ovl
License: GPLv2+

Source0: https://github.com/FlorianLudwig/dnf-plugin-ovl/archive/%{version}.tar.gz

BuildRequires: python3-devel

Requires: python3-dnf

%description
TBD

%global debug_package %{nil}

%prep
%autosetup

%build


%install
mkdir -p %{buildroot}/%{python3_sitelib}/dnf-plugins/
cp ovl.py %{buildroot}/%{python3_sitelib}/dnf-plugins/ovl.py

%files
%{python3_sitelib}/dnf-plugins/ovl.py
%{python3_sitelib}/dnf-plugins/__pycache__/ovl.cpython-36.pyc
%{python3_sitelib}/dnf-plugins/__pycache__/ovl.cpython-36.opt-1.pyc

%changelog
