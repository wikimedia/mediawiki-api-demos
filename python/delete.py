#!/usr/bin/python3

"""
    delete.py

    MediaWiki Action API Code Samples
    Demo of `Delete` module: post request to delete a page
    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

# Step1: Retrieve login token
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step2: Send a post request to login. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    'action':"login",
    'lgname':"your_bot_username",
    'lgpassword':"your_bot_password",
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)

# Step 3: When logged in, retrieve a CSRF token
PARAMS_2 = {
    'action':"query",
    'meta':"tokens",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: Send a post request to delete a page
PARAMS_3 = {
    'action':"delete",
    'title':"enter_a_page_title",
    'token':CSRF_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()

print(DATA)
