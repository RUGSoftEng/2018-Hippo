from dateutil.relativedelta import relativedelta
from itsdangerous import Serializer, SignatureExpired, BadSignature
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.hash import pbkdf2_sha256
from datetime import date
import base64

from hippo_web import db, app

from elasticsearch_dsl import *



class AgeGroup:
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
        if group.min <= age <= group.max:
            return group

    return age_groups[-1]


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    password_hash = db.Column(db.String(256))

    # If null: opt-out for data collection, record datetime for opt-in.
    data_collection_consent = db.Column(db.DateTime())
    marketing_consent = db.Column(db.DateTime())

    birthday = db.Column(db.Date())
    location_country = db.Column(db.String(3))

    def get_age(self) -> int:
        return relativedelta(datetime.today(), self.birthday).years

    def hash_password(self, password: str):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password: str) -> bool:
        return pbkdf2_sha256.verify(password, self.password_hash)

    def generate_auth_token(self) -> str:
        serializer = Serializer(app.config['SECRET_KEY'])

        return serializer.dumps({'id': self.id}).decode("utf-8")

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

        user = User.query.get(data['id'])

        return user


#class Like(db.Model):
#    __tablename__ = 'likes'

#    id = db.Column(db.Integer, primary_key=True)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class User_ES(DocType):
    email = Text()
    passhash = Text()
    first_name = Text()
    last_name = Text()
    birthdate = Date()
    gender = Text()
    dataCollectionConsent = Boolean()
    marketingConsent = Boolean()

    def get_age(self):
        current=date.today()
        age=current.year-self.birthdate.year-((current.month, current.day)<(self.birthdate.month, self.birthdate.day))
        return age

    def hash_password(self, password: str):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password: str) -> bool:
        return pbkdf2_sha256.verify(password, self.password_hash)

    def generate_auth_token(self):
        serializer = Serializer(app.config['SECRET_KEY'])
        return serializer.dumps({'id': self.meta.id}).decode("utf-8")

    @staticmethod
    def verify_auth_token(token: str) -> object:
        serializer = Serializer(app.config['SECRET_KEY'])

        try:
            data = serializer.loads(token)
            print(data)
        except SignatureExpired:
            # Valid token, but expired.
            return None

        except BadSignature:
            # Invalid token.
            return None

        return User.get(data["id"])

    class Meta:
        index = 'user'

    def save(self, **kwargs):
        return super(User, self).save(**kwargs)


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
