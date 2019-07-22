<?php

/*
    purge_two_pages.php

    MediaWiki API Demos
	Demo of `purge` module: Sending post request to purge two or more pages

    MIT license
*/

$endPoint = "https://en.wikipedia.org/w/api.php";

purge();

function purge() {
	global $endPoint;

	$params = [
		"action" => "purge",
		"titles" => "Main_Page|Nonexistent",
		"format" => "json"
	];

	$ch = curl_init();

	curl_setopt( $ch, CURLOPT_URL, $endPoint );
	curl_setopt( $ch, CURLOPT_POST, true );
	curl_setopt( $ch, CURLOPT_POSTFIELDS, http_build_query( $params ) );
	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );

	$output = curl_exec( $ch );
	curl_close( $ch );

	echo ( $output );
}
