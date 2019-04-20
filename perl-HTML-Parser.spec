#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-Parser
Version  : 3.72
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/G/GA/GAAS/HTML-Parser-3.72.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GAAS/HTML-Parser-3.72.tar.gz
Summary  : 'HTML parser class'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-HTML-Parser-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTML::Tagset)
BuildRequires : perl(HTTP::Headers)
BuildRequires : perl(URI)

%description
OVERVIEW
The HTML-Parser distribution is is a collection of modules that parse
and extract information from HTML documents.  The modules present in
this collection are:

%package dev
Summary: dev components for the perl-HTML-Parser package.
Group: Development
Requires: perl-HTML-Parser-lib = %{version}-%{release}
Provides: perl-HTML-Parser-devel = %{version}-%{release}

%description dev
dev components for the perl-HTML-Parser package.


%package lib
Summary: lib components for the perl-HTML-Parser package.
Group: Libraries

%description lib
lib components for the perl-HTML-Parser package.


%prep
%setup -q -n HTML-Parser-3.72

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/HTML/Entities.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/HTML/Filter.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/HTML/HeadParser.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/HTML/LinkExtor.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/HTML/Parser.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/HTML/PullParser.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/HTML/TokeParser.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::Entities.3
/usr/share/man/man3/HTML::Filter.3
/usr/share/man/man3/HTML::HeadParser.3
/usr/share/man/man3/HTML::LinkExtor.3
/usr/share/man/man3/HTML::Parser.3
/usr/share/man/man3/HTML::PullParser.3
/usr/share/man/man3/HTML::TokeParser.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/HTML/Parser/Parser.so
