from typing import Optional

from dateutil.relativedelta import relativedelta
from itsdangerous import Serializer, SignatureExpired, BadSignature
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.hash import pbkdf2_sha256
from datetime import date
import base64

from hippo_web import db, app

from elasticsearch_dsl import *

SECRET_KEY = app.config['SECRET_KEY']


class AgeGroup:
    def __init__(self, min: int, max: int, name: str, description: str):
        self.min = min
        self.max = max
        self.name = name
        self.description = description


age_groups = [
    AgeGroup(0, 15, "lower_15", "<16"),
    AgeGroup(16, 24, "16_24", "16-24"),
    AgeGroup(25, 34, "25_34", "25-34"),
    AgeGroup(35, 44, "35_44", "35-44"),
    AgeGroup(45, 54, "45_54", "45-54"),
    AgeGroup(55, 64, "55_64", "55-64"),
    AgeGroup(65, 200, "65_higher", "65+"),
]


def get_age_group(age: int) -> AgeGroup:
    for group in age_groups:
        if group.min <= age <= group.max:
            return group

    return age_groups[-1]


class Demographics(db.Model):
    __tablename__ = 'demographics'

    id = db.Column(db.Integer, primary_key=True)
    keywords = db.Column(db.String(128), index=True)

    views = db.Column(db.Integer)
    views_male = db.Column(db.Integer)
    views_female = db.Column(db.Integer)

    views_lower_15 = db.Column(db.Integer)
    views_16_24 = db.Column(db.Integer)
    views_25_34 = db.Column(db.Integer)
    views_35_44 = db.Column(db.Integer)
    views_45_54 = db.Column(db.Integer)
    views_55_64 = db.Column(db.Integer)
    views_65_higher = db.Column(db.Integer)

    likes = db.Column(db.Integer)
    likes_male = db.Column(db.Integer)
    likes_female = db.Column(db.Integer)

    likes_lower_15 = db.Column(db.Integer)
    likes_16_24 = db.Column(db.Integer)
    likes_25_34 = db.Column(db.Integer)
    likes_35_44 = db.Column(db.Integer)
    likes_45_54 = db.Column(db.Integer)
    likes_55_64 = db.Column(db.Integer)
    likes_65_higher = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    gender = db.Column(db.String(1))

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

    # TODO: We need to know how long tokens remain valid, when do they expire?
    def generate_auth_token(self) -> str:
        serializer = Serializer(SECRET_KEY)

        return serializer.dumps({'id': self.id}).decode("utf-8")

    @staticmethod
    def verify_auth_token(token: str) -> Optional[object]:
        serializer = Serializer(SECRET_KEY)

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


# TODO: make list for per user likes.
# class Like(db.Model):
#    __tablename__ = 'likes'

#    id = db.Column(db.Integer, primary_key=True)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# NOTE: Other method currently used.
# class User_ES(DocType):
#     email = Text()
#     passhash = Text()
#     first_name = Text()
#     last_name = Text()
#     birthdate = Date()
#     gender = Text()
#     dataCollectionConsent = Boolean()
#     marketingConsent = Boolean()
#
#     def get_age(self):
#         current = date.today()
#         age = current.year - self.birthdate.year - (
#                     (current.month, current.day) < (self.birthdate.month, self.birthdate.day))
#         return age
#
#     def hash_password(self, password: str):
#         self.passhash = pbkdf2_sha256.hash(password)
#
#     def verify_password(self, password: str) -> bool:
#         return pbkdf2_sha256.verify(password, self.password_hash)
#
#     def generate_auth_token(self):
#         serializer = Serializer(SECRET_KEY)
#         return serializer.dumps({'id': self.meta.id}).decode("utf-8")
#
#     @staticmethod
#     def verify_auth_token(token: str) -> object:
#         serializer = Serializer(SECRET_KEY)
#
#         try:
#             data = serializer.loads(token)
#             print(data)
#         except SignatureExpired:
#             # Valid token, but expired.
#             return None
#
#         except BadSignature:
#             # Invalid token.
#             return None
#
#         return User.get(data["id"])
#
#     class Meta:
#         index = 'user'
#
#     def save(self, **kwargs):
#         return super(User, self).save(**kwargs)
#
#
# # Demographics model.
# class Demographic_ES(DocType):
#     count = Integer()
#     age_group = Text()
#     country = Text()
#
#
# class Demographics_ES(DocType):
#     keywords = Text()
#     data = Nested(Demographic_ES)
#
#     class Meta:
#         index = 'demographics'
