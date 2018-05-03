Name: pygobject2
Version: 3.24.1
Release: 1
License: LGPLv2+
Group: Development/Languages
Summary: Python 2 bindings for GObject 
URL: https://git.gnome.org/browse/pygobject
Source: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(python2)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(pycairo) >= 1.11.1
BuildRequires: gnome-common

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package devel
Summary: Development files for building add-on libraries
Group: Development/Languages
Requires: %{name} = %{version}-%{release}
Requires: %{name}-codegen = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: glib2-devel
Requires: python2-devel

%description devel
This package contains files required to build wrappers for %{name}-based
libraries such as pygtk2.

%prep
%setup -q -n %{name}-%{version}/upstream
find -name '*.py' -print0 | xargs -n1 -0 sed -i '1s|^#!python|#!%{__python}|'

%build
PYTHON=%{__python} 
export PYTHON
%autogen
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -delete
find $RPM_BUILD_ROOT -name '*.a' -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%{python_sitearch}/gi
%{python_sitearch}/pygtkcompat
%{python_sitearch}/pygobject*

%files devel
%defattr(644, root, root, 755)
%dir %{_includedir}/pygobject-3.0
%{_includedir}/pygobject-3.0
%{_libdir}/pkgconfig/pygobject-3.0.pc
