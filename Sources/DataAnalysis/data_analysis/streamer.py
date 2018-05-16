import json

from elasticsearch_dsl import *
from elasticsearch_dsl import connections
from tweepy import *

consumer_key = "19zbXP0QH2etpYqk1oHwVFRrA"
consumer_secret = "P4i0N3umEfmxCoseeL10X8EgxWLlc5v59pZRms1EYj5tKJk8Gi"

access_token = "2813757815-DLqLnonqdGiFM8M6AMLE2fp5fgL7t9VCZlC23z1"
access_token_secret = "3yBbtW8CICUyS6wjY9ZQPzRTs0yuwynTguvsA2R35ZknW"

connections.create_connection(hosts=['localhost'])

class Tweet(DocType):
    keywords = Text(analyzer='snowball', fields={'raw': Keyword()})
    date = Date()
    content = Text(analyzer='snowball')
    raw = Text()

    class Meta:
        index = 'tweet'

    def save(self, ** kwargs):
        return super(Tweet, self).save(** kwargs)


class _TwitterStreamListener(StreamListener):

    def on_data(self, data):
        print(type(data))

        json_tweet = json.loads(data)

        print(json_tweet["text"])
        tweet = Tweet()

        tweet.content = json_tweet["text"]
        tweet.date = json_tweet["created_at"]
        tweet.raw = data

        tweet.save()

        return True

    def on_error(self, status):
        print(status)


class TwitterStreaming:

    def __init__(self):
        self.stream_listener = _TwitterStreamListener()

    def start(self, keyword_filter: [str]):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = Stream(auth, self.stream_listener)
        stream.filter(track=keyword_filter)
