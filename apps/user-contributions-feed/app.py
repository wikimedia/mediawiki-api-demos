#!/usr/bin/python3

"""
    app.py

    MediaWiki Action API Code Samples

    User contributions feed app: Demp app that uses `list=usercontribs` module
    to fetch the top 50 edits made by a user

    MIT license
"""

from flask import Flask, render_template, request
import requests

WIKI_URL = "https://en.wikipedia.org"
API_ENDPOINT = WIKI_URL + "/w/api.php"

# App config.
DEBUG = True
APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'enter_your_secret_key'


@APP.route("/", methods=['GET'])
def index():
    """ Displays the index page accessible at '/'
    """
    username = request.args.get('username')

    if username is not None:
        data = get_user_contribs(username)
    else:
        data = None

    return render_template('user_contributions.html', data=data, \
        username=username, wikiurl=WIKI_URL)

def get_user_contribs(username):
    """ Fetch user contributions via MediaWiki API's Usercontribs module """
    params = {
        "action": "query",
        "format": "json",
        "list": "usercontribs",
        "ucprop": "user|ids|title|sizediff",
        "ucuser": username,
        "uclimit": 50
    }

    response = requests.get(url=API_ENDPOINT, params=params)
    data = response.json()
    return data['query']['usercontribs']

if __name__ == '__main__':
    APP.run()
