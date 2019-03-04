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

URL = "https://en.wikipedia.org/w/api.php"
# To change a page's protection level, a CSRF token is required. 
# Step 1: Retrieve a CSRF token using GET request
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "csrf",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 2: Changing 'edit protection level' of a page using POST request
PARAMS = {
    "title": "Main Page",
    "edit": "autoconfirmed",
    "move": "sysop",
    "expiry": "infinite",
    "token": CSRF_TOKEN,
    "action": "protect"
}

R = S.post(url=URL, params=PARAMS)
