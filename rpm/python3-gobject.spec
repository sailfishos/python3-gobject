Name: python3-gobject
Version: 3.38.0
Release: 1
License: LGPLv2+
Summary: Python 3 bindings for GObject
URL: https://git.gnome.org/browse/pygobject
Source: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(py3cairo) >= 1.11.1
BuildRequires: meson

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python 3 programs.

%package devel
Summary: Development files for building add-on libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-codegen = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: glib2-devel
Requires: python3-devel

%description devel
This package contains files required to build wrappers for %{name}-based
libraries such as pygtk2.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%meson -Dpython=%{__python3}
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install
find $RPM_BUILD_ROOT -name '*.la' -delete
find $RPM_BUILD_ROOT -name '*.a' -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%{python3_sitearch}/gi
%{python3_sitearch}/PyGObject*
%{python3_sitelib}/gi
%{python3_sitelib}/pygtkcompat

%files devel
%defattr(644, root, root, 755)
%dir %{_includedir}/pygobject-3.0
%{_includedir}/pygobject-3.0/*.h
%{_libdir}/pkgconfig/pygobject-3.0.pc
