try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Gothon game on the web',
    'author': 'Emil Raubach',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'eraubach@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'gothonweb'
}

setup(**config)
