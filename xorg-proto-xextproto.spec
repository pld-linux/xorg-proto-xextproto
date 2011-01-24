Summary:	XExt extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzeń XExt
Name:		xorg-proto-xextproto
Version:	7.1.2
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/xextproto-%{version}.tar.bz2
# Source0-md5:	263ae968b223c23b2986603d84e5c30e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.20
BuildRequires:	xorg-sgml-doctools >= 1.5
BuildRequires:	xorg-util-util-macros >= 1.10
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
%doc COPYING ChangeLog README specs/*.html
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xextproto.pc
