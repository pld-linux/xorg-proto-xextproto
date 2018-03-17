# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	XExt extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzeń XExt
Name:		xorg-proto-xextproto
Version:	7.3.0
Release:	2.1
Epoch:		1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/xextproto-%{version}.tar.bz2
# Source0-md5:	70c90f313b4b0851758ef77b95019584
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Header files for X protocol extensions, covering:
- DOUBLE-BUFFER
- DPMS
- Extended-Visual-Information
- Generic Event Extension
- LBX
- MIT-SHM
- MIT-SUNDRY-NONSTANDARD
- Multi-Buffering
- SECURITY
- SHAPE
- SYNC
- TOG-CUP
- XC-APPGROUP
- XTEST

%description -l pl.UTF-8
Pliki nagłówkowe rozszerzeń protokołu X, obejmujące:
- DOUBLE-BUFFER
- DPMS
- Extended-Visual-Information
- Generic Event Extension
- LBX
- MIT-SHM
- MIT-SUNDRY-NONSTANDARD
- Multi-Buffering
- SECURITY
- SHAPE
- SYNC
- TOG-CUP
- XC-APPGROUP
- XTEST

%package devel
Summary:	XExt extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzeń XExt
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Suggests:	xorg-lib-libXext-devel >= 1:1.1
Obsoletes:	xextensions

%description devel
Header files for X protocol extensions, covering:
- DOUBLE-BUFFER
- DPMS
- Extended-Visual-Information
- Generic Event Extension
- LBX
- MIT-SHM
- MIT-SUNDRY-NONSTANDARD
- Multi-Buffering
- SECURITY
- SHAPE
- SYNC
- TOG-CUP
- XC-APPGROUP
- XTEST

%description devel -l pl.UTF-8
Pliki nagłówkowe rozszerzeń protokołu X, obejmujące:
- DOUBLE-BUFFER
- DPMS
- Extended-Visual-Information
- Generic Event Extension
- LBX
- MIT-SHM
- MIT-SUNDRY-NONSTANDARD
- Multi-Buffering
- SECURITY
- SHAPE
- SYNC
- TOG-CUP
- XC-APPGROUP
- XTEST

%prep
%setup -q -n xextproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--without-fop

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/xextproto

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README specs/*.html
%{_includedir}/X11/extensions/EVI*.h
%{_includedir}/X11/extensions/ag*.h
%{_includedir}/X11/extensions/cup*.h
%{_includedir}/X11/extensions/dbe*.h
%{_includedir}/X11/extensions/dpms*.h
%{_includedir}/X11/extensions/ge*.h
%{_includedir}/X11/extensions/lbx*.h
%{_includedir}/X11/extensions/mitmisc*.h
%{_includedir}/X11/extensions/multibuf*.h
%{_includedir}/X11/extensions/secur*.h
%{_includedir}/X11/extensions/shape*.h
%{_includedir}/X11/extensions/shm*.h
%{_includedir}/X11/extensions/sync*.h
%{_includedir}/X11/extensions/xtest*.h
%{_pkgconfigdir}/xextproto.pc
