# Notes: Authentication implemented according to: https://blog.miguelgrinberg.com/post/restful-authentication-with-flask

from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

from elasticsearch import Elasticsearch

from hippo.models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

app = Flask(__name__)
app.secret_key = ""
auth = HTTPBasicAuth()

es = Elasticsearch()


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
def tweet(tweet_id: int):
    pass


# TODO: Finish function.
@app.route('/api/search/<terms>', methods=['GET'])
def search(terms):
    terms = terms.split()

    results = [str]

    for term in terms:
        results = es.search(index="hippo", body={"query": {"match": {"keywords": term}}})
        for hit in results['hits']['hits']:
            result = hit['_source']
            result['id'] = hit['_id']
            if result not in results:
                results.extend(result)

    return jsonify(results)


# '{"email":"idiot@murica.usa", "password":"trump2016", "first_name":"Thierry", "last_name":"Baudet"}'
@app.route('/api/users', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')

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

    db.session.add(user)
    db.session.commit()

    jsonify({'email': user.email}), 201, {'Location': url_for('get_user', id=user.id, _external=True)}


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})


@app.route('/user/profile')
@auth.login_required
def user():
    return jsonify({ 'data': 'Hello, %s!' % g.user.email })


# TODO: Is redundant now due to basic/token authentication?
@app.route('/login', methods=['POST'])
def login():
    pass


# TODO: Is redundant now due to basic/token authentication?
@app.route('/logout', methods=['GET'])
def logout():
    pass


if __name__ == '__main__':
    app.run(debug=True)
