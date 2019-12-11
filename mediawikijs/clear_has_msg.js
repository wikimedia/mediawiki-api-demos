/*
	clear_has_msg.js

    MediaWiki API Demos
    Demo of `ClearHasMsg` module: Clear the hasmsg flag for the current user.

    MIT License
*/

var params = {
    action: "clearhasmsg",
    format: "json"
},
api = new mw.Api();

api.post( params ).done( function ( data ) {
console.log( data );
} );
