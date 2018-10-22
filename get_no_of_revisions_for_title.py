#!/usr/bin/python3

"""
    get_no_of_revisions_for_title.py

    MediaWiki Action API Code Samples
    Demo of `Revisions` module: Get data including content of last 5 revisions of the title [[API:Geosearch]] made after the 1st of July 2018 i.e 2018-07-01 excluding changes made by the user MichelleACodes
    MIT license
"""
import requests

S = requests.Session()


URL = 'https://www.mediawiki.org/w/api.php'
rvprop = 'timestamp|user|comment|content'

search_params = {
    'action': 'query',
    'prop': 'revisions',
    'titles': 'API:Geosearch',
    'rvlimit': 5,
    'rvprop': rvprop,
    'rvslots':'main',
    'rvdir': 'newer',
    'rvstart': '2018-07-01T00:00:00Z',
    'rvexcludeuser': 'MichelleACodes',
    'format': 'json',
    'formatversion': 2
}

data_req = S.get(url=URL, params=search_params)
data = data_req.json()

title_data = data["query"]["pages"] # Gives a list containing the page requested and its revisions

apigeosearch_title_dict = title_data[0]
no_of_revisions = 0 # set number of revisions to 0

apigeosearch_title_dict_revisions_list = apigeosearch_title_dict["revisions"]
print("For {} title:".format(apigeosearch_title_dict["title"]))


for index in range(len(apigeosearch_title_dict_revisions_list)):
    no_of_revisions += 1
    print("Revision {}:".format(no_of_revisions))
    print("Name of user: {}\nTime of revision: {}\nComment: {}\nContent: {}\n".format(apigeosearch_title_dict["revisions"][index]["user"], 
            apigeosearch_title_dict["revisions"][index]["timestamp"], apigeosearch_title_dict["revisions"][index]["comment"],
            apigeosearch_title_dict["revisions"][index]["slots"]["main"]["content"]))