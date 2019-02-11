document.addEventListener("DOMContentLoaded", function() {
    const potdDiv = document.querySelector(".potd");
    const dateDiv = document.querySelector(".date");
    const xmlHttp = new XMLHttpRequest();

    const prepHtml = function(openingTag, content, closingTag) {
        return openingTag.concat(content).concat(closingTag);
    };

    xmlHttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (xmlHttp.status == 200) {
                const response = JSON.parse(xmlHttp.response);
                const results = response["results"];
                const item = results[0];
                
                const title = item["title"];
                const image = item["image"];
                const description = item["description"];
                const date = item["date"];

                const itemLinkTag = prepHtml("<a href = \"", image, "\" target = \"blank\">");
                const itemTitleLink = prepHtml("<h2>", title, "</h2>")
                const fullItemTitleHtml = prepHtml(itemLinkTag, itemTitleLink, "</a>");
                const fullItemImageHtml = prepHtml("<img src = \"", image, "\" />");
                const descriptionHtml = prepHtml("<p>", description, "</p>");

                potdDiv.innerHTML += fullItemImageHtml.concat(fullItemTitleHtml).concat(descriptionHtml);
                dateDiv.innerHTML += date;
            }
            else {
                potdDiv.innerHTML += xmlHttp.status.concat(": ").concat(xmlHttp.statusText);
            };
         };
    };

    xmlHttp.open("POST", "/", true);
    xmlHttp.send();
});