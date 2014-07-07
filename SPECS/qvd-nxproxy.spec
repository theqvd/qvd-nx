Name:           qvd-nxproxy
%if 0%{?suse_version}
BuildRequires:  gcc-c++ libjpeg-devel libpng-devel openssl-devel xorg-x11-proto-devel xorg-x11-util-devel qvd-libXcomp3-devel
%else
BuildRequires:  gcc-c++ libjpeg-devel libpng-devel openssl-devel xorg-x11-proto-devel qvd-libXcomp3-devel
%endif
License:        LGPL v2.1 or later; Other uncritical OpenSource License
Url:            http://www.nomachine.com/sources.php
Group:          System/X11/Servers/XF86_4
Version:        3.5.0
Release:        1
Summary:        NX Proxy
Source0:        qvd-nxproxy-3.5.0-patched.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NX provides a proxy system for the X Window System.

Authors:
--------
    Nomachine <www.nomachine.com>

%prep
%setup -n qvd-nxproxy
cd $RPM_BUILD_DIR/qvd-nxproxy
#%patch -p1

%build
export CFLAGS="%{optflags}" 
export CXXFLAGS="%{optflags}" 
export CXXINCLUDES="-I. -I/usr/include/nx -I/usr/include/X11 -I/usr/include/xorg -I/usr/include/pixman-1"
export CCINCLUDES="-I. -I/usr/include/nx -I/usr/include/X11 -I/usr/include/xorg -I/usr/include/pixman-1"
cd $RPM_BUILD_DIR/qvd-nxproxy
autoreconf -fi
./configure
make
strip -v --strip-unneeded nxproxy

%install
cd $RPM_BUILD_DIR/qvd-nxproxy
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -m0755 nxproxy $RPM_BUILD_ROOT/usr/bin
install -m 644 {COPYING,LICENSE,README,VERSION} $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc /usr/share/doc/packages/%{name}
/usr/bin/nxproxy

%changelog
* Tue Jun 7 2011 cyanez@qindel.com
- Initial package.

