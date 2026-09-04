#!/usr/bin/env python3
"""
build/build-publications.py — Compiles Markdown publications to HTML

Converts .md files located in build/markdown/publications/ to publication HTML
in publications/, applying publication templates, callouts, and table of contents.
Also updates the typed catalog src/data/publications.ts.

The index retains ALL existing publications in publications/:
- Those newly compiled from build/markdown/publications/ are updated/added.
- Pre-existing files in publications/*.html are preserved.

Usage:
  python3 build/build-publications.py
"""
import os
import re
import sys
import glob
import json
from datetime import datetime
from markdown_processor import (
    parseFrontmatter,
    deriveSlug,
    estimateReadingTime,
    compileMarkdownBody,
)

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templatePath = os.path.join(rootDir, "templates/publication-template.html")
markdownDir = os.path.join(rootDir, "build/markdown/publications")
outputDir = os.path.join(rootDir, "publications")
imagesDir = os.path.join(rootDir, "public/images/post")
dataPublicationsPath = os.path.join(rootDir, "src/data/publications.ts")


def convertMarkdownFile(filePath, htmlTemplate):
    with open(filePath, "r", encoding="utf-8") as sourceFile:
        rawContent = sourceFile.read()

    metaData, bodyMarkdown = parseFrontmatter(rawContent)
    articleSlug = deriveSlug(filePath)

    if not metaData["title"]:
        titleMatch = re.search(r"^#\s+(.+)$", bodyMarkdown, flags=re.MULTILINE)
        metaData["title"] = titleMatch.group(1).strip() if titleMatch else articleSlug.replace("-", " ").capitalize()

    cleanDate = (metaData["created"] or datetime.today().strftime("%Y-%m-%d"))[:10]
    metaData["created"] = cleanDate

    compilationResult = compileMarkdownBody(bodyMarkdown)
    if compilationResult is None:
        print(f"  ✗  Error converting {filePath}", file=sys.stderr)
        return None
    htmlBody, tocHtml = compilationResult

    tagsList = metaData["tags"] or ["Linux", "Sistemas"]
    tagsHtml = " ".join(f'<span class="tag">#{tagItem}</span>' for tagItem in tagsList)

    slugWithoutDate = re.sub(r"^\d{6}-", "", articleSlug)
    bannerFound = None
    for candidateFile in [
        f"{articleSlug}.avif",
        f"{slugWithoutDate}.avif",
        f"{articleSlug}.webp",
        f"{slugWithoutDate}.webp",
    ]:
        if os.path.exists(os.path.join(imagesDir, candidateFile)):
            bannerFound = candidateFile
            break

    bannerHtml = (
        f'\n          <div class="article-banner-wrapper">'
        f'\n            <img class="article-banner-img"'
        f' src="/images/post/{bannerFound}" alt="{metaData["title"]}">'
        f"\n          </div>"
        if bannerFound
        else ""
    )

    readingTime = estimateReadingTime(bodyMarkdown)
    summaryText = metaData["description"] or f"Notas e investigación sobre {metaData['title']}."

    finalHtml = htmlTemplate
    replacementMap = [
        ("$title$", metaData["title"]),
        ("$summary$", summaryText),
        ("$date$", cleanDate),
        ("$reading_time$", readingTime),
        ("$author$", metaData.get("author", "Guillermo Galavís")),
        ("$tags$", tagsHtml),
        ("$banner_html$", bannerHtml),
        ("$toc$", tocHtml),
        ("$body$", htmlBody),
    ]
    for placeholderKey, replacementValue in replacementMap:
        finalHtml = finalHtml.replace(placeholderKey, replacementValue)

    os.makedirs(outputDir, exist_ok=True)
    destinationFile = os.path.join(outputDir, f"{articleSlug}.html")
    with open(destinationFile, "w", encoding="utf-8") as fileWriter:
        fileWriter.write(finalHtml)

    print(f"   ✓  publications/{articleSlug}.html  ({metaData['title']})")
    return {
        "id": articleSlug,
        "title": metaData["title"],
        "slug": f"{articleSlug}.html",
        "summary": summaryText,
        "date": cleanDate,
        "readingTime": readingTime,
        "tags": tagsList,
        "image": f"/images/post/{bannerFound}" if bannerFound else None,
    }


def scanExistingPublicationsHtml():
    """Scans all publications/*.html files and extracts metadata for the catalog."""
    discoveredEntries = {}
    if not os.path.exists(outputDir):
        return discoveredEntries

    for htmlFilePath in glob.glob(os.path.join(outputDir, "*.html")):
        with open(htmlFilePath, "r", encoding="utf-8") as htmlReader:
            fileContent = htmlReader.read()
        entrySlug = os.path.splitext(os.path.basename(htmlFilePath))[0]

        titleMatch = re.search(r'class="article-title"[^>]*>(.*?)</h1>', fileContent, re.DOTALL)
        articleTitle = (
            re.sub(r"<[^>]+>", "", titleMatch.group(1)).strip()
            if titleMatch
            else entrySlug.replace("-", " ").capitalize()
        )

        dateMatch = re.search(r'<time[^>]*datetime="([^"]+)"', fileContent)
        publishedDate = dateMatch.group(1)[:10] if dateMatch else "2024-01-01"

        tagsFound = re.findall(r'<span class="tag">#([^<]+)</span>', fileContent)
        articleTags = tagsFound if tagsFound else ["Linux"]

        readingTimeMatch = re.search(r'(\d+ min de lectura)', fileContent)
        readingTime = readingTimeMatch.group(1) if readingTimeMatch else "5 min de lectura"

        descriptionMatch = re.search(r'<meta name="description" content="([^"]+)"', fileContent)
        articleSummary = descriptionMatch.group(1) if descriptionMatch else f"Artículo sobre {articleTitle}."

        imageMatch = re.search(r'class="article-banner-img" src="([^"]+)"', fileContent)
        bannerImage = imageMatch.group(1) if imageMatch else None

        discoveredEntries[entrySlug] = {
            "id": entrySlug,
            "title": articleTitle,
            "slug": f"{entrySlug}.html",
            "summary": articleSummary,
            "date": publishedDate,
            "readingTime": readingTime,
            "tags": articleTags,
            "image": bannerImage,
        }
    return discoveredEntries


def updatePublicationsIndex(newlyCompiledArticles):
    allCatalogEntries = scanExistingPublicationsHtml()

    if os.path.exists(dataPublicationsPath):
        try:
            with open(dataPublicationsPath, "r", encoding="utf-8") as dataReader:
                catalogContent = dataReader.read()
            dataMatch = re.search(r"export const publicationsData: Publication\[\] = (\[.*\]);", catalogContent, re.DOTALL)
            if not dataMatch:
                dataMatch = re.search(r"export const articlesData: Article\[\] = (\[.*\]);", catalogContent, re.DOTALL)
            if dataMatch:
                for existingItem in json.loads(dataMatch.group(1)):
                    allCatalogEntries[existingItem["id"]] = existingItem
        except Exception:
            pass

    for compiledItem in newlyCompiledArticles:
        allCatalogEntries[compiledItem["id"]] = compiledItem

    sortedEntries = sorted(allCatalogEntries.values(), key=lambda item: item["date"], reverse=True)

    typeScriptOutput = (
        "export interface Publication {\n"
        "  id: string;\n"
        "  title: string;\n"
        "  slug: string;\n"
        "  summary: string;\n"
        "  date: string;\n"
        "  readingTime: string;\n"
        "  tags: string[];\n"
        "  image?: string | null;\n"
        "}\n\n"
        "export const publicationsData: Publication[] = "
        + json.dumps(sortedEntries, indent=2, ensure_ascii=False)
        + ";\n"
    )
    os.makedirs(os.path.dirname(dataPublicationsPath), exist_ok=True)
    with open(dataPublicationsPath, "w", encoding="utf-8") as dataFileWriter:
        dataFileWriter.write(typeScriptOutput)
    print(f"   ✓  Catalog updated: src/data/publications.ts ({len(sortedEntries)} publications)\n")


def main():
    os.makedirs(outputDir, exist_ok=True)

    if len(sys.argv) > 1:
        markdownFiles = sys.argv[1:]
    else:
        markdownFiles = sorted(glob.glob(os.path.join(markdownDir, "*.md")))

    if not markdownFiles:
        print(f"   ℹ No .md files found in {markdownDir}/ — preserving existing publications")
    else:
        print(f"\n · Compiling {len(markdownFiles)} Markdown publication(s) → HTML")

    templateContent = ""
    if os.path.exists(templatePath):
        with open(templatePath, "r", encoding="utf-8") as templateReader:
            templateContent = templateReader.read()

    newlyCompiled = []
    for filePath in markdownFiles:
        publicationInfo = convertMarkdownFile(filePath, templateContent)
        if publicationInfo:
            newlyCompiled.append(publicationInfo)

    updatePublicationsIndex(newlyCompiled)


if __name__ == "__main__":
    main()
