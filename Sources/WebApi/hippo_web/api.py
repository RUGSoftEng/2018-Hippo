from datetime import datetime
from typing import Optional

import dateutil
from flask_cors import CORS

from email_validator import validate_email, EmailNotValidError
from zxcvbn import zxcvbn

from flask import *
import elasticsearch_dsl

from collections import defaultdict
from operator import itemgetter
from hippo_web.models import User, get_age_group, Demographics
from hippo_web import app, auth, db, es

# Easier during development, remove and add cross-origin resource sharing in deployment.
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
    tweets = [dict(hit._d_) for hit in results]

    for tweet in tweets:
        del tweet["raw"]
        tweet["id"] = "https://twitter.com/statuses" + tweet["id"]

    return tweets


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

    collection_name = collection_mapping(terms.split())

    demographics = get_demographics(collection_name)

    results.append({'keywords': terms.split(), 'likes': demographics.likes, 'views': demographics.views, 'tweets': query_results})

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
    for i in range(min(len(keyword_frequencies), 5)):
        keyword = keyword_frequencies[-(i + 1)][0]
        new_terms = terms + " " + keyword
        new_results = search_by_keywords(terms + " " + keyword)

        collection_name = collection_mapping(terms.split())

        demographics = get_demographics(collection_name)

        results.append({'keywords': new_terms.split(), 'likes': demographics.likes, 'views': demographics.views, 'tweets': new_results})

    return jsonify(results)


# NOTE: Other method currently used.
# @app.route('/api/view/<tweet_id>', methods=['POST'])
# @auth.login_required
# def view(tweet_id):
#     # update nr views for tweet id
#     q = {"script": {"inline": "views=views?views+=1:1"}, "query": {"match": {"id": tweet_id}}}
#     es.update_by_query(body=q, index="tweets")
#
#     # update views per age group for tweet id
#     age_group = get_age_group(g.user.get_age())
#     categ = "views_" + str(age_group)
#     q = {"script": {"inline": "categ=categ?categ+=1:1"}, "query": {"match": {"id": tweet_id}}}
#     es.update_by_query(body=q, index="tweets")
#
#
# @app.route('/api/like/<tweet_id>', methods=['POST'])
# @auth.login_required
# def like(tweet_id):
#     # update nr likes for tweet id
#     q = {"script": {"inline": "age=age?age+=1:1"}, "query": {"match": {"id": tweet_id}}}
#     es.update_by_query(body=q, index="tweets")
#
#     # update likes per age group for tweet id
#     age_group = get_age_group(g.user.get_age())
#     categ = "likes_" + str(age_group)
#     q = {"script": {"inline": "categ=categ?categ+=1:1"}, "query": {"match": {"id": tweet_id}}}
#     es.update_by_query(body=q, index="tweets")
#
#
# # likes/views-total, group likes/views- count for max groups
# @app.route('/api/demographics/<tweet_id>', methods=['GET'])
# @auth.login_required
# def demographics(tweet_id):
#     # get tweet
#     q = elasticsearch_dsl.Q("bool", tweet_id=tweet_id, minimum_should_match=1)
#     s = elasticsearch_dsl.Search(using=es, index="tweet").query(q)
#     res = s.execute()
#     tweet = res[0]._d_
#     # determine group w most likes/views
#     group_likes = get_group(tweet, "likes")
#     group_views = get_group(tweet, "views")
#
#     return jsonify(
#         {'likes': tweet.likes, 'views': tweet.views, 'most_likes_group': group_likes[0], 'group_likes': group_likes[1],
#          'most_views_group': group_views[0], 'group_views': group_views[1]})
#
#
# # returns a tuple with (group name, value)
# def get_group(tweet, field):
#     if field is "views":
#         views = [('age_26_24', tweet['views_age_16_24']), ('age_25_34', tweet['views_age_25_34']),
#                  ('age_35_44', tweet['views_age_35_44']), ('age_55_64', tweet['views_age_55_64']),
#                  ('age_65_plus', tweet['views_age_65_plus'])]
#         return max(views, key=itemgetter(1))
#     else:
#         likes = [('age_26_24', tweet['likes_age_16_24']), ('age_25_34', tweet['likes_age_25_34']),
#                  ('age_35_44', tweet['likes_age_35_44']), ('age_55_64', tweet['likes_age_55_64']),
#                  ('age_65_plus', tweet['likes_age_65_plus'])]
#         return max(likes, key=itemgetter(1))


def collection_mapping(keywords: [str]) -> str:
    keywords = list(map(lambda x: x.lower(), keywords))

    keywords.sort()

    return ''.join(keywords)


def get_demographics(keywords: str) -> Demographics:
    demographics = Demographics.query.filter_by(keywords=keywords).first()

    if demographics is None:
        demographics = Demographics()

        demographics.keywords = keywords

        demographics.views = 0

        demographics.views_male = 0
        demographics.views_female = 0

        demographics.views_lower_15 = 0
        demographics.views_16_24 = 0
        demographics.views_25_34 = 0
        demographics.views_35_44 = 0
        demographics.views_45_54 = 0
        demographics.views_55_64 = 0
        demographics.views_65_higher = 0

        demographics.likes = 0

        demographics.likes_male = 0
        demographics.likes_female = 0

        demographics.likes_lower_15 = 0
        demographics.likes_16_24 = 0
        demographics.likes_25_34 = 0
        demographics.likes_35_44 = 0
        demographics.likes_45_54 = 0
        demographics.likes_55_64 = 0
        demographics.likes_65_higher = 0

        db.session.add(demographics)
        db.session.commit()

    return demographics


@app.route('/api/collections/<terms>/view', methods=['POST'])
@auth.login_required
def view_collection(terms: str):
    user = g.user

    collection_name = collection_mapping(terms.split())

    demographics = get_demographics(collection_name)

    demographics.views = demographics.views + 1

    if user.data_collection_consent is not None:
        if user.gender == "m":
            demographics.views_male = demographics.views_male + 1
        else:
            demographics.views_female = demographics.views_female + 1

        age_group = get_age_group(user.get_age())

        setattr(demographics, "views_" + age_group.name, getattr(demographics, "views_" + age_group.name) + 1)

    db.session.commit()

    return jsonify(description="success")


@app.route('/api/collections/<terms>/like', methods=['POST'])
@auth.login_required
def like_collection(terms: str):
    user = g.user

    collection_name = collection_mapping(terms.split())

    demographics = get_demographics(collection_name)

    demographics.likes = demographics.likes + 1

    if user.data_collection_consent is not None:
        if user.gender == "m":
            demographics.likes_male = demographics.likes_male + 1
        else:
            demographics.likes_female = demographics.likes_female + 1

        age_group = get_age_group(user.get_age())

        setattr(demographics, "likes_" + age_group.name, getattr(demographics, "likes_" + age_group.name) + 1)

    db.session.commit()

    return jsonify(description="success")


def check_valid_email(email: str) -> Optional[str]:
    try:
        validate_email(email)["email"]
    except EmailNotValidError as ex:
        return str(ex)

    return None


def check_password(email: str, password: str, first_name: str, last_name: str) -> Optional[str]:
    password_results = zxcvbn(password, user_inputs=[email, first_name, last_name])

    # NOTE: score is between 0 (very weak password) and 4 (very strong password).
    if password_results["score"] < 2:
        # Ensure that the user gets feedback, since there are no clear password requirements.
        suggestions = ""
        for suggestion in password_results["feedback"]["suggestions"]:
            suggestions += suggestion + "\n"

        return suggestions

    return None


# TODO: use external API to resolve IP location, return ISO 3166-1 (preferably alpha-3) code.
def get_location(ip_address: str) -> str:
    pass


@app.route('/api/users', methods=['POST'])
def register():
    # Ensure that the database tables exist.
    db.create_all()

    # Ensure all strings that can be displayed are escaped, to protect against cross-site scripting (XSS).
    email: str = escape(request.json.get('email'))
    password: str = request.json.get('password')
    first_name: str = escape(request.json.get('first_name'))
    last_name: str = escape(request.json.get('last_name'))
    birthday: str = request.json.get('birthday')
    gender: str = request.json.get('gender')
    data_collection_consent: bool = request.json.get('data_collection_consent')
    marketing_consent: bool = request.json.get('marketing_consent')

    if None in (email, password, first_name, last_name, gender):
        return jsonify(description="MISSING_INFO",
                       message="Not enough valid information to finish the registration has been given."), 400

    if check_valid_email(email) is not None:
        return jsonify(description="INVALID_EMAIL", message="The given email is invalid."), 400

    if User.query.filter_by(email=email).first():
        return jsonify(description="USER_ALREADY_EXISTS",
                       message="A user with that email has already been registered."), 400

    result = check_password(email, password, first_name, last_name)

    if result is not None:
        return jsonify(description="WEAK_PASSWORD", message="The given password is insecure. \n" + result), 400

    user = User()

    user.email = email
    user.hash_password(password)

    user.first_name = first_name
    user.last_name = last_name
    user.gender = gender

    # It's possible to select non-existing dates in date selector, thus, we need to filter those out.
    if birthday is not None:
        try:
            user.birthday = dateutil.parser.parse(birthday)
        except ValueError:
            return jsonify(description="INVALID_DATE", message="The given date is invalid."), 400

    # We need to save the date at which the user gave consent, GDPR.
    if data_collection_consent is True:
        user.data_collection_consent = datetime.utcnow()

        # user.location_country = get_location(request.remote_addr)

    if marketing_consent is True:
        user.marketing_consent = datetime.utcnow()

    db.session.add(user)
    db.session.commit()

    return jsonify(description="success")


# Notes: Authentication implemented according to: https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
@auth.verify_password
def verify_password(email_or_token: str, password: str) -> bool:
    # First try to authenticate by token, otherwise try with username/password.

    # Migrate an issue in Axios, authentication headers not send correctly in POST requests.
    if email_or_token == "" and request.json is not None and "username" in request.json.get("auth"):
        email_or_token = request.json.get('auth')['username']

    user = User.verify_auth_token(email_or_token)

    if not user:
        user = User.query.filter_by(email=email_or_token).first()

        if not user:
            return False

        # Had an issue with an empty hash, only in development.
        if not user.verify_password(password):
            return False

    g.user = user

    return True


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify(token=token)


@app.route('/api/user/account', methods=['GET'])
@auth.login_required
def account():
    user = g.user

    if user.data_collection_consent is None:
        data_consent = False
    else:
        data_consent = True

    if user.marketing_consent is None:
        marketing = False
    else:
        marketing = True

    return jsonify({'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name,
                    'gender': user.gender, 'data_collection_consent': data_consent,
                    'marketing_consent': marketing})


@app.route('/api/user/account', methods=['POST'])
@auth.login_required
def change_account():
    # Ensure all strings that can be displayed are escaped, to protect against cross-site scripting (XSS).
    email: str = escape(request.json.get('email'))
    password: str = request.json.get('password')
    first_name: str = escape(request.json.get('first_name'))
    last_name: str = escape(request.json.get('last_name'))
    gender: str = request.json.get('gender')
    data_collection_consent: bool = request.json.get('data_collection_consent')
    marketing_consent: bool = request.json.get('marketing_consent')

    if None in (email, first_name, last_name, gender):
        return jsonify(description="MISSING_INFO",
                       message="Not enough valid information to finish the registration has been given."), 400

    if check_valid_email(email) is not None:
        return jsonify(description="INVALID_EMAIL", message="The given email is invalid."), 400

    user = g.user

    # Make sure only to run the tests when these values have changed.
    if email != user.email and User.query.filter_by(email=email).first():
        return jsonify(description="USER_ALREADY_EXISTS",
                       message="A user with that email has already been registered."), 400

    if password != "":
        result = check_password(email, password, first_name, last_name)
        if result is not None:
            return jsonify(description="WEAK_PASSWORD", message="The given password is insecure. \n" + result), 400

        user.hash_password(password)

    user.email = email

    user.first_name = first_name
    user.last_name = last_name
    user.gender = gender

    # We need to save the date at which the user gave consent, GDPR.
    if data_collection_consent is True and user.data_collection_consent is not True:
        user.data_collection_consent = datetime.utcnow()

    if marketing_consent is True and user.marketing_consent is not True:
        user.marketing_consent = datetime.utcnow()

    db.session.commit()

    return jsonify(description="success")


@app.route('/api/user/account', methods=['DELETE'])
@auth.login_required
def delete_user():
    db.session.delete(g.user)
    db.session.commit()

    return jsonify(description="success")


# TODO: Serialise User data model in json, zip it and send it to the user. (GDPR compliance)
@app.route('/api/user/data', methods=['GET'])
@auth.login_required
def get_personal_data():
    pass
