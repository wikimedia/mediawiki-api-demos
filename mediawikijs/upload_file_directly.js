/*
    upload_file_directly.js

    MediaWiki API Demos
    Demo of `Upload` module: Sending post request to upload a file directly
    MIT license
*/

var param = {
		filename: 'File_1.jpg',
		format: 'json',
		ignorewarnings: 1
	},
	fileInput = $( '<input/>' ).attr( 'type', 'file' ),
	submitBtn = $( '<input/>' ).attr( 'type', 'button' ).attr( 'value', 'Upload' ),
	api = new mw.Api();

$( '#bodyContent' ).append( [ fileInput, submitBtn ] );

$( submitBtn ).on( 'click', function () {
	api.upload( fileInput[ 0 ], param ).done( function ( data ) {
		console.log( data.upload.filename + ' has sucessfully uploaded.' );
	} ).fail( function ( data ) {
		console.log( data );
	} );
} );
