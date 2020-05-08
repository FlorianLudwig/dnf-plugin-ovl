# Copyright (C) 2015  Red Hat, Inc.
#               2018  Grey Rook GmbH
#
# Authors: Pavel Odvody <podvody@redhat.com>
#          Florian Ludwig <f.ludwig@greyrook.com>
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

from os import utime, walk, path
import logging

import dnf


def should_touch():
    """
    Touch the files only once we've verified that
    we're on overlay mount
    """
    with open('/etc/mtab') as mtab:
        for line in mtab:
            if line.split()[1] == '/':  # Check rootfs only
                return 'overlay' in line  # Some images say "overlay" and others "overlayfs"
    return False


class OVLPlugin(dnf.Plugin):
    """workaround OverlayFS non compliance with posix"""
    name = "ovl"

    def __init__(self, base, cli):
        super(OVLPlugin, self).__init__(base, cli)

        if not should_touch():
            return

        logger = logging.getLogger('dnf.plugin')
        logger.info('OverlayFS detected')
        rpmdb_path = base.conf.installroot + 'var/lib/rpm/'
        try:
            for root, _, files in walk(rpmdb_path):
                for f in files:
                    p = path.join(root, f)
                    with open(p, 'a'):
                        utime(p, None)
        except Exception as e:
            logger.error("Error while doing RPMdb copy-up:\n%s", e)
