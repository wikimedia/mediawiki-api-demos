#!/usr/bin/python3

"""
    MediaWiki Action API Code Samples
    Demo app of `API:Usercontribs`
    This will show Top 50 edits made by user

    MIT license
"""

from flask import Flask, render_template, request
import requests

WIKI_URL = "https://en.wikipedia.org"
API_ENDPOINT = WIKI_URL + "/w/api.php"

# App config.
DEBUG = True
app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter_your_secret_key'


@app.route("/", methods=['GET'])
def index():
    # Get the username from request arguments
    username = request.args.get('username')

    # Check whether the username present in request or not
    if username is not None:
        data = get_user_contribs(username)
    else:
        data = None

    # render the template
    return render_template('user_contributions.html', data=data, username=username, wikiurl=WIKI_URL)


def get_user_contribs(username):
    """ Fetch user contributions via `usercontribs` module """

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
    app.run()
