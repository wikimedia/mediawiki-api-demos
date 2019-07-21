/*
	create_account.js

	MediaWiki API Demos
    Demo of `createaccount` module: Create an account on a wiki without the
    special authentication extensions

	MIT License
*/

var params = {
		action: 'query',
		meta: 'tokens',
		type: 'createaccount',
		format: 'json'
	},
	api = new mw.Api();

api.get( params ).done( function ( data ) {
	var token = data.query.tokens.createaccounttoken,
		params1 = {
			action: 'createaccount',
			username: 'your_username',
			password: 'your_password',
			retype: 'retype_your_password',
			createreturnurl: 'http:' + mw.config.get( 'wgServer' ),
			createtoken: token,
			format: 'json'
		};

	api.post( params1 ).done( function ( data ) {
		console.log( data );
	} );
} );
