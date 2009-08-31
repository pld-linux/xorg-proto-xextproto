Summary:	XExt extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzeń XExt
Name:		xorg-proto-xextproto
# don't update to 7.1.0 unless xserver 1.7 exists
Version:	7.0.5
Release:	2
Epoch:		1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xextproto-%{version}.tar.bz2
# Source0-md5:	e6841018a7c64983b0954aa2c564d115
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XExt extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzeń XExt.

%package devel
Summary:	XExt extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzeń XExt
Group:		X11/Development/Libraries
Requires:	xorg-proto-inputproto-devel
Requires:	xorg-proto-xproto-devel
Obsoletes:	xextensions

%description devel
XExt extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzeń XExt.

%prep
%setup -q -n xextproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog geproto.txt
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xextproto.pc
