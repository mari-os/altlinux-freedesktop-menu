Name: altlinux-freedesktop-menu
Version: 0.17
Release: alt1

Summary: Implementation of the freedesktop.org menu specification
License: BSD
Group: Graphical desktop/Other

URL: http://altlinux.org/
Source: %name-%version.tar
Packager: Igor Vlasenko <viy@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: intltool glib2-devel
BuildArch: noarch

%description
altlinux freedesktop.org menu

%package common
Summary: common files for altlinux freedesktop menus
Group: Graphical desktop/Other
Requires: %name-icon-theme-default > 0.0.9

%description common
%summary

%package shallow-menu
Summary: altlinux freedesktop menu with shallow layout
Group: Graphical desktop/Other
Requires: %name-common
Provides: %name

%description shallow-menu
freedesktop.org compliant altlinux menu with shallow layout

%package nested-menu
Summary: altlinux freedesktop menu with shallow layout
Group: Graphical desktop/Other
Requires: %name-common
Provides: %name

%description nested-menu
freedesktop.org compliant altlinux menu with nested layout

%package xfce
Summary: xfce freedesktop menu
Group: Graphical desktop/XFce
Provides: xfce-freedesktop-menu
Conflicts: libgarcon-freedesktop-menu
Obsoletes: libgarcon-freedesktop-menu
Requires: %name

%description xfce
ALTLinux freedesktop.org menu for XFCE


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
#Obsoletes: gnome-menus-default < 2.90.%version

Requires: %name

%description gnome
ALTLinux freedesktop.org menu for GNOME



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

mkdir -p %buildroot%_datadir/desktop-directories %buildroot%_sysconfdir/xdg/menus %buildroot%_altdir

%__cat <<EOF >>%buildroot%_altdir/%name-nested-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-nested.menu	1000
EOF
%__cat <<EOF >>%buildroot%_altdir/%name-shallow-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-shallow.menu	100
EOF

%post lxde
# hack around lxde
touch /etc/xdg/menus/lxde-applications.menu

#files 
#-f %name.lang
#doc AUTHORS ChangeLog NEWS README

%files common
%_datadir/desktop-directories/altlinux-*.directory
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/altlinux-*.menu

%files nested-menu
%_altdir/%name-nested-menu

%files shallow-menu
%_altdir/%name-shallow-menu

%files xfce
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/xfce-applications.menu

%files lxde
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/lxde-applications.menu

%files gnome
%config %_sysconfdir/xdg/menus/gnome-applications.menu
%config %_sysconfdir/xdg/menus/settings.menu

%changelog
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

