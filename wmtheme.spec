Summary:	Window manager theme utility
Summary(pl.UTF-8):	Narzędzie do obsługi motywów graficznych
Name:		wmtheme
Version:	1.3.3
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e5fb31fcec80f326357ec8314eea0987
Patch0:		%{name}-Makefile.patch
URL:		http://wmtheme.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmtheme is a command-line perl program to manage window manager
themes. There is support for AfterStep, Blackbox, Enlightenment,
Golem, GTK+, IceWM, Oroborus, Sawfish, Window Maker, and xmms. wmtheme
can be used to activate, install, uninstall, and list themes.

%description -l pl.UTF-8
wmtheme jest programem zarządzającym motywami graficznymi. Posiada
wsparcie dla AfterStepa, Blackboksa, Enlightenmenta, Golema, GTK+,
IceWM-a, Oroborusa, Sawfisha, Window Makera i xmms-a. wmtheme może
aktywować, instalować, odinstalować i wyświetlić listę dostępnych
motywów graficznych.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CODING CREDITS README*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/wmtheme/
%{_mandir}/man1/*
