# Python
Code snippets in Python demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.py](tokens.py): get tokens for data modifying operations
* [API:Login](https://www.mediawiki.org/wiki/API:Login)
  * [login.py](login.py): login
* [API:Logout](https://www.mediawiki.org/wiki/API:Logout)
  * [logout.py](logout.py): logout

### Accounts and users 
* [API:Account creation](https://www.mediawiki.org/wiki/API:Account_creation)
  *  [create_account.py](create_account.py): create an account on a wiki without any special authentication extensions
* [API:Block](https://www.mediawiki.org/wiki/API:Block)
  *  [block_user.py](block_user.py): block a user
* [API:Blocks](https://www.mediawiki.org/wiki/API:Blocks)
  *  [get_blocked_users.py](get_blocked_users.py): get information about recent blocked users
* [API:Users](https://www.mediawiki.org/wiki/API:Users)
  *  [get_users.py](get_users.py): get information about a list of users
* [API:User contributions](https://www.mediawiki.org/wiki/API:User_contributions)
  *  [get_usercontribs.py](get_usercontribs.py): list user contributions
* [API:User group membership](https://www.mediawiki.org/wiki/API:User_group_membership)
  *  [userrights.py](userrights.py): add and remove user rights
* [API:Watchlist feed](https://www.mediawiki.org/wiki/API:Watchlist_feed)
  * [get_my_watchlist_feed.py](get_my_watchlist_feed.py): access an RSS feed of your own watchlist
  * [get_user_watchlist_feed.py](get_user_watchlist_feed.py): access an RSS feed of another user's watchlist
* [API:Options](https://www.mediawiki.org/wiki/API:Options)
  * [change_user_options.py](change_user_options.py): change preferences of current user
* [API:Emailuser](https://www.mediawiki.org/wiki/API:Emailuser)
  *  [send_an_email.py](send_an_email.py): send an email to user
* [API:Watchlist](https://www.mediawiki.org/wiki/API:Watchlist)
  * [get_watchlist.py](get_watchlist.py): get the currently logged-in user's watchlist
* [API:Watchlistraw](https://www.mediawiki.org/wiki/API:Watchlistraw)
  * [get_watchlistraw.py](get_watchlistraw.py): get three pages on the logged-in user's watchlist from the main namespace

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.py](parse.py): parse content of a page
  *  [parse_wikitable.py](search.py): parse a section of its page and fetch its table data
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.py](get_category_items.py): list twenty items in a category
  *  [get_recent_category_items.py](get_recent_category_items.py): get the ten articles most recently added to a category
  *  [get_subcategories.py](get_subcategories.py): get ten subcategories of a category
* [API:Categoryinfo](https://www.mediawiki.org/wiki/API:Categoryinfo)
  *  [get_category_info.py](get_category_info.py): get info about few categories
* [API:Images](https://www.mediawiki.org/wiki/API:Images) 
  * [get_page_images.py](get_page_images.py): get page images embedded on a page
* [API:Purge](https://www.mediawiki.org/wiki/API:Purge)
  *  [purge_two_pages.py](purge_two_pages.py): purge cache of two or more pages
  *  [purge_namespace_pages.py](purge_namespace_pages.py): purge cache of the first 10 pages in the main namespace
* [API:Redirects](https://www.mediawiki.org/wiki/API:Redirects)
  *  [redirects.py](get_redirects.py): return redirects to the given page(s)
* [API:Delete](https://www.mediawiki.org/wiki/API:Delete)
  *  [delete.py](delete.py): delete a page
* [API:Deletedrevs](https://www.mediawiki.org/wiki/API:Deletedrevs)
  *  [get_deleted_revisions.py](get_deleted_revisions.py): list deleted revisions from a user
* [API:Revisions](https://www.mediawiki.org/wiki/API:Revisions)
  *  [get_pages_revisions.py](get_pages_revisions.py): get revision data of multiple pages
  *  [get_filtered_page_revisions.py](get_filtered_page_revisions.py): get revision data of a page filtered by date and user
* [API:Allrevisions](https://www.mediawiki.org/wiki/API:Allrevisions)
  *  [get_allrevisions.py](python/get_allrevisions.py): get revision data of multiple pages and users
* [API:Links](https://www.mediawiki.org/wiki/API:Links)
  *  [get_links.py](get_links.py): get links embedded on a page
  *  [get_red_links.py](get_red_links.py): get the first twenty red links in a page
* [API:Info](https://www.mediawiki.org/wiki/API:Info)
  * [get_info.py](get_info.py): get basic information about a page
* [API:Allpages](https://www.mediawiki.org/wiki/API:Allpages)
  * [get_allpages.py](get_allpages.py): get all pages which fit a certain criteria, within a namespace
* [API:Edit](https://www.mediawiki.org/wiki/API:Edit)
  * [edit.py](edit.py): edit a page
* [API:Allimages](https://www.mediawiki.org/wiki/API:Allimages)
  * [get_allimages_by_date.py](get_allimages_by_date.py): list all images in a namespace, starting from a certain timestamp 
  * [get_allimages_by_name.py](get_allimages_by_name.py): list all images in a namespace, starting from a certain filename
* [API:Imageinfo](https://www.mediawiki.org/wiki/API:Imageinfo)
  * [get_imageinfo.py](get_imageinfo.py) get information about an image file
* [API:Categories](https://www.mediawiki.org/wiki/API:Categories)
  * [get_categories.py](get_categories.py): get categories associated with a page
* [API:Allcategories](https://www.mediawiki.org/wiki/API:Allcategories)
  * [get_allcategories.py](get_allcategories.py): get all categories that fit certain criteria relating to their titles
* [API:Allusers](https://www.mediawiki.org/wiki/API:Allusers)
  * [get_allusers.py](get_allusers.py): get a list of all registered users, as ordered by username
  * [get_allcategories.py](get_allcategories.py): get all categories that fit certain criteria relating to their titles
* [API:Backlinks](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_backlinks.py](get_backlinks.py): list pages which link to a certain page
* [API:Random](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_random.py](get_random.py): get a list of random pages
* [API:Move](https://www.mediawiki.org/wiki/API:Move)
  * [move.py](move.py): move a page
* [API:Watch](https://www.mediawiki.org/wiki/API:Watch)
  * [watch.py](watch.py): add a page to your watchlist 
* [API:Alllinks](https://www.mediawiki.org/wiki/API:Alllinks)
  * [get_alllinks.py](get_alllinks.py): list links to a namespace
* [API:Exturlusage](https://www.mediawiki.org/wiki/API:Exturlusage)
  * [get_exturlusage.py](get_exturlusage.py): enumerate pages that contain a given URL
* [API:RecentChanges](https://www.mediawiki.org/wiki/API:RecentChanges)
  * [get_recent_changes.py](get_recent_changes.py): get the three most recent changes with sizes and flags
* [API:Querypage](https://www.mediawiki.org/wiki/API:Querypage)
  * [get_querypage_list.py](get_querypage_list.py): List first 10 pages which are uncategorized
* [API:SetPageLanguage](https://www.mediawiki.org/wiki/API:SetPageLanguage)
  *  [set_page_language.py](set_page_language.py): change page language
* [API:Embeddedin](https://www.mediawiki.org/wiki/API:Embeddedin)
  * [get_embedded_pages.py](get_embedded_pages.py): get all page(s) that embed a page
* [API:Rollback](https://www.mediawiki.org/wiki/API:Rollback)
  * [rollback.py](rollback.py): rollback the last edits made to a given page
* [API:Allfileusages](https://www.mediawiki.org/wiki/API:Allfileusages)
  * [get_allfileusages.py](get_allfileusages.py): list of all file usages
* [API:Protect](https://www.mediawiki.org/wiki/API:Protect)
  * [protect.py](protect.py): Change the protection level of a given page
* [API:Upload](https://www.mediawiki.org/wiki/API:Upload)
  * [upload_file_directly.py](upload_file_directly.py): upload a file directly from the system
  * [upload_file_from_url.py](upload_file_from_url.py): upload a file from a URL 
  * [upload_file_in_chunks.py](upload_file_in_chunks.py): upload a file in chunks
* [API:Pagepropnames](https://www.mediawiki.org/wiki/API:Pagepropnames)
  * [get_pagepropnames.py](get_pagepropnames.py): List all page property names in use on the wiki
* [API:Protectedtitles](https://www.mediawiki.org/wiki/API:Protectedtitles)
  * [get_protectedtitles.py](get_protectedtitles.py): List the first 2 titles which only sysops can create
* [API:Imageusage](https://www.mediawiki.org/wiki/API:Imageusage)
  * [get_imageusage.py](get_imageusage.py): List the first three pages that use a given image title.
* [API:Import](https://www.mediawiki.org/wiki/API:Import)
  * [import_interwiki.py](import_interwiki.py): Import a page from another wiki by specifying its title
  * [import_xml.py](import_xml.py): Import a page from another wiki by uploading its xml dump
* [API:Patrol](https://www.mediawiki.org/wiki/API:Patrol)
  * [patrol.py](patrol.py): Patrol a recent change
* [API:Iwlinks](https://www.mediawiki.org/wiki/API:Iwlinks)
  * [get_iwlinks.py](get_iwlinks.py): get the interwiki links from a given page
* [API:Undelete](https://www.mediawiki.org/wiki/API:Undelete)
  * [undelete.py](undelete.py): restore two revisions of a deleted page
* [API:Logevents](https://www.mediawiki.org/wiki/API:Logevents)
  * [get_logevents.py](get_logevents.py): get the three most recent log events
* [API:Tags](https://www.mediawiki.org/wiki/API:Tags)
  * [get_tags.py](get_tags.py): get the first three change tags and their hitcounts
* [API:Allredirects](https://www.mediawiki.org/wiki/API:Allredirects)
  * [get_allredirects.py](get_allredirects.py): get the first three unique pages containing redirects to the main namespace
* [API:Alltransclusions](https://www.mediawiki.org/wiki/API:Alltransclusions)
  * [get_alltransclusions.py](get_alltransclusions.py): get three unique pages in the main namespace which contain transclusions
* [API:Mergehistory](https://www.mediawiki.org/wiki/API:Mergehistory)
  * [mergehistory.py](mergehistory.py): Merge the page revisions of Oldpage
    dating up to 2015-12-31T04:37:41Z into Newpage
* [API:Stashedit](https://www.mediawiki.org/wiki/API:Stashedit)
  * [stashedit.py](stashedit.py): Prepare an edit in shared cache


### Search 
* [API:Search](https://www.mediawiki.org/wiki/API:Search)
  * [search.py](search.py): search for a title or a text
* [API:Geosearch](https://www.mediawiki.org/wiki/API:Geosearch)
  * [geosearch.py](geosearch.py): search for pages nearby
  * [geoimagesearch.py](geoimagesearch.py): search for pages nearby with images
  * [geocoordinates.py](geocoordinates.py): obtain coordinates for wiki pages nearby
* [API:Opensearch](https://www.mediawiki.org/wiki/API:Opensearch)
  * [opensearch.py](opensearch.py): fetch results in an opensearch format
* [API:Prefixsearch](https://www.mediawiki.org/wiki/API:Prefixsearch)
  * [prefixsearch.py](prefixsearch.py): perform a prefix search for page titles
* [API:Languagesearch](https://www.mediawiki.org/wiki/API:Languagesearch)
  * [languagesearch.py](languagesearch.py): search for a language 

### Basics
* [API:Parameter information](https://www.mediawiki.org/wiki/API:Parameter_information)
  * [paraminfo.py](paraminfo.py): get information about another action API module and its parameters