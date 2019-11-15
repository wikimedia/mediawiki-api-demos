"""
	get_deleted_revs.py

    MediaWiki Action API Code Samples
    Demo of `Deleted Revisions module:Get a list of deleted revision for a page` module
    MIT license
"""


import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

# Retrieve login token
PARAMS_0 = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Send a post request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    'action':"login",
    'lgname':"your_bot_username",
    'lgpassword':"your_bot_password",
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)

#Send a get request to get the list of deleted revisions
PARAMS_2 = {
    'action':"query",
    'format':"json",
    'titles':"Talk:MainPage",
    'prop':"deletedrevisions",
    'drv':"prop"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

print(DATA)