<?php

/*
    create_account.php

    MediaWiki API Demos
    Demo of `createaccount` module: Create an account on a wiki without the
    special authentication extensions
    MIT license
*/

$wikiUrl = "http://dev.wiki.local.wmftest.net:8080";
$endPoint = $wikiUrl . "/w/api.php";

$createAccount_Token = getCreateAccountToken(); // Step 1
createAccount( $createAccount_Token ); // Step 2

// Step 1: GET Request to fetch createaccount token
function getCreateAccountToken() {
	global $endPoint;

	$params1 = [
		"action" => "query",
		"meta" => "tokens",
		"type" => "createaccount",
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
	return $result["query"]["tokens"]["createaccounttoken"];
}

// Step 2: POST Request with the fetched token and other data (user information,
// return URL, etc.)  to the API to create an account
function createAccount( $createAccount_Token ) {
	global $endPoint, $wikiUrl;

	$params2 = [
		"action" => "createaccount",
		"createtoken" => $createAccount_Token,
		"username" => "your_username",
		"password" => "your_password",
		"retype" => "retype_your_password",
		"createreturnurl" => $wikiUrl,
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

	echo( $output );
}
