/*
	duplicate_files.js

    MediaWiki API Demos
    Demo of `Duplicatefiles` module: List duplicates of the given files.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "query",
    titles: "Image:1995.jpg|Image:Welcome.gif",
    prop: "duplicatefiles",
    format: "json"
};
request.get({ url: url, qs: params }, function(error, res, body) {
    if (error) {
        return;
    }
    console.log(body);
});
