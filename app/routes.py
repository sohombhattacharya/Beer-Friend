from app import app
from flask import jsonify, request
from .constants import *
import requests

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'text': "Hello World"})

@app.route('/search/beers', methods = {'POST'})
def searchBeers():
    print (request.get_json())
    searchStr = '%s/search?q=%s&type=beer&key=%s' % (API_URL, request.get_json()['q'], API_KEY)
    print (searchStr)
    r = requests.get(searchStr)
    if r.status_code == 200:
        return jsonify({"status": "success", "result": r.json()})
    else:
        return jsonify({"status": "failure", "error code": r.status_code})

