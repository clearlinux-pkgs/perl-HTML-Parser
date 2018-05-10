#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-Parser
Version  : 3.72
Release  : 18
URL      : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/HTML-Parser-3.72.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/HTML-Parser-3.72.tar.gz
Summary  : 'HTML parser class'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-HTML-Parser-lib
Requires: perl-HTML-Parser-doc
BuildRequires : perl(HTML::Tagset)
BuildRequires : perl(HTTP::Headers)
BuildRequires : perl(URI)

%description
OVERVIEW
The HTML-Parser distribution is is a collection of modules that parse
and extract information from HTML documents.  The modules present in
this collection are:

%package doc
Summary: doc components for the perl-HTML-Parser package.
Group: Documentation

%description doc
doc components for the perl-HTML-Parser package.


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
make V=1  %{?_smp_mflags}
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
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/HTML/Entities.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/HTML/Filter.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/HTML/HeadParser.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/HTML/LinkExtor.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/HTML/Parser.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/HTML/PullParser.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/HTML/TokeParser.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/HTML/Parser/Parser.so
