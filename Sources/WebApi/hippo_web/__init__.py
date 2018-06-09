from elasticsearch import Elasticsearch
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

auth = HTTPBasicAuth()

db = SQLAlchemy(app)

es = Elasticsearch()

import hippo_web.config
import hippo_web.models
import hippo_web.api
