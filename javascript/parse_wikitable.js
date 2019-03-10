/*
    parse_wikitable.js

    MediaWiki Action API Code Samples
    Demo of `Parse` module: Parse a section of a page,
    fetch its table data and save it to a CSV file
    MIT license
*/

var url = "https://en.wikipedia.org/w/api.php";

var title = "Wikipedia:Unusual_articles/Places_and_infrastructure";

var params = {
    "action": "parse",
    "page": title,
    "prop": "wikitext",
    "section": 5,
    "format": "json"
};

url = url + "?origin=*";
Object.keys(params).forEach(function(key){url += "&" + key + "=" + params[key];});

fetch(url)
    .then(function(response){return response.json();})
    .then(function(response){
        var data = response;
        var wikitext = data.parse.wikitext['*'];
        var lines = wikitext.split("|-");
        var parsedData = "";

        lines.forEach(function(line) {
            if (line.indexOf("\n|") === 0){
                var tableRow = (line.slice(2).split("\n|"));
                tableRow[0] = tableRow[0].trim().replace("'''[[", "").replace("]]'''", "");
                parsedData += tableRow[0] + "," + tableRow[1] +"\n";
            }
        });
        
        console.log(parsedData);
    })
    .catch(function(error){console.log(error);});
