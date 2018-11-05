Name:    dnf-plugin-ovl
Version: 0.0.1
Release: 2%{?dist}
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
* Mon Nov 05 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.0.1-2
- Add missing Requires and BuildRequires
- Make package noarch

* Sun Feb 25 2018 Florian Ludwig <vierzigundzwei@gmail.com> - 0.0.1-1
- Initial package
