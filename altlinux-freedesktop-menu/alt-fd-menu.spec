%def_with kde4
Name: altlinux-freedesktop-menu
Version: 0.30
Release: alt1

Summary: Implementation of the freedesktop.org menu specification
License: BSD
Group: Graphical desktop/Other

URL: http://altlinux.org/
Source: %name-%version.tar
Packager: Igor Vlasenko <viy@altlinux.org>

BuildRequires: intltool glib2-devel
BuildArch: noarch

%description
altlinux freedesktop.org menu

%package common
Summary: common files for altlinux freedesktop menus
Group: Graphical desktop/Other
Requires: %name-icon-theme
Requires: wm-common-freedesktop

%description common
%summary

%package nested-menu
Summary: altlinux freedesktop menu with shallow layout
Group: Graphical desktop/Other
Requires: %name-common
Provides: %name

%description nested-menu
freedesktop.org compliant altlinux menu with nested layout

%package shallow-menu
Summary: altlinux freedesktop menu with shallow layout
Group: Graphical desktop/Other
Requires: %name-common
Provides: %name

%description shallow-menu
freedesktop.org compliant altlinux menu with shallow layout

%package gnomish-menu
Summary: altlinux freedesktop menu with shallow layout (GNOME-based)
Group: Graphical desktop/Other
Requires: %name-common
Provides: %name
Requires: gnome-menus-common

%description gnomish-menu
freedesktop.org compliant altlinux menu with shallow layout
that use GNOME desktop directories and looks like GNOME menu.

%package xfce
Summary: xfce freedesktop menu
Group: Graphical desktop/XFce
Provides: xfce-freedesktop-menu
Conflicts: libgarcon-freedesktop-menu
Obsoletes: libgarcon-freedesktop-menu
Requires: %name

%description xfce
ALTLinux freedesktop.org menu for XFCE

%package enlightenment
Summary: Enlightenment freedesktop menu
Group: Graphical desktop/Other
Provides: enlightenment-freedesktop-menu
Requires: %name

%description enlightenment
ALTLinux freedesktop.org menu for Enlightenment DE

%package lxde
Summary: lxde freedesktop menu
Group: Graphical desktop/Other
Provides: lxde-freedesktop-menu
Conflicts: lxde-lxmenu-data
Obsoletes: lxde-lxmenu-data < 0.2
# specifics of lxde menu migration
Requires(pre): %name
Requires: %name

%description lxde
ALTLinux freedesktop.org menu for LXDE

%package gnome
Summary: gnome freedesktop menu
Group: Graphical desktop/GNOME
Provides: gnome-freedesktop-menu
Provides: gnome-menus = 2.90.%version
Conflicts: gnome-menus-default
Obsoletes: gnome-menus-default < 2.90.%version

Requires: %name

%description gnome
ALTLinux freedesktop.org menu for GNOME

%package kde3
Summary: kde3 freedesktop menu
Group: Graphical desktop/KDE
Provides: kde3-freedesktop-menu
Conflicts: kde3-menu-original
Obsoletes: kde3-menu-original
Requires: %name
Requires: kde3-menu-common
Conflicts: kdelibs <= 3.5.12-alt8

%description kde3
ALTLinux freedesktop.org menu for KDE3

%package kde4
Summary: kde4 freedesktop menu
Group: Graphical desktop/KDE
Provides: kde4-freedesktop-menu
Conflicts: kde4-menu-original
Obsoletes: kde4-menu-original
Requires: %name
Requires: %name-generic
#Requires: kde4-menu-common
Conflicts: altlinux-menus
Conflicts: kde4libs <= 4.6.2-alt6
Conflicts: kde4base-runtime-core <= 4.6.2-alt1

%description kde4
ALTLinux freedesktop.org menu for KDE4

%package generic
Summary: generic freedesktop menu
Group: Graphical desktop/Other
Provides: generic-freedesktop-menu
Requires: %name
Conflicts: altlinux-menus
Conflicts: kde4libs <= 4.6.2-alt6
Conflicts: kde4base-runtime-core <= 4.6.2-alt1

%description generic
ALTLinux freedesktop.org menu for a generic freedesktop-compliant DE

%prep
%setup

%build
touch AUTHORS ChangeLog NEWS README
intltoolize
%autoreconf 
%configure 
%make_build

%install
%makeinstall_std
#find_lang %name

mkdir -p %buildroot%_sysconfdir/xdg/menus/{,enlightenment-,gnome-,kde3-,lxde-,xfce-}applications-merged

install -D -m644 layout/kde4-merged.menu %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/50-kde4-merged.menu

# gnomish menu resources
mkdir -p %buildroot%_datadir/desktop-directories %buildroot%_sysconfdir/xdg/menus %buildroot%_altdir
cp -a gnome/desktop-directories %buildroot%_datadir/desktop-directories/gnome

# alternatives
cat <<EOF >>%buildroot%_altdir/%name-nested-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-nested.menu	1000
EOF
cat <<EOF >>%buildroot%_altdir/%name-shallow-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-shallow.menu	100
EOF
cat <<EOF >>%buildroot%_altdir/%name-gnomish-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-shallow-gnomish.menu	80
EOF

%post lxde
# hack around lxde
touch /etc/xdg/menus/lxde-applications.menu

#files 
#-f %name.lang
#doc AUTHORS ChangeLog NEWS README

%files common
%dir %_sysconfdir/xdg/menus/applications-merged
%_datadir/desktop-directories/altlinux-*.directory
%_datadir/desktop-directories/gnome/*.directory
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/altlinux-*.menu

%files nested-menu
%_altdir/%name-nested-menu

%files shallow-menu
%_altdir/%name-shallow-menu

%files gnomish-menu
%_altdir/%name-gnomish-menu

%files xfce
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/xfce-applications.menu
%dir %_sysconfdir/xdg/menus/xfce-applications-merged

%files lxde
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/lxde-applications.menu
%dir %_sysconfdir/xdg/menus/lxde-applications-merged

%files gnome
%config %_sysconfdir/xdg/menus/gnome-applications.menu
%config %_sysconfdir/xdg/menus/settings.menu
%dir %_sysconfdir/xdg/menus/gnome-applications-merged

%files kde3
%config %_sysconfdir/xdg/menus/kde3-applications.menu
%dir %_sysconfdir/xdg/menus/kde3-applications-merged

%files generic
%config %_sysconfdir/xdg/menus/applications.menu

%files enlightenment
%config %_sysconfdir/xdg/menus/enlightenment-applications.menu
%dir %_sysconfdir/xdg/menus/enlightenment-applications-merged

%if_with kde4
%files kde4
%config %_sysconfdir/kde4/xdg/menus/applications-merged/50-kde4-merged.menu
%dir %_sysconfdir/kde4/xdg/menus/applications-merged
%endif

%changelog
* Thu May 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- merge sequence is set according to the menu policy draft

* Tue May 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- enabled KDE4 menu

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- Enlightenment freedesktop menu: does not support MergeDir yet

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- added Enlightenment freedesktop menu

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- added generic freedesktop menu (used by Enlightenment)

* Sun May 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- added KDE4 menu (disabled)

* Sat Apr 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- more pixmaps in layouts

* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- more pixmaps in layouts

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- nested menu: added Dev>Tools, misc layout improvements 

* Tue Apr 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- added KDE3 menu

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- nested menu: added documentation, preparations for KDE

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- added DE-private merge directories
- updated categories

* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- added shallow gnomish menu (thanks to shrek@)
  based on native GNOME desktop directories.

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- GNOME menu: temporarily removed Obsoletes: gnome-menus-default

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added GNOME menu

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- use System Tools for Gnome and System for the rest

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- use System Tools in shallow menu too (thanks to aris@)

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- use System Tools for applications-system (thanks to aris@)

* Thu Mar 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added shortcut .directory files

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- support for GNOME menu

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- Network menu internally uses Internet for RH/Gnome compatibility

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added native LXDE menu.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- optimizations for LXDE and XFCE settings; ShallowSettings.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- sisyphus release

* Fri Mar 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- shallow layout fixes (thanks to sem@)

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- shallow layout fixes (thanks to gns@)

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- Initial build
