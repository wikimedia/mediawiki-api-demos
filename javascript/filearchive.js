/*
    filearchive.js

    MediaWiki API Demos
    Demo of `Filearchive` module: Enumerate all deleted files from filearchive table sequentially.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php";

var params = {
  "action": "query",
  "format": "json",
  "list": "filearchive"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response) {
        var filearchive = response.query.filearchive;
        for (var f in filearchive) {
            console.log(filearchive[f].name);
        }
    })
    .catch(function(error){console.log(error);});
