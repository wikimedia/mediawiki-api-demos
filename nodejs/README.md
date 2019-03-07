# MediaWiki Action API Code Samples
Code snippets in nodejs demonstrating how to use various modules of the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)

### Page Operations
* [API:Imageinfo](https://www.mediawiki.org/wiki/API:Imageinfo)
  * [get_imageinfo.js](nodejs/get_imageinfo.js) get information about an image file
* [API:Random](https://www.mediawiki.org/wiki/API:Backlinks)
  * [get_random.js](nodejs/get_random.js): get a list of random pages

### Installation
```
$ git clone https://github.com/wikimedia/MediaWiki-Action-API-Code-Samples.git
$ cd MediaWiki-Action-API-Code-Samples/nodejs
$ npm install request
$ node name_of_the_file.js
```