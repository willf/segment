This module segments text according word frequency using the Viterbi algorithm. Probably
due to Peter Norvig somehow.

Three sources of frequency information is provided.

One is from the Google NGram corpus, a general web corpus.

The second is from the Rovereto Twitter N-Gram Corpus, which is better for some Twitter data.

The third is from a webcrawl dataset of anchor text provided
by Vinay Goel of the Internet Archive.

    > from segment.segmenter import Analyzer
    > e = Analyzer('en')
    > e.segment("AbeLincoln")
    ['Abe', 'Lincoln']
    > e.segment("BieberHeartsBeliebers")
    ['Bi', 'e', 'ber', 'Hearts', 'Be', 'lieber', 's']
    > t = Analyzer('twitter')
    > t.segment("BieberHeartsBeliebers")
    ['Bieber', 'Hearts', 'Beliebers']
    > t = Analyzer('anchor')
    > t.segment("wordpress&sex")
    ['wordpress', '&', 'sex']
