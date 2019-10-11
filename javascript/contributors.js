/*  
    contributors.js
 
    MediaWiki API Demos
    Demo of `Contributors` module: List all logged-in contributors and count of anonymous contributors to a page.

    MIT license
*/

const fetch = require('node-fetch');
var url = "https://en.wikipedia.org/w/api.php";

var params = {
    action: "query",
    titles: "MediaWiki",
    prop: "contributors",
    format: "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        var pages = response.query.pages;
        for (var page in pages) {
            console.log(pages[page].anoncontributors);
            console.log(pages[page].contributors);
        }
    })
    .catch(function(error){console.log(error);});
