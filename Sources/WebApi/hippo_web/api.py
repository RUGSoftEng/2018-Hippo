# Notes: Authentication implemented according to: https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
from datetime import datetime
from flask_cors import CORS

from email_validator import validate_email, EmailNotValidError
from zxcvbn import zxcvbn

from flask import *
import elasticsearch_dsl

from collections import defaultdict
from operator import itemgetter
from hippo_web.models import User
from hippo_web import app, auth, db, es

CORS(app)


# hardcoded keywords that need to be excluded.
excluded_keywords = {"https", "i"}


def search_by_keywords(terms):
    # create the query
    terms_list = terms.split()
    should = []
    for term in terms_list:
        query = elasticsearch_dsl.Q("match", keywords=term)
        should.append(query)

    # perform the query
    q = elasticsearch_dsl.Q("bool", should=should, minimum_should_match=1)
    s = elasticsearch_dsl.Search(using=es, index="tweet").query(q)

    # return the first 250 hits
    results = s[:250]

    return [hit._d_ for hit in results]


@app.route('/api/search/<terms>', methods=['GET'])
@auth.login_required
def search(terms):
    return jsonify(search_by_keywords(terms))


@app.route('/api/search_category/<terms>')
@auth.login_required
def search_category(terms):
    results = []

    # query and add the terms themselves
    query_results = search_by_keywords(terms)
    results.append({'keywords': terms.split(), 'tweets': query_results})

    # make a keyword frequency dictionary
    keyword_frequencies = defaultdict(int)
    for hit in query_results:
        keywords = hit["keywords"]

        for keyword in keywords:
            # make the keyword lowercase, to remove duplicates that differ in case
            keyword = keyword.lower()

            # exclude searched terms and hardcoded exclusions
            if keyword not in excluded_keywords and keyword not in terms:
                keyword_frequencies[keyword] += 1

    # sort the keywords by frequency
    keyword_frequencies = dict(keyword_frequencies)
    keyword_frequencies = sorted(keyword_frequencies.items(), key=itemgetter(1))

    # add the 4 most common keywords
    for i in range(0, 5):
        keyword = keyword_frequencies[-(i + 1)][0]
        new_terms = terms + " " + keyword
        new_results = search_by_keywords(terms + " " + keyword)
        results.append({'keywords': new_terms.split(), 'tweets': new_results})

    return jsonify(results)


@app.route('/api/view', methods=['POST'])
def view():
    pass


@app.route('/api/like', methods=['POST'])
def like():
    pass

  
def check_valid_email(email: str) -> str:
    try:
        return validate_email(email)["email"]
    except EmailNotValidError as ex:
        abort(400, jsonify(description="INVALID_EMAIL", message="The given email is invalid:" + str(ex)))


def check_password(email: str, password: str, first_name: str, last_name: str):
    password_results = zxcvbn(password, user_inputs=[email, first_name, last_name])

    # score is between 0 (very bad password) and 4 (very good password)
    if password_results["score"] < 2:
        abort(400, jsonify(description="WEAK_PASSWORD", message="The given password is insecure."))


@app.route('/api/users', methods=['POST'])
def register():
    db.create_all()

    email: str = request.json.get('email')
    password: str = request.json.get('password')
    first_name: str = request.json.get('first_name')
    last_name: str = request.json.get('last_name')
    birthday: str = request.json.get('birthday')
    data_collection_consent: bool = request.json.get('data_collection_consent')
    marketing_consent: bool = request.json.get('marketing_consent')

    if None in (email, password, first_name, last_name):
        abort(400, jsonify(description="MISSING_INFO", message="Not enough valid information to finish the registration has been given."))

    check_valid_email(email)

    if User.query.filter_by(email=email).first():
        abort(400, jsonify(description="USER_ALREADY_EXISTS", message="A user with that email has already been registered."))

    check_password(email, password, first_name, last_name)

    user = User()

    user.email = email
    user.hash_password(password)

    user.first_name = first_name
    user.last_name = last_name

    if birthday is not None:
        user.birthday = birthday

    # We need to save the date at which the user gave consent, GDPR.
    if data_collection_consent is True:
        user.data_collection_consent = datetime.utcnow()

    if marketing_consent is True:
        user.marketing_consent = datetime.utcnow()

    db.session.add(user)
    db.session.commit()

    return jsonify({'email': email})


@auth.verify_password
def verify_password(email_or_token, password):
    # First try to authenticate by token, otherwise try with username/password.

    # Migrate an issue in Axios.
    if email_or_token == "":
        email_or_token = request.json.get('auth')['username']

    user = User.verify_auth_token(email_or_token)

    if not user:
        user = User.query.filter_by(email=email_or_token).first()

        if not user or not user.verify_password(password):
            return False

    g.user = user

    return True


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token})


@app.route('/api/user/account', methods=['GET'])
@auth.login_required
def account():
    user = g.user
    return jsonify({'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name, 'data_collection_consent': user.data_collection_consent, 'marketing_consent': user.marketing_consent})


@app.route('/api/user/account1', methods=['POST'])
@auth.login_required
def change_account():
    email: str = request.json.get('email')
    password: str = request.json.get('password')
    first_name: str = request.json.get('first_name')
    last_name: str = request.json.get('last_name')
    data_collection_consent: bool = request.json.get('data_collection_consent')
    marketing_consent: bool = request.json.get('marketing_consent')

    if None in (email, first_name, last_name):
        abort(400, jsonify(description="MISSING_INFO",
                           message="Not enough valid information to finish the registration has been given."))

    check_valid_email(email)
    user = g.user

    if email != user.email and User.query.filter_by(email=email).first():
        abort(400,
              jsonify(description="USER_ALREADY_EXISTS", message="A user with that email has already been registered."))

    if password != "":
        check_password(email, password, first_name, last_name)
        user.hash_password(password)

    user.email = email

    user.first_name = first_name
    user.last_name = last_name

    # We need to save the date at which the user gave consent, GDPR.
    if data_collection_consent is True and user.data_collection_consent is not True:
        user.data_collection_consent = datetime.utcnow()

    if marketing_consent is True and user.marketing_consent is not True:
        user.marketing_consent = datetime.utcnow()

    db.session.commit()

    return jsonify({'result': 'success'})


# TODO: Implement functions for GDPR compliance for production.
@app.route('/api/user/delete', methods=['POST'])
@auth.login_required
def delete_user():
    db.session.delete(g.user)
    db.session.commit()

    return 200


# TODO: Serialise User data model in json, zip it and send it to the user. (GDPR compliance)
@app.route('/api/user/data', methods=['GET'])
def get_personal_data():
    pass
