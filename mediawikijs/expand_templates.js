/*
	expand_templates.js

    MediaWiki API Demos
    Demo of `Expandtemplates` module: Expand the Project:Sandbox template.

    MIT License
*/

var params = {
    action: "expandtemplates",
    text: "{{Project:Sandbox}}",
    prop: "wikitext",
    format: "json"
},
api = new mw.Api();

api.get( params ).done( function ( data ) {
console.log( data );
} );
