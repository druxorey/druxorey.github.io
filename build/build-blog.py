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


def parseFrontmatter(content):
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
            fmText, body = parts[1], parts[2]
            currentKey = None
            for line in fmText.splitlines():
                lineStrip = line.strip()
                if not lineStrip:
                    continue
                if lineStrip.startswith("- ") and currentKey == "tags":
                    meta["tags"].append(lineStrip[2:].strip().strip('"').strip("'"))
                elif ":" in line:
                    key, val = line.split(":", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    currentKey = key
                    if key in meta and key != "tags":
                        meta[key] = val
                    elif key == "tags" and val:
                        meta["tags"].extend([t.strip() for t in val.split(",")])
            return meta, body
    return meta, content


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")

def deriveSlug(filepath):
    return slugify(os.path.splitext(os.path.basename(filepath))[0])


def estimateReadingTime(text):
    words = len(re.findall(r"\w+", text))
    minutes = max(1, round(words / 180))
    return f"{minutes} min de lectura"


def preprocessWikilinks(md_text):
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
    "QUESTION": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>',
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
    "QUESTION": "PREGUNTA",
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
    "QUESTION": "note",
}

def processCallouts(html):
    def replaceCallout(match):
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
    return re.sub(pattern, replaceCallout, html, flags=re.DOTALL)


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

def formatLang(rawLang):
    clean = rawLang.strip().lower()
    return LANG_DISPLAY.get(clean, clean.capitalize() if clean else "Text")


def processCodeBlocks(html):
    def wrap(lang, code_body):
        displayLang = formatLang(lang)
        return (
            f'<div class="code-block-wrapper">\n'
            f'  <button class="copy-code-btn" type="button" data-lang="{displayLang}" title="Copiar código al portapapeles">{displayLang}</button>\n'
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


def extractTocAndAddAnchors(html):
    tocItems = []

    def replaceHeading(match):
        tag   = match.group(1)
        attrs = match.group(2) or ""
        title = match.group(3).strip()
        idMatch = re.search(r'id="([^"]+)"', attrs)
        if idMatch:
            anchorId = idMatch.group(1)
        else:
            anchorId = slugify(re.sub(r"<[^>]+>", "", title))
            attrs = f'{attrs} id="{anchorId}"'.strip()
        cleanTitle = re.sub(r"<[^>]+>", "", title)
        isSub = " toc-sub" if tag == "h3" else ""
        tocItems.append(
            f'<li class="toc-item{isSub}">'
            f'<a class="toc-link" href="#{anchorId}">{cleanTitle}</a></li>'
        )
        return f"<{tag} {attrs}>{title}</{tag}>"

    html = re.sub(r"<(h[23])([^>]*)>(.*?)</\1>", replaceHeading, html, flags=re.DOTALL)
    tocHtml = (
        "\n".join(tocItems) if tocItems
        else '<li class="toc-item"><a class="toc-link" href="#main-content">Contenido</a></li>'
    )
    return html, tocHtml


def convertMarkdownFile(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()

    meta, bodyMd = parseFrontmatter(raw)
    slug = deriveSlug(filepath)

    # Título desde frontmatter o primer heading
    if not meta["title"]:
        m = re.search(r"^#\s+(.+)$", bodyMd, flags=re.MULTILINE)
        meta["title"] = m.group(1).strip() if m else slug.replace("-", " ").capitalize()

    # Quitar <h1> duplicado del body
    bodyMd = re.sub(r'<h1 id="[^"]*"[^>]*>.*?</h1>', "", bodyMd, flags=re.DOTALL)

    dateClean = (meta["created"] or datetime.today().strftime("%Y-%m-%d"))[:10]
    meta["created"] = dateClean

    # Procesar wikilinks en el Markdown ANTES de Pandoc
    # (así los code blocks con [[ ]] de bash no son tocados)
    bodyMd = preprocessWikilinks(bodyMd)

    # Pandoc: markdown → HTML (headings desplazados un nivel: # → h2)
    cmd = ["pandoc", "--from=markdown", "--to=html5", "--shift-heading-level-by=1"]
    proc = subprocess.Popen(
        cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    out, err = proc.communicate(input=bodyMd)
    if proc.returncode != 0:
        print(f"  ✗  Error convirtiendo {filepath}: {err}", file=sys.stderr)
        return None

    htmlBody = processCallouts(out)
    htmlBody = processCodeBlocks(htmlBody)
    htmlBody, toc_html = extractTocAndAddAnchors(htmlBody)

    tagsList = meta["tags"] or ["Linux", "Sistemas"]
    tagsHtml = " ".join(f'<span class="tag">#{t}</span>' for t in tagsList)

    # Banner image
    cleanNoDate = re.sub(r"^\d{6}-", "", slug)
    bannerFound  = None
    for candidate in [f"{slug}.avif", f"{cleanNoDate}.avif", f"{slug}.webp", f"{cleanNoDate}.webp"]:
        if os.path.exists(os.path.join(IMAGES_DIR, candidate)):
            bannerFound = candidate
            break

    bannerHtml = (
        f'\n          <div class="article-banner-wrapper">'
        f'\n            <img class="article-banner-img"'
        f' src="/images/post/{bannerFound}" alt="{meta["title"]}">'
        f'\n          </div>'
        if bannerFound else ""
    )

    readingTime = estimateReadingTime(bodyMd)
    summary      = meta["description"] or f"Notas e investigación sobre {meta['title']}."

    with open(TEMPLATE_PATH, "r", encoding="utf-8") as tf:
        template = tf.read()

    finalHtml = template
    for key, val in [
        ("$title$",        meta["title"]),
        ("$summary$",      summary),
        ("$date$",         dateClean),
        ("$reading_time$", readingTime),
        ("$author$",       meta.get("author", "Guillermo Galavís")),
        ("$tags$",         tagsHtml),
        ("$banner_html$",  bannerHtml),
        ("$toc$",          toc_html),
        ("$body$",         htmlBody),
    ]:
        finalHtml = finalHtml.replace(key, val)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_file = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(out_file, "w", encoding="utf-8") as outf:
        outf.write(finalHtml)

    print(f"   ✓  {out_file}  ({meta['title']})")
    return {
        "id":          slug,
        "title":       meta["title"],
        "slug":        f"{slug}.html",
        "summary":     summary,
        "date":        dateClean,
        "readingTime": readingTime,
        "tags":        tagsList,
        "image":       f"/images/post/{bannerFound}" if bannerFound else None,
    }


def scanExistingBlogHtmls():
    """Lee todos los blog/*.html y extrae metadatos básicos para el índice.
    Esto asegura que artículos sin .md fuente en build/markdown/ nunca
    desaparezcan del índice.
    """
    entries = {}
    for htmlPath in glob.glob(os.path.join(OUTPUT_DIR, "*.html")):
        with open(htmlPath, "r", encoding="utf-8") as f:
            content = f.read()
        slug = os.path.splitext(os.path.basename(htmlPath))[0]

        titleM = re.search(r'class="article-title"[^>]*>(.*?)</h1>', content, re.DOTALL)
        title = re.sub(r"<[^>]+>", "", titleM.group(1)).strip() if titleM else slug.replace("-", " ").capitalize()

        dateM = re.search(r'<time[^>]*datetime="([^"]+)"', content)
        date = dateM.group(1)[:10] if dateM else "2024-01-01"

        tagsFound = re.findall(r'<span class="tag">#([^<]+)</span>', content)
        tags = tagsFound if tagsFound else ["Linux"]

        rtM = re.search(r'(\d+ min de lectura)', content)
        reading_time = rtM.group(1) if rtM else "5 min de lectura"

        metaDesc = re.search(r'<meta name="description" content="([^"]+)"', content)
        summary = metaDesc.group(1) if metaDesc else f"Artículo sobre {title}."

        imgM = re.search(r'class="article-banner-img" src="([^"]+)"', content)
        image = imgM.group(1) if imgM else None

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


def updateArticlesIndex(newlyCompiled):
    import json

    allEntries = scanExistingBlogHtmls()

    if os.path.exists(DATA_ARTICLES_PATH):
        try:
            with open(DATA_ARTICLES_PATH, "r", encoding="utf-8") as f:
                c = f.read()
            m = re.search(r"export const articlesData: Article\[\] = (\[.*\]);", c, re.DOTALL)
            if m:
                for a in json.loads(m.group(1)):
                    allEntries[a["id"]] = a
        except Exception:
            pass

    for item in newlyCompiled:
        allEntries[item["id"]] = item

    merged = sorted(allEntries.values(), key=lambda x: x["date"], reverse=True)

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
    print(f"   ✓  Updated index: {DATA_ARTICLES_PATH} ({len(merged)} articles)")


def main():
    if len(sys.argv) > 1:
        mdFiles = sys.argv[1:]
    else:
        mdFiles = sorted(glob.glob(os.path.join(MARKDOWN_DIR, "*.md")))

    if not mdFiles:
        print(f"   ℹ There are no .md files in {MARKDOWN_DIR}/ — updating only the index")
    else:
        print(f"\n · Compiling {len(mdFiles)} article(s) Markdown → HTML")

    newlyCompiled = []
    for fpath in mdFiles:
        info = convertMarkdownFile(fpath)
        if info:
            newlyCompiled.append(info)

    updateArticlesIndex(newlyCompiled)


if __name__ == "__main__":
    main()
