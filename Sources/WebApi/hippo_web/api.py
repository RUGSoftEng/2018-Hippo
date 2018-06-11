# Notes: Authentication implemented according to: https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
from datetime import datetime
from flask_cors import CORS

from email_validator import validate_email, EmailNotValidError
from zxcvbn import zxcvbn

from flask import *
import elasticsearch_dsl

from collections import defaultdict
from operator import itemgetter
from hippo_web.models import User, get_age_group
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


@app.route('/api/view/<tweet_id>', methods=['POST'])
@auth.login_required
def view(tweet_id):
    # update nr views for tweet id
    q = {"script": {"inline": "views=views?views+=1:1"}, "query": {"match": {"id": tweet_id}}}
    es.update_by_query(body=q, index="tweets")

    # update views per age group for tweet id
    age_group = get_age_group(g.user.get_age())
    categ = "views_" + str(age_group)
    q = {"script": {"inline": "categ=categ?categ+=1:1"}, "query": {"match": {"id": tweet_id}}}
    es.update_by_query(body=q, index="tweets")


@app.route('/api/like/<tweet_id>', methods=['POST'])
@auth.login_required
def like(tweet_id):
    # update nr likes for tweet id
    q = {"script": {"inline": "age=age?age+=1:1"}, "query": {"match": {"id": tweet_id}}}
    es.update_by_query(body=q, index="tweets")

    # update likes per age group for tweet id
    age_group = get_age_group(g.user.get_age())
    categ = "likes_" + str(age_group)
    q = {"script": {"inline": "categ=categ?categ+=1:1"}, "query": {"match": {"id": tweet_id}}}
    es.update_by_query(body=q, index="tweets")


# likes/views-total, group likes/views- count for max groups
@app.route('/api/demographics/<tweet_id>', methods=['GET'])
@auth.login_required
def demographics(tweet_id):
    # get tweet
    q = elasticsearch_dsl.Q("bool", tweet_id=tweet_id, minimum_should_match=1)
    s = elasticsearch_dsl.Search(using=es, index="tweet").query(q)
    res = s.execute()
    tweet = res[0]._d_
    # determine group w most likes/views
    group_likes = get_group(tweet, "likes")
    group_views = get_group(tweet, "views")

    return jsonify(
        {'likes': tweet.likes, 'views': tweet.views, 'most_likes_group': group_likes[0], 'group_likes': group_likes[1],
         'most_views_group': group_views[0], 'group_views': group_views[1]})


# returns a tuple with (group name, value)
def get_group(tweet, field):
    if field is "views":
        views = [('age_26_24', tweet['views_age_16_24']), ('age_25_34', tweet['views_age_25_34']),
                 ('age_35_44', tweet['views_age_35_44']), ('age_55_64', tweet['views_age_55_64']),
                 ('age_65_plus', tweet['views_age_65_plus'])]
        return max(views, key=itemgetter(1))
    else:
        likes = [('age_26_24', tweet['likes_age_16_24']), ('age_25_34', tweet['likes_age_25_34']),
                 ('age_35_44', tweet['likes_age_35_44']), ('age_55_64', tweet['likes_age_55_64']),
                 ('age_65_plus', tweet['likes_age_65_plus'])]
        return max(likes, key=itemgetter(1))


def check_valid_email(email):
    try:
        validate_email(email)["email"]
    except EmailNotValidError as ex:
        return str(ex)

    return None


def check_password(email: str, password: str, first_name: str, last_name: str):
    password_results = zxcvbn(password, user_inputs=[email, first_name, last_name])

    # score is between 0 (very bad password) and 4 (very good password)
    if password_results["score"] < 2:
        return False

    return True


@app.route('/api/users', methods=['POST'])
def register():
    db.create_all()

    email: str = escape(request.json.get('email'))
    password: str = request.json.get('password')
    first_name: str = escape(request.json.get('first_name'))
    last_name: str = escape(request.json.get('last_name'))
    birthday: str = request.json.get('birthday')
    gender: int = request.json.get('gender')
    data_collection_consent: bool = request.json.get('data_collection_consent')
    marketing_consent: bool = request.json.get('marketing_consent')

    if None in (email, password, first_name, last_name):
        return jsonify(description="MISSING_INFO",
                       message="Not enough valid information to finish the registration has been given.")

    if check_valid_email(email) is not None:
        return jsonify(description="INVALID_EMAIL", message="The given email is invalid:")

    if User.query.filter_by(email=email).first():
        return jsonify(description="USER_ALREADY_EXISTS", message="A user with that email has already been registered.")

    if not check_password(email, password, first_name, last_name):
        return jsonify(description="WEAK_PASSWORD", message="The given password is insecure.")

    user = User()

    user.email = email
    user.hash_password(password)

    user.first_name = first_name
    user.last_name = last_name

    if birthday is not None:
        user.birthday = birthday

    if gender is not None:
        user.gender = gender

    # We need to save the date at which the user gave consent, GDPR.
    if data_collection_consent is True:
        user.data_collection_consent = datetime.utcnow()

    if marketing_consent is True:
        user.marketing_consent = datetime.utcnow()

    db.session.add(user)
    db.session.commit()

    return jsonify(description="success")


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
    return jsonify(token=token)


@app.route('/api/user/account', methods=['GET'])
@auth.login_required
def account():
    user = g.user
    return jsonify({'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name,
                    'data_collection_consent': user.data_collection_consent,
                    'marketing_consent': user.marketing_consent})


@app.route('/api/user/account', methods=['POST'])
@auth.login_required
def change_account():
    email: str = escape(request.json.get('email'))
    password: str = request.json.get('password')
    first_name: str = escape(request.json.get('first_name'))
    last_name: str = escape(request.json.get('last_name'))
    data_collection_consent: bool = request.json.get('data_collection_consent')
    marketing_consent: bool = request.json.get('marketing_consent')

    if None in (email, first_name, last_name):
        return jsonify(description="MISSING_INFO",
                       message="Not enough valid information to finish the registration has been given.")

    if check_valid_email(email) is not None:
        return jsonify(description="INVALID_EMAIL", message="The given email is invalid:")

    user = g.user

    if email != user.email and User.query.filter_by(email=email).first():
        return jsonify(description="USER_ALREADY_EXISTS", message="A user with that email has already been registered.")

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

    return jsonify(description="success")


@app.route('/api/user/delete', methods=['POST'])
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
