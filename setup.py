#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: python273
@contact: https://vk.com/python273
@license: MIT

Copyright (C) 2018
"""

from setuptools import setup
from precursion import __version__

with open('README.md') as f:
    long_description = f.read()

setup(
    name='precursion',
    version=__version__,

    author='python273',
    author_email='whoami@python273.pw',

    description='No more `RecursionError: maximum recursion depth exceeded`',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/python273/precursion',
    download_url='https://github.com/python273/precursion/archive/v{}.zip'.format(
        __version__
    ),
    license='MIT',
    packages=['precursion'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
