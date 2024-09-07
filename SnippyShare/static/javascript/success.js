var copyBtn = document.getElementById("copy-btn");
var copyText = document.getElementById("copy-text");

copyBtn.onclick = function () {
    navigator.clipboard.writeText(document.location.href + copyText.getAttribute("href").slice(1));
};
