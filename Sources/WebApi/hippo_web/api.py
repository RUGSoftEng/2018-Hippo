# Notes: Authentication implemented according to: https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
from datetime import datetime

from flask import *
import elasticsearch_dsl

from collections import defaultdict
from operator import itemgetter
from hippo_web.models import User
from hippo_web import app, auth, db, es

excluded_keywords = {"https", "i"}

def search_by_keywords(terms):
    terms_list = terms.split()
    should = []
    for term in terms_list:
        query = elasticsearch_dsl.Q("match", keywords=term)
        should.append(query)

    q = elasticsearch_dsl.Q("bool", should=should, minimum_should_match=1)
    s = elasticsearch_dsl.Search(using=es, index="tweet").query(q)

    results = s[:250]

    return [hit._d_ for hit in results]


@app.route('/api/search/<terms>', methods=['GET'])
def search(terms):
    return jsonify(search_by_keywords(terms))


@app.route('/api/search_category/<terms>')
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
            if keyword not in excluded_keywords and keyword not in terms:
                keyword_frequencies[keyword] += 1

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


#@app.route('', methods=['POST'])
def like():
    pass

def get_user(user_email):
    if not es.indices.exists(index="user"):
        es.indices.create(index="user")
        return None

    must = elasticsearch_dsl.Q('match', email=user_email)
    q = elasticsearch_dsl.Q('bool', should=[must])
    s = elasticsearch_dsl.Search(using=es, index="user").query(q)
    results = s.execute()
    
    for hit in results:
        if (hit._d_['email'] == user_email):
            return User.get(hit.meta.id)
    
    return None
    
@app.route('/api/users', methods=['POST'])
def register():
    email: str = request.json.get('email')
    password: str = request.json.get('password')
    first_name: str = request.json.get('first_name')
    last_name: str = request.json.get('last_name')
    birthday: str = request.json.get('birthday')
    data_collection_consent: bool = request.json.get('data_collection_consent')
    marketing_consent: bool = request.json.get('marketing_consent')

    if None in (email, password, first_name, last_name):
        abort(400, description="Not enough valid information to finish the registration has been given.")

    if (get_user(email)):
        abort(400, description="A user with that email has already been registered.")
    
    user = User()
    user.email = email
    user.hash_password(password)
    user.first_name = first_name
    user.last_name = last_name
    
    if birthday != None:
        user.birthday = birthday
    
    if data_collection_consent != None:
        user.data_collection_consent = data_collection_consent
    
    if marketing_consent != None:
        user.marketing_consent = marketing_consent
    
    user.save()
    
    return jsonify({'email': email}), 201

import inspect    

@auth.verify_password
def verify_password(email_or_token, password):
    # First try to authenticate by token, otherwise try with username/password.
    user = User.verify_auth_token(email_or_token)

    if not user:
        user = get_user(email_or_token)
        if not user or not user.verify_password(password):
            return False

    g.user = user
    return True

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token})

@app.route('/api/user/profile')
@auth.login_required
def user():
    return jsonify({'data': 'Hello, %s!' % g.user.email})

# TODO: Is redundant now due to basic/token authentication?
@app.route('/api/login', methods=['POST'])
def login():
    pass

# TODO: Is redundant now due to basic/token authentication?
@app.route('/api/logout', methods=['GET'])
def logout():
    pass

# TODO: Implement functions for GDPR compliance for production.
@app.route('/api/user/delete', methods=['POST'])
@auth.login_required
def delete_user():
    db.session.delete(g.user)
    db.session.commit()

# TODO: Serialise User data model in json, zip it and send it to the user. (GDPR compliance)
@app.route('/api/user/data', methods=['GET'])
def get_personal_data():
    pass
