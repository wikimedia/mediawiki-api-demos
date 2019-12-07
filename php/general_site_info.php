<?php

/*
    general_site_info.php

    MediaWiki API Demos
    Demo of `Siteinfo` module: Obtain general site info.

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "query",
    "meta" => "siteinfo",
    "formatversion" => "2",
    "format" => "json"
];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

echo( $output );
