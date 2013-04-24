Name:		puppet-rsync	
Version:	0.1
Release:	1cisco%{?dist}
Summary:	Puppet rsync module

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-rsync.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
 This module manages rsync clients, repositories, and servers as well as providing defines to easily grab data via rsync.


%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{name}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{name}/

%files
%dir %{_usr}/share/puppet/modules/%{name}/
%{_usr}/share/puppet/modules/%{name}/*


%defattr(-,root,root,-)
%doc README.markdown LICENSE CHANGELOG

%clean
rm -rf %{buildroot}

%changelog
* Tue Apr 24 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

