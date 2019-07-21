/*
	import_interwiki.js

	MediaWiki API Demos
	Demo of `Import` module: Import a page from another wiki by
    specifying its title

	MIT License
*/

var params = {
		action: 'import',
		interwikisource: 'en:w',
		interwikipage: 'Template:!-',
		fullhistory: 'true',
		namespace: '100',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
