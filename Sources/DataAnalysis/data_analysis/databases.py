from elasticsearch_dsl import connections

connections.create_connection(hosts=['elasticsearch'])
