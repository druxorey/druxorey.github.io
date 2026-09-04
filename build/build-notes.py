#!/usr/bin/env python3
"""
build/build-notes.py — Compiles academic Markdown notes to HTML

Converts .md files located in build/markdown/notes/ into notes/*.html,
calculating sequential note indices (#01, #02...) ordered by creation date
within each subject, extracting summaries from [!TLDR] callouts,
and maintaining the typed catalog src/data/notes.ts.

Usage:
  python3 build/build-notes.py
"""
import os
import re
import sys
import glob
import json
from markdown_processor import (
    parseFrontmatter,
    deriveSlug,
    extractTldrSummary,
    compileMarkdownBody,
)

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templatePath = os.path.join(rootDir, "templates/note-template.html")
markdownDir = os.path.join(rootDir, "build/markdown/notes")
outputDir = os.path.join(rootDir, "notes")
dataNotesPath = os.path.join(rootDir, "src/data/notes.ts")


def scanExistingNoteHtml():
    """Reads notes/*.html and recovers previously compiled notes to preserve in index."""
    discoveredEntries = {}
    if not os.path.exists(outputDir):
        return discoveredEntries

    for htmlFilePath in glob.glob(os.path.join(outputDir, "*.html")):
        with open(htmlFilePath, "r", encoding="utf-8") as htmlReader:
            fileContent = htmlReader.read()
        entrySlug = os.path.splitext(os.path.basename(htmlFilePath))[0]

        titleMatch = re.search(r'class="article-title"[^>]*>(.*?)</h1>', fileContent, re.DOTALL)
        fullTitle = re.sub(r"<[^>]+>", "", titleMatch.group(1)).strip() if titleMatch else entrySlug

        descriptionMatch = re.search(r'<meta name="description" content="([^"]+)"', fileContent)
        noteSummary = descriptionMatch.group(1) if descriptionMatch else f"Apuntes sobre {fullTitle}."

        subjectMatch = re.search(r'class="article-kicker"[^>]*>Apuntes\s*·\s*([^·<]+)', fileContent)
        subjectName = subjectMatch.group(1).strip() if subjectMatch else "General"

        orderMatch = re.search(r'#(\d+)', fullTitle)
        orderNumber = int(orderMatch.group(1)) if orderMatch else 1
        orderBadge = f"#{orderNumber:02d}"

        rawTitle = re.sub(r"^#\d+\s*-\s*", "", fullTitle)

        tagsFound = re.findall(r'<span class="tag">#([^<]+)</span>', fileContent)
        noteTags = tagsFound if tagsFound else ["académico"]

        discoveredEntries[entrySlug] = {
            "id": entrySlug,
            "title": fullTitle,
            "rawTitle": rawTitle,
            "slug": f"{entrySlug}.html",
            "subject": subjectName,
            "order": orderNumber,
            "orderBadge": orderBadge,
            "summary": noteSummary,
            "tags": noteTags,
        }
    return discoveredEntries


def main():
    os.makedirs(outputDir, exist_ok=True)

    markdownFiles = glob.glob(os.path.join(markdownDir, "**/*.md"), recursive=True)
    if not markdownFiles:
        markdownFiles = glob.glob(os.path.join(markdownDir, "*.md"))

    print(f"\n · Compiling {len(markdownFiles)} academic note(s) Markdown → HTML")

    with open(templatePath, "r", encoding="utf-8") as templateReader:
        htmlTemplate = templateReader.read()

    # 1. Parse metadata from all .md files to order by date within each subject
    parsedNotesList = []
    for sourceFilePath in markdownFiles:
        with open(sourceFilePath, "r", encoding="utf-8") as fileReader:
            rawContent = fileReader.read()

        metaData, bodyMarkdown = parseFrontmatter(rawContent)
        noteSlug = deriveSlug(sourceFilePath)

        if not metaData["title"]:
            titleMatch = re.search(r"^#\s+(.+)$", bodyMarkdown, flags=re.MULTILINE)
            metaData["title"] = titleMatch.group(1).strip() if titleMatch else noteSlug.replace("-", " ").capitalize()

        cleanDate = (metaData["created"] or "2026-01-01")[:19]
        subjectName = metaData.get("subject") or "General"

        summaryText = extractTldrSummary(bodyMarkdown)
        if not summaryText:
            paragraphMatch = re.search(r"\n\n([A-Za-z0-9\s.,;:\-_()]{30,})\n", bodyMarkdown)
            summaryText = paragraphMatch.group(1).strip() if paragraphMatch else f"Apuntes académicos sobre {metaData['title']}."

        parsedNotesList.append({
            "filepath": sourceFilePath,
            "slug": noteSlug,
            "meta": metaData,
            "bodyMarkdown": bodyMarkdown,
            "subject": subjectName,
            "date": cleanDate,
            "tldrSummary": summaryText,
            "tags": metaData["tags"] or ["académico"],
            "author": metaData.get("author", "Guillermo Galavís"),
        })

    # 2. Group notes by subject and sort chronologically
    notesBySubject = {}
    for noteEntry in parsedNotesList:
        subj = noteEntry["subject"]
        if subj not in notesBySubject:
            notesBySubject[subj] = []
        notesBySubject[subj].append(noteEntry)

    for subj in notesBySubject:
        notesBySubject[subj].sort(key=lambda item: item["date"])

    # 3. Compile each note injecting sequence index (#01, #02...)
    compiledEntries = {}
    for subj, subjectNotes in notesBySubject.items():
        for noteIndex, noteEntry in enumerate(subjectNotes, start=1):
            orderNumber = noteIndex
            orderBadge = f"#{orderNumber:02d}"
            formattedTitle = f"{orderBadge} - {noteEntry['meta']['title']}"

            compilationResult = compileMarkdownBody(noteEntry["bodyMarkdown"])
            if compilationResult is None:
                print(f"  ✗  Error compiling {noteEntry['filepath']}", file=sys.stderr)
                continue
            htmlBody, tocHtml = compilationResult

            tagsHtml = " ".join(f'<span class="tag">#{tagItem}</span>' for tagItem in noteEntry["tags"])

            finalHtml = htmlTemplate
            replacementMap = [
                ("$title$", formattedTitle),
                ("$summary$", noteEntry["tldrSummary"]),
                ("$order_badge$", f"Nota {orderBadge}"),
                ("$author$", noteEntry["author"]),
                ("$subject$", noteEntry["subject"]),
                ("$tags$", tagsHtml),
                ("$toc$", tocHtml),
                ("$body$", htmlBody),
            ]
            for placeholderKey, replacementValue in replacementMap:
                finalHtml = finalHtml.replace(placeholderKey, replacementValue)

            destinationFile = os.path.join(outputDir, f"{noteEntry['slug']}.html")
            with open(destinationFile, "w", encoding="utf-8") as fileWriter:
                fileWriter.write(finalHtml)

            print(f"   ✓  notes/{noteEntry['slug']}.html  ({formattedTitle})")

            compiledEntries[noteEntry["slug"]] = {
                "id": noteEntry["slug"],
                "title": formattedTitle,
                "rawTitle": noteEntry["meta"]["title"],
                "slug": f"{noteEntry['slug']}.html",
                "subject": noteEntry["subject"],
                "order": orderNumber,
                "orderBadge": orderBadge,
                "summary": noteEntry["tldrSummary"],
                "tags": noteEntry["tags"],
            }

    # 4. Merge with existing pre-compiled notes
    existingCatalog = scanExistingNoteHtml()
    for existingSlug, existingNote in existingCatalog.items():
        if existingSlug not in compiledEntries:
            compiledEntries[existingSlug] = existingNote

    # 5. Sort catalog by subject then order
    sortedNotesList = sorted(
        compiledEntries.values(),
        key=lambda item: (item["subject"], item["order"]),
    )

    typeScriptOutput = (
        "export interface AcademicNote {\n"
        "  id: string;\n"
        "  title: string;\n"
        "  rawTitle: string;\n"
        "  slug: string;\n"
        "  subject: string;\n"
        "  order: number;\n"
        "  orderBadge: string;\n"
        "  summary: string;\n"
        "  tags: string[];\n"
        "}\n\n"
        "export const notesData: AcademicNote[] = "
        + json.dumps(sortedNotesList, indent=2, ensure_ascii=False)
        + ";\n"
    )

    os.makedirs(os.path.dirname(dataNotesPath), exist_ok=True)
    with open(dataNotesPath, "w", encoding="utf-8") as dataFileWriter:
        dataFileWriter.write(typeScriptOutput)

    print(f"   ✓  Catalog updated: src/data/notes.ts ({len(sortedNotesList)} notes)\n")


if __name__ == "__main__":
    main()
