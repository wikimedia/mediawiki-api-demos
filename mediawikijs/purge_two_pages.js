/*
	purge_namespace_pages.js

	MediaWiki API Demos
	Demo of `purge` module: Sending post request to purge first 10 pages in the main namespace

	MIT License
*/

var params = {
		action: 'purge',
		titles: 'Main_Page|Nonexistent',
		format: 'json'
	},
	api = new mw.Api();

api.post( params ).done( function ( data ) {
	console.log( data );
} );
