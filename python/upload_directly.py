"""
    upload_directly.py

    MediaWiki Action API Code Samples
    Demo of `Upload` module: Sending post request to upload a file directly

    MIT license
"""

import requests
import time

S = requests.Session()
URL = "https://www.mediawiki.org/w/api.php"

#Step 1: Retrieve a login token
PARAMS_1 = {
	"action":"query",
	"meta":"tokens",
	"type":"login",
	"format":"json"
}

R = S.get(url=URL, params=PARAMS_1)
DATA = R.json()

LOGIN_TOKEN = DATA["query"]["tokens"]["logintoken"]


# Step2: Send a post request to login. Use of main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_2 = {
	"action":"login",
	"lgname": "bot_username",
	"lgpassword":"bot_password",
	"format":"json",
	"lgtoken": LOGIN_TOKEN
}

R = S.post(URL, data=PARAMS_2)

PARAMS_3 = {
	"action": "query",
	"meta":"tokens",
	"format":"json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()

CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

#Step 4: Post request to upload a file directly
PARAMS_4 = {
    "action": "upload",
    "filename": "file_1.jpg",
    "file": ('f.jpg',open('f.jpg','rb'),'multipart/form-data'),
    "format": "json",
    "token": CSRF_TOKEN,
    "ignorewarnings": 1
}
file = {'file':('f.jpg',open('f.jpg','rb'),'multipart/form-data')}

R = S.post(URL, files=file, data=PARAMS_4)
DATA = R.json()

print(DATA)


