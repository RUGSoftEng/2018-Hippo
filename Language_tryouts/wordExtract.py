from __future__ import division

import nltk
from nltk.book import *

from collections import Counter
from matplotlib.pyplot import *
from numpy import logspace, log10

from nltk.corpus import brown

#ignore punctuation
f = open("tweet.txt", "r")
inputfile = f.read()
tokens = nltk.tokenize.word_tokenize(inputfile)
text = [w.lower() for w in tokens if w.isalpha()]

#sort out unnecessary stuff. I sort out to and prepositions(?), however, articles (a/an/the) must be sorted out too
intermid = nltk.pos_tag(text)
tag_pairs = nltk.bigrams(intermid)
text = [a[0] for (a, b) in tag_pairs if b[1] != 'PRP' and b[1] != 'TO']

#find frequency distibution
fdist = FreqDist(text)
print(fdist)

#plot 10 most frequent words
fdist.plot(10, cumulative=False)
