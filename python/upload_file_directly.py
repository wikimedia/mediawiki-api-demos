"""
    upload_file_directly.py

    MediaWiki API Demos
    Demo of `Upload` module: Sending post request to upload a file directly

    MIT license
"""

import requests

S = requests.Session()
URL = "https://test.wikipedia.org/w/api.php"
FILE_PATH = 'f.jpg'

# Step 1: Retrieve a login token
PARAMS_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]

# Step 2: Send a post request to login. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_2 = {
    "action": "login",
    "lgname": "bot_username",
    "lgpassword": "bot_password",
    "format": "json",
    "lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)

# Step 3: Obtain a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta":"tokens",
    "format":"json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Post request to upload a file directly
PARAMS_4 = {
    "action": "upload",
    "filename": "file_1.jpg",
    "format": "json",
    "token": CSRF_TOKEN,
    "ignorewarnings": 1
}

FILE = {'file':('file_1.jpg', open(FILE_PATH, 'rb'), 'multipart/form-data')}

R = S.post(URL, files=FILE, data=PARAMS_4)
DATA = R.json()
print(DATA)
