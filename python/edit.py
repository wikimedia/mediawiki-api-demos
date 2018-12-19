#!/usr/bin/python3

"""
    edit.py

    MediaWiki Action API Code Samples
    Demo of `Edit` module: POST request to edit a page
    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

# Step 1: GET Request to fetch login token
PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: POST Request to log in
PARAMS_1 = {
    "action":"login",
    "lgname":"bot's_user_name",
    "lgpassword":"bot's_password",
    "lgtoken":LOGIN_TOKEN,
    "format":"json"
}

R = S.post(URL, data=PARAMS_1)

# Step 3: GET request to fetch CSRF token
PARAMS_2 = {
    "action":"query",
    "meta":"tokens",
    "format":"json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: POST request to edit a page
PARAMS_3 = {
    "action":"edit",
    "title":"Sandbox",
    "token":CSRF_TOKEN,
    "format":"json",
    "appendtext": "Hello" 
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()

print(DATA)
