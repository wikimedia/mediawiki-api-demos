/*  
    upload_file_directly.js
 
    MediaWiki API Demos
    Demo of `Upload` module: Sending post request to upload a file directly

    MIT license
*/

var fs = require('fs'),
    request = require('request').defaults({jar: true}),
    url = "https://test.wikipedia.org/w/api.php";

// Step 1: GET Request to fetch login token
function getLoginToken() {
    var params_0 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    };

    request.get({ url: url, qs: params_0 }, function (error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        loginRequest(data.query.tokens.logintoken);
    });
}

// Step 2: POST Request to log in. 
// Use of main account for login is not
// supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function loginRequest(login_token) {
    var params_1 = {
        action: "login",
        lgname: "bot_username",
        lgpassword: "bot_password",
        lgtoken: login_token,
        format: "json"
    };

    request.post({ url: url, form: params_1 }, function (error, res, body) {
        if (error) {
            return;
        }
        getCsrfToken();
    });
}

// Step 3: GET request to fetch CSRF token
function getCsrfToken() {
    var params_2 = {
        action: "query",
        meta: "tokens",
        format: "json"
    };

    request.get({ url: url, qs: params_2 }, function(error, res, body) {
        if (error) {
            return;
        }
        var data = JSON.parse(body);
        upload(data.query.tokens.csrftoken);
    });
}

// Step 4: POST request to upload a file directly
function upload(csrf_token) {
    var params_3 = {
        action: "upload",
        filename: "Sandboxfile1.jpg",
        ignorewarnings: "1",
        token: csrf_token,
        format: "json"
    };

    var file = {
        file: fs.createReadStream('My.jpg')
    };

    var formData = Object.assign( {}, params_3, file );

    request.post({ url: url, formData: formData }, function (error, res, body) {
        body = JSON.parse(body);
        if (error) {
            return;
        }
        else if (body.upload.result === "Success"){
            console.log("File Uploaded :)");
        }
    });
}

// Start From Step 1
getLoginToken();