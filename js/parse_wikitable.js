
/* 
    parse_wikitable.js

    MediaWiki Action API Code Samples
    Demo of `Parse` module: Parse a section of a page, fetch its table data and save
    it to a CSV file

    MIT license
*/

let URL = "https://en.wikipedia.org/w/api.php";

let TITLE = "Wikipedia:Unusual_articles/Places_and_infrastructure";

const PARAMS = {
    'origin': "*",
    'action': "parse",
    'page': TITLE,
    'prop': 'wikitext',
    'section': 5,
    'format': "json"
}

function query_url(url, params) {
    let query = Object.keys(params).map(key => key + "=" + params[key]).join("&");
    return url + query;
}

function get_table() {
    /*
        Parse a section of a page, fetch its table data and save it to a CSV file
    */
    fetch(query_url(URL, PARAMS))
        .then(response => response.json())
        .then(response => {
            let data = response;
            let wikitext = data['parse']['wikitext']['*']; 
            let lines = wikitext.split('|-');
            let parsedData = "";

            lines.forEach(line => {
                if (line.indexOf('\n|') === 0) {
                    var tableRow = (line.slice(2).split('\n|'));
                    tableRow[0] = tableRow[0].trim().replace("'''[[", "").replace("]]'''", "");
                    parsedData += tableRow[0] + "," + tableRow[1] +"\n";
                }      
            });
            //TODO: save parsedData to a new csv file.
            console.log(parsedData);
        })
        .catch(error => console.log(error));
}

get_table();