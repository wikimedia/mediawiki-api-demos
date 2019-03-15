"""
    chunked_uploading.py

    MediaWiki Action API Code Samples
    Demo of `Upload` module: Multiple Post requests to upload a file in chunks

    MIT license
"""

import os
import requests

def read_chunks(file_object, chunk_size=5000):
    """Generator to return the next chunk"""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

S = requests.Session()
URL = "https://test.wikipedia.org/w/api.php"

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

# Step 3: While logged in, retrieve a CSRF token
PARAMS_3 = {
    "action": "query",
    "meta":"tokens",
    "format":"json"
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()
CSRF_TOKEN = DATA["query"]["tokens"]["csrftoken"]

# Step 4: Post requests to upload a file in chunks using "stash" mode,
# to build a file up in pieces and then commit it at the end.

# filepath contains the path of the file's location
FILE_PATH = 'f.jpg'
FILE = open(FILE_PATH, 'rb')
FILE_SIZE = os.stat(FILE_PATH).st_size
CHUNKS = read_chunks(FILE)
CHUNK = next(CHUNKS)

#parameters for the first chunk
PARAMS_4 = {
    "action": "upload",
    "stash": 1,
    "filename": "chunk_test.jpg",
    "filesize": FILE_SIZE,
    "offset": 0,
    "format": "json",
    "token": CSRF_TOKEN,
    "ignorewarnings": 1
}

INDEX = 0
FILE = {'chunk':('{}.jpg'.format(INDEX), CHUNK, 'multipart/form-data')}
INDEX += 1
R = S.post(URL, files=FILE, data=PARAMS_4)
DATA = R.json()
print(DATA)

#For the second and further chunks, pass in the filekey parameter as well
for chunk in CHUNKS:
    PARAMS_4 = {
        "action": "upload",
        "stash": 1,
        "offset": DATA["upload"]["offset"],
        "filename": "chunk_test.jpg",
        "filesize": FILE_SIZE,
        "filekey": DATA["upload"]["filekey"],
        "format": "json",
        "token": CSRF_TOKEN,
        "ignorewarnings": 1
    }
    FILE = {'chunk':('{}.jpg'.format(INDEX), chunk, 'multipart/form-data')}
    INDEX += 1
    R = S.post(URL, files=FILE, data=PARAMS_4)
    DATA = R.json()
    print(DATA)

#Final upload using the filekey to commit the upload out of the stash area
PARAMS_5 = {
    "action": "upload",
    "filename": "chunk_test.jpg",
    "filekey": DATA["upload"]["filekey"],
    "format": "json",
    "comment": "Upload Testing",
    "token": CSRF_TOKEN,
}

R = S.post(URL, data=PARAMS_5)
DATA = R.json()
print(DATA)
