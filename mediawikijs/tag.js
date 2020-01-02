/*
	tag.js

    MediaWiki API Demos
    Demo of `Tag` module: Remove the spam tag from log entry ID 123 with the reason Wrongly applied

    MIT license
*/

var params = {
    
    action: "compare",
    format: "json",
    token: csrf_token,
    logid: "123",
    remove: "spam",
    reason: "Wrongly applied"
},
api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
console.log( data );
} );
