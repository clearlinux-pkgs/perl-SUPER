#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-SUPER
Version  : 1.20190531
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/SUPER-1.20190531.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHROMATIC/SUPER-1.20190531.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsuper-perl/libsuper-perl_1.20141117-1.debian.tar.xz
Summary  : 'control superclass method dispatch'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-SUPER-license = %{version}-%{release}
Requires: perl-SUPER-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Sub::Identify)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution SUPER,
version 1.20190531:
control superclass method dispatch

%package dev
Summary: dev components for the perl-SUPER package.
Group: Development
Provides: perl-SUPER-devel = %{version}-%{release}
Requires: perl-SUPER = %{version}-%{release}

%description dev
dev components for the perl-SUPER package.


%package license
Summary: license components for the perl-SUPER package.
Group: Default

%description license
license components for the perl-SUPER package.


%package perl
Summary: perl components for the perl-SUPER package.
Group: Default
Requires: perl-SUPER = %{version}-%{release}

%description perl
perl components for the perl-SUPER package.


%prep
%setup -q -n SUPER-1.20190531
cd %{_builddir}
tar xf %{_sourcedir}/libsuper-perl_1.20141117-1.debian.tar.xz
cd %{_builddir}/SUPER-1.20190531
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/SUPER-1.20190531/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-SUPER
cp %{_builddir}/SUPER-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-SUPER/7ebe815bdb539d0c747618dbc46d09c878aa77d8 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-SUPER/103d8dfb2241a1d5256bf2e16db3d80201e4b90d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/SUPER.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-SUPER/103d8dfb2241a1d5256bf2e16db3d80201e4b90d
/usr/share/package-licenses/perl-SUPER/7ebe815bdb539d0c747618dbc46d09c878aa77d8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
