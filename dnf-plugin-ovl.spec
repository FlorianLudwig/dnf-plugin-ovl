Name:    dnf-plugin-ovl
Version: 0.0.1
Release: 1%{?dist}
Summary: GNU Hello
URL:     https://github.com/FlorianLudwig/dnf-plugin-ovl
License: GPLv2+

Source0: https://github.com/FlorianLudwig/dnf-plugin-ovl/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

Requires: python3-dnf

%description
TBD

%prep
%autosetup

%build


%install
install -D -p ovl.py %{buildroot}/%{python3_sitelib}/dnf-plugins/ovl.py

%files
%{python3_sitelib}/dnf-plugins/ovl.py
%{python3_sitelib}/dnf-plugins/__pycache__/ovl.*
%{python3_sitelib}/dnf-plugins/__pycache__/ovl.*

%changelog
