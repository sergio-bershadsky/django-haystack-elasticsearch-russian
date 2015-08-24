#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages


setup\
    ( name='haystack_russian'
    , version='1.0'
    , description='Haystack backend and hacks to work with russian analyser'
    , author='Sergey Nikitin'
    , author_email='nikitinsm@gmail.com'
    , url='https://github.com/nikitinsm/django-haystack-elasticsearch-russian'
    , packages = find_packages('src')
    , package_dir = {'': 'src'}
    , include_package_data = True
    , install_requires =
      [ "django-haystack"
      , ]
    )