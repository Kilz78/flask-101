# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Helfefelo World!"
@app.route('/api/v1/products')
def products():
    #test2=[1,2,3]
    test = {
            1: { 'id': 1, 'name': 'Skello' },
            2: { 'id': 2, 'name': 'Socialive.tv' },
           }
    return jsonify(list(test.values()))

