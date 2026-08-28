export function initializeCodeCopy(): void {
	const copyButtons = document.querySelectorAll<HTMLButtonElement>('.copy-code-btn');

	copyButtons.forEach((btn) => {
		btn.addEventListener('click', async () => {
			const codeWrapper = btn.closest('.code-block-wrapper');
			const codeEl = codeWrapper?.querySelector('code');
			const textToCopy = codeEl ? codeEl.innerText : btn.getAttribute('data-code') || '';

			if (!textToCopy) return;

			try {
				await navigator.clipboard.writeText(textToCopy);
				const originalText = btn.textContent;
				btn.textContent = '✓ Copiado';
				btn.classList.add('copied');

				setTimeout(() => {
					btn.textContent = originalText;
					btn.classList.remove('copied');
				}, 2000);
			} catch (err) {
				console.error('Error copying code to clipboard:', err);
			}
		});
	});
}

document.addEventListener('DOMContentLoaded', initializeCodeCopy);
