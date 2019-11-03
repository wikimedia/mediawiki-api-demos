<?php
/*
    get_deleted_revs.php

    MediaWiki API Demos
    Demo of `Deleted revisions:Get a list of deleted revision for Talk:Main Page` module

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";

$login_Token = getLoginToken(); // Step 1
loginRequest( $login_Token ); // Step 2


// Step 1: GET Request to fetch login token
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
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "/tmp/cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "/tmp/cookie.txt" );

	$output = curl_exec( $ch );
	curl_close( $ch );

	$result = json_decode( $output, true );
	return $result["query"]["tokens"]["logintoken"];
}

// Step 2: POST Request to log in. Use of main account for login is not
// supported. Obtain credentials via Special:BotPasswords
// (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

function loginRequest( $logintoken ) {
	global $endPoint;

	$params2 = [
		"action" => "login",
		"lgname" => "your_bot_username",
		"lgpassword" => "your_bot_password",
		"lgtoken" => $logintoken,
		"format" => "json"
	];

	$ch = curl_init();

	curl_setopt( $ch, CURLOPT_URL, $endPoint );
	curl_setopt( $ch, CURLOPT_POST, true );
	curl_setopt( $ch, CURLOPT_POSTFIELDS, http_build_query( $params2 ) );
	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "/tmp/cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "/tmp/cookie.txt" );

	$output = curl_exec( $ch );
	curl_close( $ch );

	echo( $output);

}

// Step 3: GET Request to get a list of deleted revisions

$endPoint = "https://en.wikipedia.org/w/api.php";
$params3 = [
    "action" => "query",
    "format" => "json",
    "titles" => "Talk:MainPage",
    "prop"   => "deletedrevisions",
    "drv"    => "prop"
];

$url = $endPoint . "?" . http_build_query( $params3 );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

$result = json_decode( $output, true );

echo( $result );