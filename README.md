This module segments text according word frequency using the Viterbi algorithm. Probably
due to Peter Norvig somehow.

Two sources of frequency information is provided. One is from the Google NGram corpus, and
the other from the Rovereto Twitter N-Gram Corpus, which is better for some Twitter data.

    In[3]: from segment.segmenter import Analyzer
    In[4]: e = Analyzer('en')
    In[5]: e.segment("AbeLincoln")
    Out[5]: ['Abe', 'Lincoln']
    In[6]: e.segment("BieberHeartsBeliebers")
    Out[6]: ['Bi', 'e', 'ber', 'Hearts', 'Be', 'lieber', 's']
    In[7]: t = Analyzer('twitter')
    In[8]: t.segment("BieberHeartsBeliebers")
    Out[8]: ['Bieber', 'Hearts', 'Beliebers']

