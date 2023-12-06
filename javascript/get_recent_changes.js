//This file is autogenerated. See modules.json and autogenerator.py for details

const fetch = require('node-fetch');

/*
    get_recent_changes.js

    MediaWiki API Demos
    Demo of `RecentChanges` module: Get the three most recent changes with sizes and flags

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    list: "recentchanges",
    rcprop: "title|ids|sizes|flags|user",
    rclimit: "3",
    format: "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        var recentchanges = response.query.recentchanges;
        for (var rc in recentchanges) {
            console.log(recentchanges[rc].title);
        }
    })
    .catch(function(error){console.log(error);});
