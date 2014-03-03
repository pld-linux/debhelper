#
# Conditional build:
%bcond_with	tests		# build with tests

Summary:	Helper programs for debian/rules
Summary(pl.UTF-8):	Programy pomocnicze dla debian/rules
Name:		debhelper
Version:	9.20140228
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	ftp://ftp.debian.org/debian/pool/main/d/debhelper/%{name}_%{version}.tar.gz
# Source0-md5:	40946706785d914567f91fa36d78848a
URL:		http://kitenet.net/~joey/code/debhelper/
BuildRequires:	dpkg
BuildRequires:	fakeroot
BuildRequires:	perl-tools-pod
BuildRequires:	po4a
# uses man-db specific --recode option in dh_installman
BuildRequires:	man-db
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of programs that can be used in a debian/rules file to
automate common tasks related to building Debian packages. Programs
are included to install various files into your package, compress
files, fix file permissions, integrate your package with the Debian
menu system, debconf, doc-base, etc.

Most Debian packages use debhelper as part of their build process.

%description -l pl.UTF-8
Zestaw programów, których można używać w pliku debian/rules do
automatyzacji często wykonywanych zadań związanych z budowaniem
pakietów Debiana. Zawiera programy do instalowania różnych plików
pakietu, kompresji plików, poprawiania uprawnień plików, integracji
pakietu z systemem menu Debiana, debconfem, doc-base itp.

%prep
%setup -q -n %{name}

%build
%{!?with_tests:DEB_BUILD_OPTIONS=nocheck} \
fakeroot debian/rules binary
mv debian/debhelper%{_docdir}/debhelper doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
cp -a debian/debhelper/* $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT/DEBIAN

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/dh
%attr(755,root,root) %{_bindir}/dh_*
%{_datadir}/%{name}

%dir %{perl_vendorlib}/Debian
%dir %{perl_vendorlib}/Debian/Debhelper
%{perl_vendorlib}/Debian/Debhelper/Dh_Buildsystems.pm
%{perl_vendorlib}/Debian/Debhelper/Dh_Getopt.pm
%{perl_vendorlib}/Debian/Debhelper/Dh_Lib.pm
%{perl_vendorlib}/Debian/Debhelper/Dh_Version.pm
%{perl_vendorlib}/Debian/Debhelper/Sequence
%{perl_vendorlib}/Debian/Debhelper/Buildsystem
%{perl_vendorlib}/Debian/Debhelper/Buildsystem.pm

%{_mandir}/man1/dh.1*
%{_mandir}/man1/dh_*.1*
%lang(de) %{_mandir}/de/man1/dh.1*
%lang(de) %{_mandir}/de/man1/dh_*.1*
%lang(es) %{_mandir}/es/man1/dh.1*
%lang(es) %{_mandir}/es/man1/dh_*.1*
%lang(fr) %{_mandir}/fr/man1/dh.1*
%lang(fr) %{_mandir}/fr/man1/dh_*.1*
%{_mandir}/man7/debhelper.7*
%lang(de) %{_mandir}/de/man7/debhelper.7*
%lang(es) %{_mandir}/es/man7/debhelper.7*
%lang(fr) %{_mandir}/fr/man7/debhelper.7*
