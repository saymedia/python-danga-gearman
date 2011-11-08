#!/usr/bin/env python

from distutils.core import setup

from dangagearman import __version__ as version

setup(
    name = 'danga-gearman',
    version = version,
    description = 'Client for the Danga (Perl) Gearman implementation',
    author = 'Samuel Stauffer',
    author_email = 'samuel@descolada.com',
    url = 'http://github.com/saymedia/python-danga-gearman/tree/master',
    packages = ['dangagearman'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
