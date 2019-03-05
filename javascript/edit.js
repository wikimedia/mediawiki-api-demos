"use strict";

/** 
 * edit.js
 * 
 * MediaWiki Action API Code Samples
 * Demo of `Edit` module: POST request to edit a page
 * MIT license
 */

let URL = "https://test.wikipedia.org/w/api.php";

async function main() {
    // Step 1: GET Request to fetch login token
    const PARAMS_0 = {
        action: "query",
        meta: "tokens",
        type: "login",
        format: "json"
    }

    let query = URL + '?' + Object.keys(PARAMS_0).map(key => key + "=" + PARAMS_0[key]).join("&");
    let response = await fetch(query);
    let data = await response.json();

    let LOGIN_TOKEN = data.query.tokens.logintoken;

    // Step2: Send a post request to login. Use of main account for login is not
    //  supported. Obtain credentials via Special:BotPasswords
    // (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
    const PARAMS_1 = {
        action: "login",
        lgname: "your_bot_username",
        lgpassword: "your_bot_password",
        lgtoken: LOGIN_TOKEN,
        format: "json"
    }
    
    response = await fetch(URL, {
        method: 'POST',
        body: JSON.stringify(PARAMS_1),
    });

    // Step 3: GET request to fetch CSRF token
    const PARAMS_2 = {
        action: "query",
        meta: "tokens",
        format: "json"
    }

    query = URL + '?' + Object.keys(PARAMS_2).map(key => key + "=" + PARAMS_2[key]).join("&");
    response = await fetch(query);
    data = await response.json();

    let CSRF_TOKEN = data.query.tokens.csrftoken;

    // Step 4: POST request to edit a page
    const PARAMS_3 = {
        action: "edit",
        title: "Sandbox",
        token: CSRF_TOKEN,
        format: "json",
        appendtext: "Hello"
    }

    response = await fetch(URL, {
        method: 'POST',
        body: JSON.stringify(PARAMS_3),
    });
    data = await response.json();

    // console.log(data);
}

main();