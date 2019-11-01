/*
    get_deleted_revs.js

    MediaWiki API Demos
    Demo of `Deleted revisions:Get a list of deleted revision for Talk:Main Page` module

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    format: "json",
    titles: "Talk:MainPage",
    prop:   "deletedrevisions",
    drv:    "prop"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        console.log(response);
    })
    .catch(function(error){console.log(error);});
