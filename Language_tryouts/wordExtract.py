from __future__ import division

import nltk
import json

from nltk.book import *
from matplotlib.pyplot import *

from nltk.tree import Tree
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import wordnet, brown

#this function is taken and slightly modified from
#https://stackoverflow.com/questions/24398536/named-entity-recognition-with-regular-expression-nltk
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))

    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk and named_entity != "":
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk and named_entity != "":
            continuous_chunk.append(named_entity)

    return continuous_chunk



#ignore punctuation
f = open("tweet.txt", "r")
inputfile = f.read()
tokens = nltk.tokenize.word_tokenize(inputfile)
aplha_tokens = [w.lower() for w in tokens if w.isalpha()]

#sort out unnecessary stuff
pos_tagged = nltk.pos_tag(aplha_tokens)

# NP chunking
#chunk nouns
grammar = r"""
           KEYWORD:
                {<NN.*>}              #nouns
                {<V.*>}             #all types of verbs
                {<JJ.*>}              #adjectives
            """

cp = nltk.RegexpParser(grammar)
chunks = cp.parse(pos_tagged)
print(chunks)
sorted_keys = []

#extract keywords
for subtree in chunks.subtrees():
        if subtree.label() == "KEYWORD":
            sorted_keys += subtree.leaves()

#find frequency dist of kwywords and show 3 most common
fdistKeys = FreqDist(sorted_keys)
fdistKeys.plot(3, cumulative=False)

#named entity recognition
fdistNames = FreqDist(get_continuous_chunks(inputfile))
fdistNames.plot(3, cumulative=False)

#getting synonumous of sorted_keys
synonyms = []
for (key, type) in sorted_keys:
    for syn in wordnet.synsets(key):
        for l in syn.lemmas():
            if l.name() not in synonyms:
                synonyms.append(l.name())

print(synonyms)

#sort synonyms based on frequency of usage in Brown corpra
freqs = FreqDist([w.lower() for w in brown.words()])
wordlist_sorted = sorted(synonyms, key=lambda x: freqs[x.lower()], reverse=True)
for w in wordlist_sorted:
    print(w)

#create json
data = {}
data['tweet'] = inputfile
data['keywords'] = synonyms
data['id'] = 5 #get it from Jean or whoever does this part
json_data = json.dumps(data)
print (json_data)

