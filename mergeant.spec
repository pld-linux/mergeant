Summary:	Mergeant database admin tool
Summary(pl):	Narzêdzie do administrowania bazami danych
Name:		mergeant
Version:	0.12.0
Release:	1
License:	GPL
Group:		Applications/Databases
# Source0-md5:	c98825d82168fa385a5170dd33801164
Source0:	ftp://ftp.gnome-db.org/pub/gnome-db/sources/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libglade2
BuildRequires:	libgnomedb-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post):	GConf2 >= 2.3.0
Requires(post):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mergeant is a program which helps administer a DBMS database using the
gnome-db framework. Basically, it memorizes all the structure of the
database, and some queries, and does the SQL queries instead of the
user (not having to type all over again those SQL commands, although
it is still possible to do so).

%description -l pl
Mergeant to program pomagaj±cy w administrowaniu baz± DBMS przy u¿yciu
¶rodowiska gnome-db. Zapamiêtuje ca³± strukturê bazy i czê¶æ zapytañ,
a nastêpnie wykonuje zapytania SQL zamiast u¿ytkownika (który nie musi
wpisywaæ ci±gle tych samych poleceñ SQL - choæ jest to nadal mo¿liwe).

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/mergeant
%dir %{_libdir}/mergeant
%dir %{_libdir}/mergeant/plugins
%{_libdir}/mergeant/plugins/*.la
%attr(755,root,root) %{_libdir}/mergeant/plugins/*.so*
%{_datadir}/application-registry/*
%{_datadir}/applications/*
%{_datadir}/mergeant
%{_datadir}/mime-info/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/document-icons/*
%{_pixmapsdir}/mergeant
