# dnf-plugin-ovl
Workaround to run `dnf` on overlayfs. A port of `yum-plugin-ovl` to `dnf`.

## When you need it
Running `dnf` (or `yum` or `rpm`) with the RPM database on an overlayfs mount (_e.g._ in a container) will result in errors similar to
```
rpmdb: BDB0060 PANIC: fatal region error detected; run recovery
```
or
```
error: rpmdbNextIterator: skipping h# 173 blob size(4836): BAD, 8 + 16 * il(70) + dl(3708)
```
as soon as you run `dnf` on different layers when building an image.

## Install
It is included in Fedora's repository and EPEL:
```
dnf install -y dnf-plugin-ovl
```

## Verifying installation
```
dnf updateinfo -v
```
Should show (second line only if an overlayfs system detected):
```
Loaded plugins: ..., ovl, ...
OverlayFS detected
```

## Background
Opening a file on an OverlayFS in read-only mode causes the file from lower layer to be opened, then later on, if the same file is re-opened in write mode, a copy-up into the upper layer takes place, resulting into a new file being opened.

Since `dnf` opens the RPMdb first read-only, and then also with write access, we need to copy-up the files beforehand to make sure that the access is consistent.

## Building
```
rpmbuild --nobuild --nodeps dnf-plugin-ovl.spec  # Will fail, but creates missing dirs on new machine
spectool -g -R dnf-plugin-ovl.spec
rpmbuild --clean -v -bb dnf-plugin-ovl.spec
```
