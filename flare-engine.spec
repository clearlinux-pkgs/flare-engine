#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flare-engine
Version  : 1.13.04
Release  : 11
URL      : https://github.com/flareteam/flare-engine/archive/v1.13.04/flare-engine-1.13.04.tar.gz
Source0  : https://github.com/flareteam/flare-engine/archive/v1.13.04/flare-engine-1.13.04.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: flare-engine-bin = %{version}-%{release}
Requires: flare-engine-data = %{version}-%{release}
Requires: flare-engine-filemap = %{version}-%{release}
Requires: flare-engine-license = %{version}-%{release}
Requires: flare-engine-man = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : SDL2_image-dev
BuildRequires : SDL2_mixer-dev
BuildRequires : SDL2_ttf-dev
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev

%description
# Flare
Flare (Free Libre Action Roleplaying Engine) is a simple game engine
built to handle a very specific kind of game: single-player 2D action RPGs.
Flare is not a reimplementation of an existing game or engine.
It is a tribute to and exploration of the action RPG genre.

%package bin
Summary: bin components for the flare-engine package.
Group: Binaries
Requires: flare-engine-data = %{version}-%{release}
Requires: flare-engine-license = %{version}-%{release}
Requires: flare-engine-filemap = %{version}-%{release}

%description bin
bin components for the flare-engine package.


%package data
Summary: data components for the flare-engine package.
Group: Data

%description data
data components for the flare-engine package.


%package filemap
Summary: filemap components for the flare-engine package.
Group: Default

%description filemap
filemap components for the flare-engine package.


%package license
Summary: license components for the flare-engine package.
Group: Default

%description license
license components for the flare-engine package.


%package man
Summary: man components for the flare-engine package.
Group: Default

%description man
man components for the flare-engine package.


%prep
%setup -q -n flare-engine-1.13.04
cd %{_builddir}/flare-engine-1.13.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656110311
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%cmake .. -DBINDIR=bin
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DBINDIR=bin
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86_64-v4 -mprefer-vector-width=256 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake .. -DBINDIR=bin
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1656110311
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flare-engine
cp %{_builddir}/flare-engine-1.13.04/COPYING %{buildroot}/usr/share/package-licenses/flare-engine/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/flare-engine-1.13.04/cmake/Copyright.txt %{buildroot}/usr/share/package-licenses/flare-engine/8137c6d95383060d26f828eeea5ff086578c639a
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flare
/usr/share/clear/optimized-elf/bin*

%files data
%defattr(-,root,root,-)
/usr/share/applications/flare.desktop
/usr/share/games/flare/mods/default/cutscenes/credits.txt
/usr/share/games/flare/mods/default/cutscenes/intro.txt
/usr/share/games/flare/mods/default/engine/classes.txt
/usr/share/games/flare/mods/default/engine/combat.txt
/usr/share/games/flare/mods/default/engine/combat_text.txt
/usr/share/games/flare/mods/default/engine/damage_types.txt
/usr/share/games/flare/mods/default/engine/death_penalty.txt
/usr/share/games/flare/mods/default/engine/default_music.txt
/usr/share/games/flare/mods/default/engine/elements.txt
/usr/share/games/flare/mods/default/engine/equip_flags.txt
/usr/share/games/flare/mods/default/engine/font_colors.txt
/usr/share/games/flare/mods/default/engine/font_settings.txt
/usr/share/games/flare/mods/default/engine/gameplay.txt
/usr/share/games/flare/mods/default/engine/icons.txt
/usr/share/games/flare/mods/default/engine/languages.txt
/usr/share/games/flare/mods/default/engine/misc.txt
/usr/share/games/flare/mods/default/engine/primary_stats.txt
/usr/share/games/flare/mods/default/engine/resolutions.txt
/usr/share/games/flare/mods/default/engine/tileset_config.txt
/usr/share/games/flare/mods/default/engine/tooltips.txt
/usr/share/games/flare/mods/default/fonts/LiberationSans-Regular.ttf
/usr/share/games/flare/mods/default/fonts/unifont-10.0.06.ttf
/usr/share/games/flare/mods/default/images/credits/flare_default.png
/usr/share/games/flare/mods/default/images/credits/oga.png
/usr/share/games/flare/mods/default/images/credits/tiled.png
/usr/share/games/flare/mods/default/images/icons/icons.png
/usr/share/games/flare/mods/default/images/logo/icon.png
/usr/share/games/flare/mods/default/images/menus/buttons/button_default.png
/usr/share/games/flare/mods/default/images/menus/buttons/button_x.png
/usr/share/games/flare/mods/default/images/menus/buttons/checkbox_default.png
/usr/share/games/flare/mods/default/images/menus/buttons/down.png
/usr/share/games/flare/mods/default/images/menus/buttons/left.png
/usr/share/games/flare/mods/default/images/menus/buttons/listbox_default.png
/usr/share/games/flare/mods/default/images/menus/buttons/right.png
/usr/share/games/flare/mods/default/images/menus/buttons/scrollbar_default.png
/usr/share/games/flare/mods/default/images/menus/buttons/slider_default.png
/usr/share/games/flare/mods/default/images/menus/buttons/up.png
/usr/share/games/flare/mods/default/images/menus/compass_iso.png
/usr/share/games/flare/mods/default/images/menus/compass_ortho.png
/usr/share/games/flare/mods/default/images/menus/config.png
/usr/share/games/flare/mods/default/images/menus/confirm_bg.png
/usr/share/games/flare/mods/default/images/menus/dev_console.png
/usr/share/games/flare/mods/default/images/menus/entity_hidden.png
/usr/share/games/flare/mods/default/images/menus/logo.png
/usr/share/games/flare/mods/default/images/menus/movement_type.png
/usr/share/games/flare/mods/default/images/menus/movement_type_joystick.png
/usr/share/games/flare/mods/default/images/menus/movement_type_keyboard.png
/usr/share/games/flare/mods/default/images/menus/movement_type_mouse.png
/usr/share/games/flare/mods/default/images/menus/tab_active.png
/usr/share/games/flare/mods/default/images/menus/tab_inactive.png
/usr/share/games/flare/mods/default/languages/data.be.po
/usr/share/games/flare/mods/default/languages/data.bg.po
/usr/share/games/flare/mods/default/languages/data.ca.po
/usr/share/games/flare/mods/default/languages/data.cs.po
/usr/share/games/flare/mods/default/languages/data.de.po
/usr/share/games/flare/mods/default/languages/data.el.po
/usr/share/games/flare/mods/default/languages/data.es.po
/usr/share/games/flare/mods/default/languages/data.eu.po
/usr/share/games/flare/mods/default/languages/data.fi.po
/usr/share/games/flare/mods/default/languages/data.fr.po
/usr/share/games/flare/mods/default/languages/data.gd.po
/usr/share/games/flare/mods/default/languages/data.gl.po
/usr/share/games/flare/mods/default/languages/data.hu.po
/usr/share/games/flare/mods/default/languages/data.id.po
/usr/share/games/flare/mods/default/languages/data.it.po
/usr/share/games/flare/mods/default/languages/data.ja.po
/usr/share/games/flare/mods/default/languages/data.ko.po
/usr/share/games/flare/mods/default/languages/data.nb.po
/usr/share/games/flare/mods/default/languages/data.nl.po
/usr/share/games/flare/mods/default/languages/data.pl.po
/usr/share/games/flare/mods/default/languages/data.pot
/usr/share/games/flare/mods/default/languages/data.pt.po
/usr/share/games/flare/mods/default/languages/data.pt_BR.po
/usr/share/games/flare/mods/default/languages/data.ru.po
/usr/share/games/flare/mods/default/languages/data.sk.po
/usr/share/games/flare/mods/default/languages/data.sv.po
/usr/share/games/flare/mods/default/languages/data.uk.po
/usr/share/games/flare/mods/default/languages/data.vi.po
/usr/share/games/flare/mods/default/languages/data.zh.po
/usr/share/games/flare/mods/default/languages/data.zh_TW.po
/usr/share/games/flare/mods/default/languages/engine.be.po
/usr/share/games/flare/mods/default/languages/engine.bg.po
/usr/share/games/flare/mods/default/languages/engine.ca.po
/usr/share/games/flare/mods/default/languages/engine.cs.po
/usr/share/games/flare/mods/default/languages/engine.de.po
/usr/share/games/flare/mods/default/languages/engine.el.po
/usr/share/games/flare/mods/default/languages/engine.es.po
/usr/share/games/flare/mods/default/languages/engine.eu.po
/usr/share/games/flare/mods/default/languages/engine.fi.po
/usr/share/games/flare/mods/default/languages/engine.fr.po
/usr/share/games/flare/mods/default/languages/engine.gd.po
/usr/share/games/flare/mods/default/languages/engine.gl.po
/usr/share/games/flare/mods/default/languages/engine.hu.po
/usr/share/games/flare/mods/default/languages/engine.id.po
/usr/share/games/flare/mods/default/languages/engine.it.po
/usr/share/games/flare/mods/default/languages/engine.ja.po
/usr/share/games/flare/mods/default/languages/engine.ko.po
/usr/share/games/flare/mods/default/languages/engine.nb.po
/usr/share/games/flare/mods/default/languages/engine.nl.po
/usr/share/games/flare/mods/default/languages/engine.pl.po
/usr/share/games/flare/mods/default/languages/engine.pot
/usr/share/games/flare/mods/default/languages/engine.pt.po
/usr/share/games/flare/mods/default/languages/engine.pt_BR.po
/usr/share/games/flare/mods/default/languages/engine.ru.po
/usr/share/games/flare/mods/default/languages/engine.sk.po
/usr/share/games/flare/mods/default/languages/engine.sv.po
/usr/share/games/flare/mods/default/languages/engine.uk.po
/usr/share/games/flare/mods/default/languages/engine.vi.po
/usr/share/games/flare/mods/default/languages/engine.zh.po
/usr/share/games/flare/mods/default/languages/engine.zh_TW.po
/usr/share/games/flare/mods/default/menus/config.txt
/usr/share/games/flare/mods/default/menus/confirm.txt
/usr/share/games/flare/mods/default/menus/devconsole.txt
/usr/share/games/flare/mods/default/menus/fps.txt
/usr/share/games/flare/mods/default/menus/gameload.txt
/usr/share/games/flare/mods/default/menus/gamenew.txt
/usr/share/games/flare/mods/default/menus/gametitle.txt
/usr/share/games/flare/mods/default/menus/movement_type.txt
/usr/share/games/flare/mods/gcw0_defaults/engine/default_keybindings.txt
/usr/share/games/flare/mods/gcw0_defaults/engine/default_settings.txt
/usr/share/games/flare/mods/gcw0_defaults/settings.txt
/usr/share/games/flare/mods/mods.txt
/usr/share/icons/hicolor/scalable/apps/flare.svg

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-flare-engine

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flare-engine/8137c6d95383060d26f828eeea5ff086578c639a
/usr/share/package-licenses/flare-engine/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man6/flare.6
