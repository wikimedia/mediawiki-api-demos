/*
    validatepassword.js

    MediaWiki Action API Code Samples
    Demo of `Validatepassword` module: Validate a password against the wiki's password policies.
    MIT license
*/


var request = require("request").defaults({jar: true}),
url = 'https://en.wikipedia.org/w/api.php';

function validatePassword() {
    var params = {
        action: "validatepassword",
        password: "your_password",
        format: "json"
    };
    
    request.post({ url: url, form: params }, function (error, res, body) {
        if (error) {
            return;
        }
        console.log(body);
    });
}
