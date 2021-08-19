#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['tomli']

package_data = \
{'': ['*']}

setup(name='tomli',
      version='@VERSION@',
      description="A lil' TOML parser",
      author=None,
      author_email='Taneli Hukkinen <hukkin@users.noreply.github.com>',
      url=None,
      packages=packages,
      package_data=package_data,
      python_requires='>=3.6',
     )