Summary:	helper programs for debian/rules
Name:		debhelper
Version:	5.0.62
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.debian.org/debian/pool/main/d/debhelper/%{name}_%{version}.tar.gz
# Source0-md5:	7c611f49e95db3638f0bdef2458677ed
URL:		http://kitenet.net/~joey/code/debhelper/
BuildRequires:	dpkg
BuildRequires:	fakeroot
BuildRequires:	perl-tools-pod
BuildRequires:	po4a
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A collection of programs that can be used in a debian/rules file to
automate common tasks related to building Debian packages. Programs
are included to install various files into your package, compress
files, fix file permissions, integrate your package with the Debian
menu system, debconf, doc-base, etc.

Most Debian packages use debhelper as part of their build process.

%prep
%setup -q -n %{name}

%build
fakeroot debian/rules binary
mv debian/debhelper/usr/share/doc/debhelper doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
cp -a debian/debhelper/* $RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT/DEBIAN
rm -rf $RPM_BUILD_ROOT%{_docdir}/debhelper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/* examples debian/changelog
%attr(755,root,root) %{_bindir}/dh_*
%{_datadir}/%{name}

%dir %{perl_vendorlib}/Debian
%dir %{perl_vendorlib}/Debian/Debhelper
%{perl_vendorlib}/Debian/Debhelper/Dh_Getopt.pm
%{perl_vendorlib}/Debian/Debhelper/Dh_Lib.pm
%{perl_vendorlib}/Debian/Debhelper/Dh_Version.pm

%{_mandir}/man1/dh_*.1*
%lang(es) %{_mandir}/es/man1/dh_*.1*
%lang(fr) %{_mandir}/fr/man1/dh_*.1*
%{_mandir}/man7/debhelper.7*
%lang(es) %{_mandir}/es/man7/debhelper.7*
%lang(fr) %{_mandir}/fr/man7/debhelper.7*