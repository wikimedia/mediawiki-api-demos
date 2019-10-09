#!/usr/bin/python3

"""
    mergehistory.py

    MediaWiki API Demos
    Demo of `mergehistory` module: Merge the page revisions of Oldpage
    dating up to 2015-12-31T04:37:41Z into Newpage

"""
import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: Send a post request to log in using the clientlogin method.
# import rights can't be granted using Special:BotPasswords
# hence using bot passwords may not work.
# See https://www.mediawiki.org/wiki/API:Login for more
# information on log in methods.
PARAMS_2 = {
    "action": "login",
    "lgname": "user_name",
    "lgpassword": "password",
    "format": "json",
    "loginreturnurl": "http://127.0.0.1:5000/",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)
DATA = R.json()

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Send a POST request  to merge the page revisions
#  of Oldpage dating up to 2015-12-31T04:37:41Z into Newpage
PARAMS_4 = {
    "action":"mergehistory",
    "from":"Oldpage",
    "to":"Newpage",
    "format":"json",
    "timestamp":"2015-12-31T04:37:41Z",
    "reason":"Reason",
    "token" : CSRF_TOKEN
    }

R = S.post(URL, data=PARAMS_4)
DATA = R.text

print(DATA)

# To merge entire history of Oldpage to Newpage,
# remove the "timestamp" parameter in step 4
