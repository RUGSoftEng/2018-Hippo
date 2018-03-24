from flask import *
import json
import sys

placeholder=[{'tweet-id': "ABC", 'content': "Hello world!", 'keywords': ["hello","world"]}]

app = Flask(__name__)

@app.route('/')
def start():
    return "Hippo start page"

@app.route('/search/<term>', methods=['GET'])
def search(term):
    res = [res for res in placeholder if res['keywords'].count(term)>=1]
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)