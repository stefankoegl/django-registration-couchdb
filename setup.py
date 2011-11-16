#!/usr/bin/env python
# Setup script for django-registration-couchdb

from distutils.core import setup

import re

src_main = open('registration_couchdb/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", src_main))
docstrings = re.findall('"""(.*?)"""', src_main, re.DOTALL)

# How is the package going to be called?
PACKAGE = 'registration_couchdb'

# List the modules that need to be installed/packaged
PACKAGES = (
        'registration_couchdb',
        'registration_couchdb.backends',
        'registration_couchdb.backends.default',
        'registration_couchdb.management',
        'registration_couchdb.management.commands',
)

PACKAGE_DATA = {}
for package in PACKAGES:
    PACKAGE_DATA[package] = ['_design/views/*/*.js']


# Metadata fields extracted from the main file
AUTHOR_EMAIL = metadata['author']
VERSION = metadata['version']
WEBSITE = metadata['website']
LICENSE = metadata['license']
DESCRIPTION = docstrings[0]

# Extract name and e-mail ("Firstname Lastname <mail@example.org>")
AUTHOR, EMAIL = re.match(r'(.*) <(.*)>', AUTHOR_EMAIL).groups()

setup(name=PACKAGE,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=EMAIL,
      license=LICENSE,
      url=WEBSITE,
      packages=PACKAGES,
      package_data=PACKAGE_DATA,
      download_url='http://pypi.python.org/packages/source/' + \
              PACKAGE[0] + '/' + PACKAGE + \
              '/'+PACKAGE+'-'+VERSION+'.tar.gz')
