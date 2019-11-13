/*
    validatepassword.js

    MediaWiki Action API Code Samples
    Demo of `Validatepassword` module: Validate a password against the wiki's password policies.
    MIT license
*/

    var params = {
        action: "validatepassword",
        password: "my_password",
        format: "json"
    },
	api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
	console.log( data );
} );
