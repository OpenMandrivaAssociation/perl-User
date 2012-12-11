%define upstream_name    User
%define upstream_version 1.9

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	API for locating user information regardless of OS
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/User/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module allows applications to retrieve per-user characteristics.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/User.pm
%{_mandir}/*/*


%changelog
* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.900.0-1mdv2011.0
+ Revision: 551201
- update to 1.9

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.8-5mdv2010.0
+ Revision: 430612
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.8-4mdv2009.0
+ Revision: 258728
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.8-3mdv2009.0
+ Revision: 246677
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.8-1mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.8-1mdv2008.0
+ Revision: 20767
- 1.8


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-2mdv2007.0
- Rebuild

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-1mdk
- first mdk release

