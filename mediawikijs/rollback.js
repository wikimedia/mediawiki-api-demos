/*
	rollback.js

	MediaWiki API Demos
	Demo of `rollback` module: Sending post request to rollback the
    last edits made to a given page.

	MIT License
*/

var params = {
		action: 'rollback',
		title: 'Sandbox',
		user: '10.0.2.2',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'rollback', params ).done( function ( data ) {
	console.log( data );
} );
