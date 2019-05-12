#!/usr/bin/python3

"""
    send_email.py

    MediaWiki API Demos
    Demo of `Emailuser` module: sending POST request to send email to wiki user

    MIT license
"""

import requests

S = requests.Session()

URL = "https://test.wikipedia.org/w/api.php"

# Step 1: GET Request to fetch login token
PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2: POST Request to log in. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    "action": "login",
    "lgname": "your_bot_username",
    "lgpassword": "your_bot_password",
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_1)

# Step 3: GET request to fetch Email token
PARAMS_2 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

EMAIL_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: POST request to send an email
PARAMS_3 = {
    "action": "emailuser",
    "target": "Test",
    "subject": "Hi",
    "text": "Just wanted to say hi",
    "token": EMAIL_TOKEN,
    "format": "json"
}

R = S.post(URL, data=PARAMS_3)
DATA = R.text

print(DATA)
