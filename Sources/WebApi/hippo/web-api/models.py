from itsdangerous import Serializer, SignatureExpired, BadSignature
from passlib.hash import pbkdf2_sha256

from hippo.api import db, app


# SQLAlchemy model.
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))

    def hash_password(self, password: str):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password: str) -> bool:
        return pbkdf2_sha256.verify(password, self.password_hash)

    # TODO: Check whether "serializer.dumps" returns a string or bytes.
    def generate_auth_token(self, expiration: int = 600) -> object:
        serializer = Serializer(app.config['SECRET_KEY'], expires_in=expiration)

        return serializer.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token: str):
        serializer = Serializer(app.config['SECRET_KEY'])

        try:
            data = serializer.loads(token)

        except SignatureExpired:
            # Valid token, but expired.
            return None

        except BadSignature:
            # Invalid token.
            return None

        user = User.query.get(data['id'])

        return user


# Elasticsearch model.
class Tweet(object):
    def __init__(self):
        self.sender: str = None
        self.content: str = None
