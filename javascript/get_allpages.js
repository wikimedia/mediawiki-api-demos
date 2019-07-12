//This file is autogenerated. See modules.json and autogenerator.py for details

/*
    get_allpages.js

    MediaWiki API Demos
    Demo of `Allpages` module: Get all pages whose title contains the text "Jungle," in whole or part.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    format: "json",
    list: "allpages",
    apfrom: "jungle"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        var pages = response.query.allpages;
        for (var p in pages) {
            console.log(pages[p].title);
        }
    })
    .catch(function(error){console.log(error);});
