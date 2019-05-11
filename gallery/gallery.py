#!/usr/bin/python3

"""
    gallery.py

    MediaWiki apps gallery: a collection of demo apps built using the
    MediaWiki Action APIs.

    MIT license
"""

import json
from flask import Flask, render_template
import requests


APP = Flask(__name__)
SESSION = requests.Session()


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    with open('./apps.json', 'r') as file:
        data = file.read()
        apps = json.loads(data)

    return render_template('apps.html', apps=apps)


if __name__ == '__main__':
    APP.run(debug=True)
