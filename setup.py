#!/usr/bin/env python
'''
A CLI front-end to a running salt-api system

'''
import json
import os
import re

from distutils.core import setup
from distutils.dist import Distribution
from distutils.command import sdist, install_data

setup(
    name='salt-pepper',
    version='0.5.0',
    description=__doc__,
    packages=['pepper'],
    platforms=['all'],
    scripts=['scripts/pepper'],
)
