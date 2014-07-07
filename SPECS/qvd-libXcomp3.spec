Name:           qvd-libXcomp3
BuildRequires:  gcc-c++ libjpeg-devel libpng-devel openssl-devel xorg-x11-proto-devel
License:        LGPL v2.1 or later; Other uncritical OpenSource License
Url:            http://www.nomachine.com/sources.php
Group:          System/X11/Servers/XF86_4
Version:        3.5.0
Release:        1
Summary:        NX Compression Libraries
Source0:        qvd-nxcomp-3.5.0-patched.tgz
#Patch1:         gcc4-friends.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1230
Requires: libpng15-15
BuildRequires: xorg-x11-util-devel
%endif



%description
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.

Authors:
--------
    Nomachine <www.nomachine.com>

%package devel
Group: Development/Libraries/X11
Summary: NX Compression Static Libraries
Requires: %{name} = %{version}
%description devel
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.
.
This package contains the NX Compression Static Library and Headers.

%prep
%setup -n qvd-nxcomp
cd $RPM_BUILD_DIR
#%patch1

%build
export CFLAGS="%{optflags}" 
export CXXFLAGS="%{optflags}" 
cd $RPM_BUILD_DIR
pushd qvd-nxcomp
autoreconf -fi
./configure
make
strip -v --strip-unneeded libXcomp.so.%{version}
popd

%install
cd $RPM_BUILD_DIR
mkdir -p $RPM_BUILD_ROOT/usr/include/nx
%ifarch i586
  mkdir -p $RPM_BUILD_ROOT/usr/lib
  cp -a qvd-nxcomp/libXcomp.so* $RPM_BUILD_ROOT/usr/lib
  cp -a qvd-nxcomp/libXcomp.a $RPM_BUILD_ROOT/usr/lib
%endif
%ifarch x86_64
  mkdir -p $RPM_BUILD_ROOT/usr/lib64
  cp -a qvd-nxcomp/libXcomp.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a qvd-nxcomp/libXcomp.a $RPM_BUILD_ROOT/usr/lib64
%endif
cp -a qvd-nxcomp/*.h $RPM_BUILD_ROOT/usr/include/nx
rm $RPM_BUILD_ROOT/usr/include/nx/Misc.h
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -m 644 qvd-nxcomp/LICENSE   $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -m 644 qvd-nxcomp/README    $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc /usr/share/doc/packages/%{name}
%ifarch i586
  /usr/lib/libXcomp.so.*
%endif
%ifarch x86_64
  /usr/lib64/libXcomp.so.*
%endif

%files devel
%defattr(-,root,root)
%ifarch i586
  /usr/lib/libXcomp.a
  /usr/lib/libXcomp.so
%endif
%ifarch x86_64
  /usr/lib64/libXcomp.a
  /usr/lib64/libXcomp.so
%endif
%dir /usr/include/nx
/usr/include/nx/*

%changelog
* Tue May 31 2011 cyanez@qindel.com
- Making it OSC compliant

* Mon May 30 2011 cyanez@qindel.com
- Fixed package. Moving /usr/lib/nx to /usr/lib

* Fri May 26 2011 cyanez@qindel.com
- created package

