# Javascript
Code snippets in Javascript demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.js](tokens.js): get tokens for data modifying operations
* [API:Logout](https://www.mediawiki.org/wiki/API:Logout)
  * [logout.js](logout.js): logout

### Accounts and users
* [API:User contributions](https://www.mediawiki.org/wiki/API:User_contributions)
  *  [get_usercontribs.js](get_usercontribs.js): list user contributions
* [API:Watchlist feed](https://www.mediawiki.org/wiki/API:Watchlist_feed)
  * [get_my_watchlist_feed.js](get_my_watchlist_feed.js): access an RSS feed of your own watchlist
  * [get_user_watchlist_feed.js](get_user_watchlist_feed.js): access an RSS feed of another user's watchlist
* [API:Rsd](https://www.mediawiki.org/wiki/API:Rsd)
  *  [rsd.js](rsd.js): export an RSD schema
* [API:Validatepassword](https://www.mediawiki.org/wiki/API:validatepassword)
  *  [validatepassword.js](validatepassword.js): validate a password against the wiki's password policies

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.js](parse.js): parse content of a page
  *  [parse_wikitable.js](search.js): parse a section of its page and fetch its table data
* [API:Pageswithprop](https://www.mediawiki.org/wiki/API:Pageswithprop)
  *  [get_pageswithprop.js](get_pageswithprop.js): list all pages using a given page property
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.js](get_category_items.js): list twenty items in a category
  *  [get_recent_category_items.js](get_recent_category_items.js): get the ten articles most recently added to a category
  *  [get_subcategories.js](get_subcategories.js): get ten subcategories of a category
* [API:Images](https://www.mediawiki.org/wiki/API:Images)
  * [get_page_images.js](get_page_images.js): get page images embedded on a page
* [API:Redirects](https://www.mediawiki.org/wiki/API:Redirects)
  *  [redirects.js](get_redirects.js): return redirects to the given page(s)
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
* [API:Mergehistory](https://www.mediawiki.org/wiki/API:Mergehistory)
  * [mergehistory.js](mergehistory.js): Merge the page revisions of Oldpage
    dating up to 2015-12-31T04:37:41Z into Newpage
* [API:Contributors](https://www.mediawiki.org/wiki/API:Contributors)
  * [get_contributors.js](get_contributors.js): get request to list all logged-in contributors and count of anonymous contributors to a page
* [API:Stashedit](https://www.mediawiki.org/wiki/API:Stashedit)
  * [stashedit.js](stashedit.js): Prepare an edit in shared cache
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
* [API:Iwbacklinks](https://www.mediawiki.org/wiki/API:Iwbacklinks)
  * [iwbacklinks.js](iwbacklinks.js): Get pages that link to a given interwiki link.
* [API:Checktoken](https://www.mediawiki.org/wiki/API:Checktoken)
  * [check_token.js](check_token.js): Check a CSRF token
* [API:Deletedrevisions](https://www.mediawiki.org/wiki/API:Deletedrevisions)
  * [deleted_revisions.js](deleted_revisions.js): Get a list of deleted revisions for Talk:Main Page.
* [API:Revisiondelete](https://www.mediawiki.org/wiki/API:Revisiondelete)
  * [revision_delete.js](revision_delete.js): Hide all information about a certain revision ID. 
  (The target, Sample Page, is unnecessary in this case.)

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

