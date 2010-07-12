%define upstream_name    User
%define upstream_version 1.9

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:        API for locating user information regardless of OS
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/User/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{upstream_version}

%description
This module allows applications to retrieve per-user characteristics.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/User.pm
%{_mandir}/*/*
