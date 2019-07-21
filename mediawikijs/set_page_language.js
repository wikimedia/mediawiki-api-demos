/*
	set_page_language.js

	MediaWiki API Demos
	Demo of `SetPageLanguage` module: POST request to change
    the language of a page

	MIT License
*/

var params = {
		action: 'setpagelanguage',
		pageid: '66400',
		lang: 'es',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
