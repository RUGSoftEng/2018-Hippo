from flask import *
import json
from elasticsearch import Elasticsearch
import sys
from decimal import Decimal

def searchES(term):
    terms=term.split()
    res=[]
    for t in terms:
        results = es.search(index="hippo", body={"query": {"match": {"keywords": t}}}) #assuming field is called keywords
        for h in results['hits']['hits']:
            r=h['_source']
            r['id']=h['_id']
            if r not in res:
                res.extend(r)
    return res

placeholder=[]

app = Flask(__name__)
es = Elasticsearch()

@app.route('/')
def start():
    return "Hippo start page"

@app.route('/search/<term>', methods=['GET'])
def search(term): #todo replace w searchES once ES is set up
    terms=term.split()
    res=[]
    for t in terms:
        r = [r for r in placeholder if r['keywords'].count(t)>=1]
        if r not in res:
            res.extend(r)
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