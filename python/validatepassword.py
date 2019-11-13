#!/usr/bin/python3

"""
    validatepassword.py

    MediaWiki Action API Code Samples
    Demo of `Validatepassword` module: Validate a password against the wiki's password policies.
    MIT license
"""

import requests

URL = "https://en.wikipedia.org/w/api.php"

S = requests.Session()

PARAMS = {
    "action": "validatepassword",
    "format": "json",
    "password": "your_password",
}

R = S.post(URL, data=PARAMS)
DATA = R.json()

print(DATA)
