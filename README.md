# MediaWiki Action API Code Samples
Code snippets in Python demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Authentication
* [API:Tokens](https://www.mediawiki.org/wiki/API:Tokens)
  * [tokens.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/tokens.py): get tokens for data modifying operations
* [API:Login](https://www.mediawiki.org/wiki/API:Login)
  * [login.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/login.py) & [clientlogin.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/clientlogin.py): login

### Page Operations
* [API:Parse](https://www.mediawiki.org/wiki/API:Parse)
  *  [parse.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/parse.py): parse content of a page
  *  [parse_wikitable.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/search.py): parse a section of its page and fetch its table data
* [API:Categorymembers](https://www.mediawiki.org/wiki/API:Categorymembers)
  *  [get_category_items.py](get_category_items.py): list twenty items in a category
  *  [get_recent_category_items.py](get_recent_category_items.py): get the ten articles most recently added to a category 
  *  [get_subcategories.py](get_subcategories.py): get ten subcategories of a category
* [API:Purge](https://www.mediawiki.org/wiki/API:Purge)
  *  [purge_two_pages.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/purge_two_pages.py): purge cache of two or more pages
  *  [purge_namespace_pages.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/purge_namespace_pages.py): purge cache of the first 10 pages in the main namespace
* [API:Random](https://www.mediawiki.org/wiki/API:Purge)
  *  [get_two_random_pages.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/random_page.py): get list of two random pages by specifying rnlimit
  *  [get_random_set_of_pages.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/random_pages.py): get random set of pages including information such as titles, content, images, etc.


### Search 
* [API:Search](https://www.mediawiki.org/wiki/API:Search)
  * [search.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/search.py): search for a title or a text
* [API:Geosearch](https://www.mediawiki.org/wiki/API:Geosearch)
  * [geosearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/geosearch.py): search for pages nearby
  * [geoimagesearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/geoimagesearch.py): search for pages nearby with images
  * [geocoordinates.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/geocoordinates.py): obtain coordinates for wiki pages nearby
* [API:Opensearch](https://www.mediawiki.org/wiki/API:Opensearch)
  * [opensearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/opensearch.py): fetch results in an opensearch format
* [API:Prefixsearch](https://www.mediawiki.org/wiki/API:Prefixsearch)
  * [prefixsearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/prefixsearch.py): perform a prefix search for page titles
* [API:Languagesearch](https://www.mediawiki.org/wiki/API:Languagesearch)
  * [languagesearch.py](https://github.com/srish/MediaWiki_Action_API_Code_Samples/blob/master/languagesearch.py): search for a language 

### Demo apps
* [Article suggestion](https://github.com/srish/MediaWiki_Action_API_Code_Samples/tree/master/demos/article%20suggestion): 
A sample app that uses MediaWiki Action API:Search allows you to pick a category and suggest articles to write on that don't yet exist on English Wikipedia. This app uses Flask and WTForms for rendering form.

### Installation
```
$ git clone https://github.com/srish/MediaWiki_Action_API_Code_Samples
$ cd MediaWiki_Action_API_Code_Samples
Install the necessary python modules with pip
$ python3 name_of_the_file.py #Enter any credentials if required in the file
```
