#import flask
from flask import *
from elasticsearch import Elasticsearch as es
import os
import sys

#init
app=Flask('hippo')
app.config.from_object(__name__)
host=os.environ['DOCKER_MACHINE_IP'] #tbd
e=es([host])
#print(e.info())


#default timeline
@app.route('/')
def public_timeline():
    return "Hippo start page"

#timeline showing results of search term
@app.route('/<term>')
def timeline(term): #results-json
    #note: match querries have an opt to auto gen synonyms - true by default
    #content->tags? depends on elasticsearch set up
    results = es.search(index="", body={"query": {"match": {"content": term}}})
    res=[]
    for h in results['hits']['hits']:
        r=h['_source']
        r['id']=h['_id']
        res.append(r)
    return res

