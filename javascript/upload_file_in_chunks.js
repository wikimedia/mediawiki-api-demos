/*  
    upload_file_in_chunks.js
 
    MediaWiki API Demos
    Demo of `Upload` module: Step-by-step process to upload a file in chunks

    MIT license
*/

var fs = require('fs'),
    request = require('request').defaults({jar: true}),
    url = "http://dev.wiki.local.wmftest.net:8080/w/api.php",
    filename = "My.jpg";

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

// Step 4: POST request to upload a file
function upload(csrf_token) {
    /*
        Send multiple post requests to upload a file in chunks using `stash` mode.
        Stash mode is used to build a file up in pieces and then commit it at the end
    */
    var fileSizeInBytes = fs.statSync(filename).size;
    var headers = {
        "Content-Type": "multipart/form-data"
    };

    var params_3 = {
        action: "upload",
        stash: "1",
        filename: "Sandboxfile1.jpg",
        filesize: fileSizeInBytes,
        offset: "0",
        ignorewarnings: "1",
        token: csrf_token,
        format: "json"
    };

    var file = {
        file: fs.createReadStream(filename)
    };

    var formData = Object.assign( {}, params_3, file );

    request.post({ url: url, headers: headers, formData: formData }, function (error, res, body) {
        body = JSON.parse(body);
        if (error) {
            return;
        }

        params_4 = {
            action: "upload",
            filename: "Sandboxfile1.jpg",
            filekey: body.upload.filekey,
            comment: "Upload Testing",
            token: csrf_token,
            format: "json"
        };

        request.post({ url: url, form: params_4 }, function (error, res, body) {
            body = JSON.parse(body);
            if (error) {
                return;
            }
            console.log(body.upload.result);
        });
    });
}

// Start From Step 1
getLoginToken();