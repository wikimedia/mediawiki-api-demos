#!/usr/bin/python3

"""
    get_no_of_revisions_for_title.py

    MediaWiki Action API Code Samples
    Demo of `Revisions` module: Get data including content of last 5 revision of the title [[API:Geosearch]]
    MIT license
"""
import requests

req_ssn = requests.Session()


api_url = 'https://www.mediawiki.org/w/api.php'
rvprop = 'timestamp|user|comment|content'

search_params = {
    'action': 'query',
    'prop': 'revisions',
    'titles': 'API:Geosearch',
    'rvlimit': 5,
    'rvprop': rvprop,
    'rvslots':'main',
    'format': 'json',
    'formatversion': 2
}

data_req = req_ssn.get(url=api_url, params=search_params)
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