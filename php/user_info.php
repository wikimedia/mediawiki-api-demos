<?php

/*
    user_info.php

    MediaWiki API Demos
    Demo of `Userinfo` module: Get general user info and user rights.

    MIT License
*/

$endPoint = "https://test.wikipedia.org/w/api.php";

$login_Token = getLoginToken(); // Step 1
loginRequest( $login_Token ); // Step 2
userInfo(); // Step 3

// Step 1: GET request to fetch login token
function getLoginToken() {
	global $endPoint;

	$params1 = [
		"action" => "query",
		"meta" => "tokens",
		"type" => "login",
		"format" => "json"
	];

	$url = $endPoint . "?" . http_build_query( $params1 );

	$ch = curl_init( $url );
	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

	$output = curl_exec( $ch );
	curl_close( $ch );

	$result = json_decode( $output, true );
	return $result["query"]["tokens"]["logintoken"];
}

// Step 2: Send a POST request to log in. For this login method, 
// obtain credentials by first visiting https://www.test.wikipedia.org/wiki/Manual:Bot_passwords
// See https://www.mediawiki.org/wiki/API:Login for more information on log in methods.
function loginRequest( $logintoken ) {
	global $endPoint;

	$params2 = [
		"action" => "login",
		"lgname" => "user_name",
		"lgpassword" => "password",
		"lgtoken" => $logintoken,
		"format" => "json"
	];

	$ch = curl_init();

	curl_setopt( $ch, CURLOPT_URL, $endPoint );
	curl_setopt( $ch, CURLOPT_POST, true );
	curl_setopt( $ch, CURLOPT_POSTFIELDS, http_build_query( $params2 ) );
	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

	$output = curl_exec( $ch );
	curl_close( $ch );
}

// Step 3: Send a GET request to get general user info and user rights.
function userInfo() {
    global $endPoint;

    $params = [
        "action" => "query",
        "meta" => "userinfo",
        "uiprop" => "rights",
        "format" => "json"
    ];

    $url = $endPoint . "?" . http_build_query( $params );

    $ch = curl_init( $url );
    curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
    $output = curl_exec( $ch );
    curl_close( $ch );

    $result = json_decode( $output, true );
    var_dump( $result );

}
