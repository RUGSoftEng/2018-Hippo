from elasticsearch import Elasticsearch
from sqlalchemy import create_engine


def connect_elasticsearch():
    es = Elasticsearch()


def connect_postgresql():
    engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
