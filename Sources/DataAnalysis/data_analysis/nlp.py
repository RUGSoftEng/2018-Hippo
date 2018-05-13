from nltk import ne_chunk, pos_tag, word_tokenize, re
from nltk.tree import Tree


def get_continuous_chunks(text):
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


def check_wish(c):
    wish = ['I wish there was ']
    for i in wish:
        if re.search(i, c):
            result = re.sub(i, "", c)
            return result
    return ""
