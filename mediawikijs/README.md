# MediaWiki Javascript
Code snippets in MediaWiki native Javascript demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page). These code snippets are vaild within MediaWiki Sites. And works in MediaWiki Javascript wikipages like MediaWiki:Common.js, User:ABC/common.js
and User:ABC/global.js

These code snippets are usefull to create Userscripts and Gadgets.

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.js](tokens.js): get tokens for data modifying operations
* [API:Logout](https://www.mediawiki.org/wiki/API:Logout)
  * [logout.js](logout.js): logout
* [API:Login](https://www.mediawiki.org/wiki/API:Login)
  * [login.js](login.js): Sending request to login

### Accounts and users 
* [API:User contributions](https://www.mediawiki.org/wiki/API:User_contributions)
  *  [get_usercontribs.js](get_usercontribs.js): list user contributions
* [API:Watchlist](https://www.mediawiki.org/wiki/API:Watchlist)
  * [get_watchlist.js](get_watchlist.js): get the currently logged-in user's watchlist
* [API:Block](https://www.mediawiki.org/wiki/API:Block)
  * [block_user.js](block_user.js): block a user
* [API:Options](https://www.mediawiki.org/wiki/API:Options)
  * [change_user_options.js](change_user_options.js): change three options for current user
* [API:Blocks](https://www.mediawiki.org/wiki/API:Blocks)
  * [get_blocker_user.js](get_blocked_user.js): get request to list recent blocked users
* [API:Users](https://www.mediawiki.org/wiki/API:Users)
  * [get_users.js](get_users.js): get information about several users: [[1.2.3.4]], [[Catrope]], [[Vandal01]], and [[Bob]]
* [API:Emailuser](https://www.mediawiki.org/wiki/API:Emailuser)
  * [send_email.js](send_email.js): post request to send email to wiki user
* [API:Userrights](https://www.mediawiki.org/wiki/API:Userrights)
  * [userrights.js](userrights.js): add and remove user rights by changing the user's group membership
* [API:Rsd](https://www.mediawiki.org/wiki/API:Rsd)
  *  [rsd.js](rsd.js): export an RSD schema
* [API:Validatepassword](https://www.mediawiki.org/wiki/API:validatepassword)
  *  [validatepassword.js](validatepassword.js): validate a password against the wiki's password policies

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.js](parse.js): parse content of a page
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.js](get_category_items.js): list twenty items in a category
  *  [get_recent_category_items.js](get_recent_category_items.js): get the ten articles most recently added to a category
  *  [get_subcategories.js](get_subcategories.js): get ten subcategories of a category
* [API:Images](https://www.mediawiki.org/wiki/API:Images)
  * [get_page_images.js](get_page_images.js): get page images embedded on a page
* [API:Redirects](https://www.mediawiki.org/wiki/API:Redirects)
  *  [get_redirects.js](get_redirects.js): return redirects to the given page(s)
* [API:Deletedrevs](https://www.mediawiki.org/wiki/API:Deletedrevs)
  *  [get_deleted_revisions.js](get_deleted_revisions.js): list deleted revisions from a user
* [API:Deletedrevisions](https://www.mediawiki.org/wiki/API:Deletedrevisions)
| *  [get_deleted_revs.js](get_deleted_revs.js): list deleted revisions for a page 
* [API:Revisions](https://www.mediawiki.org/wiki/API:Revisions)
  *  [get_pages_revisions.js](get_pages_revisions.js): get revision data of multiple pages
  *  [get_filtered_page_revisions.js](get_filtered_page_revisions.js): get revision data of a page filtered by date and user
* [API:Alldeletedrevisions](https://www.mediawiki.org/wiki/API:Alldeletedrevisions)
  *  [get_alldeletedrevs.js](get_alldeletedrevs.js): get all deleted revision data by a user or in a namespace.
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
* [API:Alllinks](https://www.mediawiki.org/wiki/API:Alllinks)
  * [get_alllinks.js](get_alllinks.js): list links to a namespace
* [API:Embeddedin](https://www.mediawiki.org/wiki/API:Embeddedin)
  * [get_embedded_pages.js](get_embedded_pages.js): get all page(s) that embed a page
* [API:Contributors](https://www.mediawiki.org/wiki/API:Contributors)
  * [get_contributors.js](get_contributors.js): get request to list all logged-in contributors and count of 
  anonymous contributors to a page
* [API:Delete](https://www.mediawiki.org/wiki/API:Delete)
  * [delete.js](delete.js): delete a page
* [API:Fileusage](https://www.mediawiki.org/wiki/API:Fileusage)
  * [get_allfileusage.js](get_allfileusage.js): list all file usages, including non-existing
* [API:Allredirects](https://www.mediawiki.org/wiki/API:Allredirects)
  * [get_allredirects.js](get_allredirects.js): get the first three unique pages containing redirects to the main namespace
* [API:Allrevisions](https://www.mediawiki.org/wiki/API:Allrevisions)
  * [get_allrevisions.js](get_allrevisions.js): get revision data of multiple pages and users
* [API:Alltransclusions](https://www.mediawiki.org/wiki/API:Alltransclusions)
  * [get_alltransclusions.js](get_alltransclusions.js): get three unique pages in the main namespace which contain transclusions
* [API:Categoryinfo](https://www.mediawiki.org/wiki/API:Categoryinfo)
  * [get_category_info.js](get_category_info.js): get information about a few categories
* [API:Exturlusage](https://www.mediawiki.org/wiki/API:Exturlusage)
  * [get_exturlusage.js](get_exturlusage.js): enumerate pages that contain a given URL
* [API:Imageusage](https://www.mediawiki.org/wiki/API:Imageusage)
  * [get_imageusage.js](get_imageusage.js): list the first 3 pages that use a given image title
* [API:Iwlinks](https://www.mediawiki.org/wiki/API:Iwlinks)
  * [get_iwlinks.js](get_iwlinks.js): get the interwiki links from a given page
* [API:Logevents](https://www.mediawiki.org/wiki/API:Logevents)
  * [get_logevents.js](get_logevents.js): get the three most recent logevents
* [API:Pagepropnames](https://www.mediawiki.org/wiki/API:Pagepropnames)
  * [get_pagepropnames.js](get_pagepropnames.js): list page property names on the given wiki
* [API:Protectedtitles](https://www.mediawiki.org/wiki/API:Protectedtitles)
  * [get_protectedtitles.js](get_protectedtitles.js): get the first 2 titles which only sysops can create
* [API:Querypage](https://www.mediawiki.org/wiki/API:Querypage)
  * [get_querypage_list.js](get_querypage_list.js): list first 10 pages which are uncategorized
* [API:RecentChanges](https://www.mediawiki.org/wiki/API:RecentChanges)
  * [get_recent_changes.js](get_recent_changes.js): get the three most recent changes with sizes and flags
* [API:Tags](https://www.mediawiki.org/wiki/API:Tags)
  * [get_tags.js](get_tags.js): get the first three change tags and their hitcounts
* [API:Watchlistraw](https://www.mediawiki.org/wiki/API:Watchlistraw)
  * [get_watchlistraw.js](get_watchlistraw.js): get three pages on the logged-in user's watchlist from the main namespace.
* [API:Import](https://www.mediawiki.org/wiki/API:Import)
  * [import_interwiki.js](import_interwiki.js): import a page from another wiki by specifying its title
* [API:Move](https://www.mediawiki.org/wiki/API:Move)
  * [move.js](move.js): Move a page with its talk page, leaving a redirect behind
* [API:Patrol](https://www.mediawiki.org/wiki/API:Patrol)
  * [patrol.js](patrol.js): Patrol a recent change
* [API:Protect](https://www.mediawiki.org/wiki/API:Protect)
  * [protect.js](protect.js): demo to change the edit protection
* [API:Purge](https://www.mediawiki.org/wiki/API:Purge)
  * [purge_namespace_pages.js](purge_namespace_pages.js): post request to purge first 10 pages in the main namespace
  * [purge_two_pages.js](purge_two_pages.js): post request to purge two or more pages
* [API:Rollback](https://www.mediawiki.org/wiki/API:Rollback)
  * [rollback.js](rollback.js): post request to rollback the last edits made to a given page
* [API:SetPageLanguage](https://www.mediawiki.org/wiki/API:SetPageLanguage)
  * [set_page_language.js](set_page_language.js): post request to change the language of a page
* [API:Undelete](https://www.mediawiki.org/wiki/API:Undelete)
  * [undelete.js](undelete.js): restore two revisions of a deleted page
* [API:Upload](https://www.mediawiki.org/wiki/API:Upload)
  * [upload_file_directly.js](upload_file_directly.js): post request to upload a file directly
  * [upload_file_from_url.js](upload_file_from_url.js): post request to upload a file from a URL
  * [upload_file_in_chunks.js](upload_file_in_chunks.js): step-by-step process to upload a file in chunks
* [API:Watch](https://www.mediawiki.org/wiki/API:Watch)
  * [watch.js](watch.js): add a page to your watchlist
* [API:Filearchive](https://www.mediawiki.org/wiki/API:Filearchive)
  * [filearchive.js](filearchive.js): Enumerate all deleted files from filearchive table sequentially
* [API:Siteinfo](https://www.mediawiki.org/wiki/API:Siteinfo)
  * [general_site_info.js](general_site_info.js): obtain general site info
* [API:Expandtemplates](https://www.mediawiki.org/wiki/API:Expandtemplates)
  * [expand_templates.js](expand_templates.js): expand the Project:Sandbox template
* [API:ClearHasMsg](https://www.mediawiki.org/wiki/API:ClearHasMsg)
  * [clear_has_msg.js](clear_has_msg.js): clear the hasmsg flag for the current user
* [API:Compare](https://www.mediawiki.org/wiki/API:Compare)
  * [compare.js](compare.js): Compare the current revisions of two different pages
* [API:Tag](https://www.mediawiki.org/wiki/API:Tag)
  * [tag.js](tag.js): Remove the spam tag from log entry ID 123 with the reason Wrongly applied
* [API:Duplicatefiles](https://www.mediawiki.org/wiki/API:Duplicatefiles)
  * [duplicate_files.js](duplicate_files.js): list duplicates of the given files
* [API:Filerepoinfo](https://www.mediawiki.org/wiki/API:Filerepoinfo)
  * [file_repo_info.js](file_repo_info.js): get information about file repositories

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
* [API:Pageswithprop](https://www.mediawiki.org/wiki/API:Pageswithprop)
  *  [get_pageswithprop.js](get_pageswithprop.js): list all pages using a given page property

### Basics
* [API:Parameter information](https://www.mediawiki.org/wiki/API:Parameter_information)
  * [paraminfo.js](paraminfo.js): get information about another action API module and its parameters

