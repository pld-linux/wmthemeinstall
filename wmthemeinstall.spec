Summary:	Window Maker theme installation program
Summary(pl):	Program do instalacji tematów dla Window Makera
Name:		wmthemeinstall
Version:	0.62
Release:	2
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
License:	GPL
Source0:	http://hellblazer.dhis.org/projects/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-options.patch
URL:		http://hellblazer.dhis.org/projects/
BuildRequires:	gtk+-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	WindowMaker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6

%description
Window Maker Theme Install is a quick little WindowMaker theme
installation program that allows for the themes to be installed for
the whole system or a single user easily.

%description -l pl
Window Maker Theme Install jest szybkim i ma³ym programem, s³u¿±cym do
instalacji tematów WindowMakera. Pozwala na ³atw± instalacjê tematów
zarówno dla ca³ego systemu jak i dla pojedyñczego u¿ytkownika.

%prep
%setup -q
%patch -p0

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

gzip -9nf README ChangeLog AUTHORS NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/wmthemeinstall
%{_applnkdir}/Utilities/wmthemeinstall.desktop
