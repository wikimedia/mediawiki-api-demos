<?php
/*
    get_deleted_revs.php

    MediaWiki API Demos
    Demo of `Deleted revisions:Get a list of deleted revision for Talk:Main Page` module

    MIT License
*/

$endPoint = "https://en.wikipedia.org/w/api.php";
$params = [
    "action" => "query",
    "format" => "json",
    "titles" => "Talk:MainPage",
    "prop"   => "deletedrevisions",
    "drv"    => "prop"
];

$url = $endPoint . "?" . http_build_query( $params );

$ch = curl_init( $url );
curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
$output = curl_exec( $ch );
curl_close( $ch );

$result = json_decode( $output, true );

echo( $result );