/*  
    import_xml.js
 
    MediaWiki API Demos
    Demo of `Import` module: Import a page from another wiki
    by uploading its xml dump

    MIT license
*/

var fs = require('fs'),
    request = require('request').defaults({jar: true}),
    url = "http://dev.wiki.local.wmftest.net:8080/w/api.php";

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
        action: "clientlogin",
        username: "username",
        password: "password",
        loginreturnurl: "http://127.0.0.1:5000/",
        logintoken: login_token,
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
        import_xml(data.query.tokens.csrftoken);
    });
}

// Step 4: POST request to upload xml dump.
// xml dumps can be downloaded through Special:Export
// See https://www.mediawiki.org/wiki/Special:Export
function import_xml(csrf_token) {
    var params_3 = {
        action: "import",
        interwikiprefix: "en",
        token: csrf_token,
        format: "json"
    };

    var file = {
        xml: fs.createReadStream('a.xml')
    };

    var formData = Object.assign( {}, params_3, file );

    request.post({ url: url, formData: formData }, function (error, res, body) {
        if (error) {
            return;
        }
        console.log(body);
    });
}

// Start From Step 1
getLoginToken();