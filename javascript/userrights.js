/*
   userrights.js

    MediaWiki Action API Code Samples
    Demo of `Userrights` module: Add and remove user rights by
    changing the user's group membership.
    MIT license
*/

var url = "https://test.wikipedia.org/w/api.php";

// Step 1: GET Request to fetch login token
var params_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
};

var query_url = url + "?";
Object.keys(params_1).forEach(function(key){query_url += "&" + key + "=" + params_1[key];});

fetch(query_url)
    .then(function(response){return response.json();})
    .then(function(response){
        var data = response;
        var login_token = data.query.tokens.logintoken;
        
        // Step2: Send a post request to login. Use of main account for login is not
        //  supported. Obtain credentials via Special:BotPasswords
        // (https://www.mediawiki.org/wiki/Special:BotPasswords)
        // for lgname & lgpassword

        var params_2 = {
            "action": "login",
            "lgname": "your_bot_username",
            "lgpassword": "your_bot_password",
            "lgtoken": login_token,
            "format": "json"
        };

        fetch(url , {
            method: "POST",
            body: JSON.stringify(params_2),
            headers: {
                "Content-Type": "application/json"
            }
            })
            .then(function(response){
                // Step 3: Obtain a Userrights token

                var params_3 = {
                    "action": "query",
                    "format": "json",
                    "meta": "tokens",
                    "type": "userrights"
                };

                query_url = url + "?";
                Object.keys(params_3).forEach(function(key){query_url += "&" + key + "=" + params_3[key];});
                
                fetch(query_url)
                    .then(function(response){return response.json();})
                    .then(function(response){
                        var data = response;
                        var userrights_token = data.query.tokens.userrightstoken;
                        
                        // Step 4:Post request to add or remove a user from a group

                        var params_4 = {
                            "action": "userrights",
                            "format": "json",
                            "user": "Bob",
                            "add": "sysop",
                            "remove": "bureaucrat",
                            "reason": "OOPS! added Bob to the wrong group",
                            "token": userrights_token
                        };

                        fetch(url, {
                            method: "POST",
                            body: JSON.stringify(params_4),
                            headers: {
                                "Content-Type": "application/json"
                            }
                            })
                            .then(function(response){
                                var data = response;
                                console.log(data);
                            })
                            .catch(function(error){console.log(error);});
                    })
                    .catch(function(error){console.log(error);});
            })
            .catch(function(error){console.log(error);});   
    })
    .catch(function(error){console.log(error);});