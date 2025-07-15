Summary:	Window Maker theme installation program
Summary(pl.UTF-8):	Program do instalacji motywów dla Window Makera
Name:		wmthemeinstall
Version:	0.62
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://hellblazer.dhis.org/projects/download/%{name}-%{version}.tar.gz
# Source0-md5:	6af50990ac02973bd09d3cb0e06a74ff
Source1:	%{name}.desktop
Patch0:		%{name}-options.patch
URL:		http://hellblazer.dhis.org/projects/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	zlib-devel
Requires:	WindowMaker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Window Maker Theme Install is a quick little WindowMaker theme
installation program that allows for the themes to be installed for
the whole system or a single user easily.

%description -l pl.UTF-8
Window Maker Theme Install jest szybkim i małym programem, służącym do
instalacji motywów WindowMakera. Pozwala na łatwą instalację motywów
zarówno dla całego systemu jak i dla pojedynczego użytkownika.

%prep
%setup -q
%patch -P0 -p0

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS
%attr(755,root,root) %{_bindir}/wmthemeinstall
%{_desktopdir}/docklets/%{name}.desktop
