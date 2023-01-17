# Contribution guidelines
Have you developed a demo app using the [MediaWiki Action API](https://www.mediawiki.org/wiki/API:Main_page)? We would love to showcase it in the MediaWiki Apps Gallery!
 
Learn below the criteria for a demo app we are looking to integrate into the gallery and submission instructions.

## App criteria
- Simple and easy to understand and use for all types of developers and API consumers
- Demonstrates use of more than one API module
- Consists of <=1000 lines of code
- Built in any programming language or framework that is widely used (e.g., Python, Flask, Node.js, Django, etc.)
- Both the source code and the app is hosted somewhere.
- Optionally, the app is hosted on Toolforge and the source code in the apps folder of [mediawiki-api-demos repository](https://github.com/wikimedia/mediawiki-api-demos). If you wish to add your app to this repository, make sure you comply with the MIT license that the repo uses.

## Submitting your app
  - If you would like to host the source code of your demo app in this repository, send a pull request.
  - Add your app details to the `apps.json` file in the `gallery` folder in the following format:
  ```
     {
      "title": "name of the app in < 20 chars", 
      "thumbnail": "app thumbnail of ratio ~1:1.6 (e.g., 765x484 pixels)”,
      "description": "description of the app in < 75 chars”,
      "modules": [“api module used 1", “api module used 2”, “...”], 
      "source": "link to the source code",
      "owner": "your GitHub username",
      “url”: “hosted app link,
  }
  ```
