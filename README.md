# dnf-plugin-ovl
workaround to run dnf on overlayfs. A port of yum-plugin-ovl to dnf.

## When you need it
Running dnf (or yum or rpm) within inside overlayfs (for example inside docker) will result in errors similar to 
```
rpmdb: BDB0060 PANIC: fatal region error detected; run recovery
```
as soon as you run dnf on different layers.

## Install

It is included in Fedora's repository:
```
dnf install -y dnf-plugin-ovl
```

## Background

Opening a file on OverlayFS in read-only mode causes the file from
lower layer to be opened, then later on, if the same file is opened
in write mode, a copy-up into the upper    layer    takes    place,
resulting into a new file being opened.
Since dnf opens the RPMdb first read-only, and then
also with write access, we need to copy-up the files beforehand to
make sure that the access is consistent.

## Building

```
spectool -g -R dnf-plugin-ovl.spec
rpmbuild --target noarch --clean -v -bb dnf-plugin-ovl.spec 
```
