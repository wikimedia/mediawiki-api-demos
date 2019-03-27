# MediaWiki Action API Code Samples
Code snippets in Python demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.py](python/tokens.py): get tokens for data modifying operations
* [API:Login](https://www.mediawiki.org/wiki/API:Login)
  * [login.py](python/login.py) & [clientlogin.py](python/clientlogin.py): login
* [API:Logout](https://www.mediawiki.org/wiki/API:Logout)
  * [logout.py](python/logout.py): logout

### Accounts and users 
* [API:Account creation](https://www.mediawiki.org/wiki/API:Account_creation)
  *  [create_account.py](python/create_account.py): create an account on a wiki without any special authentication extensions
  *  [create_account_with_captcha.py](python/create_account_with_captcha.py): create an account on a wiki with a captcha enabling extension installed
* [API:Block](https://www.mediawiki.org/wiki/API:Block)
  *  [block_user.py](python/block_user.py): block a user
* [API:Blocks](https://www.mediawiki.org/wiki/API:Blocks)
  *  [get_blocked_users.py](python/get_blocked_users.py): get information about recent blocked users
* [API:Users](https://www.mediawiki.org/wiki/API:Users)
  *  [get_users.py](python/get_users.py): get information about a list of users
* [API:User contributions](https://www.mediawiki.org/wiki/API:User_contributions)
  *  [get_usercontribs.py](python/get_usercontribs): list user contributions
* [API:User group membership](https://www.mediawiki.org/wiki/API:User_group_membership)
  *  [userrights.py](python/userrights): add and remove user rights
* [API:Watchlist feed](https://www.mediawiki.org/wiki/API:Watchlist_feed)
  * [get_my_watchlist_feed.py](python/get_my_watchlist_feed.py): access an RSS feed of your own watchlist
  * [get_user_watchlist_feed.py](python/get_user_watchlist_feed.py): access an RSS feed of another user's watchlist
* [API:Options](https://www.mediawiki.org/wiki/API:Options)
  * [change_user_options.py](python/change_user_options.py): change preferences of current user
* [API:Emailuser](https://www.mediawiki.org/wiki/API:Emailuser)
  *  [send_an_email.py](python/send_an_email.py): send an email to user

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.py](python/parse.py): parse content of a page
  *  [parse_wikitable.py](python/search.py): parse a section of its page and fetch its table data
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.py](python/get_category_items.py): list twenty items in a category
  *  [get_recent_category_items.py](python/get_recent_category_items.py): get the ten articles most recently added to a category
  *  [get_subcategories.py](python/get_subcategories.py): get ten subcategories of a category
* [API:Categoryinfo](https://www.mediawiki.org/wiki/API:Categoryinfo)
  *  [get_category_info.py](python/get_category_info.py): get info about few categories
* [API:Images](https://www.mediawiki.org/wiki/API:Images) 
  * [get_page_images.py](python/get_page_images.py): get page images embedded on a page
* [API:Purge](https://www.mediawiki.org/wiki/API:Purge)
  *  [purge_two_pages.py](python/purge_two_pages.py): purge cache of two or more pages
  *  [purge_namespace_pages.py](python/purge_namespace_pages.py): purge cache of the first 10 pages in the main namespace
* [API:Redirects](https://www.mediawiki.org/wiki/API:Redirects)
  *  [redirects.py](python/redirects.py): return redirects to the given page(s)
* [API:Delete](https://www.mediawiki.org/wiki/API:Delete)
  *  [delete.py](python/delete.py): delete a page
* [API:Deletedrevs](https://www.mediawiki.org/wiki/API:Deletedrevs)
  *  [get_deleted_revisions.py](python/get_deleted_revisions.py): list deleted revisions from a user
* [API:Revisions](https://www.mediawiki.org/wiki/API:Revisions)
  *  [get_pages_revisions.py](python/get_pages_revisions.py): get revision data of multiple pages
  *  [get_filtered_page_revisions.py](python/get_filtered_page_revisions.py): get revision data of a page filtered by date and user
* [API:Links](https://www.mediawiki.org/wiki/API:Links)
  *  [get_links.py](python/get_links.py): get links embedded on a page
  *  [get_red_links.py](python/get_red_links.py): get the first twenty red links in a page
* [API:Info](https://www.mediawiki.org/wiki/API:Info)
  * [get_info.py](python/get_info.py): get basic information about a page
* [API:Allpages](https://www.mediawiki.org/wiki/API:Allpages)
  * [get_allpages.py](python/get_allpages.py): get all pages which fit a certain criteria, within a namespace
* [API:Edit](https://www.mediawiki.org/wiki/API:Edit)
  * [edit.py](python/edit.py): edit a page
* [API:Allimages](https://www.mediawiki.org/wiki/API:Allimages)
  * [get_allimages_by_date.py](python/get_allimages_by_date.py): list all images in a namespace, starting from a certain timestamp 
  * [get_allimages_by_name.py](python/get_allimages_by_name.py): list all images in a namespace, starting from a certain filename
* [API:Imageinfo](https://www.mediawiki.org/wiki/API:Imageinfo)
  * [get_imageinfo.py](python/get_imageinfo.py) get information about an image file
* [API:Categories](https://www.mediawiki.org/wiki/API:Categories)
  * [get_categories.py](python/get_categories.py): get categories associated with a page
* [API:Allcategories](https://www.mediawiki.org/wiki/API:Allcategories)
  * [get_allcategories.py](python/get_allcategories.py): get all categories that fit certain criteria relating to their titles
* [API:Allusers](https://www.mediawiki.org/wiki/API:Allusers)
  * [get_allusers.py](python/get_allusers.py): get a list of all registered users, as ordered by username
  * [get_allcategories.py](python/get_allcategories.py): get all categories that fit certain criteria relating to their titles
* [API:Backlinks](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_backlinks.py](python/get_backlinks.py): list pages which link to a certain page
* [API:Random](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_random.py](python/get_random.py): get a list of random pages
* [API:Move](https://www.mediawiki.org/wiki/API:Move)
  * [move.py](python/move.py): move a page
* [API:Watch](https://www.mediawiki.org/wiki/API:Watch)
  * [watch.py](python/watch.py): add a page to your watchlist 
* [API:Alllinks](https://www.mediawiki.org/wiki/API:Alllinks)
  * [get_alllinks.py](python/get_alllinks.py): list links to a namespace
* [API:Exturlusage](https://www.mediawiki.org/wiki/API:Exturlusage)
  * [get_exturlusage.py](python/get_exturlusage.py): enumerate pages that contain a given URL
* [API:RecentChanges](https://www.mediawiki.org/wiki/API:RecentChanges)
  * [get_recent_changes.py](python/get_recent_changes.py): get the three most recent changes with sizes and flags
* [API:Querypage](https://www.mediawiki.org/wiki/API:Querypage)
  * [get_querypage_list.py](python/get_querypage_list.py): List first 10 pages which are uncategorized
* [API:SetPageLanguage](https://www.mediawiki.org/wiki/API:SetPageLanguage)
  *  [set_page_language.py](python/set_page_language.py): change page language
* [API:Embeddedin](https://www.mediawiki.org/wiki/API:Embeddedin)
  * [get_embedded_pages.py](python/get_embedded_pages.py): get all page(s) that embed a page
* [API:Rollback](https://www.mediawiki.org/wiki/API:Rollback)
  * [rollback.py](python/rollback.py): rollback the last edits made to a given page
* [API:Allfileusages](https://www.mediawiki.org/wiki/API:Allfileusages)
  * [get_allfileusages.py](python/get_allfileusages.py): list of all file usages
* [API:Protect](https://www.mediawiki.org/wiki/API:Protect)
  * [protect.py](python/protect.py): Change the protection level of a given page
* [API:Upload](https://www.mediawiki.org/wiki/API:Upload)
  * [upload_file_directly.py](python/upload_file_directly.py): upload a file directly from the system
  * [upload_file_from_url.py](python/upload_file_from_url.py): upload a file from a URL 
  * [upload_file_in_chunks.py](python/upload_file_in_chunks.py): upload a file in chunks
* [API:Pagepropnames](https://www.mediawiki.org/wiki/API:Pagepropnames)
  * [get_pagepropnames.py](python/get_pagepropnames.py): List all page property names in use on the wiki

### Search 
* [API:Search](https://www.mediawiki.org/wiki/API:Search)
  * [search.py](python/search.py): search for a title or a text
* [API:Geosearch](https://www.mediawiki.org/wiki/API:Geosearch)
  * [geosearch.py](python/geosearch.py): search for pages nearby
  * [geoimagesearch.py](python/geoimagesearch.py): search for pages nearby with images
  * [geocoordinates.py](python/geocoordinates.py): obtain coordinates for wiki pages nearby
* [API:Opensearch](https://www.mediawiki.org/wiki/API:Opensearch)
  * [opensearch.py](python/opensearch.py): fetch results in an opensearch format
* [API:Prefixsearch](https://www.mediawiki.org/wiki/API:Prefixsearch)
  * [prefixsearch.py](python/prefixsearch.py): perform a prefix search for page titles
* [API:Languagesearch](https://www.mediawiki.org/wiki/API:Languagesearch)
  * [languagesearch.py](python/languagesearch.py): search for a language 

### Basics
* [API:Parameter information](https://www.mediawiki.org/wiki/API:Parameter_information)
  * [paraminfo.py](python/paraminfo.py): get information about another action API module and its parameters

### Demo apps
* [Article ideas generator](python/demos/article-ideas-generator): 
Demo app that suggests articles from various categories that don't yet exist on English Wikipedia. The app uses [Parse](https://www.mediawiki.org/wiki/API:Parse) and [Links](https://www.mediawiki.org/wiki/API:Links) module.
* [Nearby places viewer](python/demos/nearby-places-viewer): 
Demo of geo search for wiki pages near a location using the [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) and MediaWiki Action API's [Geosearch](https://www.mediawiki.org/wiki/API:Geosearch) module.
* [Picture of the day viewer](python/demos/picture-of-the-day-viewer):
Demo app that uses [prop=images](https://www.mediawiki.org/wiki/API:Images) module to fetch Wikipedia's Picture of the Day (POTD) from a template page and displays it on a webpage. The app also allows users to go backward or forward a date to view other POTD.
* [User Contributions](python/demos/user-contributions-feed)
A sample app that uses MediaWiki Action [API:Usercontribs](https://www.mediawiki.org/wiki/API:Usercontribs) allows you to see the latest top 50 edits made by a user. This app uses Flask Framework as backend.

### Installation
```
$ git clone https://github.com/wikimedia/MediaWiki-Action-API-Code-Samples.git
$ cd MediaWiki-Action-API-Code-Samples
Install the necessary python modules with pip
$ python3 name_of_the_file.py #Enter any credentials if required in the file
```

### Contributing code samples
First, propose an idea for a code sample, demo app, etc. by creating an issue around it in the repository. After discussing your idea with the repo contributors, start working, and then send a pull request, when you've your changes ready to be accepted/ merged! You can autogenerate python files for GET Requests demos where feasible by following the instructions below:
```
$ cd MediaWiki-Action-API-Code-Samples
$ Add module information to `modules.json`
$ cd python
$ python autogenerator.py
$ Make desired changes to the newly generated file(s)
```
