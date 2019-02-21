document.addEventListener("DOMContentLoaded", function() {
    const potdDiv = document.querySelector(".potd");
    const dateDiv = document.querySelector(".current-date");
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

                const prettyDate = new Date(date).toLocaleDateString();

                const titleHtml = prepHtml("<h2>", title, "</h2>");
                const linkTag = prepHtml("<a href = \"", description, "\" target = \"blank\">");
                const linkBoilerplate = "View on Wikimedia Commons";
                const linkHtml = prepHtml(linkTag, linkBoilerplate, "</a>");
                const linkWrapper = prepHtml("<figcaption>", linkHtml.concat(titleHtml), "</figcaption>");
                const imageHtml = prepHtml("<img src = \"", image, "\" />");
                const fullFigureHtml = prepHtml("<figure>", imageHtml.concat(linkWrapper), "</figure>")

                potdDiv.innerHTML = fullFigureHtml;
                dateDiv.innerHTML = prettyDate;
            }
            else {
                potdDiv.innerHTML += xmlHttp.status.concat(": ").concat(xmlHttp.statusText);
            };
         };
    };

    xmlHttp.open("POST", "/", true);
    xmlHttp.send();
});