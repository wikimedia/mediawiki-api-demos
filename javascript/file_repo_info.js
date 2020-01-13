/*
	file_repo_info.js

    MediaWiki API Demos
    Demo of `Filerepoinfo` module: Get information about file repositories.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    meta: "filerepoinfo",
    format: "json",
    friprop: "url|name|displayname"
};
request.get({ url: url, qs: params }, function(error, res, body) {
    if (error) {
        return;
    }
    console.log(body);
});
