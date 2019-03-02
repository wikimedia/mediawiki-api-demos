# Article ideas generator
Demo app that suggests articles from various categories that don't yet exist on English Wikipedia. The app uses [Parse](https://www.mediawiki.org/wiki/API:Parse) and [Links](https://www.mediawiki.org/wiki/API:Links) module and fetches data from this resource:	
https://en.wikipedia.org/wiki/Wikipedia:Requested_articles

Install
-------

```
$ git clone https://github.com/wikimedia/MediaWiki-Action-API-Code-Samples
$ cd MediaWiki-Action-API-Code-Samples/python/demos/article ideas generator
$ pip install flask
Install the necessary python modules with pip
$ python3 articles.py
```

Screenshots
-----------
<table>
	<tr>
		<td>
			<img src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Article_ideas_generator_demo_app_screenshot_%282%29.png" width="300" style="border 5px solid black">
		</td>
		<td>
		<img src="https://upload.wikimedia.org/wikipedia/commons/f/f7/Article_ideas_generator_demo_app_screenshot_%283%29.png" width="300" style="border 5px solid black">
		</td>
		<td>
			<img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Article_ideas_generator_demo_app_screenshot_%284%29.png" width="300" style="border 5px solid black">
		</td>
	</tr>
	<tr>
		<td>1. Choose a category</td>
		<td>2. Choose a subcategory</td>
		<td>3. View missing links</td>
	</tr>
</table>
