document.addEventListener('DOMContentLoaded', () => {
	const form = document.getElementById('contactForm') as HTMLFormElement | null;
	const statusMsg = document.getElementById('formStatus') as HTMLDivElement | null;
	const copyBtn = document.getElementById('copyEmailBtn') as HTMLButtonElement | null;
	const directEmail = 'druxorey@gmail.com';

	if (copyBtn) {
		copyBtn.addEventListener('click', async () => {
			try {
				await navigator.clipboard.writeText(directEmail);
				const originalText = copyBtn.innerHTML;
				copyBtn.innerHTML = `
					<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-green">
						<polyline points="20 6 9 17 4 12"></polyline>
					</svg>
					<span>¡Copiado!</span>
				`;
				setTimeout(() => {
					copyBtn.innerHTML = originalText;
				}, 2500);
			} catch (err) {
				console.error('Error al copiar al portapapeles:', err);
			}
		});
	}

	if (form) {
		form.addEventListener('submit', (e) => {
			e.preventDefault();

			const nameInput = document.getElementById('contactName') as HTMLInputElement | null;
			const emailInput = document.getElementById('contactEmail') as HTMLInputElement | null;
			const subjectInput = document.getElementById('contactSubject') as HTMLInputElement | null;
			const messageInput = document.getElementById('contactMessage') as HTMLTextAreaElement | null;

			const name = nameInput?.value.trim() || '';
			const email = emailInput?.value.trim() || '';
			const subject = subjectInput?.value.trim() || 'Contacto desde portafolio web';
			const message = messageInput?.value.trim() || '';

			if (!message) {
				if (statusMsg) {
					statusMsg.className = 'form-status visible error';
					statusMsg.textContent = 'Por favor escribe un mensaje antes de enviar.';
				}
				return;
			}

			const mailtoBody = encodeURIComponent(
				`Hola Guillermo,\n\n${message}\n\n---\nDe: ${name} (${email})`
			);
			const mailtoSubject = encodeURIComponent(`[Portafolio] ${subject}`);
			const mailtoUrl = `mailto:${directEmail}?subject=${mailtoSubject}&body=${mailtoBody}`;

			if (statusMsg) {
				statusMsg.className = 'form-status visible success';
				statusMsg.textContent = 'Abriendo tu cliente de correo para enviar el mensaje... Si no se abre, puedes escribir directamente a druxorey@gmail.com.';
			}

			window.location.href = mailtoUrl;
		});
	}
});
