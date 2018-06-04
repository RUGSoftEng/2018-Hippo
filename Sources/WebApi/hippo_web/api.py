# Notes: Authentication implemented according to: https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
from datetime import datetime

from flask import *
import elasticsearch_dsl
import collections
from operator import itemgetter
from hippo_web.models import User
from hippo_web import app, auth, db, es

@auth.verify_password
def verify_password(email_or_token, password):
    # First try to authenticate by token, otherwise try with username/password.
    user = User.verify_auth_token(email_or_token)

    if not user:
        user = User.query.filter_by(email=email_or_token).first()

        if not user or not user.verify_password(password):
            return False

    g.user = user

    return True


@app.route('/api/tweet/<int:tweet_id>', methods=['GET'])
def get_tweet(tweet_id: int):
    pass


@app.route('/api/search/<terms>', methods=['GET'])
def search(terms):
    #terms = terms.split()
    result_tweets = []
    terms_list=terms.split()
    should = []
    for term in terms_list:
        #content->keyw
        query=elasticsearch_dsl.Q("match", content=term)
        should.append(query)


    q = elasticsearch_dsl.Q("bool", should=should, minimum_should_match=1)
    s = elasticsearch_dsl.Search(using=es, index="tweet").query(q)

    results = s[:100]
    
    #alternative: for field in hit ...
    for hit in results:
        result_tweets.append(hit._d_)
        
    return jsonify(result_tweets)

#generate (most general) synonym from terms/keyw
@app.route('/api/category/<terms>', methods=['GET'])
def pick_category(terms):
    #placeholder - compiled (manual) categories from tweets on ES
    options=["app","music", "pets","school","food","flowers","car","art","fashion","bar","hotel","friends","business"]
    categories = {}
    categ=terms.split()

    #get synonyms for tweet keywords from ES
    #analyzer=elasticsearch_dsl.analyzer('analyzer', tokenizer=elasticsearch_dsl.tokenizer('tokenizer', 'tweet'), filter=['lowercase'])
    #res=analyzer.execute()
    
    #synonyms/suggestions
    res=suggestions(terms)
    res=json.loads(res)
    categ.extend(res)

    #TODO - scoring
    for category in categ:
        for option in options:
            if category==option: 
                score=1
                if category not in categories:
                    categories[category]=score
                else:
                    categories[category]+=score

    #sort
    if len(categories) > 0:
        sortedCategories = sorted(categories.items(), key=itemgetter(1), reverse=True)
        category = sortedCategories[0][0]

    return category

#add individual tweet to a category idx
def add_to_category(tweet):
    #pick general categ
    category=pick_category(tweet)

    #create idx for categ if non existent
    if not(elasticsearch_dsl.Index.exists(category)):
        index=elasticsearch_dsl.Index(category)
        index.create()
    
    #add results to categ idx
    elasticsearch_dsl.DocType(tweet).init(index=category, using=es)
    return 0

#returns tweets in a category index
@app.route('/api/collection/<terms>', methods=['GET'])
def get_collection(category):
    result_tweets=[]
    
    #if term doesn't match existing try synonym of categ
    if not(elasticsearch_dsl.Index.exists(category)):
        category=pick_category(category)

    #get + return idx content
    s=elasticsearch_dsl.Search(using=es, index=category)
    results=s.execute()

    for hit in results:
        result_tweets.append(hit.content)
        
    return jsonify(result_tweets)


@app.route('/api/suggestions/<terms>', methods=['GET'])
def suggestions(terms):
    suggestions=[]
    terms_list=terms.split()
    should = []
    for term in terms_list:
        query=elasticsearch_dsl.Q("match", keywords=term)
        should.append(query)

    q=elasticsearch_dsl.Q("bool", should=should, minimum_should_match=1)
    s=elasticsearch_dsl.Search(using=es, index="tweet").query(q)

    results=s.execute()

    for hit in results:
        hit_keywords=hit.keywords
        for keyword in hit_keywords:
            if keyword not in terms_list and keyword not in suggestions:
                suggestions.append(keyword)

    return jsonify(suggestions)


# '{"email":"idiot@murica.usa", "password":"trump2016", "first_name":"Thierry", "last_name":"Baudet"}'
@app.route('/api/users', methods=['POST'])
def register():
    email: str = request.json.get('email')
    password: str = request.json.get('password')
    first_name: str = request.json.get('first_name')
    last_name: str = request.json.get('last_name')
    birthday: str = request.json.get('birthday')
    data_collection_consent: bool = request.json.get('birthday')
    marketing_consent: bool = request.json.get('birthday')

    if email is None or password is None or first_name is None or last_name is None:
        abort(400, description="Not enough valid information to finish the registration has been given.")

    if User.query.filter_by(email=email).first() is not None:
        abort(400, description="An user with this email account already exists.")

    user = User()

    user.email = email

    # TODO: Implement server side check for weak passwords, highly recommended to use zxcvbn.
    # Description: https://blogs.dropbox.com/tech/2012/04/zxcvbn-realistic-password-strength-estimation/
    # Python bindings: https://github.com/dwolfhub/zxcvbn-python).
    user.hash_password(password)

    user.first_name = first_name
    user.last_name = last_name

    if data_collection_consent is True:
        user.data_collection_consent = datetime.utcnow()

    if marketing_consent is True:
        user.marketing_consent = datetime.utcnow()

    db.session.add(user)
    db.session.commit()

    jsonify({'email': user.email}), 201, {'Location': url_for('get_user', id=user.id, _external=True)}


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})


@app.route('/api/user/profile')
@auth.login_required
def user():
    return jsonify({ 'data': 'Hello, %s!' % g.user.email })


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
