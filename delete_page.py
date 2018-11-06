#!/usr/bin/python3

"""
    delete_page.py

    MediaWiki Action API Code Samples
    Send a Post request to delete a page on wikipedia.org
    (Note that you will actually need adminstrative rights to perform this action, thanks!)
    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

#1st Step;Fetching token of type `csrf`
PARAMS_0 = {
       "action":"query", 
       "meta":"tokens", 
       "type":"csrf", 
       "format":"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

print(CSRF_TOKEN)

#2nd Step;Used fetched 'csrf_token' to delete a page in a post request

PARAMS_1 = {
        "action":"delete", 
        "title":"Rabosot", 
        "token":CSRF_TOKEN, 
        "format":"json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)
