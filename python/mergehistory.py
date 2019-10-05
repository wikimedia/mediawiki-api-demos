#!/usr/bin/python3

"""
    mergehistory.py

    MediaWiki API Demos
    Demo of `mergehistory` module: Merge the entire history of Oldpage to Newpage

"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: Send a POST request to log in.
PARAMS_2 = {
    "action": "login",
    "lgname": "user_name",
    "lgpassword": "password",
    "format": "json",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)
DATA = R.json()

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Send a POST request to merge history of Oldpage to Newpage
PARAMS_4 = {
	"action":"mergehistory",
	"from":"Oldpage",
	"to":"Newpage",
	"format":"json",
	"reason":"Reason"
	
}

payload = { "token":CSRF_TOKEN }
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", URL, data=payload, headers=headers, params=PARAMS_4)

print(response.text)