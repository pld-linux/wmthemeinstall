Summary:	Window Maker theme installation program
Summary(pl):	Program do instalacji tematów dla Window Makera
Name:		wmthemeinstall
Version:	0.31
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source0:	http://hellblazer.dhis.org/projects/download/%{name}-%{version}.tar.gz
Source1:	wmthemeinstall.desktop
Patch:		wmthemeinstall-options.patch
URL:		http://hellblazer.dhis.org/projects/
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
Requires:	WindowMaker
BuildRoot:   	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

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
%configure 

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Utilities

make install-strip DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Utilities

gzip -9nf README ChangeLog AUTHORS NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS,NEWS}.gz
%attr(755,root,root) %{_bindir}/wmthemeinstall
/usr/X11R6/share/applnk/Utilities/wmthemeinstall.desktop
