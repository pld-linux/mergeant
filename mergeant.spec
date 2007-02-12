Summary:	Mergeant database admin tool
Summary(pl.UTF-8):   Narzędzie do administrowania bazami danych
Name:		mergeant
Version:	0.52
Release:	4
License:	GPL
Group:		Applications/Databases
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mergeant/0.52/%{name}-%{version}.tar.bz2
# Source0-md5:	e9f96b824e452e9b9406b4c11f005b95
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-pluginsdir.patch
Patch2:		%{name}-libgda.patch
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.11
BuildRequires:	libgda-devel >= 1.2.1
BuildRequires:	libglade2 >= 2.0.1
BuildRequires:	libgnomedb-devel >= 1.2.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires:	%{name}-libs >= %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mergeant is a program which helps administer a DBMS database using the
gnome-db framework. Basically, it memorizes all the structure of the
database, and some queries, and does the SQL queries instead of the
user (not having to type all over again those SQL commands, although
it is still possible to do so).

%description -l pl.UTF-8
Mergeant to program pomagający w administrowaniu bazą DBMS przy użyciu
środowiska gnome-db. Zapamiętuje całą strukturę bazy i część zapytań,
a następnie wykonuje zapytania SQL zamiast użytkownika (który nie musi
wpisywać ciągle tych samych poleceń SQL - choć jest to nadal możliwe).

%package libs
Summary:	Mergeant libraries
Summary(pl.UTF-8):   Biblioteki Mergeanta
Group:		X11/Libraries
Requires:	gtk+2 >= 2:2.4.4

%description libs
Mergeant libraries.

%description libs -l pl.UTF-8
Biblioteki Mergeanta.

%package devel
Summary:	Libmergeant development files
Summary(pl.UTF-8):   Pliki nagłówkowe libmergeant
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.4
Requires:	libgda-devel >= 1.2.1
Requires:	libgnomedb-devel >= 1.2.1
Requires:	libxml2-devel

%description devel
Libmergeant development files.

%description devel -l pl.UTF-8
Pliki nagłówkowe libmergeant.

%package static
Summary:	Static Mergeant libraries
Summary(pl.UTF-8):   Biblioteki statyczne Mergeanta
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Mergeant libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Mergeanta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv po/{no,nb}.po

%build
rm -f missing
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	pkgconfigdir=%{_pkgconfigdir} \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name} --with-gnome --all-name

# Remove testing binaries
rm -f $RPM_BUILD_ROOT%{_bindir}/mg-test*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/mergeant
%attr(755,root,root) %{_bindir}/mg-db-browser
%attr(755,root,root) %{_bindir}/mg-verify-file
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*.so*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/application-registry/*
%{_desktopdir}/*.desktop
%{_datadir}/mergeant
%{_datadir}/mime-info/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/document-icons/*
%{_pixmapsdir}/mergeant

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libmergeant
%{_gtkdocdir}/libmergeant

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
