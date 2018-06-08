from itsdangerous import Serializer, SignatureExpired, BadSignature
from passlib.hash import pbkdf2_sha256

from hippo_web import app

from elasticsearch_dsl import *

class AgeGroup():
    def __init__(self, min, max, str_rep):
        self.min = min
        self.max = max
        self.str_rep = str_rep

age_groups = [
    AgeGroup(0, 15, "<16"),
    AgeGroup(16, 24, "16-24"),
    AgeGroup(25, 34, "25-34"),
    AgeGroup(35, 44, "35-44"),
    AgeGroup(45, 54, "45-54"),
    AgeGroup(55, 64, "55-64"),
    AgeGroup(65, 200, "65+"),
]

def get_age_group(age: int):
    for group in age_groups:
        if (group.min <= age and age <= group.max):
            return group
    
    return age_groups[-1]

class User(DocType):
    email = Text()
    passhash = Text()
    first_name = Text()
    last_name = Text()
    birthdate = Date()
    dataCollectionConsent = Boolean()
    marketingConsent = Boolean()

    # TODO: calculate the age of the user
    def get_age(self):
        return 0
    
    def hash_password(self, password: str):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password: str) -> bool:
        return pbkdf2_sha256.verify(password, self.password_hash)

    # TODO: Check whether "serializer.dumps" returns a string or bytes.
    def generate_auth_token(self, expiration: int = 600) -> object:
        serializer = Serializer(app.config['SECRET_KEY'], expires_in=expiration)

        return serializer.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token: str) -> object:
        serializer = Serializer(app.config['SECRET_KEY'])

        try:
            data = serializer.loads(token)

        except SignatureExpired:
            # Valid token, but expired.
            return None

        except BadSignature:
            # Invalid token.
            return None

        
    class Meta:
        index = 'user'
        
    def save(self, ** kwargs):
        return super(User, self).save(** kwargs)


# Elasticsearch model.
class Tweet(object):
    def __init__(self):
        self.sender: str = None
        self.content: str = None

# Demographics model.

class Demographic(DocType):
    count = Integer()
    age_group = Text()
    country = Text()
        
class Demographics(DocType):
    keywords = Text()
    data = Nested(Demographic)

    class Meta:
        index = 'demographics'
