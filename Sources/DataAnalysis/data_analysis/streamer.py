from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "19zbXP0QH2etpYqk1oHwVFRrA"
consumer_secret = "P4i0N3umEfmxCoseeL10X8EgxWLlc5v59pZRms1EYj5tKJk8Gi"

access_token = "2813757815-DLqLnonqdGiFM8M6AMLE2fp5fgL7t9VCZlC23z1"
access_token_secret = "3yBbtW8CICUyS6wjY9ZQPzRTs0yuwynTguvsA2R35ZknW"

keyword_filter1 = ['basketball']


class _TwitterStreamListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


class TwitterStreaming:

    def __init__(self):
        self.stream_listener = _TwitterStreamListener

    def start(self, keyword_filter: [str]):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = Stream(auth, self.stream_listener)
        stream.filter(track = keyword_filter)