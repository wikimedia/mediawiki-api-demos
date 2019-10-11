<?php

/*
    get_all_deleted_revisions.php

    MediaWiki API Demos
    Demo of `alldeletedrevisions` module: List all the deleted revisions from User:Mahesh

    MIT License
*/

$endPoint ="https://www.thetestwiki.org/w/api.php"

$login_Token = getLoginToken(); // Step 1
loginRequest( $login_Token ); // Step 2
all_deleted_revisions(); // Step 3

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
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

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
		"lgname" => "bot_user_name",
		"lgpassword" => "bot_password",
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

// Step 3: GET Request to get all the deleted revisions
function all_deleted_revisions() {
	global $endPoint;

    $params3 = [
        "action" => "query",
        "list" => "alldeletedrevisions",
        "adruser" => "mahesh",
        "adrprop" => "ids|user|comment",

        "format" => "json"
    ];

	$url = $endPoint . "?" . http_build_query( $params3 );

	$ch = curl_init( $url );

	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	curl_setopt( $ch, CURLOPT_COOKIEJAR, "cookie.txt" );
	curl_setopt( $ch, CURLOPT_COOKIEFILE, "cookie.txt" );

	$output = curl_exec( $ch );
	curl_close( $ch );

    $result = json_decode( $output, true );

	foreach( $result["query"]["alldeletedrevisions"] as $page ){
        echo( "Revision for page " . $page["title"] . "\n" );
        foreach( $page["revisions"] as $adrev ){
            var_dump( $adrev );
        }
    }
}
