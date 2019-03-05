/*
    edit.js
    MediaWiki Action API Code Samples
    Demo of `Edit` module: POST request to edit a page
    MIT license
*/

let URL = "https://test.wikipedia.org/w/api.php";

function query_url(url, params) {
    let query = Object.keys(params).map(key => key + "=" + params[key]).join("&");
    //    Object.keys(PARAMS_0).forEach(key => URL = URL + "&" + key + "=" + PARAMS_0[key]);

    return url + "?origin=*&" + query;
}

async function edit_page() {
    // Step 1: GET Request to fetch login token
    const PARAMS_0 = {
        'action': "query",
        'meta': "tokens",
        'type': "login",
        'format': "json"
    }

    let response = await fetch(query_url(URL, PARAMS_0));
    let data = await response.json();
    let LOGIN_TOKEN = data['query']['tokens']['logintoken'];

    // Step2: Send a post request to login. Use of main account for login is not
    //  supported. Obtain credentials via Special:BotPasswords
    // (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
    const PARAMS_1 = {
        'action': "login",
        'lgname': "your_bot_username",
        'lgpassword': "your_bot_password",
        'lgtoken': LOGIN_TOKEN,
        'format': "json"
    }

    response = await fetch(URL, {
        method: 'POST',
        body: JSON.stringify(PARAMS_1),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    // Step 3: GET request to fetch CSRF token
    const PARAMS_2 = {
        'action': "query",
        'meta': "tokens",
        'format': "json"
    }

    response = await fetch(query_url(URL, PARAMS_2));
    data = await response.json();
    let CSRF_TOKEN = data['query']['tokens']['csrftoken'];

    // Step 4: POST request to edit a page
    const PARAMS_3 = {
        'action': "edit",
        'title': "Sandbox",
        'token': CSRF_TOKEN,
        'format': "json",
        'appendtext': "Hello"
    }

    response = await fetch(URL, {
        method: 'POST',
        body: JSON.stringify(PARAMS_3),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    data = await response.json();

    console.log(data);
}

edit_page();