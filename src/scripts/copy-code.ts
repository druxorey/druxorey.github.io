export function initializeCodeCopy(): void {
	const copyButtons = document.querySelectorAll<HTMLButtonElement>('.copy-code-btn');

	copyButtons.forEach((btn) => {
		btn.addEventListener('click', async () => {
			const codeWrapper = btn.closest('.code-block-wrapper');
			const codeEl = codeWrapper?.querySelector('code');
			if (!codeEl) return;

			// Extract clean code text
			const textToCopy = (codeEl.innerText || codeEl.textContent || '')
				.replace(/\u00a0/g, ' ')
				.replace(/^\n+|\n+$/g, '');

			if (!textToCopy) return;

			const originalLang = btn.getAttribute('data-lang') || btn.textContent || 'Code';

			try {
				await navigator.clipboard.writeText(textToCopy);
				btn.textContent = '✓ Copiado';
				btn.classList.add('copied');

				setTimeout(() => {
					btn.textContent = originalLang;
					btn.classList.remove('copied');
				}, 2000);
			} catch (err) {
				console.error('Error copying code to clipboard:', err);
			}
		});
	});
}

if (document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', initializeCodeCopy);
} else {
	initializeCodeCopy();
}


