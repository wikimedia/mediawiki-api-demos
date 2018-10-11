#!/usr/bin/python3

"""
    get_last_revision_en.py

    MediaWiki Action API Code Samples
    Demo of `Revisions` module: Get data including content of last revision of titles [[:en:API]] and [[:en:Main Page]]
    MIT license
"""
import requests

req_ssn = requests.Session()

api_url = 'https://en.wikipedia.org/w/api.php'
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

data_req = req_ssn.get(url=api_url, params=search_params)
data = data_req.json()

title_data = data["query"]["pages"] # gives a list of the pages and revisions

mainpage_title_dict = title_data[0]
api_title_dict = title_data[1]

no_of_revisions = 0

#For Main Page Title
mainpage_title_dict_revisions_list = mainpage_title_dict["revisions"]
print("For {} title:".format(mainpage_title_dict["title"]))
for index in range(len(mainpage_title_dict_revisions_list)):
    no_of_revisions += 1
    print("Revision {}:".format(no_of_revisions))
    print("Name of user: {}\nTime of revision: {}\nComment: {}\nContent: {}\n".format(mainpage_title_dict["revisions"][index]["user"], 
            mainpage_title_dict["revisions"][index]["timestamp"], mainpage_title_dict["revisions"][index]["comment"],
            mainpage_title_dict["revisions"][index]["slots"]["main"]["content"]))


#For the API title
api_title_dict_revisions_list = api_title_dict["revisions"]
print("For {} title:".format(api_title_dict["title"]))
for index in range(len(api_title_dict_revisions_list)):
    no_of_revisions += 1
    print("Revision {}:".format(no_of_revisions))
    print("Name of user: {}\nTime of revision: {}\nComment: {}\nContent: {}\n".format(api_title_dict["revisions"][index]["user"], 
            api_title_dict["revisions"][index]["timestamp"], api_title_dict["revisions"][index]["comment"],
            api_title_dict["revisions"][index]["slots"]["main"]["content"]))