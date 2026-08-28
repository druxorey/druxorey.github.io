#!/usr/bin/env python3
"""
build/build-blog.py — Compilador de artículos Markdown → HTML

Convierte archivos .md ubicados en build/markdown/ al HTML final en blog/,
aplicando la plantilla de artículo, resaltado de código, callouts y tabla
de contenidos. También actualiza el índice src/data/articles.ts.

El índice mantiene TODOS los artículos existentes en blog/:
- Los compilados ahora desde build/markdown/ se actualizan/añaden.
- Los que ya estaban en blog/*.html (sin .md fuente) se preservan intactos.

Uso:
  python3 build/build-blog.py                   # Compila todos en build/markdown/
  python3 build/build-blog.py ruta/archivo.md   # Compila uno específico
"""
import os
import re
import sys
import glob
import subprocess
import unicodedata
from datetime import datetime

TEMPLATE_PATH      = "templates/article-template.html"
MARKDOWN_DIR       = "build/markdown"
OUTPUT_DIR         = "blog"
IMAGES_DIR         = "public/images/post"
DATA_ARTICLES_PATH = "src/data/articles.ts"


# ─── Frontmatter ──────────────────────────────────────────────────────────────

def parse_frontmatter(content):
    meta = {
        "title": "",
        "created": "",
        "author": "Guillermo Galavís",
        "description": "",
        "tags": [],
    }
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text, body = parts[1], parts[2]
            current_key = None
            for line in fm_text.splitlines():
                line_strip = line.strip()
                if not line_strip:
                    continue
                if line_strip.startswith("- ") and current_key == "tags":
                    meta["tags"].append(line_strip[2:].strip().strip('"').strip("'"))
                elif ":" in line:
                    key, val = line.split(":", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    current_key = key
                    if key in meta and key != "tags":
                        meta[key] = val
                    elif key == "tags" and val:
                        meta["tags"].extend([t.strip() for t in val.split(",")])
            return meta, body
    return meta, content


# ─── Slug ─────────────────────────────────────────────────────────────────────

def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def derive_slug(filepath):
    return slugify(os.path.splitext(os.path.basename(filepath))[0])


# ─── Tiempo de lectura ────────────────────────────────────────────────────────

def estimate_reading_time(text):
    words = len(re.findall(r"\w+", text))
    minutes = max(1, round(words / 180))
    return f"{minutes} min de lectura"


# ─── Wikilinks (en Markdown, ANTES de Pandoc) ─────────────────────────────────

def preprocess_wikilinks(md_text):
    """Convierte Obsidian wikilinks a enlaces Markdown estándar.
    Solo procesa texto fuera de bloques de código para evitar
    que bash [[ ... ]] u otros operadores sean modificados.
    """
    # Separar en partes de código (fenced o inline) y texto normal
    parts = re.split(r'(```.*?```|`[^`\n]+`)', md_text, flags=re.DOTALL)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Bloque de código: no tocar
            result.append(part)
        else:
            # [[Note#Section|Label]] → [Label](#section)
            part = re.sub(
                r'\[\[([^|\]#]+)#([^|\]]+)\|([^\]]+)\]\]',
                lambda m: f'[{m.group(3)}](#{slugify(m.group(2))})',
                part
            )
            # [[Note|Label]] → [Label](#note)
            part = re.sub(
                r'\[\[([^|\]#]+)\|([^\]]+)\]\]',
                lambda m: f'[{m.group(2)}](#{slugify(m.group(1))})',
                part
            )
            # [[Note]] → [Note](#note)
            part = re.sub(
                r'\[\[([^|\]#\s][^|\]#]*)\]\]',
                lambda m: f'[{m.group(1)}](#{slugify(m.group(1))})',
                part
            )
            result.append(part)
    return ''.join(result)


# ─── Procesadores HTML (aplicados al output de Pandoc) ───────────────────────

CALLOUT_ICONS = {
    "RESOURCES": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>',
    "REFERENCE": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>',
    "REFERENCES": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>',
    "NOTE": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>',
    "INFO": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>',
    "TIP": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5.76.76 1.23 1.52 1.41 2.5"></path></svg>',
    "HINT": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5.76.76 1.23 1.52 1.41 2.5"></path></svg>',
    "IMPORTANT": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    "WARNING": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    "CAUTION": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
    "EXAMPLE": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
}

DEFAULT_TITLES = {
    "RESOURCES": "REFERENCIAS",
    "REFERENCE": "REFERENCIAS",
    "REFERENCES": "REFERENCIAS",
    "NOTE": "NOTA",
    "INFO": "INFORMACIÓN",
    "TIP": "CONSEJO",
    "HINT": "PISTA",
    "IMPORTANT": "IMPORTANTE",
    "WARNING": "ADVERTENCIA",
    "CAUTION": "PRECAUCIÓN",
    "EXAMPLE": "EJEMPLO",
}

CALLOUT_FLAVORS = {
    "RESOURCES": "resources",
    "REFERENCE": "resources",
    "REFERENCES": "resources",
    "NOTE": "note",
    "INFO": "note",
    "TIP": "tip",
    "HINT": "tip",
    "IMPORTANT": "important",
    "WARNING": "warning",
    "CAUTION": "warning",
    "EXAMPLE": "example",
}

def process_callouts(html):
    def replace_callout(match):
        ctype = match.group(1).upper()
        custom_title = (match.group(2) or "").strip()
        body = match.group(3).strip() if match.group(3) else ""

        flavor = CALLOUT_FLAVORS.get(ctype, "note")
        icon_svg = CALLOUT_ICONS.get(ctype, CALLOUT_ICONS["NOTE"])
        title_text = custom_title if custom_title else DEFAULT_TITLES.get(ctype, ctype)

        return (
            f'<div class="callout-box {flavor}">\n'
            f'  <div class="callout-title">\n'
            f'    <span class="callout-icon">{icon_svg}</span>\n'
            f'    <span class="callout-title-text">{title_text}</span>\n'
            f'  </div>\n'
            f'  <div class="callout-content">\n'
            f'{body}\n'
            f'  </div>\n'
            f'</div>'
        )

    pattern = r"<blockquote>\s*<p>\[!([A-Za-z]+)\](?:\s*(.*?))?</p>(.*?)</blockquote>"
    return re.sub(pattern, replace_callout, html, flags=re.DOTALL)


LANG_DISPLAY = {
    "bash": "Shell",
    "sh": "Shell",
    "shell": "Shell",
    "zsh": "Shell",
    "git": "Git",
    "python": "Python",
    "py": "Python",
    "c": "C",
    "cpp": "C++",
    "c++": "C++",
    "rust": "Rust",
    "rs": "Rust",
    "go": "Go",
    "golang": "Go",
    "javascript": "JavaScript",
    "js": "JavaScript",
    "typescript": "TypeScript",
    "ts": "TypeScript",
    "html": "HTML",
    "css": "CSS",
    "json": "JSON",
    "yaml": "YAML",
    "yml": "YAML",
    "lua": "Lua",
    "markdown": "Markdown",
    "md": "Markdown",
    "sql": "SQL",
}

def format_lang(raw_lang):
    clean = raw_lang.strip().lower()
    return LANG_DISPLAY.get(clean, clean.capitalize() if clean else "Text")


def process_code_blocks(html):
    def wrap(lang, code_body):
        display_lang = format_lang(lang)
        return (
            f'<div class="code-block-wrapper">\n'
            f'  <button class="copy-code-btn" type="button" data-lang="{display_lang}" title="Copiar código al portapapeles">{display_lang}</button>\n'
            f'  <pre class="code-pre"><code>{code_body.strip()}</code></pre>\n'
            f'</div>'
        )

    # 1. Pandoc sourceCode divs (allows multiline attributes)
    html = re.sub(
        r'<div\s+class="sourceCode"[^>]*>\s*<pre\s+class="sourceCode\s+([^"]*)"\s*><code[^>]*>(.*?)</code>\s*</pre>\s*</div>',
        lambda m: wrap(m.group(1) or "code", m.group(2)),
        html,
        flags=re.DOTALL | re.IGNORECASE
    )

    # 2. Pre with class (e.g. <pre class="git"><code>...</code></pre>), ignoring already wrapped .code-pre
    html = re.sub(
        r'<pre\s+class="(?!code-pre)([^"]+)"\s*><code[^>]*>(.*?)</code>\s*</pre>',
        lambda m: wrap(m.group(1) or "code", m.group(2)),
        html,
        flags=re.DOTALL | re.IGNORECASE
    )

    # 3. Generic bare pre>code blocks (ignoring already wrapped .code-pre)
    html = re.sub(
        r'<pre(?:\s+class="(?!code-pre)([^"]*)")?\s*><code(?:\s+class="(?:language-)?([^"]*)")?\s*>(.*?)</code>\s*</pre>',
        lambda m: wrap(m.group(1) or m.group(2) or "code", m.group(3)),
        html,
        flags=re.DOTALL | re.IGNORECASE
    )

    return html


def extract_toc_and_add_anchors(html):
    toc_items = []

    def replace_heading(match):
        tag   = match.group(1)
        attrs = match.group(2) or ""
        title = match.group(3).strip()
        id_match = re.search(r'id="([^"]+)"', attrs)
        if id_match:
            anchor_id = id_match.group(1)
        else:
            anchor_id = slugify(re.sub(r"<[^>]+>", "", title))
            attrs = f'{attrs} id="{anchor_id}"'.strip()
        clean_title = re.sub(r"<[^>]+>", "", title)
        is_sub = " toc-sub" if tag == "h3" else ""
        toc_items.append(
            f'<li class="toc-item{is_sub}">'
            f'<a class="toc-link" href="#{anchor_id}">{clean_title}</a></li>'
        )
        return f"<{tag} {attrs}>{title}</{tag}>"

    html = re.sub(r"<(h[23])([^>]*)>(.*?)</\1>", replace_heading, html, flags=re.DOTALL)
    toc_html = (
        "\n".join(toc_items) if toc_items
        else '<li class="toc-item"><a class="toc-link" href="#main-content">Contenido</a></li>'
    )
    return html, toc_html


# ─── Conversión principal ─────────────────────────────────────────────────────

def convert_markdown_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()

    meta, body_md = parse_frontmatter(raw)
    slug = derive_slug(filepath)

    # Título desde frontmatter o primer heading
    if not meta["title"]:
        m = re.search(r"^#\s+(.+)$", body_md, flags=re.MULTILINE)
        meta["title"] = m.group(1).strip() if m else slug.replace("-", " ").capitalize()

    # Quitar <h1> duplicado del body
    body_md = re.sub(r'<h1 id="[^"]*"[^>]*>.*?</h1>', "", body_md, flags=re.DOTALL)

    date_clean = (meta["created"] or datetime.today().strftime("%Y-%m-%d"))[:10]
    meta["created"] = date_clean

    # Procesar wikilinks en el Markdown ANTES de Pandoc
    # (así los code blocks con [[ ]] de bash no son tocados)
    body_md = preprocess_wikilinks(body_md)

    # Pandoc: markdown → HTML (headings desplazados un nivel: # → h2)
    cmd = ["pandoc", "--from=markdown", "--to=html5", "--shift-heading-level-by=1"]
    proc = subprocess.Popen(
        cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    out, err = proc.communicate(input=body_md)
    if proc.returncode != 0:
        print(f"  ✗  Error convirtiendo {filepath}: {err}", file=sys.stderr)
        return None

    html_body = process_callouts(out)
    html_body = process_code_blocks(html_body)
    html_body, toc_html = extract_toc_and_add_anchors(html_body)

    tags_list = meta["tags"] or ["Linux", "Sistemas"]
    tags_html = " ".join(f'<span class="tag">#{t}</span>' for t in tags_list)

    # Banner image
    clean_no_date = re.sub(r"^\d{6}-", "", slug)
    banner_found  = None
    for candidate in [f"{slug}.avif", f"{clean_no_date}.avif", f"{slug}.webp", f"{clean_no_date}.webp"]:
        if os.path.exists(os.path.join(IMAGES_DIR, candidate)):
            banner_found = candidate
            break

    banner_html = (
        f'\n          <div class="article-banner-wrapper">'
        f'\n            <img class="article-banner-img"'
        f' src="/images/post/{banner_found}" alt="{meta["title"]}">'
        f'\n          </div>'
        if banner_found else ""
    )

    reading_time = estimate_reading_time(body_md)
    summary      = meta["description"] or f"Notas e investigación sobre {meta['title']}."

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as tf:
        template = tf.read()

    final_html = template
    for key, val in [
        ("$title$",        meta["title"]),
        ("$summary$",      summary),
        ("$date$",         date_clean),
        ("$reading_time$", reading_time),
        ("$author$",       meta.get("author", "Guillermo Galavís")),
        ("$tags$",         tags_html),
        ("$banner_html$",  banner_html),
        ("$toc$",          toc_html),
        ("$body$",         html_body),
    ]:
        final_html = final_html.replace(key, val)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_file = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(out_file, "w", encoding="utf-8") as outf:
        outf.write(final_html)

    print(f"  ✓  {out_file}  ({meta['title']})")
    return {
        "id":          slug,
        "title":       meta["title"],
        "slug":        f"{slug}.html",
        "summary":     summary,
        "date":        date_clean,
        "readingTime": reading_time,
        "tags":        tags_list,
        "image":       f"/images/post/{banner_found}" if banner_found else None,
    }


# ─── Scan de HTMLs existentes ─────────────────────────────────────────────────

def scan_existing_blog_htmls():
    """Lee todos los blog/*.html y extrae metadatos básicos para el índice.
    Esto asegura que artículos sin .md fuente en build/markdown/ nunca
    desaparezcan del índice.
    """
    entries = {}
    for html_path in glob.glob(os.path.join(OUTPUT_DIR, "*.html")):
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        slug = os.path.splitext(os.path.basename(html_path))[0]

        title_m = re.search(r'class="article-title"[^>]*>(.*?)</h1>', content, re.DOTALL)
        title = re.sub(r"<[^>]+>", "", title_m.group(1)).strip() if title_m else slug.replace("-", " ").capitalize()

        date_m = re.search(r'<time[^>]*datetime="([^"]+)"', content)
        date = date_m.group(1)[:10] if date_m else "2024-01-01"

        tags_found = re.findall(r'<span class="tag">#([^<]+)</span>', content)
        tags = tags_found if tags_found else ["Linux"]

        rt_m = re.search(r'(\d+ min de lectura)', content)
        reading_time = rt_m.group(1) if rt_m else "5 min de lectura"

        meta_desc = re.search(r'<meta name="description" content="([^"]+)"', content)
        summary = meta_desc.group(1) if meta_desc else f"Artículo sobre {title}."

        img_m = re.search(r'class="article-banner-img" src="([^"]+)"', content)
        image = img_m.group(1) if img_m else None

        entries[slug] = {
            "id":          slug,
            "title":       title,
            "slug":        f"{slug}.html",
            "summary":     summary,
            "date":        date,
            "readingTime": reading_time,
            "tags":        tags,
            "image":       image,
        }
    return entries


# ─── Índice articles.ts ───────────────────────────────────────────────────────

def update_articles_index(newly_compiled):
    import json

    # 1. Base: scan de TODOS los blog/*.html existentes
    all_entries = scan_existing_blog_htmls()

    # 2. Capa existente de articles.ts (más precisa que el scan)
    if os.path.exists(DATA_ARTICLES_PATH):
        try:
            with open(DATA_ARTICLES_PATH, "r", encoding="utf-8") as f:
                c = f.read()
            m = re.search(r"export const articlesData: Article\[\] = (\[.*\]);", c, re.DOTALL)
            if m:
                for a in json.loads(m.group(1)):
                    all_entries[a["id"]] = a
        except Exception:
            pass

    # 3. Capa de artículos recién compilados (la más fresca)
    for item in newly_compiled:
        all_entries[item["id"]] = item

    merged = sorted(all_entries.values(), key=lambda x: x["date"], reverse=True)

    ts = (
        "export interface Article {\n"
        "  id: string;\n"
        "  title: string;\n"
        "  slug: string;\n"
        "  summary: string;\n"
        "  date: string;\n"
        "  readingTime: string;\n"
        "  tags: string[];\n"
        "  image?: string | null;\n"
        "}\n\n"
        "export const articlesData: Article[] = "
        + json.dumps(merged, indent=2, ensure_ascii=False)
        + ";\n"
    )
    os.makedirs(os.path.dirname(DATA_ARTICLES_PATH), exist_ok=True)
    with open(DATA_ARTICLES_PATH, "w", encoding="utf-8") as df:
        df.write(ts)
    print(f"  ✓  Índice actualizado: {DATA_ARTICLES_PATH} ({len(merged)} artículos)")


# ─── Punto de entrada ─────────────────────────────────────────────────────────

def main():
    if len(sys.argv) > 1:
        md_files = sys.argv[1:]
    else:
        md_files = sorted(glob.glob(os.path.join(MARKDOWN_DIR, "*.md")))

    if not md_files:
        print(f"  ℹ  No hay archivos .md en {MARKDOWN_DIR}/ — actualizando solo el índice")
    else:
        print(f"\n── Compilando {len(md_files)} artículo(s) Markdown → HTML ──")

    newly_compiled = []
    for fpath in md_files:
        info = convert_markdown_file(fpath)
        if info:
            newly_compiled.append(info)

    update_articles_index(newly_compiled)


if __name__ == "__main__":
    main()
