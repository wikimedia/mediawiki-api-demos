/*
    general_site_info.js

    MediaWiki API Demos
    Demo of `Siteinfo` module: Obtain general site info.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    meta: "siteinfo",
    formatversion: "2",
    format: "json"
};
request.get({ url: url, qs: params }, function(error, res, body) {
    if (error) {
        return;
    }
    console.log(body);
});
