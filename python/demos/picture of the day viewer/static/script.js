document.addEventListener("DOMContentLoaded", function() {
    const linksDiv = document.querySelector(".links");
    let xmlHttp = new XMLHttpRequest();

    // Helper functions

    const prepItemUrlHtml = function(url) {
        return "<a href = ".concat(url).concat(" target = \"blank\">");
    }

    const prepItemTitleHtml = function(title, url) {
        const openLinkTag = prepItemUrlHtml(url);

        return "<h2>".concat(openLinkTag).concat(title).concat("</a>").concat("</h2>");
    }

    const prepItemImageHtml = function(image) {
        return "<img src =".concat(image).concat(" width = 500>");
    }

    const prepContainerDivHtml = function(...args) {
        let divContainer = "<div>";

        for (let item of args) {
            divContainer += item;
        }

        return divContainer.concat('</div>')
    }

    const prepLinkItemHtml = function(item) {
        return "<li>".concat(item).concat("</li>"); 
    }

    // The actual call

    xmlHttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (xmlHttp.status == 200) {
                const response = JSON.parse(xmlHttp.response);
                const results = response["results"];
                
                for (let item of results) {
                    const title = item["title"];
                    const image = item["image"];

                    const itemTitleHtml = prepItemTitleHtml(title, image);
                    const itemImageHtml = prepItemImageHtml(image);

                    const container = prepContainerDivHtml(itemTitleHtml, itemImageHtml);
                    const fullItemHtml = prepLinkItemHtml(container);

                    linksDiv.innerHTML += "".concat(fullItemHtml);
                }
            }
            else {
                linkDiv.innerHTML += xmlHttp.status.concat(": ").concat(xmlHttp.statusText);
            }
         }
    };

    xmlHttp.open("POST", "/", true);
    xmlHttp.send();
});