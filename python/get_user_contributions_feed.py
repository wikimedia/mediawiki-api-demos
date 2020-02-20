#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    get_user_contributions_feed.py

    MediaWiki API Demos
    Demo of `Feedcontributions` module: Show contributions of a user as an RSS feed.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "feedcontributions",
    "user": "Jimbo Wales",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.content

print(DATA)
