import nltk

from nltk.tree import Tree
from nltk import ne_chunk, pos_tag, word_tokenize

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")


# TODO: Check whether still needed.
# this function is taken and slightly modified from
# https://stackoverflow.com/questions/24398536/named-entity-recognition-with-regular-expression-nltk
def get_continuous_chunks(text: str):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))

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


def analyse_tweet(tweet: str) -> [str]:
    keywords = get_keywords(tweet)

    return keywords


def get_keywords(text: str) -> [str]:
    tokens = nltk.tokenize.word_tokenize(text)
    alpha_tokens = [w.lower() for w in tokens if w.isalpha()]

    pos_tagged = nltk.pos_tag(alpha_tokens)

    grammar = r"""
                KEYWORD:
                    {<NN.*>}              #nouns
                    {<V.*>}               #all types of verbs
                    {<JJ.*>}              #adjectives
                    """

    cp = nltk.RegexpParser(grammar)
    chunks = cp.parse(pos_tagged)

    keywords = []

    # extract keywords
    for subtree in chunks.subtrees():
        if subtree.label() == "KEYWORD":
            keywords.append((subtree.leaves()[0])[0])

    return keywords
