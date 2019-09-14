/*
    upload_file_in_chunks.js

    MediaWiki API Demos
    Demo of `Upload` module: Step-by-step process to upload a file in chunks
    MIT license
*/

var param = {
		filename: 'TestFile_2.jpg',
		format: 'json',
		ignorewarnings: 1
	},
	fileInput = $( '<input/>' ).attr( 'type', 'file' ),
	submitBtn = $( '<input/>' ).attr( 'type', 'button' ).attr( 'value', 'Upload' ),
	api = new mw.Api();

$( '#bodyContent' ).append( [ fileInput, submitBtn ] );

$( submitBtn ).on( 'click', function () {
	api.uploadToStash( fileInput[ 0 ], param ).done( function ( finish ) {
		finish( param ).done( function ( data ) {
			console.log( data.upload.filename + ' has sucessfully uploaded.' );
		} ).fail( function ( data ) {
			console.log( data );
		} );
	} );
} );
