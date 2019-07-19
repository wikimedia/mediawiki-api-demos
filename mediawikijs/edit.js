/*
	edit.js

	MediaWiki API Demos
	Demo of `Edit` module: POST request to edit a page

	MIT License
*/

var params = {
		action: 'edit',
		title: 'Sandbox',
		appendtext: 'Hello',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
