from elasticsearch import Elasticsearch
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

auth = HTTPBasicAuth()

db = SQLAlchemy(app)
es = Elasticsearch()

import sys
print(sys.version)

import hippo_web.config
import hippo_web.databases
import hippo_web.models
import hippo_web.api

#app.secret_key = hippo_web.infrastructure["API_SECRET_KEY"]
