# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grimoirelab_toolkit', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.8.0,<3.0.0']

setup_kwargs = {
    'name': 'grimoirelab-toolkit',
    'version': '0.3.0',
    'description': 'Toolkit of common functions used across GrimoireLab',
    'long_description': '# GrimoireLab Toolkit [![Build Status](https://github.com/chaoss/grimoirelab-toolkit/workflows/tests/badge.svg)](https://github.com/chaoss/grimoirelab-toolkit/actions?query=workflow:tests+branch:master+event:push) [![Coverage Status](https://img.shields.io/coveralls/chaoss/grimoirelab-toolkit.svg)](https://coveralls.io/r/chaoss/grimoirelab-toolkit?branch=master)\n\nToolkit of common functions used across GrimoireLab projects.\n\nThis package provides a library composed by functions widely used in other\nGrimoireLab projects. These function deal with date handling, introspection,\nURIs/URLs, among other topics.\n\n## Requirements\n\n* Python >= 3.7\n* python3-dateutil >= 2.6\n\n## Installation\n\n```\n$ pip3 install -r requirements.txt\n$ python3 setup.py install\n```\n\n## License\n\nLicensed under GNU General Public License (GPL), version 3 or later.\n',
    'author': 'GrimoireLab Developers',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://chaoss.github.io/grimoirelab/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
