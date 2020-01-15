#This file is auto-generated. See modules.json and autogenerator.py for details

#!/usr/bin/python3

"""
    file_repo_info.py

    MediaWiki API Demos
    Demo of `Filerepoinfo` module: Get information about file repositories.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "meta": "filerepoinfo",
    "friprop": "url|name|displayname",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)
