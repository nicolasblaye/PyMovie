try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'PyMovie',
    'author': 'Nicolas Blaye',
    'url': 'https://github.com/nicolasblaye/PyMovie',
    'download_url': 'https://github.com/nicolasblaye/PyMovie',
    'author_email': 'nicolas.blaye@telecom-bretagne.eu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['PyMovie'],
    'scripts': [],
    'name': 'pyMovie'
}

setup(**config)
