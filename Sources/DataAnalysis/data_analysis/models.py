from elasticsearch_dsl import *


class Tweet(DocType):
    keywords = Text(analyzer='snowball', fields={'raw': Keyword()})
    synonyms = Text()
    date = Date()
    content = Text(analyzer='snowball')
    raw = Text()
    id = Text()

    class Meta:
        index = 'tweet'

    def save(self, ** kwargs):
        return super(Tweet, self).save(** kwargs)