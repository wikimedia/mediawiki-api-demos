# MediaWiki Action API Code Samples
Code snippets in Python demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.py](python/tokens.py): get tokens for data modifying operations
* [API:Login](https://www.mediawiki.org/wiki/API:Login)
  * [login.py](python/login.py) & [clientlogin.py](python/clientlogin.py): login

### Accounts and users 
* [API:Account creation](https://www.mediawiki.org/wiki/API:Account_creation)
  *  [create_account.py](python/create_account.py): create an account on a wiki without any special authentication extensions
  *  [create_account_with_captcha.py](python/create_account_with_captcha.py): Create an account on a wiki with a captcha enabling extension installed

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.py](python/parse.py): parse content of a page
  *  [parse_wikitable.py](python/search.py): parse a section of its page and fetch its table data
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.py](get_category_items.py): list twenty items in a category
  *  [get_recent_category_items.py](get_recent_category_items.py): get the ten articles most recently added to a category 
  *  [get_subcategories.py](get_subcategories.py): get ten subcategories of a category
* [API:Images](https://www.mediawiki.org/wiki/API:Images) 
  * [get_page_images.py](get_page_images.py): get page images embedded on a page
* [API:Purge](https://www.mediawiki.org/wiki/API:Purge)
  *  [purge_two_pages.py](python/purge_two_pages.py): purge cache of two or more pages
  *  [purge_namespace_pages.py](python/purge_namespace_pages.py): purge cache of the first 10 pages in the main namespace
* [API:Redirects](https://www.mediawiki.org/wiki/API:Redirects)
  *  [redirects.py](python/redirects.py): return redirects to the given page(s)
* [API:Delete](https://www.mediawiki.org/wiki/API:Delete)
  *  [delete.py](python/delete.py): delete a page
* [API:Revisions](https://www.mediawiki.org/wiki/API:Revisions)
  *  [get_pages_revisions.py](python/get_pages_revisions.py): get revision data of multiple pages
  *  [get_filtered_page_revisions.py](python/get_filtered_page_revisions.py): get revision data of a page filtered by date and user

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

### Demo apps
* [Article suggestion](python/demos/article%20suggestion): 
A sample app that uses MediaWiki Action API:Search allows you to pick a category and suggest articles to write on that don't yet exist on English Wikipedia. This app uses Flask and WTForms for rendering form.

### Installation
```
$ git clone https://github.com/srish/MediaWiki_Action_API_Code_Samples
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
$ python autogenerate.py
$ Make desired changes to the newly generated file(s)
```
