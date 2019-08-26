/*
	login.js

	MediaWiki API Demos
	Demo of `Login` module: Sending request to login

	MIT License
*/

var api = new mw.Api();

api.login( 'your_bot_username', 'your_bot_password' ).done( function ( data ) {
	console.log( 'You are logged in as ' + data.login.lgusername );
} );
