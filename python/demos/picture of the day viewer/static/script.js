document.addEventListener("DOMContentLoaded", function() {
    const linksDiv = document.querySelector(".links");
    let xmlHttp = new XMLHttpRequest();

    const prepHtml = function(openingTag, content, closingTag) {
        return openingTag.concat(content).concat(closingTag);
    }

    xmlHttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (xmlHttp.status == 200) {
                const response = JSON.parse(xmlHttp.response);
                const results = response["results"];
                
                for (let item of results) {
                    const title = item["title"];
                    const image = item["image"];

                    const itemLinkTag = prepHtml("<a href = \"", image, "\" target = \"blank\">");
                    const itemTitleLink = prepHtml(itemLinkTag, title, "</a>")
                    const fullItemTitleHtml = prepHtml("<h2>", itemTitleLink, "</h2>");
                    const fullItemImageHtml = prepHtml("<img src = \"", image, "\" />");

                    linksDiv.innerHTML += "".concat(fullItemImageHtml).concat(fullItemTitleHtml);
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