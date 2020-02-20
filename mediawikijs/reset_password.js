/*
	reset_password.js

    MediaWiki API Demos
    Demo of `Resetpassword` module: Reset password for all users with an email address.

    MIT license
*/

var params = {
    action: 'resetpassword',
    email: 'user@mediawiki.org',
    format: 'json'
},
api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
console.log( data );
} );