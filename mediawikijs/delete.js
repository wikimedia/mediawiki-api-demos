/*
	delete.js

	MediaWiki API Demos
	Demo of `Delete` module: post request to delete a page

	MIT License
*/

var params = {
		action: 'delete',
		title: 'enter_a_page_title',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
