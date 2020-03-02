#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    userinfo.py

    MediaWiki API Demos
    Demo of `Userinfo` module: Get general user info and user rights

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "meta": "userinfo",
    "uiprop": "rights",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
