from typing import Dict

from hippo_web import app

infrastructure: Dict[str, str] = {
    "ELASTICSEARCH_SERVER": "localhost",
    "ELASTICSEARCH_USERNAME": "",
    "ELASTICSEARCH_PASSWORD": "",

    "POSTGRESQL_SERVER": "localhost",
    "POSTGRESQL_USERNAME": "",
    "POSTGRESQL_PASSWORD": "",

    "API_SERVER": "localhost",
    "API_SECRET_KEY": "",
}

app.secret_key = infrastructure["API_SECRET_KEY"]