#!/usr/bin/env python
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from setuptools import setup
import re
import os
import ConfigParser


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_require_version(name):
    if minor_version % 2:
        require = '%s >= %s.%s.dev0, < %s.%s'
    else:
        require = '%s >= %s.%s, < %s.%s'
    require %= (name, major_version, minor_version,
        major_version, minor_version + 1)
    return require

config = ConfigParser.ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
version = info.get('version', '0.0.1')
major_version, minor_version, _ = version.split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)
name = 'silex_party_br'

download_url = 'http://www.silexsistemas.com.br'
if minor_version % 2:
    version = '%s.%s.dev0' % (major_version, minor_version)
    download_url = (
        'hg+http://hg.tryton.org/modules/%s#egg=%s-%s' % (
            name[8:], name, version))

requires = ['python-sql']
for dep in info.get('depends', []):
    if not re.match(r'(ir|res|webdav)(\W|$)', dep):
        requires.append(get_require_version('trytond_%s' % dep))
requires.append(get_require_version('trytond'))

setup(name=name,
    version=version,
    description='Tryton module with specific fields for Brazilian parties/people',
    long_description=read('README'),
    author='Sílex Sistemas',
    author_email='silex@silexsistemas.com.br',
    url='http://www.silexsistemas.com.br/',
    download_url=download_url,
    keywords='tryton party brazil',
    package_dir={'silex_party_br': '.'},
    packages=[
        'silex_party_br',
        'silex_party_br.tests',
        ],
    package_data={
        'silex_party_br': (info.get('xml', [])
            + ['tryton.cfg', 'view/*.xml', 'locale/*.po', '*.odt',
                'icons/*.svg']),
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Brazilian Portuguese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
        ],
    license='GPL-3',
    install_requires=requires,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    silex_party_br = silex_party_br
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
    )