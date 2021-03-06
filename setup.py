#!/usr/bin/python

# Rapache - Apache Configuration Tool
# Copyright (C) 2008 Stefano Forenza,  Jason Taylor, Emanuele Gentili
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess, glob, os.path
from os import path
from distutils.core import setup
setup(
    name='rapache',
    author='Rapache Developers',
    author_email='rapache-devel@lists.launchpad.net',
    maintainer='Emanuele Gentili',
    maintainer_email='emgent@ubuntu.com',
    description='Simple tool for managing and configuring an apache2 instance',
    url = 'http://www.rapache.org',
    license='GNU GPL',
    packages=['RapacheCore', 'RapacheGtk'],
    scripts=['rapache', 'hosts-manager'],
    data_files=[
                ('share/rapache/Glade', glob.glob('Glade/*')),
                ('lib/rapache/plugins/', glob.glob('plugins/__init__.py')),
                ('lib/rapache/plugins/ssl', glob.glob('plugins/ssl/*')),
                ('lib/rapache/plugins/advanced', glob.glob('plugins/advanced/*')),
                ('lib/rapache/plugins/basic_authentication', glob.glob('plugins/basic_authentication/*')),
                ('share/applications', ['data/rapache.desktop']),
               ],
    )

