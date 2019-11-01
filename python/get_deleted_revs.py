"""
	get_deleted_revs.py

    MediaWiki Action API Code Samples
    Demo of `Deleted Revisions:Get a list of deleted revision for Talk:Main Page` module
    MIT license
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    'action':"query",
    'format':"json",
    'titles':"Talk:MainPage",
    'prop':"deletedrevisions",
    'drv':"prop"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

print(DATA)