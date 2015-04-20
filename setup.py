import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='segment',
      version="0.0.1",
      author="Will Fitzgerald",
      author_email="will.fitzgerald@pobox.com",
      description="Text Segmenter based on probabilities",
      url='http://github.com/willf/segment',
      license="BSD",
      keywords="nlp sentiment",
      long_description=read("README.md"),
      packages=find_packages(),
      package_data={'': ['*.tsv']})
