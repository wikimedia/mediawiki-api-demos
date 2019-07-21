/*
	undelete.js

	MediaWiki API Demos
	Demo of `Undelete` module: Restore two revisions of a deleted page

	MIT License
*/

var params = {
		action: 'undelete',
		title: 'Sandbox',
		reason: 'Test undeleting via the API',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
