#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_usercontribs.py

    MediaWiki API Demos
    Demo of `Usercontribs` module: List user contributions.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "usercontribs",
    "ucuser": "Jimbo Wales"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
