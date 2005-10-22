Summary:	XExt protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XExt i pomocnicze
Name:		xorg-proto-xextproto
Version:	7.0.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/xextproto-%{version}.tar.bz2
# Source0-md5:	2ad511ee64710d58497f294fa3035423
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XExt protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u XExt i pomocnicze.

%package devel
Summary:	XExt protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u XExt i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-inputproto-devel
Requires:	xorg-proto-xproto-devel
Obsoletes:	xextensions

%description devel
XExt protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u XExt i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xextproto.pc
