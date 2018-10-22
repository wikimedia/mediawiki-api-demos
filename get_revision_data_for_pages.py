#!/usr/bin/python3

"""
    get_last_revision.py

    MediaWiki Action API Code Samples
    Demo of `Revisions` module: Get revision data with content for pages with titles [[API]] and [[Main Page]]
    MIT license
"""
import requests

S = requests.Session()

URL = 'https://www.mediawiki.org/w/api.php'
titles = 'API|Main Page'
rvprop = 'timestamp|user|comment|content'

search_params = {
    'action': 'query',
    'prop': 'revisions',
    'titles': titles,
    'rvprop': rvprop,
    'rvslots': 'main',
    'format': 'json',
    'formatversion': 2
}

data_req = S.get(url=URL, params=search_params)
data = data_req.json()

title_data = data["query"]["pages"] # Gives a list containing the pages requested and their revisions

print(title_data)