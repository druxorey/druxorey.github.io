<h1 align="center">Druxorey Website</h1>

<div align="center">

_Personal portfolio and blog <a href="https://druxorey.github.io">druxorey.github.io</a>_

[![stars](https://img.shields.io/github/stars/druxorey/druxorey.github.io?color=8BE9FD&labelColor=191A21&style=for-the-badge)](https://github.com/druxorey/druxorey.github.io/stargazers)
[![size](https://img.shields.io/github/repo-size/druxorey/druxorey.github.io?label=Size&color=50FA7B&labelColor=191A21&style=for-the-badge)](https://github.com/druxorey/druxorey.github.io)
[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdruxorey%2Fdruxorey.github.io&label=Views&labelColor=%23191A21&countColor=%23FFB86C)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdruxorey%2Fdruxorey.github.io)
[![license](https://img.shields.io/github/license/druxorey/druxorey.github.io?color=FF5555&labelColor=191A21&style=for-the-badge)](https://github.com/druxorey/druxorey.github.io/blob/main/LICENSE)

</div>

## Local Workflow

### Requirements

| Tool | Minimum Version | Purpose |
|------|-----------------|---------|
| Node.js | 18+ | Vite + TypeScript |
| Python 3 | 3.9+ | Build scripts |
| Pandoc | any | Markdown → HTML conversion |

### 1. Install dependencies

```bash
npm install
```

### 2. Add a new blog article

1. Write your article in Markdown with YAML frontmatter:

```markdown
---
title: "My New Article"
created: 2025-01-15
description: "Short description for SEO and the blog card."
tags:
  - Linux
  - Networks
---

# Introduction

Article content...

> [!IMPORTANT]
> This renders as an warning callout.

> [!NOTE]
> This renders as an information callout.
```

2. Save the `.md` file in `build/markdown/`

3. (Optional) Add a `.avif` or `.webp` cover image in `public/images/post/` using the same slug name (e.g., `my-new-article.avif` or `my-new-article.webp`)

### 3. Local build

```bash
npm run build
```

This automatically runs the following in order:
1. **`build/fetch-github-projects.py`** → Updates `src/data/projects.ts` and the contributions SVG from the GitHub API
2. **`build/build-blog.py`** → Compiles the `.md` files from `build/markdown/` to `blog/*.html`
3. **`tsc`** → TypeScript type checking
4. **`vite build`** → Generates the final bundle in `dist/`

### 4. Development server

```bash
npm run dev
```

> **Note:** `npm run dev` does not run the prebuild. Run `npm run build` first to ensure articles and projects are up-to-date, then use `npm run dev` to iterate on styles and scripts.

## Build Scripts

| Script | Direct Command | Description |
|--------|----------------|-------------|
| Complete build | `npm run build` | fetch + blog + vite |
| Projects fetch only | `python3 build/fetch-github-projects.py` | Updates projects.ts and the SVG |
| Blog compile only | `python3 build/build-blog.py` | Compiles all .md files in build/markdown/ |
| Compile specific article | `python3 build/build-blog.py build/markdown/my-article.md` | Compiles a single article |

---

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for more details.