#This file is partly auto-generated

#!/usr/bin/python3

"""
    get_users.py

    MediaWiki Action API Code Samples
    Demo of `Users` module: Get information about several users: 
    [[1.2.3.4]], [[Catrope]], [[Vandal01]], and [[Bob]]

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "users",
    "ususers": "1.2.3.4|Catrope|Vandal01|Bob",
    "usprop": "blockinfo|groups|editcount|registration|emailable|gender"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
