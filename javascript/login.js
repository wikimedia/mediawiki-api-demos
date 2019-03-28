/* 
    login.js
    MediaWiki Action API Code Samples
    Demo of `Login` module: Sending post request to login
    MIT license
*/
var fetch = require('node-fetch');
var url = "https://mediawiki.org/w/api.php";
url = url + "?";
var cookie;

// Step 1: GET Request to fetch login token
function getLoginToken() {
    var PARAMS_0 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    };

    var query = url;
    Object.keys(PARAMS_0).forEach(function (key) {
        query += "&" + key + "=" + PARAMS_0[key];
    });

    fetch(query)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            doLogin(data.query.tokens.logintoken);
        })
        .catch(function (error) {
            console.log(error);
        });
}
// Step 2: POST Request to log in. 
// Use of main account for login is not
// supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
function doLogin(LOGIN_TOKEN){
	var PARAMS_1 = {
    action:"login",
    lgname:"your_bot_username",
    lgpassword:"your_bot_password",
    lgtoken:LOGIN_TOKEN,
    format:"json"
};
  fetch(url,{credentials:"include",
              method:"POST",
			  body:JSON.stringify(PARAMS_1),
			  header:{
				  "Content-type":"application/json"
			  }
  })
  .then(function(response){
	  var setCookie = response.headers.get('set-cookie');
      cookie = setCookie.substr(0, setCookie.indexOf(';'));
	  return response.json();
  })
   .then(function (data) {
            console.log(data)
    })
  .catch(function (error){
	  console.log(error);
  });
  }
