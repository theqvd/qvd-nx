Name:           qvd-nx-x11
#BuildRequires:  gcc-c++ bzip2 libjpeg-devel libpng-devel libopenssl-devel zlib-devel alsa-devel audiofile-devel libXcomp3-devel libXcompshad3-devel xorg-x11-libX11-devel xorg-x11-server-sdk freetype2-devel xorg-x11-libXpm-devel xorg-x11-devel xorg-x11-libXext-devel libXcompext3-devel

%if 0%{?suse_version}
BuildRequires:  gcc-c++ bzip2 libjpeg-devel libpng-devel libopenssl-devel zlib-devel alsa-devel audiofile-devel qvd-libXcomp3-devel xorg-x11-libX11-devel xorg-x11-server-sdk freetype2-devel xorg-x11-libXpm-devel xorg-x11-devel xorg-x11-libXext-devel
%else
BuildRequires:  gcc-c++ bzip2  libjpeg-devel libpng-devel openssl-devel zlib-devel alsa-lib-devel qvd-libXcomp3-devel libX11-devel freetype-devel libXpm-devel libX11-devel libXext-devel
%endif
License:        LGPL v2.1 or later; Other uncritical OpenSource License
Url:            http://www.nomachine.com/sources.php
Group:          System/X11/Servers/XF86_4
Version:        3.5.0
Release:        1
Summary:        Proxy System for X11
Source0:	qvd-nxagent-3.5.0-patched.tgz
#Source1:	nxagent.keyboard
#Source2:	rgb
#Source3:	nxagent.1
#Patch0:         01_build_nx-X11_without_nxcomp.dpatch
#Patch2:         03_dont_compile_nxauth.dpatch
#Patch3:         85_nx-X11_debian-ld.dpatch
#Patch4:         86_set_rgb_path.dpatch
#Patch5:         87_set_securitypolicy_path.dpatch
#Patch6:         90_set_X0-config_path.dpatch
#Patch7:         93_export_remote_keyboard_config.dpatch
#Patch8:         95_fix_Imakefile.dpatch
#Patch9:         98_font_path.dpatch
#Patch10:	99_nxagent_logo.dpatch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NX provides a proxy system for the X Window System.



Authors:
--------
    Nomachine <www.nomachine.com>


%package -n qvd-nxlibs3
Summary: NX Support Libraries
Group: System/X11/Servers/XF86_4
%description -n qvd-nxlibs3
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.
.
This package contains the libraries needed by NX agent

%package -n qvd-nxlibs3-devel
Summary: NX Support Libraries Development Files
Group: Development/Libraries/X11
Requires: nxlibs3 = %{version}
%description -n qvd-nxlibs3-devel
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.
.
This package contains the static libraries and headers for the NX Library.

%package -n qvd-nxagent
Summary: X Server for remote access
Group: System/X11/Servers/XF86_4
%if 0%{?suse_version} >= 1230
Requires: xorg-x11-fonts-core
%endif
%description -n qvd-nxagent
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.
.
This package contains the NX agent

%package -n qvd-nxagent-devel
Summary: X Server for remote access Development Files
Group: Development/Libraries/X11
Requires: nxagent = %{version}
Requires: qvd-libXcompshad3
%description -n qvd-nxagent-devel
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.
.
This package contains the static libraries and headers for NX Agent.


%package -n qvd-libXcompext3
Summary: NX Extended Compression Libraries
Group:          System/X11/Servers/XF86_4

%if 0%{?suse_version} > 1230
Requires: libpng15-15
%else
Requires: libpng14-14
%endif

%description -n qvd-libXcompext3
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.

Authors:
--------
    Nomachine <www.nomachine.com>

%package -n qvd-libXcompext3-devel
Summary: NX Extended Compression Static Libraries
Group: Development/Libraries/X11
Requires: %{name} = %{version}
%description -n qvd-libXcompext3-devel
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.
.
This package contains the NX Extended Compression Static Library and Headers.

%package -n qvd-libXcompshad3
Summary:        NX Shadow Libraries
Group:          System/X11/Servers/XF86_4
Version:        3.5.0
%description -n qvd-libXcompshad3
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.

Authors:
--------
    Nomachine <www.nomachine.com>

%package -n qvd-libXcompshad3-devel
Summary: NX Shadow Static Libraries
Group: Development/Libraries/X11 
Version: 3.5.0
Requires: %{name} = %{version}
%description -n qvd-libXcompshad3-devel
NX is a X server for remote access. It implements a very efficient
compression of the X11 protocol. This increases performance when
using X applications over a network, providing a near local experience.
.
This package contains the NX Shadow Static Library and Headers.



%prep
%setup -n qvd-nxagent -b 0
cd $RPM_BUILD_DIR/
#%patch -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
#%patch8 -p1
#%patch9 -p1
#%patch10 -p2

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export CXXINCLUDES="-I. -I/usr/include/nx -I/usr/include/X11 -I/usr/include/xorg -I/usr/include/pixman-1"
export CCINCLUDES="-I. -I/usr/include/nx -I/usr/include/X11 -I/usr/include/xorg -I/usr/include/pixman-1"

cat >> qvd-nxagent/nx-X11/config/cf/host.def << EOF
/* #define ExtraLoadFlags ${LDFLAGS}
#define SharedLibraryLoadFlags -shared ${LDFLAGS} */
#define StandardIncludes ${CCINCLUDES}
#ifdef  i386Architecture
#undef  DefaultGcc2i386Opt
#define DefaultGcc2i386Opt      $RPM_OPT_FLAGS GccAliasingArgs
#endif
#ifdef  MipsArchitecture
#undef  DefaultGcc2MipsOpt
#define DefaultGcc2MipsOpt      $RPM_OPT_FLAGS GccAliasingArgs
#endif
#ifdef s390xArchitecture
#undef OptimizedCDebugFlags
#define OptimizedCDebugFlags	$RPM_OPT_FLAGS GccAliasingArgs
#endif
#define HasZlib	YES
#/* X.Org 7 changes */
#define XLocaleDir /usr/share/X11/locale
#define DefaultRGBDatabase /usr/share/X11/rgb
#define ServerConfigDir /usr/%{_lib}/xserver
#define BuildLoadableXlibI18n NO
REQUIREDI18NLIBS = DlLibrary
EOF

%build
cd $RPM_BUILD_DIR
pwd
cd qvd-nxagent
rm -rf nx-X11/programs/Xserver/hw/nxagent
[ ! -d nx-X11/programs/Xserver/hw/nxagent ] && \
		echo "Injecting NXAgent into tree" && \
		cp -r programs/Xserver/hw/nxagent nx-X11/programs/Xserver/hw/
cd nxcomp     && autoreconf -fi && cd .. 
cd nxcompext  && autoreconf -fi && cd ..
cd nxcompshad && autoreconf -fi && cd .. 
cd nx-X11
make World
strip -v --strip-unneeded programs/Xserver/nxagent
mv lib/X11/libNX_X11.so.6.2               lib/X11/libX11-nx.so.6.2
mv lib/Xext/libNX_Xext.so.6.4             lib/Xext/libXext-nx.so.6.4
mv lib/Xrender/libNX_Xrender.so.1.2.2     lib/Xrender/libXrender-nx.so.1.2.2
mv lib/Xdamage/libNX_Xdamage.so.1.0       lib/Xdamage/libXdamage-nx.so.1.0
mv lib/Xrandr/libNX_Xrandr.so.2.0         lib/Xrandr/libXrandr-nx.so.2.0
mv lib/Xtst/libNX_Xtst.so.6.1             lib/Xtst/libXtst-nx.so.6.1
mv lib/Xcomposite/libNX_Xcomposite.so.1.0 lib/Xcomposite/libXcomposite-nx.so.1.0
mv lib/Xfixes/libNX_Xfixes.so.3.0         lib/Xfixes/libXfixes-nx.so.3.0
ln -s libX11-nx.so.6.2        lib/X11/libX11-nx.so
ln -s libXext-nx.so.6.4       lib/Xext/libXext-nx.so
ln -s libXrender-nx.so.1.2.2  lib/Xrender/libXrender-nx.so
ln -s libXdamage-nx.so.1.0    lib/Xdamage/libXdamage-nx.so
ln -s libXrandr-nx.so.2.0     lib/Xrandr/libXrandr-nx.so
ln -s libXtst-nx.so.6.1       lib/Xtst/libXtst-nx.so
ln -s libXcomposite-nx.so.1.0 lib/Xcomposite/libXcomposite-nx.so
ln -s libXfixes-nx.so.3.0     lib/Xfixes/libXfixes-nx.so
strip -v --strip-unneeded lib/X11/libX11-nx.so.6.2
strip -v --strip-unneeded lib/Xext/libXext-nx.so.6.4
strip -v --strip-unneeded lib/Xrender/libXrender-nx.so.1.2.2

%install

cd $RPM_BUILD_DIR/qvd-nxagent
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/include/nx
mkdir -p $RPM_BUILD_ROOT/etc/nxagent
mkdir -p $RPM_BUILD_ROOT/usr/share/nxagent
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps

%ifarch i586
  mkdir -p $RPM_BUILD_ROOT/usr/lib
  cp -a nx-X11/lib/X11/libX11-nx.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nx-X11/lib/Xext/libXext-nx.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nx-X11/lib/Xrender/libXrender-nx.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nx-X11/lib/Xdamage/libXdamage-nx.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nx-X11/lib/Xrandr/libXrandr-nx.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nx-X11/lib/Xtst/libXtst-nx.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nx-X11/lib/Xcomposite/libXcomposite-nx.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nx-X11/lib/Xfixes/libXfixes-nx.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nxcompext/libXcompext.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nxcompext/libXcompext.a $RPM_BUILD_ROOT/usr/lib
  cp -a nxcompshad/libXcompshad.so* $RPM_BUILD_ROOT/usr/lib
  cp -a nxcompshad/libXcompshad.a $RPM_BUILD_ROOT/usr/lib
%endif
%ifarch x86_64
  mkdir -p $RPM_BUILD_ROOT/usr/lib64
  cp -a nx-X11/lib/X11/libX11-nx.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nx-X11/lib/Xext/libXext-nx.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nx-X11/lib/Xrender/libXrender-nx.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nx-X11/lib/Xdamage/libXdamage-nx.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nx-X11/lib/Xrandr/libXrandr-nx.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nx-X11/lib/Xtst/libXtst-nx.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nx-X11/lib/Xcomposite/libXcomposite-nx.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nx-X11/lib/Xfixes/libXfixes-nx.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nxcompext/libXcompext.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nxcompext/libXcompext.a $RPM_BUILD_ROOT/usr/lib64
  cp -a nxcompshad/libXcompshad.so* $RPM_BUILD_ROOT/usr/lib64
  cp -a nxcompshad/libXcompshad.a $RPM_BUILD_ROOT/usr/lib64
%endif
cp -a nx-X11/programs/Xserver/include/dix.h $RPM_BUILD_ROOT/usr/include/nx
cp -a nx-X11/programs/Xserver/hw/nxagent/qvd.xpm $RPM_BUILD_ROOT/usr/share/pixmaps
cp -RL nx-X11/exports/include/* $RPM_BUILD_ROOT/usr/include/nx
install -m0755 nx-X11/programs/Xserver/nxagent $RPM_BUILD_ROOT/usr/bin
cp -a $RPM_SOURCE_DIR/nxagent.keyboard $RPM_BUILD_ROOT/etc/nxagent
cp -a $RPM_SOURCE_DIR/rgb $RPM_BUILD_ROOT/usr/share/nxagent
cp -a nx-X11/programs/Xserver/Xext/SecurityPolicy $RPM_BUILD_ROOT/usr/share/nxagent
cp -a $RPM_SOURCE_DIR/nxagent.1 $RPM_BUILD_ROOT/usr/share/man/man1
cp -a nx-X11/programs/Xserver/hw/nxagent/*.h $RPM_BUILD_ROOT/usr/include/nx
cp -a nxcompext/*.h $RPM_BUILD_ROOT/usr/include/nx
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/qvd-nxcompext
install -m 644 nxcompext/LICENSE   $RPM_BUILD_ROOT/usr/share/doc/packages/qvd-nxcompext
install -m 644 nxcompext/README    $RPM_BUILD_ROOT/usr/share/doc/packages/qvd-nxcompext
cp -a nxcompshad/*.h $RPM_BUILD_ROOT/usr/include/nx
rm -f RPM_BUILD_ROOT/usr/include/nx/Misc.h
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/qvd-nxcompshad
install -m 644 nxcompshad/LICENSE   $RPM_BUILD_ROOT/usr/share/doc/packages/qvd-nxcompshad

#popd

%clean
rm -rf %{buildroot}

%post -n qvd-libXcompshad3
/sbin/ldconfig

%postun -n qvd-libXcompshad3
/sbin/ldconfig

%post -n qvd-libXcompext3
/sbin/ldconfig

%postun -n qvd-libXcompext3
/sbin/ldconfig

%post -n qvd-nxlibs3
/sbin/ldconfig

%postun -n qvd-nxlibs3
/sbin/ldconfig

%files -n qvd-nxlibs3
%defattr(-,root,root)
%ifarch i586
/usr/lib/libX11-nx.so.*
/usr/lib/libXext-nx.so.*
/usr/lib/libXrender-nx.so.*
/usr/lib/libXdamage-nx.so.*
/usr/lib/libXrandr-nx.so.*
/usr/lib/libXtst-nx.so.*
/usr/lib/libXcomposite-nx.so.*
/usr/lib/libXfixes-nx.so.*
%endif
%ifarch x86_64
/usr/lib64/libX11-nx.so.*
/usr/lib64/libXext-nx.so.*
/usr/lib64/libXrender-nx.so.*
/usr/lib64/libXdamage-nx.so.*
/usr/lib64/libXrandr-nx.so.*
/usr/lib64/libXtst-nx.so.*
/usr/lib64/libXcomposite-nx.so.*
/usr/lib64/libXfixes-nx.so.*
%endif

%files -n qvd-nxlibs3-devel
%defattr(-,root,root)
/usr/include/nx/dix.h
## dserrano 20140521: commenting these out
#/usr/include/nx/expat.h
#/usr/include/nx/ft2build.h
%dir /usr/include/nx/GL/
/usr/include/nx/GL/*
## dserrano 20140521: commenting these out
#%dir /usr/include/nx/freetype2/
#/usr/include/nx/freetype2/*
#%dir /usr/include/nx/fontconfig/
#/usr/include/nx/fontconfig/*
%dir /usr/include/nx/X11/
/usr/include/nx/X11/*
%ifarch i586
/usr/lib/libX11-nx.so
/usr/lib/libXext-nx.so
/usr/lib/libXrender-nx.so
/usr/lib/libXdamage-nx.so
/usr/lib/libXrandr-nx.so
/usr/lib/libXtst-nx.so
/usr/lib/libXcomposite-nx.so
/usr/lib/libXfixes-nx.so
%endif
%ifarch x86_64
/usr/lib64/libX11-nx.so
/usr/lib64/libXext-nx.so
/usr/lib64/libXrender-nx.so
/usr/lib64/libXdamage-nx.so
/usr/lib64/libXrandr-nx.so
/usr/lib64/libXtst-nx.so
/usr/lib64/libXcomposite-nx.so
/usr/lib64/libXfixes-nx.so
%endif

%files -n qvd-nxagent
%defattr(-,root,root)
/usr/share/man/man1/nxagent.1*
/usr/share/pixmaps/qvd.xpm
%dir /usr/share/nxagent/
/usr/share/nxagent/*
/usr/bin/nxagent
%dir /etc/nxagent/
%config /etc/nxagent/nxagent.keyboard

%files -n qvd-nxagent-devel
%defattr(-,root,root)
%dir /usr/include/nx
/usr/include/nx/NXxrandr.h
/usr/include/nx/Binder.h
/usr/include/nx/GCs.h
/usr/include/nx/Reconnect.h
/usr/include/nx/Trap.h
/usr/include/nx/Error.h
/usr/include/nx/Keystroke.h
/usr/include/nx/Dialog.h
/usr/include/nx/Cursor.h
/usr/include/nx/Utils.h
/usr/include/nx/Options.h
/usr/include/nx/Image.h
/usr/include/nx/Colormap.h
/usr/include/nx/NXcompositeext.h
/usr/include/nx/Drawable.h
/usr/include/nx/Holder.h
/usr/include/nx/NXcompositeint.h
/usr/include/nx/NXglyphstr.h
/usr/include/nx/Events.h
/usr/include/nx/Handlers.h
/usr/include/nx/Millis.h
/usr/include/nx/Pixmaps.h
/usr/include/nx/Icons.h
/usr/include/nx/Pixels.h
/usr/include/nx/Screen.h
/usr/include/nx/NXxrandrint.h
/usr/include/nx/Font.h
/usr/include/nx/Keyboard.h
/usr/include/nx/Client.h
/usr/include/nx/GCOps.h
/usr/include/nx/Init.h
/usr/include/nx/Visual.h
/usr/include/nx/NXpicturestr.h
/usr/include/nx/Literals.h
/usr/include/nx/Split.h
/usr/include/nx/Atoms.h
/usr/include/nx/Splash.h
/usr/include/nx/NXcompositeproto.h
/usr/include/nx/Extensions.h
/usr/include/nx/Render.h
/usr/include/nx/Clipboard.h
/usr/include/nx/Composite.h
/usr/include/nx/Windows.h
/usr/include/nx/Display.h
/usr/include/nx/NXcomposite.h
/usr/include/nx/Args.h
/usr/include/nx/Agent.h
/usr/include/nx/Rootless.h
/usr/include/nx/Pointer.h
## dserrano 20140521: adding this
/usr/include/nx/NXlocalevents.h

%files -n qvd-libXcompext3
%defattr(-,root,root)
%doc /usr/share/doc/packages/qvd-nxcompext
%ifarch i586
  /usr/lib/libXcompext.so.*
%endif
%ifarch x86_64
  /usr/lib64/libXcompext.so.*
%endif

%files -n qvd-libXcompext3-devel
%defattr(-,root,root)
%ifarch i586
  /usr/lib/libXcompext.so
  /usr/lib/libXcompext.a
%endif
%ifarch x86_64
  /usr/lib64/libXcompext.so
  /usr/lib64/libXcompext.a
%endif
%dir /usr/include/nx/
/usr/include/nx/Alpha.h
/usr/include/nx/Bitmap.h
/usr/include/nx/Clean.h
/usr/include/nx/Colormap.h
/usr/include/nx/Jpeg.h
/usr/include/nx/Mask.h
/usr/include/nx/NXlib.h
/usr/include/nx/NXlibint.h
/usr/include/nx/Pgn.h
/usr/include/nx/Rgb.h
/usr/include/nx/Rle.h
/usr/include/nx/Z.h


%files -n qvd-libXcompshad3
%defattr(-,root,root)
%doc /usr/share/doc/packages/qvd-nxcompshad
%ifarch i586
  /usr/lib/libXcompshad.so.*
%endif
%ifarch x86_64
  /usr/lib64/libXcompshad.so.*
%endif

%files -n qvd-libXcompshad3-devel
%defattr(-,root,root)
%ifarch i586
  /usr/lib/libXcompshad.so
  /usr/lib/libXcompshad.a
%endif
%ifarch x86_64
  /usr/lib64/libXcompshad.so
  /usr/lib64/libXcompshad.a
%endif
%dir /usr/include/nx
/usr/include/nx/Core.h
/usr/include/nx/Input.h
/usr/include/nx/Misc.h
/usr/include/nx/Logger.h
/usr/include/nx/Manager.h
/usr/include/nx/Poller.h
/usr/include/nx/Regions.h
/usr/include/nx/Shadow.h
/usr/include/nx/Updater.h
/usr/include/nx/Win.h
/usr/include/nx/X11.h




%changelog
* Tue Mar 06 2012 vtroshchinskiy@qindel.com
- Fix font path for SuSE

* Mon May 30 2011 cyanez@qindel.com
- Moved from /usr/lib/nx to /usr/lib

* Fri May 27 2011 cyanez@qindel.com
- created package

