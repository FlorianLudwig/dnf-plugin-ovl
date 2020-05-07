Name:    dnf-plugin-ovl
Version: 0.0.4
Release: 1%{?dist}
Summary: GNU Hello
URL:     https://github.com/FlorianLudwig/dnf-plugin-ovl
License: GPLv2+

Source0: https://github.com/AaronDMarasco/dnf-plugin-ovl/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel

Requires: python3-dnf

%description
Workaround to run dnf on overlayfs. A port of yum-plugin-ovl to dnf.

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
* Thu May 07 2020 Aaron D. Marasco <dnf-plugin-ovl@marascos.net> - 0.0.4-1
- Fix overlayfs detection on CentOS 8 / RHEL 8 / Red Hat's UBI images

* Mon Nov 05 2018 Till Hofmann <thofmann@fedoraproject.org> - 0.0.1-2
- Add missing Requires and BuildRequires
- Make package noarch

* Sun Feb 25 2018 Florian Ludwig <vierzigundzwei@gmail.com> - 0.0.1-1
- Initial package
