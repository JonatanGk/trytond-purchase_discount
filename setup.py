#!/usr/bin/env python
# This file is part purchase_discount module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from setuptools import setup
import re
import os
import io
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

MODULE2PREFIX = {
    'account_invoice_discount': 'trytonspain',
    }


def read(fname):
    return io.open(
        os.path.join(os.path.dirname(__file__), fname),
        'r', encoding='utf-8').read()


def get_require_version(name):
    if minor_version % 2:
        require = '%s >= %s.%s.dev0, < %s.%s'
    else:
        require = '%s >= %s.%s, < %s.%s'
    require %= (name, major_version, minor_version,
        major_version, minor_version + 1)
    return require

config = ConfigParser()
config.readfp(open('tryton.cfg'))
info = dict(config.items('tryton'))
for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()
version = info.get('version', '0.0.1')
major_version, minor_version, _ = version.split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)
name = 'trytonspain_purchase_discount'
download_url = 'https://bitbucket.org/trytonspain/trytond-purchase_discount'

requires = []
for dep in info.get('depends', []):
    if not re.match(r'(ir|res)(\W|$)', dep):
        prefix = MODULE2PREFIX.get(dep, 'trytond')
        requires.append(get_require_version('%s_%s' % (prefix, dep)))
requires.append(get_require_version('trytond'))

tests_require = [get_require_version('proteus')]
dependency_links = []
if minor_version % 2:
    # Add development index for testing with proteus
    dependency_links.append('https://trydevpi.tryton.org/')
    dependency_links.append('http://trydevpi.trytonspain.com/')

setup(name=name,
    version=version,
    description='Tryton Purchase Discount Module',
    long_description=read('README'),
    author='TrytonSpain',
    author_email=sergi@koolpi.com'',
    url='https://bitbucket.org/trytonspain/',
    download_url=download_url,
    keywords='',
    package_dir={'trytond.modules.purchase_discount': '.'},
    packages=[
        'trytond.modules.purchase_discount',
        'trytond.modules.purchase_discount.tests',
        ],
    package_data={
        'trytond.modules.purchase_discount': (info.get('xml', [])
            + ['tryton.cfg', 'view/*.xml', 'locale/*.po', '*.odt',
                'icons/*.svg', 'tests/*.rst']),
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: Bulgarian',
        'Natural Language :: Catalan',
        'Natural Language :: Czech',
        'Natural Language :: Dutch',
        'Natural Language :: English',
        'Natural Language :: French',
        'Natural Language :: German',
        'Natural Language :: Hungarian',
        'Natural Language :: Italian',
        'Natural Language :: Portuguese (Brazilian)',
        'Natural Language :: Russian',
        'Natural Language :: Slovenian',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Office/Business',
        ],
    license='GPL-3',
    install_requires=requires,
    dependency_links=dependency_links,
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    purchase_discount = trytond.modules.purchase_discount
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
    tests_require=tests_require,
    use_2to3=True,
    convert_2to3_doctests=[
        'tests/scenario_purchase.rst',
        ],
    )
