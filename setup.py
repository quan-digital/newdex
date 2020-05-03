#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import join, dirname

here = dirname(__file__)

setup(name='newdex',
      version='0.1.0',
      description="Unnoficial Newdex API wrapper for Python 3.",
      long_description=open(join(here, 'README.md')).read(),
      author='canokaue',
      author_email='kaue.cano@quan.digital',
      url='quan.digital',
      install_requires=[
        'requests==2.23.0'
      ],
      packages=find_packages(),
      )
