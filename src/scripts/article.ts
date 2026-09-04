export function initializeArticle(): void {
	const tocLinks = document.querySelectorAll<HTMLAnchorElement>('.toc-link');
	const headings: HTMLElement[] = [];

	tocLinks.forEach((link) => {
		const href = link.getAttribute('href');
		if (href && href.startsWith('#')) {
			const target = document.querySelector<HTMLElement>(href);
			if (target) {
				headings.push(target);
			}
		}
	});

	function updateActiveHeading(): void {
		const scrollPosition = window.scrollY + 120;
		let currentActiveIndex = -1;

		headings.forEach((heading, idx) => {
			if (heading.offsetTop <= scrollPosition) {
				currentActiveIndex = idx;
			}
		});

		tocLinks.forEach((link, idx) => {
			const parentItem = link.closest('.toc-item');
			if (idx === currentActiveIndex) {
				parentItem?.classList.add('active');
			} else {
				parentItem?.classList.remove('active');
			}
		});
	}

	window.addEventListener('scroll', updateActiveHeading, { passive: true });
	updateActiveHeading();

	// Renderizado automático de fórmulas KaTeX
	function renderMath(): void {
		// @ts-ignore
		const katex = window.katex;
		if (!katex) {
			setTimeout(renderMath, 40);
			return;
		}

		document.querySelectorAll<HTMLElement>('.math.inline').forEach((el) => {
			try {
				katex.render(el.textContent || '', el, {
					displayMode: false,
					throwOnError: false,
				});
			} catch (_) {}
		});

		document.querySelectorAll<HTMLElement>('.math.display').forEach((el) => {
			try {
				katex.render(el.textContent || '', el, {
					displayMode: true,
					throwOnError: false,
				});
			} catch (_) {}
		});
	}

	renderMath();

	const copyLinkBtn = document.getElementById('copyArticleLinkBtn');
	if (copyLinkBtn) {
		copyLinkBtn.addEventListener('click', async () => {
			try {
				await navigator.clipboard.writeText(window.location.href);
				const originalText = copyLinkBtn.textContent;
				copyLinkBtn.textContent = '✓ ¡Enlace copiado!';
				setTimeout(() => {
					copyLinkBtn.textContent = originalText;
				}, 2000);
			} catch (err) {
				console.error('Error copying link:', err);
			}
		});
	}
}

document.addEventListener('DOMContentLoaded', initializeArticle);
