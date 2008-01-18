Summary:	Mergeant database admin tool
Summary(pl.UTF-8):	Narzędzie do administrowania bazami danych
Name:		mergeant
Version:	0.67
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mergeant/0.67/%{name}-%{version}.tar.bz2
# Source0-md5:	c0cf45891f7704b11fb00281068b2f6f
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.11
BuildRequires:	libgda3-devel >= 1.2.1
BuildRequires:	libglade2 >= 2.0.1
BuildRequires:	libgnomedb3-devel >= 1.2.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Obsoletes:	mergeant-devel
Obsoletes:	mergeant-libs
Obsoletes:	mergeant-static
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

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-update-mimedb \
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

%post
/usr/bin/scrollkeeper-update
%update_mime_database
%update_desktop_database_post
%update_icon_cache hicolor

%postun
/usr/bin/scrollkeeper-update
%update_desktop_database_postun
%update_mime_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/mergeant
%{_libdir}/bonobo/servers/*.server
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/mergeant
%{_pixmapsdir}/mergeant.png
%{_iconsdir}/hicolor/48x48/mimetypes/*.png
%{_datadir}/mime/packages/mergeant.xml
