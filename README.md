# MediaWiki Action API Code Samples
Code snippets in Python demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/tokens.py): get tokens for data modifying operations
* [API:Login](https://www.mediawiki.org/wiki/API:Login)
  * [login.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/login.py) & [clientlogin.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/clientlogin.py): login

### Accounts and users 
* [API:Account creation](https://www.mediawiki.org/wiki/API:Account_creation)
  *  [create_account.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/create_account.py): create an account on a wiki without any special authentication extensions
  *  [create_account_with_captcha.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/create_account_with_captcha.py): Create an account on a wiki with a captcha enabling extension installed

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/parse.py): parse content of a page
  *  [parse_wikitable.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/search.py): parse a section of its page and fetch its table data
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.py](get_category_items.py): list twenty items in a category
  *  [get_recent_category_items.py](get_recent_category_items.py): get the ten articles most recently added to a category 
  *  [get_subcategories.py](get_subcategories.py): get ten subcategories of a category
* [API:Images](https://www.mediawiki.org/wiki/API:Images) 
  * [get_page_images.py](get_page_images.py): get page images embedded on a page
* [API:Purge](https://www.mediawiki.org/wiki/API:Purge)
  *  [purge_two_pages.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/purge_two_pages.py): purge cache of two or more pages
  *  [purge_namespace_pages.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/purge_namespace_pages.py): purge cache of the first 10 pages in the main namespace
* [API:Redirects](https://www.mediawiki.org/wiki/API:Redirects)
  *  [redirects.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/redirects.py): return redirects to the given page(s)

### Search 
* [API:Search](https://www.mediawiki.org/wiki/API:Search)
  * [search.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/search.py): search for a title or a text
* [API:Geosearch](https://www.mediawiki.org/wiki/API:Geosearch)
  * [geosearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/geosearch.py): search for pages nearby
  * [geoimagesearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/geoimagesearch.py): search for pages nearby with images
  * [geocoordinates.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/geocoordinates.py): obtain coordinates for wiki pages nearby
* [API:Opensearch](https://www.mediawiki.org/wiki/API:Opensearch)
  * [opensearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/opensearch.py): fetch results in an opensearch format
* [API:Prefixsearch](https://www.mediawiki.org/wiki/API:Prefixsearch)
  * [prefixsearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/prefixsearch.py): perform a prefix search for page titles
* [API:Languagesearch](https://www.mediawiki.org/wiki/API:Languagesearch)
  * [languagesearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/languagesearch.py): search for a language 

### Demo apps
* [Article suggestion](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/python/demos/article%20suggestion): 
A sample app that uses MediaWiki Action API:Search allows you to pick a category and suggest articles to write on that don't yet exist on English Wikipedia. This app uses Flask and WTForms for rendering form.

### Installation
```
$ git clone https://github.com/srish/MediaWiki_Action_API_Code_Samples
$ cd MediaWiki-Action-API-Code-Samples
Install the necessary python modules with pip
$ python3 name_of_the_file.py #Enter any credentials if required in the file
```

### Contributing code samples
* First, propose an idea for a code sample, demo app, etc. by creating an issue around it in the repository. After discussing your idea with the repo contributors, start working, and then send a pull request, when you've your changes ready to be accepted/ merged!  
* You can autogenerate python files for GET Requests demos where feasible by following the instructions below:
  ```
  * $ cd MediaWiki-Action-API-Code-Samples
  * $ cd python
  * $ Add module information to `modules.json`
  * $ python autogenerate.py # This will autogenerate new files
  * $ Make additional changes to the new file such as printing output in a desired format
  ```
