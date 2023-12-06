//This file is autogenerated. See modules.json and autogenerator.py for details

const fetch = require('node-fetch');

/*
    get_tags.js

    MediaWiki API Demos
    Demo of `Tags` module: Get the first three change tags and their hitcounts.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    format: "json",
    list: "tags",
    tgprop: "hitcount",
    tglimit: "3"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        var tags = response.query.tags;
        for (var t in tags) {
            console.log(tags[t].name);
        }
    })
    .catch(function(error){console.log(error);});
