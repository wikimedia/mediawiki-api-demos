# Code Snippets : Javascript
Code snippets in Javascript demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.js](tokens.js): get tokens for data modifying operations
* [API:Login](https://www.mediawiki.org/wiki/API:Login)
  * [login.js](login.js) & [clientlogin.js](clientlogin.js): login
* [API:Logout](https://www.mediawiki.org/wiki/API:Logout)
  * [logout.js](logout.js): logout

### Accounts and users 
* [API:Account creation](https://www.mediawiki.org/wiki/API:Account_creation)
  *  [create_account.js](create_account.js): create an account on a wiki without any special authentication extensions
  *  [create_account_with_captcha.js](create_account_with_captcha.js): create an account on a wiki with a captcha enabling extension installed
* [API:Block](https://www.mediawiki.org/wiki/API:Block)
  *  [block_user.js](block_user.js): block a user
* [API:Blocks](https://www.mediawiki.org/wiki/API:Blocks)
  *  [get_blocked_users.js](get_blocked_users.js): get information about recent blocked users
* [API:Users](https://www.mediawiki.org/wiki/API:Users)
  *  [get_users.js](get_users.js): get information about a list of users
* [API:User contributions](https://www.mediawiki.org/wiki/API:User_contributions)
  *  [get_usercontribs.js](get_usercontribs): list user contributions
* [API:User group membership](https://www.mediawiki.org/wiki/API:User_group_membership)
  *  [userrights.js](userrights): add and remove user rights
* [API:Watchlist feed](https://www.mediawiki.org/wiki/API:Watchlist_feed)
  * [get_my_watchlist_feed.js](get_my_watchlist_feed.js): access an RSS feed of your own watchlist
  * [get_user_watchlist_feed.js](get_user_watchlist_feed.js): access an RSS feed of another user's watchlist
* [API:Options](https://www.mediawiki.org/wiki/API:Options)
  * [change_user_options.js](change_user_options.js): change preferences of current user
* [API:Emailuser](https://www.mediawiki.org/wiki/API:Emailuser)
  *  [send_an_email.js](send_an_email.js): send an email to user

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.js](parse.js): parse content of a page
  *  [parse_wikitable.js](search.js): parse a section of its page and fetch its table data
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.js](get_category_items.js): list twenty items in a category
  *  [get_recent_category_items.js](get_recent_category_items.js): get the ten articles most recently added to a category
  *  [get_subcategories.js](get_subcategories.js): get ten subcategories of a category
* [API:Categoryinfo](https://www.mediawiki.org/wiki/API:Categoryinfo)
  *  [get_category_info.js](get_category_info.js): get info about few categories
* [API:Images](https://www.mediawiki.org/wiki/API:Images) 
  * [get_page_images.js](get_page_images.js): get page images embedded on a page
* [API:Purge](https://www.mediawiki.org/wiki/API:Purge)
  *  [purge_two_pages.js](purge_two_pages.js): purge cache of two or more pages
  *  [purge_namespace_pages.js](purge_namespace_pages.js): purge cache of the first 10 pages in the main namespace
* [API:Redirects](https://www.mediawiki.org/wiki/API:Redirects)
  *  [redirects.js](redirects.js): return redirects to the given page(s)
* [API:Delete](https://www.mediawiki.org/wiki/API:Delete)
  *  [delete.js](delete.js): delete a page
* [API:Deletedrevs](https://www.mediawiki.org/wiki/API:Deletedrevs)
  *  [get_deleted_revisions.js](get_deleted_revisions.js): list deleted revisions from a user
* [API:Revisions](https://www.mediawiki.org/wiki/API:Revisions)
  *  [get_pages_revisions.js](get_pages_revisions.js): get revision data of multiple pages
  *  [get_filtered_page_revisions.js](get_filtered_page_revisions.js): get revision data of a page filtered by date and user
* [API:Links](https://www.mediawiki.org/wiki/API:Links)
  *  [get_links.js](get_links.js): get links embedded on a page
  *  [get_red_links.js](get_red_links.js): get the first twenty red links in a page
* [API:Info](https://www.mediawiki.org/wiki/API:Info)
  * [get_info.js](get_info.js): get basic information about a page
* [API:Allpages](https://www.mediawiki.org/wiki/API:Allpages)
  * [get_allpages.js](get_allpages.js): get all pages which fit a certain criteria, within a namespace
* [API:Edit](https://www.mediawiki.org/wiki/API:Edit)
  * [edit.js](edit.js): edit a page
* [API:Allimages](https://www.mediawiki.org/wiki/API:Allimages)
  * [get_allimages_by_date.js](get_allimages_by_date.js): list all images in a namespace, starting from a certain timestamp 
  * [get_allimages_by_name.js](get_allimages_by_name.js): list all images in a namespace, starting from a certain filename
* [API:Imageinfo](https://www.mediawiki.org/wiki/API:Imageinfo)
  * [get_imageinfo.js](get_imageinfo.js) get information about an image file
* [API:Categories](https://www.mediawiki.org/wiki/API:Categories)
  * [get_categories.js](get_categories.js): get categories associated with a page
* [API:Allcategories](https://www.mediawiki.org/wiki/API:Allcategories)
  * [get_allcategories.js](get_allcategories.js): get all categories that fit certain criteria relating to their titles
* [API:Allusers](https://www.mediawiki.org/wiki/API:Allusers)
  * [get_allusers.js](get_allusers.js): get a list of all registered users, as ordered by username
  * [get_allcategories.js](get_allcategories.js): get all categories that fit certain criteria relating to their titles
* [API:Backlinks](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_backlinks.js](get_backlinks.js): list pages which link to a certain page
* [API:Random](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_random.js](get_random.js): get a list of random pages
* [API:Move](https://www.mediawiki.org/wiki/API:Move)
  * [move.js](move.js): move a page
* [API:Watch](https://www.mediawiki.org/wiki/API:Watch)
  * [watch.js](watch.js): add a page to your watchlist 
* [API:Alllinks](https://www.mediawiki.org/wiki/API:Alllinks)
  * [get_alllinks.js](get_alllinks.js): list links to a namespace
* [API:Exturlusage](https://www.mediawiki.org/wiki/API:Exturlusage)
  * [get_exturlusage.js](get_exturlusage.js): enumerate pages that contain a given URL
* [API:RecentChanges](https://www.mediawiki.org/wiki/API:RecentChanges)
  * [get_recent_changes.js](get_recent_changes.js): get the three most recent changes with sizes and flags
* [API:Querypage](https://www.mediawiki.org/wiki/API:Querypage)
  * [get_querypage_list.js](get_querypage_list.js): List first 10 pages which are uncategorized
* [API:SetPageLanguage](https://www.mediawiki.org/wiki/API:SetPageLanguage)
  *  [set_page_language.js](set_page_language.js): change page language
* [API:Embeddedin](https://www.mediawiki.org/wiki/API:Embeddedin)
  * [get_embedded_pages.js](get_embedded_pages.js): get all page(s) that embed a page
* [API:Rollback](https://www.mediawiki.org/wiki/API:Rollback)
  * [rollback.js](rollback.js): rollback the last edits made to a given page
* [API:Allfileusages](https://www.mediawiki.org/wiki/API:Allfileusages)
  * [get_allfileusages.js](get_allfileusages.js): list of all file usages
* [API:Protect](https://www.mediawiki.org/wiki/API:Protect)
  * [protect.js](protect.js): Change the protection level of a given page
* [API:Upload](https://www.mediawiki.org/wiki/API:Upload)
  * [upload_file_directly.js](upload_file_directly.js): upload a file directly from the system
  * [upload_file_from_url.js](upload_file_from_url.js): upload a file from a URL 
  * [upload_file_in_chunks.js](upload_file_in_chunks.js): upload a file in chunks
* [API:Pagepropnames](https://www.mediawiki.org/wiki/API:Pagepropnames)
  * [get_pagepropnames.js](get_pagepropnames.js): List all page property names in use on the wiki

### Search 
* [API:Search](https://www.mediawiki.org/wiki/API:Search)
  * [search.js](search.js): search for a title or a text
* [API:Geosearch](https://www.mediawiki.org/wiki/API:Geosearch)
  * [geosearch.js](geosearch.js): search for pages nearby
  * [geoimagesearch.js](geoimagesearch.js): search for pages nearby with images
  * [geocoordinates.js](geocoordinates.js): obtain coordinates for wiki pages nearby
* [API:Opensearch](https://www.mediawiki.org/wiki/API:Opensearch)
  * [opensearch.js](opensearch.js): fetch results in an opensearch format
* [API:Prefixsearch](https://www.mediawiki.org/wiki/API:Prefixsearch)
  * [prefixsearch.js](prefixsearch.js): perform a prefix search for page titles
* [API:Languagesearch](https://www.mediawiki.org/wiki/API:Languagesearch)
  * [languagesearch.js](languagesearch.js): search for a language 

### Basics
* [API:Parameter information](https://www.mediawiki.org/wiki/API:Parameter_information)
  * [paraminfo.js](paraminfo.js): get information about another action API module and its parameters

