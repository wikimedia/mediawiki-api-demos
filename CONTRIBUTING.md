#  Contributing

From opening a bug report to creating a pull request: we appreciate and welcome
every contribution. If you're planning to implement a new feature or change
the API please create an issue first. This way we can ensure that your precious
work is not in vain.

There is a series of blog posts over at the [website](https://martyav.github.io/), detailing the experiences of Marty Hernandez Avedon at Wikimedia. This one in particular should be helpful for people working on the [documentation project](https://martyav.github.io/2019-01-03-wikimedia-week-5/)

### Installation
```
$ git clone https://github.com/wikimedia/MediaWiki-Action-API-Code-Samples.git
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
$ python autogenerator.py
$ Make desired changes to the newly generated file(s)
```

## Issues

If you are having difficulty after looking over your configuration carefully, please post
a question to [StackOverflow with the mediawiki tag](http://stackoverflow.com/tags/mediawiki).

**If you have discovered a bug or have a feature suggestion, please [create an issue on GitHub](https://github.com/wikimedia/MediaWiki-Action-API-Code-Samples/issues/new).**

Do you want to fix an issue?  Look at the [issues](https://github.com/wikimedia/MediaWiki-Action-API-Code-Samples/issues).

## Working on an Action Page

* Read the project description thoroughly and the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page) too.
* Pick an action page from the [list of the action APIs](https://www.mediawiki.org/wiki/Category:MediaWiki_action_API) that you would like to review and improve.
* Create a page in [your Sandbox](https://www.mediawiki.org/wiki/User:your_username/Sandbox/API:pagename) and do not make edits directly to the API pages.
* Fill it with the template content which is in [here](https://www.mediawiki.org/wiki/API:Documentation_template) (copy and paste). We encourage you to stick to the template if for some reason you feel the urge to add or remove any section, discuss with your mentors.
* For your reference, read a couple recent API pages that we modified using the new template: [API:Geosearch](https://www.mediawiki.org/wiki/API:Geosearch), [API:Parsing_wikitext](https://www.mediawiki.org/wiki/API:Parsing_wikitext)
* Contribute sample code for the API page to [this repository](https://github.com/wikimedia/MediaWiki-Action-API-Code-Samples).
* When you are done, get some feedback on your work on [Zulip](https://wikimedia.zulipchat.com/#narrow/stream/180873-gsoc19-outreachy18).

## Submitting Changes

After getting some feedbacks, push to your fork and submit a pull request. We
may suggest some changes or improvements or alternatives, but for small changes
your pull request should be accepted quickly.

Something that will increase the chance that your pull request is accepted:

* Follow the existing coding style
* Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
* When you are done making changes, make sure to run your python file with [Pylint](https://pylint.org) that will help you to produce a more cleaner and well-indented code.

## Documentation

We greatly appreciate any time spent fixing typos or clarifying sections in the
documentation.

## Discussions

For any doubts or discussions regarding the project, reach out to [ZulipChat](https://wikimedia.zulipchat.com/#narrow/stream/180873-gsoc19-outreachy18)
