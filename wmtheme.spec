Summary:	Window manager theme utility
Summary(pl):	Narz�dzie do obs�ugi motyw�w graficznych
Name:		wmtheme
Version:	1.3.2
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://belnet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	b2ee65eb741fcc9318c0e181dd7fd68c
Patch0:		%{name}-Makefile.patch
URL:		http://wmtheme.sourceforge.net/
BuildRequires:	perl
Requires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
wmtheme is a command-line perl program to manage window manager
themes. There is support for AfterStep, Blackbox, Enlightenment,
Golem, GTK+, IceWM, Oroborus, Sawfish, Window Maker, and xmms. wmtheme
can be used to activate, install, uninstall, and list themes.

%description -l pl
wmtheme jest programem zarz�dzaj�cym motywami graficznymi. Posiada
wsparcie dla AfterStepa, Blackboksa, Enlightenmenta, Golema, GTK+,
IceWM-a, Oroborusa, Sawfisha, Window Makera i xmms-a. wmtheme mo�e
aktywowa�, instalowa�, odinstalowa� i wy�wietli� list� dost�pnych
motyw�w graficznych.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CODING CREDITS README*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/wmtheme/
%{_mandir}/man1/*
