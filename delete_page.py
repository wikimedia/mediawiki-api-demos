#!/usr/bin/python3

"""
    delete_page.py

    MediaWiki Action API Code Samples
    'Delete' module:
    1st Step;Fetching token of type `csrf`
    2nd Step;Used fetched 'csrf_token' to delete a page
    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"csrf",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

print(CSRF_TOKEN)

#Use the csrf token in a post request to delete a page

PARAMS_1 = {"action":"delete", "title":"Rabosot", "token":CSRF_TOKEN, "format":"json"}
R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)
