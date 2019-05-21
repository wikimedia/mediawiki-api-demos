#!/usr/bin/python3

"""
    import_interwiki.py

    MediaWiki Action API Code Samples
    Demo of `Import` module: Import a page from another wiki by
    specifying its title
    MIT license
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

# Step 2: Send a post request to log in using the clientlogin method.
# import rights can't be granted using Special:BotPasswords
# hence using bot passwords may not work.
# See https://www.mediawiki.org/wiki/API:Login for more
# information on log in methods.
PARAMS_2 = {
    "action":"clientlogin",
    "username":"username",
    "password":"password",
    'loginreturnurl': 'http://127.0.0.1:5000/',
    "format":"json",
    "logintoken":LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: Post request to import page from another wiki
PARAMS_4 = {
    "action": "import",
    "format": "json",
    "interwikisource": "meta",
    "interwikipage": "Help:ParserFunctions",
    "fullhistory":"true",
    "namespace":"100",
    "token": CSRF_TOKEN
}

R = S.post(url=URL, data=PARAMS_4)
DATA = R.json()

print(DATA)
