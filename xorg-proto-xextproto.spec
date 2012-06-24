Summary:	XExt extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzeń XExt
Name:		xorg-proto-xextproto
Version:	7.1.1
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xextproto-%{version}.tar.bz2
# Source0-md5:	fb6ccaae76db7a35e49b12aea60ca6ff
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XExt extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzeń XExt.

%package devel
Summary:	XExt extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzeń XExt
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Suggests:	xorg-lib-libXext-devel >= 1:1.1
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
