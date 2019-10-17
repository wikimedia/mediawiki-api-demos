"""
    filearchive.py

    MediaWiki API Demos
    Demo of `Filearchive` module: Enumerate all deleted files from filearchive table sequentially.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "filearchive"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

FILESARCHIVED = DATA["query"]["filearchive"]
for f in FILESARCHIVED:
  print(f["name"])


