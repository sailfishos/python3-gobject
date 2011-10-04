%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# Last updated for version 2.19.0
%define glib2_version           2.16.0
%define python2_version         2.3.5

### Abstract ###

Name: pygobject2
Version: 2.21.3
Release: 1
License: LGPLv2+
Group: Development/Languages
Summary: Python bindings for GObject
URL: http://www.pygtk.org/
Source: http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.21/pygobject-%{version}.tar.gz
Source101: %{name}-rpmlintrc


### Build Dependencies ###

BuildRequires: automake
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: libtool
BuildRequires: python2-devel >= %{python2_version}

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package codegen
Summary: The code generation program for PyGObject
Group: Development/Languages

%description codegen
The package contains the C code generation program for PyGObject.

%package devel
Summary: Development files for building add-on libraries
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: %{name}-codegen = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: glib2-devel
Requires: pkgconfig

%description devel
This package contains files required to build wrappers for %{name}-based
libraries such as pygtk2.

%package doc
Summary: Documentation files for %{name}
Group: Development/Languages

%description doc
This package contains documentation files for %{name}.

%prep
%setup -q -n pygobject-%{version}

%build
%configure --enable-thread
export tagname=CC
make LIBTOOL=/usr/bin/libtool

%install
rm -rf $RPM_BUILD_ROOT
export tagname=CC
make LIBTOOL=/usr/bin/libtool DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f

rm examples/Makefile*

%clean
rm -fr $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc AUTHORS NEWS README

%{_libdir}/libpyglib-2.0-python.so*
%dir %{python_sitearch}/gtk-2.0
%{python_sitearch}/gtk-2.0/dsextras.*
%{python_sitearch}/pygtk.*

%defattr(755, root, root, 755)
%{python_sitearch}/gtk-2.0/gio
#%{python_sitearch}/gtk-2.0/girepository
%{python_sitearch}/gtk-2.0/glib
%{python_sitearch}/gtk-2.0/gobject

%files codegen
%defattr(755, root, root, 755)
%{_bindir}/pygobject-codegen-2.0
%defattr(644, root, root, 755)
%dir %{_datadir}/pygobject/2.0
%{_datadir}/pygobject/2.0/codegen

%files devel
%defattr(644, root, root, 755)
%dir %{_datadir}/pygobject
%dir %{_includedir}/pygtk-2.0
%{_datadir}/pygobject/2.0/defs
#%{_includedir}/pygobject/bank.h
%{_includedir}/pygtk-2.0/pyglib.h
%{_includedir}/pygtk-2.0/pygobject.h
%{_libdir}/pkgconfig/pygobject-2.0.pc

%files doc
%defattr(644, root, root, 755)
%doc examples
%{_datadir}/gtk-doc/html/pygobject
%{_datadir}/pygobject/xsl

