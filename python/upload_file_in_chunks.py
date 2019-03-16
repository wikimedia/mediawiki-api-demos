"""
    chunked_uploading.py

    MediaWiki Action API Code Samples
    Demo of `Upload` module: Multiple Post requests to upload a file in chunks

    MIT license
"""

import os
import requests

S = requests.Session()
URL = "https://test.wikipedia.org/w/api.php"

#filepath contains the path of the file's location
FILE_PATH = 'f.jpg'
FILE = open(FILE_PATH, 'rb')
FILE_SIZE = os.stat(FILE_PATH).st_size

def read_chunks(file_object, chunk_size=5000):
    """Return the next chunk of the file."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def fetch_login_token():
    """Retrieve a login token."""
    params = {
        "action":"query",
        "meta":"tokens",
        "type":"login",
        "format":"json"
    }
    res = S.get(url=URL, params=params)
    data = res.json()
    return data["query"]["tokens"]["logintoken"]

def user_login(login_token):
    """Send a post request to login."""
    #Use of main account for login is not supported. Obtain credentials via Special:BotPasswords
    #(https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
    params = {
        "action":"login",
        "lgname": "bot_username",
        "lgpassword":"bot_password",
        "format":"json",
        "lgtoken": login_token
    }
    S.post(URL, data=params)

def fetch_csrf_token():
    """While logged in, retrieve a CSRF token"""
    params = {
        "action": "query",
        "meta":"tokens",
        "format":"json"
    }
    res = S.get(url=URL, params=params)
    data = res.json()
    return data["query"]["tokens"]["csrftoken"]

def upload_file_in_chunks(csrf_token):
    """Send Multiple Post requests to upload a file in chunks using "stash" mode.

    Stash mode is used to build a file up in pieces and then commit it at the end
    """

    chunks = read_chunks(FILE)
    chunk = next(chunks)

    #parameters for the first chunk
    params = {
        "action": "upload",
        "stash": 1,
        "filename": "chunk_test.jpg",
        "filesize": FILE_SIZE,
        "offset": 0,
        "format": "json",
        "token": csrf_token,
        "ignorewarnings": 1
    }
    index = 0
    file = {'chunk':('{}.jpg'.format(index), chunk, 'multipart/form-data')}
    index += 1
    res = S.post(URL, files=file, data=params)
    data = res.json()
    print(data)

    #For the second and further chunks, pass in the filekey parameter as well
    for chunk in chunks:
        params = {
            "action": "upload",
            "stash": 1,
            "offset": data["upload"]["offset"],
            "filename": "chunk_test.jpg",
            "filesize": FILE_SIZE,
            "filekey": data["upload"]["filekey"],
            "format": "json",
            "token": csrf_token,
            "ignorewarnings": 1
        }
        file = {'chunk':('{}.jpg'.format(index), chunk, 'multipart/form-data')}
        index += 1
        res = S.post(URL, files=file, data=params)
        data = res.json()
        print(data)

    #Final upload using the filekey to commit the upload out of the stash area
    params = {
        "action": "upload",
        "filename": "chunk_test.jpg",
        "filekey": data["upload"]["filekey"],
        "format": "json",
        "comment": "Upload Testing",
        "token": csrf_token,
    }
    res = S.post(URL, data=params)
    data = res.json()
    print(data)

def main():
    """ Login to a user account and upload a file in chunks."""
    login_token = fetch_login_token()
    user_login(login_token)
    csrf_token = fetch_csrf_token()
    upload_file_in_chunks(csrf_token)


if __name__ == "__main__":
    main()
