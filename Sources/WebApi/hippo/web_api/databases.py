from sqlalchemy import create_engine


def connect_elasticsearch():
    pass


def connect_postgresql():
    engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
