%define upstream_name    Math-Random-ISAAC-XS
%define upstream_version 1.004

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    C implementation of the ISAAC PRNG Algorithm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Math/Math-Random-ISAAC-XS-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::ParseXS)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel

%description
See the Math::Random::ISAAC manpage for the full description.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%clean

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Jan 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1
+ Revision: 633535
- import perl-Math-Random-ISAAC-XS


