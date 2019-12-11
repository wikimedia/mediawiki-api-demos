/*
	expand_templates.js

    MediaWiki API Demos
    Demo of `Expandtemplates` module: Expand the Project:Sandbox template.

    MIT License
*/

var url = "https://en.wikipedia.org/w/api.php"; 

var params = {
    action: "expandtemplates",
    text: "{{Project:Sandbox}}",
    prop: "wikitext",
    format: "json"
};
request.get({ url: url, qs: params }, function(error, res, body) {
    if (error) {
        return;
    }
    console.log(body);
});
