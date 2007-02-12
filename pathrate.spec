#
Summary:	Estimate network path capacity
Name:		pathrate
Version:	2.4.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www-static.cc.gatech.edu/fac/Constantinos.Dovrolis/%{name}.tar.gz
# Source0-md5:	37d2abcd0604cec282ef94891d09d502
URL:		http://www-static.cc.gatech.edu/fac/Constantinos.Dovrolis/pathrate.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Estimate network path capacity.

%prep
%setup -q -n %{name}_%{version}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name}_snd $RPM_BUILD_ROOT%{_bindir}
install %{name}_rcv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
