 #!/usr/bin/python3

"""
    token_get.py

    MediaWiki Action API Code Samples
    Demo of `Token` module: Fetch token of type `csrf`
    MIT license
"""

import requests

S = requests.Session()

URL = "https://mediawiki.org/w/api.php"

PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"csrf",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

print(CSRF_TOKEN)


# after getting the csrf toke above, we then
# Use the post request to delete a page and moving it . 

PARAMS_1 = {
          "action": "delete",
          "title": "Main%20Page",
          "token": CSRF_TOKEN,
          "reason":"Preparing%20for%20move",
          "format": "json"
   
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)