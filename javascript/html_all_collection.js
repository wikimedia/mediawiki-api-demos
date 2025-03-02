/*
    html_all_collection.js

    Implementation and testing of the HTMLAllCollection interface according to the HTML Standard

    MIT License
*/

// Implement the HTMLAllCollection interface
class HTMLAllCollection {
    constructor() {
        this.elements = document.all;
    }

    // Retrieve all elements in the document
    getAllElements() {
        return this.elements;
    }

    // Retrieve elements by name or id
    getElementsByNameOrId(nameOrId) {
        return this.elements[nameOrId];
    }

    // Retrieve elements by index
    getElementByIndex(index) {
        return this.elements[index];
    }

    // Check if an element exists in the collection
    elementExists(element) {
        return Array.prototype.includes.call(this.elements, element);
    }
}

// Example usage
const htmlAllCollection = new HTMLAllCollection();
console.log(htmlAllCollection.getAllElements());
console.log(htmlAllCollection.getElementsByNameOrId('exampleId'));
console.log(htmlAllCollection.getElementByIndex(0));
console.log(htmlAllCollection.elementExists(document.getElementById('exampleId')));
