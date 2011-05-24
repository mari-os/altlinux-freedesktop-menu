#!/bin/sh -v

TOP=../altlinux-freedesktop-menu.git

#make distclean
rm -rf desktop-directories-kde4
cp -a $TOP/desktop-directories-kde4 .
rm -rf desktop-directories layout configure.ac Makefile.am po/*.po *.spec
cp -a $TOP/desktop-directories .
cp -a $TOP/layout .
cp -a $TOP/configure.ac .
cp -a $TOP/Makefile.am .
cp -a $TOP/AUTHORS .
cp -a $TOP/po/*.po po/
cp -a $TOP/po/LINGUAS po/
cp -a $TOP/*.spec .
#autoreconf -fisv
#./configure; make

../viy-local.git/gear-local-hasher --apt-config=/etc/apt/apt.conf.SS --with-stuff
