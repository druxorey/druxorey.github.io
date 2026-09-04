import { notesData, type AcademicNote } from '../data/notes';

export function initializeNotes(): void {
	const container = document.getElementById('notesContainer');
	const sidebarList = document.getElementById('notesSubjectsList');
	const tagsContainer = document.getElementById('notesTagsContainer');
	const searchInput = document.getElementById('notesSearchInput') as HTMLInputElement | null;
	const countIndicator = document.getElementById('notesCount');

	if (!container) return;

	// Recopilar materias únicas con sus conteos
	const subjectsMap = new Map<string, number>();
	notesData.forEach((note) => {
		const existing = subjectsMap.get(note.subject) || 0;
		subjectsMap.set(note.subject, existing + 1);
	});

	let activeSubject = 'all';
	let searchQuery = '';

	const folderSvg = `
		<svg class="notes-folder-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
			<path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
		</svg>
	`;

	function renderSidebar(): void {
		if (!sidebarList) return;
		sidebarList.innerHTML = '';

		// Botón "Todas las materias"
		const allItem = document.createElement('li');
		const allBtn = document.createElement('button');
		allBtn.className = `notes-sidebar-item ${activeSubject === 'all' ? 'active' : ''}`;
		allBtn.setAttribute('type', 'button');
		allBtn.innerHTML = `
			<span class="notes-sidebar-item-left">
				${folderSvg}
				<span class="notes-sidebar-item-name">Todas las materias</span>
			</span>
			<span class="notes-sidebar-item-count">${notesData.length}</span>
		`;
		allBtn.addEventListener('click', () => {
			activeSubject = 'all';
			updateActiveStates();
			renderNotes();
		});
		allItem.appendChild(allBtn);
		sidebarList.appendChild(allItem);

		// Listado directo de materias (sin agrupación por semestre)
		const sortedSubjects = Array.from(subjectsMap.keys()).sort((a, b) => a.localeCompare(b));
		sortedSubjects.forEach((subjName) => {
			const count = subjectsMap.get(subjName) || 0;
			const li = document.createElement('li');
			const btn = document.createElement('button');
			btn.className = `notes-sidebar-item ${activeSubject === subjName ? 'active' : ''}`;
			btn.setAttribute('type', 'button');
			btn.innerHTML = `
				<span class="notes-sidebar-item-left">
					${folderSvg}
					<span class="notes-sidebar-item-name">${subjName}</span>
				</span>
				<span class="notes-sidebar-item-count">${count}</span>
			`;
			btn.addEventListener('click', () => {
				activeSubject = subjName;
				updateActiveStates();
				renderNotes();
			});
			li.appendChild(btn);
			sidebarList.appendChild(li);
		});
	}

	function renderTags(): void {
		if (!tagsContainer) return;
		tagsContainer.innerHTML = '';

		const allBtn = document.createElement('button');
		allBtn.className = `tag tag-interactive ${activeSubject === 'all' ? 'active' : ''}`;
		allBtn.textContent = 'Todas';
		allBtn.setAttribute('type', 'button');
		allBtn.addEventListener('click', () => {
			activeSubject = 'all';
			updateActiveStates();
			renderNotes();
		});
		tagsContainer.appendChild(allBtn);

		Array.from(subjectsMap.keys())
			.sort()
			.forEach((subj) => {
				const tagBtn = document.createElement('button');
				tagBtn.className = `tag tag-interactive ${activeSubject === subj ? 'active' : ''}`;
				tagBtn.textContent = subj;
				tagBtn.setAttribute('type', 'button');
				tagBtn.addEventListener('click', () => {
					activeSubject = activeSubject === subj ? 'all' : subj;
					updateActiveStates();
					renderNotes();
				});
				tagsContainer.appendChild(tagBtn);
			});
	}

	function updateActiveStates(): void {
		// Sincronizar clases activas en sidebar
		if (sidebarList) {
			const items = sidebarList.querySelectorAll('.notes-sidebar-item');
			items.forEach((item) => {
				const nameSpan = item.querySelector('.notes-sidebar-item-name');
				const name = nameSpan ? nameSpan.textContent?.trim() : '';
				if ((activeSubject === 'all' && name === 'Todas las materias') || name === activeSubject) {
					item.classList.add('active');
				} else {
					item.classList.remove('active');
				}
			});
		}

		// Sincronizar clases activas en tags superiores
		if (tagsContainer) {
			const buttons = tagsContainer.querySelectorAll('.tag');
			buttons.forEach((btn) => {
				const text = btn.textContent?.trim();
				if ((activeSubject === 'all' && text === 'Todas') || text === activeSubject) {
					btn.classList.add('active');
				} else {
					btn.classList.remove('active');
				}
			});
		}
	}

	function renderNotes(): void {
		if (!container) return;

		const normalizedQuery = searchQuery.trim().toLowerCase();

		const filtered = notesData.filter((note) => {
			const matchesSubject = activeSubject === 'all' || note.subject === activeSubject;
			const matchesSearch =
				!normalizedQuery ||
				note.title.toLowerCase().includes(normalizedQuery) ||
				note.rawTitle.toLowerCase().includes(normalizedQuery) ||
				note.summary.toLowerCase().includes(normalizedQuery) ||
				note.subject.toLowerCase().includes(normalizedQuery) ||
				note.tags.some((t) => t.toLowerCase().includes(normalizedQuery));

			return matchesSubject && matchesSearch;
		});

		if (countIndicator) {
			const subjectSuffix = activeSubject === 'all' ? '' : ` · ${activeSubject}`;
			countIndicator.textContent = `Mostrando ${filtered.length} de ${notesData.length} notas${subjectSuffix}`;
		}

		if (filtered.length === 0) {
			container.innerHTML = `
				<div class="card blog-empty-card">
					<p class="blog-empty-text">No se encontraron apuntes que coincidan con la búsqueda.</p>
					<button id="clearNotesSearchBtn" class="btn btn-secondary btn-sm" type="button">Limpiar filtros</button>
				</div>
			`;

			const clearBtn = document.getElementById('clearNotesSearchBtn');
			if (clearBtn) {
				clearBtn.addEventListener('click', () => {
					activeSubject = 'all';
					searchQuery = '';
					if (searchInput) searchInput.value = '';
					updateActiveStates();
					renderNotes();
				});
			}
			return;
		}

		container.innerHTML = filtered.map(renderNoteCard).join('');
	}

	function renderNoteCard(note: AcademicNote): string {
		const tagsHtml = note.tags
			.map((t) => `<span class="tag">#${t}</span>`)
			.join(' ');

		return `
			<a href="./notes/${note.slug}" class="card card-interactive note-card-row" aria-label="${note.title}">
				<div class="note-card-body">
					<div class="note-card-header">
						<div class="note-card-badges">
							<span class="note-badge-order">${note.orderBadge}</span>
							<span class="note-badge-subject">${note.subject}</span>
						</div>
					</div>

					<h2 class="note-card-title">
						${note.title}
					</h2>

					<p class="note-card-summary">
						${note.summary}
					</p>

					<div class="note-card-tags">
						${tagsHtml}
					</div>
				</div>
			</a>
		`;
	}

	if (searchInput) {
		searchInput.addEventListener('input', (e) => {
			searchQuery = (e.target as HTMLInputElement).value;
			renderNotes();
		});
	}

	renderSidebar();
	renderTags();
	renderNotes();
}

document.addEventListener('DOMContentLoaded', initializeNotes);
