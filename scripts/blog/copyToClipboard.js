function copyToClipboard(selector) {
    var element = document.querySelector(selector);
    var range = document.createRange();
    range.selectNode(element);
    window.getSelection().removeAllRanges(); // Clear current selection
    window.getSelection().addRange(range); // Select text
    document.execCommand('copy');
    window.getSelection().removeAllRanges(); // Deselect text
}
