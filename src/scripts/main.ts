export function initializeNavigation(): void {
	const currentPath = window.location.pathname;

	const navLinks = document.querySelectorAll<HTMLAnchorElement>('.nav-link');
	navLinks.forEach((link) => {
		const href = link.getAttribute('href');
		if (!href) return;

		const isRoot = (currentPath === '/' || currentPath.endsWith('/index.html')) && (href === '/' || href === 'index.html' || href === './index.html');
		const isPage = href !== '/' && href !== 'index.html' && currentPath.includes(href.replace('./', ''));

		if (isRoot || isPage) {
			link.classList.add('active');
		} else {
			link.classList.remove('active');
		}
	});

	const toggleBtn = document.getElementById('navToggleBtn');
	const mobileMenu = document.getElementById('mobileMenu');

	if (toggleBtn && mobileMenu) {
		toggleBtn.addEventListener('click', () => {
			const isOpen = mobileMenu.classList.toggle('open');
			toggleBtn.setAttribute('aria-expanded', String(isOpen));
		});
	}
}

document.addEventListener('DOMContentLoaded', initializeNavigation);
