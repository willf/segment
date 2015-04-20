try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Text Segmenter based on probabilities',
    'author': 'Will Fitzgerald',
    'url': 'http://github.com/willf/',
    'download_url': 'http://github.com/willf/',
    'author_email': 'will.fitzgerald@pobox.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['segment'],
    'scripts': [],
    'name': 'segment'
}

setup(**config)
