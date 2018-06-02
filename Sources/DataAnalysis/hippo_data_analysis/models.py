from elasticsearch_dsl import *

import hippo_data_analysis.databases


class Tweet(DocType):
    keywords = Text(analyzer='snowball', fields={'raw': Keyword()})
    date = Date()
    content = Text(analyzer='snowball')
    raw = Text()

    class Meta:
        index = 'tweet'

    def save(self, ** kwargs):
        return super(Tweet, self).save(** kwargs)