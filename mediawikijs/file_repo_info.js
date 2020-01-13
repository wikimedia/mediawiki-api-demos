/*
	file_repo_info.js

    MediaWiki API Demos
    Demo of `Filerepoinfo` module: Get information about file repositories.

    MIT License
*/

var params = {
    action: "query",
    meta: "filerepoinfo",
    format: "json",
    friprop: "url|name|displayname"
},
api = new mw.Api();

api.get( params ).done( function ( data ) {
console.log( data );
} );
