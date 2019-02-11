document.addEventListener("DOMContentLoaded", function() {
    const potdDiv = document.querySelector(".potd");
    const xmlHttp = new XMLHttpRequest();

    const prepHtml = function(openingTag, content, closingTag) {
        return openingTag.concat(content).concat(closingTag);
    };

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

                    potdDiv.innerHTML += fullItemImageHtml.concat(fullItemTitleHtml);
                };
            }
            else {
                potdDiv.innerHTML += xmlHttp.status.concat(": ").concat(xmlHttp.statusText);
            };
         };
    };

    xmlHttp.open("POST", "/", true);
    xmlHttp.send();
});