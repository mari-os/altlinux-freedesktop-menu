AC_INIT([altlinux-freedesktop-menu], [0.0.1], [viy@altlinux.org])
AM_INIT_AUTOMAKE

GETTEXT_PACKAGE=alt-fd-menu
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [Name of default gettext domain])
AC_SUBST(GETTEXT_PACKAGE)

AM_GLIB_GNU_GETTEXT

IT_PROG_INTLTOOL([0.40.0])

dnl dirty hack used to prevent the installation of useless mo files.
USE_NLS=no
AC_SUBST(USE_NLS)

AC_OUTPUT([
Makefile
layout/Makefile
desktop-directories/Makefile
po/Makefile.in
])
