/*
    namespaces_and_aliases_site_info.js

    MediaWiki API Demos
    Demo of `Siteinfo` module: List namespaces and aliases site info.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    meta: "siteinfo",
    siprop: "namespaces|namespacealiases",
    formatversion: "2",
    format: "json"
};
request.get({ url: url, qs: params }, function(error, res, body) {
    if (error) {
        return;
    }
    console.log(body);
});
