/*
	revision_delete.js

    MediaWiki API Demos
    Demo of `Revisiondelete` module: Hide all information about a certain revision ID.

    MIT license
*/

var params = {
    action: 'revisiondelete',
    type: 'revision',
    ids: '71',
    format: 'json',
    hide: 'content|comment|user',
    reason: 'Because',
},
api = new mw.Api();

api.postWithToken( 'csrf', params ).done( function ( data ) {
console.log( data );
} );