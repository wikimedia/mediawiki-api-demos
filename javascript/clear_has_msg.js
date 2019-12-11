/*
	clear_has_msg.js

    MediaWiki API Demos
    Demo of `ClearHasMsg` module: Clear the hasmsg flag for the current user.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "clearhasmsg",
    format: "json"
};
request.post({ url: url, form: params }, function(error, res, body) {
    if (error) {
        return;
    }
    console.log(body);
});
