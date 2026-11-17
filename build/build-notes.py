#!/usr/bin/env python3
"""
build/build-notes.py — Compiles academic Markdown notes to HTML

Converts .md files located in build/markdown/notes/<subject-dir>/ into notes/*.html,
extracting subject name from parent directory, omitting status,
parsing semester, unit, created date, and title from inside the note.
Calculates chronological hierarchical note indices (1.1, 1.2...) ordered by creation date
within each unit, extracting summaries from [!TLDR] callouts,
and maintaining the typed catalog src/data/notes.ts sorted by semester descending.

Usage:
  python3 build/build-notes.py
"""
import glob
import importlib.util
import json
import os
import re
import sys

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
processorPath = os.path.join(rootDir, "build/markdown-processor.py")
spec = importlib.util.spec_from_file_location("markdown_processor", processorPath)
markdown_processor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(markdown_processor)
sys.modules["markdown_processor"] = markdown_processor

parseFrontmatter = markdown_processor.parseFrontmatter
slugifyText = markdown_processor.slugifyText
deriveSlug = markdown_processor.deriveSlug
extractTldrSummary = markdown_processor.extractTldrSummary
compileMarkdownBody = markdown_processor.compileMarkdownBody
syncAttachments = markdown_processor.syncAttachments

templatePath = os.path.join(rootDir, "templates/note-template.html")
markdownDir = os.path.join(rootDir, "build/markdown/notes")
outputDir = os.path.join(rootDir, "notes")
dataNotesPath = os.path.join(rootDir, "src/data/notes.ts")
imagesOutputDir = os.path.join(rootDir, "public/images/notes")


def formatSubjectFromDir(dirName):
    """Formats directory name into capitalized subject title:
    e.g. 'probabilidad-y-estadistica' -> 'Probabilidad y Estadistica'
         'comunicacion-de-datos' -> 'Comunicacion de Datos'
    """
    words = dirName.replace("-", " ").split()
    lowercase_connectors = {"y", "de", "del", "la", "las", "el", "los", "en", "a", "al", "o", "e"}
    formatted_words = []
    for idx, word in enumerate(words):
        lower = word.lower()
        if idx > 0 and lower in lowercase_connectors:
            formatted_words.append(lower)
        else:
            formatted_words.append(word.capitalize())
    return " ".join(formatted_words)


def main():
    os.makedirs(outputDir, exist_ok=True)
    os.makedirs(imagesOutputDir, exist_ok=True)

    # Synchronize attachments from markdown notes to public/images/notes/
    syncedCount = syncAttachments(markdownDir, imagesOutputDir)
    if syncedCount > 0:
        print(f"\n · Synced {syncedCount} attachment(s) → public/images/notes/")

    markdownFiles = glob.glob(os.path.join(markdownDir, "**/*.md"), recursive=True)
    if not markdownFiles:
        markdownFiles = glob.glob(os.path.join(markdownDir, "*.md"))
    markdownFiles = [f for f in markdownFiles if "attachments" not in f.split(os.sep)]

    print(f"\n · Compiling {len(markdownFiles)} academic note(s) Markdown → HTML")

    with open(templatePath, "r", encoding="utf-8") as templateReader:
        htmlTemplate = templateReader.read()

    # 1. Parse metadata from all .md files
    parsedNotesList = []
    for sourceFilePath in markdownFiles:
        with open(sourceFilePath, "r", encoding="utf-8") as fileReader:
            rawContent = fileReader.read()

        metaData, bodyMarkdown = parseFrontmatter(rawContent)

        # Subject derived from directory name
        relDir = os.path.relpath(os.path.dirname(sourceFilePath), markdownDir)
        folderName = relDir.split(os.sep)[0] if relDir != "." else ""
        subjectName = formatSubjectFromDir(folderName) if folderName else "General"

        # Note title derived from content inside the file
        noteTitle = metaData.get("title", "").strip().strip('"').strip("'")
        if not noteTitle:
            h1Match = re.search(r'<h1[^>]*>(.*?)</h1>', bodyMarkdown, flags=re.DOTALL | re.IGNORECASE)
            if h1Match:
                noteTitle = re.sub(r"<[^>]+>", "", h1Match.group(1)).strip()
            else:
                titleMatch = re.search(r"^#\s+(.+)$", bodyMarkdown, flags=re.MULTILINE)
                if titleMatch:
                    noteTitle = titleMatch.group(1).strip()
                else:
                    noteTitle = os.path.splitext(os.path.basename(sourceFilePath))[0]

        noteSlug = slugifyText(noteTitle) if noteTitle else deriveSlug(sourceFilePath)

        # Semester and unit
        try:
            semesterNumber = int(metaData.get("semester", 1))
        except (ValueError, TypeError):
            semesterNumber = 1

        try:
            unitNumber = int(metaData.get("unit", 1))
        except (ValueError, TypeError):
            unitNumber = 1

        cleanDate = str(metaData.get("created") or "2026-01-01").strip()[:19]

        summaryText = extractTldrSummary(bodyMarkdown)
        if not summaryText:
            paragraphMatch = re.search(r"\n\n([A-Za-z0-9\s.,;:\-_()]{30,})\n", bodyMarkdown)
            summaryText = paragraphMatch.group(1).strip() if paragraphMatch else f"Apuntes académicos sobre {noteTitle}."

        cleanTags = [t for t in (metaData.get("tags") or []) if t.lower() not in ("académico", "academico")]

        parsedNotesList.append({
            "filepath": sourceFilePath,
            "slug": noteSlug,
            "rawTitle": noteTitle,
            "meta": metaData,
            "bodyMarkdown": bodyMarkdown,
            "subject": subjectName,
            "semester": semesterNumber,
            "unit": unitNumber,
            "date": cleanDate,
            "tldrSummary": summaryText,
            "tags": cleanTags,
            "author": metaData.get("author", "Guillermo Galavís"),
        })

    # 2. Group notes by subject and unit, then sort chronologically
    notesBySubject = {}
    for noteEntry in parsedNotesList:
        subj = noteEntry["subject"]
        if subj not in notesBySubject:
            notesBySubject[subj] = []
        notesBySubject[subj].append(noteEntry)

    compiledEntries = {}
    validSlugs = set()

    # 3. Compile each note injecting unit.sequence index (e.g. 1.1. Title)
    for subj, subjectNotes in notesBySubject.items():
        notesByUnit = {}
        for noteEntry in subjectNotes:
            u = noteEntry["unit"]
            if u not in notesByUnit:
                notesByUnit[u] = []
            notesByUnit[u].append(noteEntry)

        for unitNum in sorted(notesByUnit.keys()):
            unitNotes = notesByUnit[unitNum]
            unitNotes.sort(key=lambda item: item["date"])

            for noteSeq, noteEntry in enumerate(unitNotes, start=1):
                orderBadge = f"{unitNum}.{noteSeq}"
                noteTitle = noteEntry["rawTitle"]

                compilationResult = compileMarkdownBody(noteEntry["bodyMarkdown"], imageBaseRoute="/images/notes/")
                if compilationResult is None:
                    print(f"  ✗  Error compiling {noteEntry['filepath']}", file=sys.stderr)
                    sys.exit(1)
                htmlBody, tocHtml = compilationResult

                tagsHtml = " ".join(f'<span class="tag">#{tagItem}</span>' for tagItem in noteEntry["tags"])

                finalHtml = htmlTemplate
                replacementMap = [
                    ("$title$", noteTitle),
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

                validSlugs.add(f"{noteEntry['slug']}.html")
                print(f"   ✓  notes/{noteEntry['slug']}.html  ([{orderBadge}] {noteTitle})")

                compiledEntries[noteEntry["slug"]] = {
                    "id": noteEntry["slug"],
                    "title": noteTitle,
                    "rawTitle": noteTitle,
                    "slug": f"{noteEntry['slug']}.html",
                    "subject": noteEntry["subject"],
                    "semester": noteEntry["semester"],
                    "unit": unitNum,
                    "order": noteSeq,
                    "orderBadge": orderBadge,
                    "summary": noteEntry["tldrSummary"],
                    "tags": noteEntry["tags"],
                }

    # Clean up orphan .html files in outputDir if any
    for existingFile in glob.glob(os.path.join(outputDir, "*.html")):
        if os.path.basename(existingFile) not in validSlugs:
            try:
                os.remove(existingFile)
                print(f"   -  Removed orphan: {existingFile}")
            except OSError:
                pass

    # 4. Sort catalog by semester descending, then subject, unit, order
    sortedNotesList = sorted(
        compiledEntries.values(),
        key=lambda item: (
            -item["semester"],
            item["subject"],
            item["unit"],
            item["order"],
        ),
    )

    typeScriptOutput = (
        "export interface AcademicNote {\n"
        "  id: string;\n"
        "  title: string;\n"
        "  rawTitle: string;\n"
        "  slug: string;\n"
        "  subject: string;\n"
        "  semester: number;\n"
        "  unit: number;\n"
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
