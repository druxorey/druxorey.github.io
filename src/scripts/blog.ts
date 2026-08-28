import { articlesData, type Article } from '../data/articles';

export function initializeBlog(): void {
	const container = document.getElementById('articlesContainer');
	const tagsContainer = document.getElementById('blogTagsContainer');
	const searchInput = document.getElementById('blogSearchInput') as HTMLInputElement | null;
	const countIndicator = document.getElementById('articleCount');

	if (!container) return;

	const allTags = new Set<string>();
	articlesData.forEach((article) => {
		article.tags.forEach((tag) => allTags.add(tag));
	});

	let activeTag = 'all';
	let searchQuery = '';

	function renderTags(): void {
		if (!tagsContainer) return;
		tagsContainer.innerHTML = '';

		const allBtn = document.createElement('button');
		allBtn.className = `tag tag-interactive ${activeTag === 'all' ? 'active' : ''}`;
		allBtn.textContent = 'Todos';
		allBtn.addEventListener('click', () => {
			activeTag = 'all';
			renderTags();
			renderArticles();
		});
		tagsContainer.appendChild(allBtn);

		Array.from(allTags).sort().forEach((tag) => {
			const tagBtn = document.createElement('button');
			tagBtn.className = `tag tag-interactive ${activeTag === tag ? 'active' : ''}`;
			tagBtn.textContent = `#${tag}`;
			tagBtn.addEventListener('click', () => {
				activeTag = activeTag === tag ? 'all' : tag;
				renderTags();
				renderArticles();
			});
			tagsContainer.appendChild(tagBtn);
		});
	}

	function renderArticles(): void {
		if (!container) return;

		const normalizedQuery = searchQuery.trim().toLowerCase();

		const filtered = articlesData.filter((article) => {
			const matchesTag = activeTag === 'all' || article.tags.includes(activeTag);
			const matchesSearch = !normalizedQuery ||
				article.title.toLowerCase().includes(normalizedQuery) ||
				article.summary.toLowerCase().includes(normalizedQuery) ||
				article.tags.some((t) => t.toLowerCase().includes(normalizedQuery));

			return matchesTag && matchesSearch;
		});

		if (countIndicator) {
			countIndicator.textContent = `Mostrando ${filtered.length} de ${articlesData.length} artículos`;
		}

		if (filtered.length === 0) {
			container.innerHTML = `
				<div class="card blog-empty-card">
					<p class="blog-empty-text">No se encontraron artículos que coincidan con la búsqueda.</p>
					<button id="clearSearchBtn" class="btn btn-secondary btn-sm">Limpiar filtros</button>
				</div>
			`;

			const clearBtn = document.getElementById('clearSearchBtn');
			if (clearBtn) {
				clearBtn.addEventListener('click', () => {
					activeTag = 'all';
					searchQuery = '';
					if (searchInput) searchInput.value = '';
					renderTags();
					renderArticles();
				});
			}
			return;
		}

		container.innerHTML = filtered.map(renderArticleCard).join('');
	}

	function renderArticleCard(article: Article): string {
		const tagsHtml = article.tags
			.map((t) => `<span class="tag">#${t}</span>`)
			.join(' ');

		const imageHtml = article.image
			? `<div class="blog-card-image-wrap">
					 <img src="${article.image}" alt="${article.title}" class="blog-card-image" loading="lazy">
				 </div>`
			: '';

		return `
			<article class="card card-interactive blog-card-row">
				<a href="./blog/${article.slug}" class="blog-card-body">
					<div>
						<div class="blog-card-meta">
							<time datetime="${article.date}">${article.date}</time>
							<span>·</span>
							<span>${article.readingTime}</span>
						</div>

						<h2 class="blog-card-title">
							${article.title}
						</h2>

						<p class="blog-card-summary">
							${article.summary}
						</p>
					</div>

					<div class="blog-card-tags">
						${tagsHtml}
					</div>
				</a>

				${imageHtml}
			</article>
		`;
	}

	if (searchInput) {
		searchInput.addEventListener('input', (e) => {
			searchQuery = (e.target as HTMLInputElement).value;
			renderArticles();
		});
	}

	renderTags();
	renderArticles();
}

document.addEventListener('DOMContentLoaded', initializeBlog);
