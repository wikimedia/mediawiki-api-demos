#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    protect.py

    MediaWiki Action API Code Samples
    Demo of `Protect` module: Demo to change the edit protection level of a given page.

    MIT License
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

# Step 2: Send a post request to login. Use of main account for login 
# is not supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & 
# lgpassword
PARAMS_2 = {
    "action": "login",
    "lgname": "bot_user_name",
    "lgpassword": "bot_password",
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_2)

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "type": "csrf",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Changing 'edit protection level' of a page using POST request
PARAMS_4 = {
    "title": "Main Page",
    "edit": "autoconfirmed",
    "move": "sysop",
    "expiry": "infinite",
    "token": CSRF_TOKEN,
    "action": "protect"
}

R = S.post(URL, data=PARAMS_4)
