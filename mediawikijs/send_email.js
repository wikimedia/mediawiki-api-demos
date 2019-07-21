/*
	send_email.js

	MediaWiki API Demos
	Demo of `Emailuser` module: sending POST request to send email to wiki user

	MIT License
*/

var params = {
		action: 'emailuser',
		target: 'ABC',
		subject: 'Hi',
		text: 'Just wanted to say hi',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
