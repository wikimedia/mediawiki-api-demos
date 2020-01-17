# PHP
Code snippets in PHP demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.php](tokens.php): get tokens for data modifying operations
* [API:Login](https://www.mediawiki.org/wiki/API:Login)
  * [login.php](login.php): login
* [API:Logout](https://www.mediawiki.org/wiki/API:Logout)
  * [logout.php](logout.php): logout

### Accounts and users
* [API:Account creation](https://www.mediawiki.org/wiki/API:Account_creation)
  *  [create_account.php](create_account.php): create an account on a wiki without any special authentication extensions
* [API:Block](https://www.mediawiki.org/wiki/API:Block)
  *  [block_user.php](block_user.php): block a user
* [API:Blocks](https://www.mediawiki.org/wiki/API:Blocks)
  *  [get_blocked_users.php](get_blocked_users.php): get information about recent blocked users
* [API:Users](https://www.mediawiki.org/wiki/API:Users)
  *  [get_users.php](get_users.php): get information about a list of users
* [API:User contributions](https://www.mediawiki.org/wiki/API:User_contributions)
  *  [get_usercontribs.php](get_usercontribs.php): list user contributions
* [API:User group membership](https://www.mediawiki.org/wiki/API:User_group_membership)
  *  [userrights.php](userrights.php): add and remove user rights
* [API:Watchlist feed](https://www.mediawiki.org/wiki/API:Watchlist_feed)
  * [get_my_watchlist_feed.php](get_my_watchlist_feed.php): access an RSS feed of your own watchlist
* [API:Options](https://www.mediawiki.org/wiki/API:Options)
  * [change_user_options.php](change_user_options.php): change preferences of current user
* [API:Emailuser](https://www.mediawiki.org/wiki/API:Emailuser)
  *  [send_an_email.php](send_an_email.php): send an email to user
* [API:Watchlist](https://www.mediawiki.org/wiki/API:Watchlist)
  * [get_watchlist.php](get_watchlist.php): get the currently logged-in user's watchlist
* [API:Watchlistraw](https://www.mediawiki.org/wiki/API:Watchlistraw)
  * [get_watchlistraw.php](get_watchlistraw.php): get three pages on the logged-in user's watchlist from the main namespace
* [API:Rsd](https://www.mediawiki.org/wiki/API:Rsd)
  * [rsd.php](rsd.php): export an RSD schema
* [API:Validatepassword](https://www.mediawiki.org/wiki/API:Validatepassword)
  * [validatepassword.php](validatepassword.php): validate a password against the wiki's password policies

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.php](parse.php): parse content of a page
* [API:Pageswithprop](https://www.mediawiki.org/wiki/API:Pageswithprop)
  *  [get_pageswithprop.php](get_pageswithprop.php): list all pages using a given page property
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.php](get_category_items.php): list twenty items in a category
  *  [get_recent_category_items.php](get_recent_category_items.php): get the ten articles most recently added to a category
  *  [get_subcategories.php](get_subcategories.php): get ten subcategories of a category
* [API:Categoryinfo](https://www.mediawiki.org/wiki/API:Categoryinfo)
  *  [get_category_info.php](get_category_info.php): get info about few categories
* [API:Images](https://www.mediawiki.org/wiki/API:Images)
  * [get_page_images.php](get_page_images.php): get page images embedded on a page
* [API:Purge](https://www.mediawiki.org/wiki/API:Purge)
  *  [purge_two_pages.php](purge_two_pages.php): purge cache of two or more pages
  *  [purge_namespace_pages.php](purge_namespace_pages.php): purge cache of the first 10 pages in the main namespace
* [API:Redirects](https://www.mediawiki.org/wiki/API:Redirects)
  *  [redirects.php](get_redirects.php): return redirects to the given page(s)
* [API:Delete](https://www.mediawiki.org/wiki/API:Delete)
  *  [delete.php](delete.php): delete a page
* [API:Deletedrevs](https://www.mediawiki.org/wiki/API:Deletedrevs)
  *  [get_deleted_revisions.php](get_deleted_revisions.php): list deleted revisions from a user
* [API:Deletedrevisions](https://www.mediawiki.org/wiki/API:Deletedrevisions)
| *  [get_deleted_revs.php](get_deleted_revs.php): list deleted revisions for a page 
* [API:Revisions](https://www.mediawiki.org/wiki/API:Revisions)
  *  [get_pages_revisions.php](get_pages_revisions.php): get revision data of multiple pages
  *  [get_filtered_page_revisions.php](get_filtered_page_revisions.php): get revision data of a page filtered by date and user
* [API:Allrevisions](https://www.mediawiki.org/wiki/API:Allrevisions)
  *  [get_allrevisions.php](get_allrevisions.php): get revision data of multiple pages and users
* [API:Alldeletedrevisions](https://www.mediawiki.org/wiki/API:Alldeletedrevisions)
  *  [get_alldeletedrevs.php](get_alldeletedrevs.php): get all deleted revision data by a user or in a namespace.
* [API:Links](https://www.mediawiki.org/wiki/API:Links)
  *  [get_links.php](get_links.php): get links embedded on a page
  *  [get_red_links.php](get_red_links.php): get the first twenty red links in a page
* [API:Info](https://www.mediawiki.org/wiki/API:Info)
  * [get_info.php](get_info.php): get basic information about a page
* [API:Allpages](https://www.mediawiki.org/wiki/API:Allpages)
  * [get_allpages.php](get_allpages.php): get all pages which fit a certain criteria, within a namespace
* [API:Edit](https://www.mediawiki.org/wiki/API:Edit)
  * [edit.php](edit.php): edit a page
* [API:Allimages](https://www.mediawiki.org/wiki/API:Allimages)
  * [get_allimages_by_date.php](get_allimages_by_date.php): list all images in a namespace, starting from a certain timestamp
  * [get_allimages_by_name.php](get_allimages_by_name.php): list all images in a namespace, starting from a certain filename
* [API:Imageinfo](https://www.mediawiki.org/wiki/API:Imageinfo)
  * [get_imageinfo.php](get_imageinfo.php) get information about an image file
* [API:Categories](https://www.mediawiki.org/wiki/API:Categories)
  * [get_categories.php](get_categories.php): get categories associated with a page
* [API:Allcategories](https://www.mediawiki.org/wiki/API:Allcategories)
  * [get_allcategories.php](get_allcategories.php): get all categories that fit certain criteria relating to their titles
* [API:Allusers](https://www.mediawiki.org/wiki/API:Allusers)
  * [get_allusers.php](get_allusers.php): get a list of all registered users, as ordered by username
* [API:Backlinks](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_backlinks.php](get_backlinks.php): list pages which link to a certain page
* [API:Random](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_random.php](get_random.php): get a list of random pages
* [API:Move](https://www.mediawiki.org/wiki/API:Move)
  * [move.php](move.php): move a page
* [API:Watch](https://www.mediawiki.org/wiki/API:Watch)
  * [watch.php](watch.php): add a page to your watchlist
* [API:Alllinks](https://www.mediawiki.org/wiki/API:Alllinks)
  * [get_alllinks.php](get_alllinks.php): list links to a namespace
* [API:Exturlusage](https://www.mediawiki.org/wiki/API:Exturlusage)
  * [get_exturlusage.php](get_exturlusage.php): enumerate pages that contain a given URL
* [API:RecentChanges](https://www.mediawiki.org/wiki/API:RecentChanges)
  * [get_recent_changes.php](get_recent_changes.php): get the three most recent changes with sizes and flags
* [API:Querypage](https://www.mediawiki.org/wiki/API:Querypage)
  * [get_querypage_list.php](get_querypage_list.php): List first 10 pages which are uncategorized
* [API:SetPageLanguage](https://www.mediawiki.org/wiki/API:SetPageLanguage)
  *  [set_page_language.php](set_page_language.php): change page language
* [API:Embeddedin](https://www.mediawiki.org/wiki/API:Embeddedin)
  * [get_embedded_pages.php](get_embedded_pages.php): get all page(s) that embed a page
* [API:Rollback](https://www.mediawiki.org/wiki/API:Rollback)
  * [rollback.php](rollback.php): rollback the last edits made to a given page
* [API:Allfileusages](https://www.mediawiki.org/wiki/API:Allfileusages)
  * [get_allfileusages.php](get_allfileusages.php): list of all file usages
* [API:Protect](https://www.mediawiki.org/wiki/API:Protect)
  * [protect.php](protect.php): Change the protection level of a given page
* [API:Upload](https://www.mediawiki.org/wiki/API:Upload)
  * [upload_file_from_url.php](upload_file_from_url.php): upload a file from a URL
* [API:Pagepropnames](https://www.mediawiki.org/wiki/API:Pagepropnames)
  * [get_pagepropnames.php](get_pagepropnames.php): List all page property names in use on the wiki
* [API:Protectedtitles](https://www.mediawiki.org/wiki/API:Protectedtitles)
  * [get_protectedtitles.php](get_protectedtitles.php): List the first 2 titles which only sysops can create
* [API:Imageusage](https://www.mediawiki.org/wiki/API:Imageusage)
  * [get_imageusage.php](get_imageusage.php): List the first three pages that use a given image title.
* [API:Import](https://www.mediawiki.org/wiki/API:Import)
  * [import_interwiki.php](import_interwiki.php): Import a page from another wiki by specifying its title
* [API:Patrol](https://www.mediawiki.org/wiki/API:Patrol)
  * [patrol.php](patrol.php): Patrol a recent change
* [API:Iwlinks](https://www.mediawiki.org/wiki/API:Iwlinks)
  * [get_iwlinks.php](get_iwlinks.php): get the interwiki links from a given page
* [API:Undelete](https://www.mediawiki.org/wiki/API:Undelete)
  * [undelete.php](undelete.php): restore two revisions of a deleted page
* [API:Logevents](https://www.mediawiki.org/wiki/API:Logevents)
  * [get_logevents.php](get_logevents.php): get the three most recent log events
* [API:Tags](https://www.mediawiki.org/wiki/API:Tags)
  * [get_tags.php](get_tags.php): get the first three change tags and their hitcounts
* [API:Allredirects](https://www.mediawiki.org/wiki/API:Allredirects)
  * [get_allredirects.php](get_allredirects.php): get the first three unique pages containing redirects to the main namespace
* [API:Alltransclusions](https://www.mediawiki.org/wiki/API:Alltransclusions)
  * [get_alltransclusions.php](get_alltransclusions.php): get three unique pages in the main namespace which contain transclusions
* [API:Mergehistory](https://www.mediawiki.org/wiki/API:Mergehistory)
  * [mergehistory.php](mergehistory.php): Merge the page revisions of Oldpage
    dating up to 2015-12-31T04:37:41Z into Newpage
* [API:Contributors](https://www.mediawiki.org/wiki/API:Contributors)
  * [get_contributors.js](get_contributors.php): get request to list all logged-in contributors and count of anonymous contributors to a page
* [API:Stashedit](https://www.mediawiki.org/wiki/API:Stashedit)
  * [stashedit.php](stashedit.php): Prepare an edit in shared cache
* [API:Filearchive](https://www.mediawiki.org/wiki/API:Filearchive)
  * [filearchive.php](filearchive.php): Enumerate all deleted files from filearchive table sequentially
* [API:Siteinfo](https://www.mediawiki.org/wiki/API:Siteinfo)
  * [general_site_info.php](general_site_info.php): obtain general site info
* [API:Expandtemplates](https://www.mediawiki.org/wiki/API:Expandtemplates)
  * [expand_templates.php](expand_templates.php): expand the Project:Sandbox template
* [API:ClearHasMsg](https://www.mediawiki.org/wiki/API:ClearHasMsg)
  * [clear_has_msg.php](clear_has_msg.php): clear the hasmsg flag for the current user
* [API:Compare](https://www.mediawiki.org/wiki/API:Compare)
  * [compare.php](compare.php): Compare the current revisions of two different pages
* [API:Tag](https://www.mediawiki.org/wiki/API:Tag)
  * [tag.php](tag.php): Remove the spam tag from log entry ID 123 with the reason Wrongly applied
* [API:Duplicatefiles](https://www.mediawiki.org/wiki/API:Duplicatefiles)
  * [duplicate_files.php](duplicate_files.php): list duplicates of the given files
* [API:Filerepoinfo](https://www.mediawiki.org/wiki/API:Filerepoinfo)
  * [file_repo_info.php](file_repo_info.php): get information about file repositories
* [API:Iwbacklinks](https://www.mediawiki.org/wiki/API:Iwbacklinks)
  * [iwbacklinks.php](iwbacklinks.php): Get pages that link to a given interwiki link.
* [API:Checktoken](https://www.mediawiki.org/wiki/API:Checktoken)
  * [check_token.php](check_token.php): Get request to check a CSRF token

### Search
* [API:Search](https://www.mediawiki.org/wiki/API:Search)
  * [search.php](search.php): search for a title or a text
* [API:Geosearch](https://www.mediawiki.org/wiki/API:Geosearch)
  * [geosearch.php](geosearch.php): search for pages nearby
  * [geoimagesearch.php](geoimagesearch.php): search for pages nearby with images
  * [geocoordinates.php](geocoordinates.php): obtain coordinates for wiki pages nearby
* [API:Opensearch](https://www.mediawiki.org/wiki/API:Opensearch)
  * [opensearch.php](opensearch.php): fetch results in an opensearch format
* [API:Prefixsearch](https://www.mediawiki.org/wiki/API:Prefixsearch)
  * [prefixsearch.php](prefixsearch.php): perform a prefix search for page titles
* [API:Languagesearch](https://www.mediawiki.org/wiki/API:Languagesearch)
  * [languagesearch.php](languagesearch.php): search for a language

### Basics
* [API:Parameter information](https://www.mediawiki.org/wiki/API:Parameter_information)
  * [paraminfo.php](paraminfo.php): get information about another action API module and its parameters
