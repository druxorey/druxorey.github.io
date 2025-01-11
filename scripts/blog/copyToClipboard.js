function copyToClipboard(selector) {
    var element = document.querySelector(selector);
    var range = document.createRange();
    range.selectNode(element);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand('copy');
    window.getSelection().removeAllRanges();
}

function changeButtonColor(button) {
	const originalColor = button.style.backgroundColor;
	button.style.backgroundColor = 'var(--color-green-2)';
	setTimeout(() => {
		button.style.backgroundColor = originalColor;
	}, 0200);
}
