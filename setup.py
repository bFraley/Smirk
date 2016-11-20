try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Smirk Web Framework',
    'author': 'Brett Fraley',
    'url': 'https://github.com/bFraley/Smirk',
    'download_url': 'https://github.com/bFraley/Smirk',
    'author_email': 'brettfraley@gmail.com',
    'version': '0.0.01',
    'packages': ['smirk'],
    'scripts': [],
    'name': 'Smirk Web Framework'
}

setup(**config)
