/*
	change_user_options.js

	MediaWiki API Demos
	Demo of `Options` module: POST request to change three options
    for current user

	MIT License
*/

var params = {
		action: 'options',
		change: 'language=en|skin=monobook',
		optionname: 'nickname',
		optionvalue: 'custom-signa|ture',
		format: 'json'
	},
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
