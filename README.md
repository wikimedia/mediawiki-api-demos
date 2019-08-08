<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/MediaWiki-notext.svg/500px-MediaWiki-notext.svg.png" height="200px" alt="MediaWiki"/>

# MediaWiki API Demos
The [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page) is a web service that allows access to some wiki-features like authentication, page operations, and search. It can provide meta information about the wiki and the logged-in user.

This repository contains demo apps and code snippets in various programming languages to assist developers for easy use of various modules of the API: 
* [Python](python/)
* [Javascript](javascript/)
* [PHP](php/)
* [MediaWikiJS](mediawikijs/)

### Apps
* [Article ideas generator](apps/article-ideas-generator):
Demo app that suggests articles from various categories that don't yet exist on English Wikipedia. The app uses [Parse](https://www.mediawiki.org/wiki/API:Parse) and [Links](https://www.mediawiki.org/wiki/API:Links) module.
* [Nearby places viewer](apps/nearby-places-viewer):
Demo of geo search for wiki pages near a location using the [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) and MediaWiki Action API's [Geosearch](https://www.mediawiki.org/wiki/API:Geosearch) module.
* [Picture of the day viewer](apps/picture-of-the-day-viewer):
Demo app that uses [prop=images](https://www.mediawiki.org/wiki/API:Images) module to fetch Wikipedia's Picture of the Day (POTD) from a template page and displays it on a webpage. The app also allows users to go backward or forward a date to view other POTD.
* [User contributions feed](apps/user-contributions-feed):
Demp app that uses [list=usercontribs](https://www.mediawiki.org/wiki/API:Usercontribs) module to fetch the top 50 edits made by a user.
* [View more demo apps](apps/)

### Installation
```
$ git clone https://github.com/wikimedia/mediawiki-api-demos.git
$ cd mediawiki-api-demos

For running python code samples: 
$ cd python
$ python3 filename.py 
Note: Install any necessary python modules with pip and enter any credentials 
required in the file to run the sample code

For running javascript code samples:
$ cd javascript
$ node filename.js
Note: Install any necessary node modules with npm and enter any credentials required
in the file to run the sample code

For running php code samples:
$ cd php
$ php filename.php
Note: Install necessary modules by `apt-get install php-cli php-curl` and enter any credentials
required in the file to run the sample code
```
