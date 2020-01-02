/*
    compare.js

    MediaWiki Action API Code Samples
    Demo of `Compare` module: Compare the current revisions of two different pages

    MIT license
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "compare",
    format: "json",
    fromtitle: "Template:Unsigned",
    totitle: "Template:UnsignedIP"

};
request.get({ url: url, qs: params }, function(error, res, body) {
    if (error) {
        return;
    }
    console.log(body);
});