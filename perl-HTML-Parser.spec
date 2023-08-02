#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-Parser
Version  : 3.81
Release  : 52
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTML-Parser-3.81.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTML-Parser-3.81.tar.gz
Summary  : 'HTML parser class'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-Parser-license = %{version}-%{release}
Requires: perl-HTML-Parser-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTML::Tagset)
BuildRequires : perl(HTTP::Headers)
BuildRequires : perl(URI)
BuildRequires : perl(URI::URL)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
HTML::Parser - HTML parser class
SYNOPSIS
use strict;
use warnings;
use HTML::Parser ();

%package dev
Summary: dev components for the perl-HTML-Parser package.
Group: Development
Provides: perl-HTML-Parser-devel = %{version}-%{release}
Requires: perl-HTML-Parser = %{version}-%{release}

%description dev
dev components for the perl-HTML-Parser package.


%package license
Summary: license components for the perl-HTML-Parser package.
Group: Default

%description license
license components for the perl-HTML-Parser package.


%package perl
Summary: perl components for the perl-HTML-Parser package.
Group: Default
Requires: perl-HTML-Parser = %{version}-%{release}

%description perl
perl components for the perl-HTML-Parser package.


%prep
%setup -q -n HTML-Parser-3.81
cd %{_builddir}/HTML-Parser-3.81

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-Parser
cp %{_builddir}/HTML-Parser-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTML-Parser/1f708223a66ca13060f180a7da8c5479b89a8b00 || :
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
/usr/share/man/man3/HTML::Entities.3
/usr/share/man/man3/HTML::Filter.3
/usr/share/man/man3/HTML::HeadParser.3
/usr/share/man/man3/HTML::LinkExtor.3
/usr/share/man/man3/HTML::Parser.3
/usr/share/man/man3/HTML::PullParser.3
/usr/share/man/man3/HTML::TokeParser.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-Parser/1f708223a66ca13060f180a7da8c5479b89a8b00

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
