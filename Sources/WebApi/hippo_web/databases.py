from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections


def connect_elasticsearch():
    es = Elasticsearch()
    connections.create_connection(hosts=['localhost'])
    
connect_elasticsearch()