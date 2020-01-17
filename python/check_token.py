#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    check_token.py

    MediaWiki API Demos
    Demo of `Checktoken` module: Get request to check a CSRF token.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "checktoken",
    "token": "123ABC",
    "type": "csrf",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
