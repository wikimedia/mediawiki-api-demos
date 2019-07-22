<?php

/*
    purge_namespace_pages.php

    MediaWiki API Demos
	Demo of `purge` module: Sending post request to purge first 10 pages in the main namespace

    MIT license
*/

$endPoint = "https://en.wikipedia.org/w/api.php";

purge();

function purge() {
	global $endPoint;

	$params = [
		"action" => "purge",
		"generator" => "allpages",
		"gapnamespace" => "0",
		"gaplimit" => "10",
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
