#!/bin/sh
if stat -t /etc/xdg/menus/*applications.menu >/dev/null 2>&1
then
    touch /etc/xdg/menus/*applications.menu
fi
if stat -t /var/tmp/kdecache-*/ >/dev/null 2>&1
then
    for kdedir in /var/tmp/kdecache-*/; do
	user=`echo $kdedir|sed -e 's,^/var/tmp/kdecache-,,;s,/$,,'`
	if [ -e "$kdedir/ksycoca4" ] && [ -x /usr/bin/kbuildsycoca4 ]; then
	    su -l -s /bin/sh -c '/usr/bin/kbuildsycoca4 --noincremental' $user >/dev/null 2>&1 ||:
	fi
	if [ -e "$kdedir/ksycoca" ] && [ -x /usr/bin/kbuildsycoca; then
	    su -l -s /bin/sh -c '/usr/bin/kbuildsycoca --noincremental' $user >/dev/null 2>&1 ||:
	fi
    done
fi
