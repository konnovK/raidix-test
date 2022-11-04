Name:		testtask
Version:	1.0
Release:	1%{?dist}
Summary:	Package for test task in RAIDIX

License:	-
Source0:	%{name}-%{version}.tar

BuildRequires:	gcc
BuildRequires:  make


%description
Test task in RAIDIX (intern devops)


%prep
%setup -q


%build
make 


%install
make install DESTDIR=%{buildroot}


%files
/usr/bin/testtask

