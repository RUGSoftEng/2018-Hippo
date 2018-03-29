from flask import *
import json
import sys
from decimal import Decimal

placeholder=[]

app = Flask(__name__)

@app.route('/')
def start():
    return "Hippo start page"

@app.route('/search/<term>', methods=['GET'])
def search(term):
    res = [res for res in placeholder if res['keywords'].count(term)>=1]
    return jsonify(res)

def setup_placeholder():
	tweets_file = open('tweets.txt', 'r')
	
	for line in tweets_file:
		arr = line.split('\t')
		tweet_id = str(int(Decimal(arr[0].replace('\"', ''))))
		tweet_contents = arr[2].replace('\"', '')
		tweet_keywords = tweet_contents.split(' ')
		placeholder.append({'tweet-id':tweet_id, 'content':tweet_contents, 'keywords':tweet_keywords})
	
if __name__ == '__main__':
	setup_placeholder()
    app.run(debug=True)
