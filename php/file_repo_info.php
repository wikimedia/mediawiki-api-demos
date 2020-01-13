<?php

/*
    file_repo_info.php

    MediaWiki API Demos
    Demo of `Filerepoinfo` module: Get information about file repositories.

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "query",
    "meta" => "filerepoinfo",
    "format" => "json",
    "friprop" => "url|name|displayname"
];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

echo( $output );
