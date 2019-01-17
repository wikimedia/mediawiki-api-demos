#!/usr/bin/python3

"""
    userrights.py

    MediaWiki Action API Code Samples
    Demo of `Userrights` module: Add and remove user rights by
    changing the user's group membership.
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

LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

# Step 2: Send a post request to log in. See
# https://www.mediawiki.org/wiki/Manual:Bot_passwords
# for a special note on logging in using a simplified
# interface when accessing wikis via an application,
# rather than the GUI
PARAMS_2 = {
    "action": "login",
    "lgname": "username",
    "lgpassword": "password",
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_2)

# Step 3: Obtain a Userrights token
PARAMS_3 = {
    "action": "query",
    "format": "json",
    "meta": "tokens",
    "type": "userrights"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

USERRIGHTS_TOKEN = DATA["query"]["tokens"]["userrightstoken"]

# Step 4: Request to add or remove a user from a group
PARAMS_4 = {
    "action": "userrights",
    "format": "json",
    "user": "Bob",
    "add": "sysop",
    "remove": "bureaucrat",
    "reason": "OOPS! added Bob to the wrong group",
    "token": USERRIGHTS_TOKEN
}

R = S.post(URL, data=PARAMS_4)
DATA = R.json()

print(DATA)
