#!/usr/bin/python3

"""
    validatepassword.py

    MediaWiki Action API Code Samples
    Demo of `validate password` module: Validate a password against the wiki's password policies.
    MIT license
"""
# Validate a password for a current user.

import requests

url = "https://en.wikipedia.org/w/api.php"

S = requests.Session()

PARAMS = {
    "action": "validatepassword",
    "format": "json",
    "password": "your_password",
}

R = S.post(url, data=PARAMS)
DATA = R.json()

print(DATA)

# Validate a password for creating a new user.

import requests

S = requests.Session()

url = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "validatepassword",
    "format": "json",
    "password": "my_password",
    "user": "new_user"
}

R = S.post(url, data=PARAMS)
DATA = R.json()

print(DATA)
