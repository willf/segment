r"""Segmenting a text using probabilities.

:mod:`py_segment` exposes an API to segment text (such as hashtags)
into its most probable segmented words

For example::

    >>> from py_segment import Segmenter
    >>> s = Segmenter('en', case_folding=True)
    >>> s.segment("#ilovenewyork"
    ["#", "i", "love", "new", "york"]
    >>> s.segment("AbeLincoln")
    ["Abe", "Lincoln"]
    >>> s.segment("#lordoftherings")
    ["lord", "ofthe", "rings"]


Note that, in the last example, the segmentation is incorrect. Which happens.

Currently, only English segmentation, using frequency data from a Google web crawl,
is provided. It is hoped that additional languages and language types will be provided.
(For example, for Twitter text, or for German)
"""
__version__ = 0.1