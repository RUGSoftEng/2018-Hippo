import json

from tweepy import *

from hippo_data_analysis.models import Tweet
from hippo_data_analysis.nlp import analyse_tweet, match_keywords_filter

consumer_key = "19zbXP0QH2etpYqk1oHwVFRrA"
consumer_secret = "P4i0N3umEfmxCoseeL10X8EgxWLlc5v59pZRms1EYj5tKJk8Gi"

access_token = "2813757815-DLqLnonqdGiFM8M6AMLE2fp5fgL7t9VCZlC23z1"
access_token_secret = "3yBbtW8CICUyS6wjY9ZQPzRTs0yuwynTguvsA2R35ZknW"


class _TwitterStreamListener(StreamListener):

    def on_data(self, data):
        json_tweet = json.loads(data)

        # TODO: Remove in production.
        print(json_tweet["text"])

        if match_keywords_filter(json_tweet["text"]):
            tweet = Tweet()

            tweet.content = json_tweet["text"]
            tweet.date = json_tweet["created_at"]
            tweet.raw = data
            tweet.id = json_tweet["id_str"]

            analyse_tweet(json_tweet["text"])

            tweet.save()

        return True

    def on_error(self, status):
        print(status)


class TwitterStreaming:

    def __init__(self):
        self.stream_listener = _TwitterStreamListener()

    def start(self, keyword_filter: [str]):
        authenticator = OAuthHandler(consumer_key, consumer_secret)
        authenticator.set_access_token(access_token, access_token_secret)

        stream = Stream(authenticator, self.stream_listener)
        stream.filter(track=keyword_filter)
