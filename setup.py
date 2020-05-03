#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import join, dirname

here = dirname(__file__)

setup(name='newdex',
      version='0.1.0',
      description="Unnoficial Newdex API wrapper for Python 3.",
      long_description=open(join(here, 'README.md')).read(),
      long_description_content_type="text/markdown",
      author='canokaue',
      author_email='kaue.cano@quan.digital',
      license='MIT',
      url='https://github.com/quan-digital/newdex',
      download_url = 'https://github.com/quan-digital/newdex/dist/newdex-0.1.0.tar.gz',
      install_requires=[
        'requests==2.23.0'
      ],
      packages=find_packages(),
      keywords = ['newdex', 'cryptocurrency', 'exchange', 'crypto-api', 'crypto-exchange', 'descentralized-exchange', 
      'newdex-api', 'eosio', 'api-wrapper'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
      ],
      )
