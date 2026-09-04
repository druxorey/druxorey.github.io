"""
build/markdown_processor.py — Shared Markdown and Pandoc processing engine

Handles frontmatter parsing, Obsidian wikilinks, Dracula-themed callouts,
KaTeX LaTeX math formulas, code blocks with copy buttons, table of contents (TOC),
and TLDR summary extraction for publications and academic notes.
"""
import os
import re
import sys
import unicodedata
import subprocess

calloutIcons = {
    "TLDR": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>',
    "SUMMARY": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>',
    "QUOTE": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"></path><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"></path></svg>',
    "DEFINITION": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="callout-icon"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>',
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

defaultTitles = {
    "TLDR": "SÍNTESIS",
    "SUMMARY": "SÍNTESIS",
    "QUOTE": "CITA",
    "DEFINITION": "DEFINICIÓN",
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

calloutFlavors = {
    "TLDR": "resources",
    "SUMMARY": "resources",
    "QUOTE": "note",
    "DEFINITION": "important",
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

languageDisplayNames = {
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


def parseFrontmatter(fileContent):
    """Extracts YAML frontmatter metadata and returns (metadataDict, bodyContent)."""
    metadataDict = {
        "title": "",
        "created": "",
        "author": "Guillermo Galavís",
        "description": "",
        "tags": [],
        "subject": "",
        "status": "",
    }
    if fileContent.startswith("---"):
        contentSections = fileContent.split("---", 2)
        if len(contentSections) >= 3:
            frontmatterText, bodyContent = contentSections[1], contentSections[2]
            currentKey = None
            for contentLine in frontmatterText.splitlines():
                strippedLine = contentLine.strip()
                if not strippedLine:
                    continue
                if strippedLine.startswith("- ") and currentKey == "tags":
                    metadataDict["tags"].append(strippedLine[2:].strip().strip('"').strip("'"))
                elif ":" in contentLine:
                    parsedKey, parsedValue = contentLine.split(":", 1)
                    parsedKey = parsedKey.strip()
                    parsedValue = parsedValue.strip().strip('"').strip("'")
                    currentKey = parsedKey
                    if parsedKey in metadataDict and parsedKey != "tags":
                        metadataDict[parsedKey] = parsedValue
                    elif parsedKey == "tags" and parsedValue:
                        metadataDict["tags"].extend([t.strip() for t in parsedValue.split(",")])
                    elif parsedKey not in metadataDict:
                        metadataDict[parsedKey] = parsedValue
            return metadataDict, bodyContent
    return metadataDict, fileContent


def slugifyText(rawText):
    normalizedText = unicodedata.normalize("NFKD", rawText).encode("ASCII", "ignore").decode("utf-8").lower()
    cleanedSlug = re.sub(r"[^a-z0-9]+", "-", normalizedText)
    return cleanedSlug.strip("-")


def deriveSlug(sourcePath):
    return slugifyText(os.path.splitext(os.path.basename(sourcePath))[0])


def estimateReadingTime(rawText):
    wordCount = len(re.findall(r"\w+", rawText))
    calculatedMinutes = max(1, round(wordCount / 180))
    return f"{calculatedMinutes} min de lectura"


def preprocessWikilinks(markdownText):
    """Converts Obsidian wikilinks [[...]] to standard Markdown links,
    safely preserving fenced and inline code blocks.
    """
    segmentedParts = re.split(r"(```.*?```|`[^`\n]+`)", markdownText, flags=re.DOTALL)
    processedSegments = []
    for segmentIndex, currentSegment in enumerate(segmentedParts):
        if segmentIndex % 2 == 1:
            processedSegments.append(currentSegment)
        else:
            updatedSegment = re.sub(
                r"\[\[([^|\]#]+)#([^|\]]+)\|([^\]]+)\]\]",
                lambda matched: f"[{matched.group(3)}](#{slugifyText(matched.group(2))})",
                currentSegment,
            )
            updatedSegment = re.sub(
                r"\[\[([^|\]#]+)\|([^\]]+)\]\]",
                lambda matched: f"[{matched.group(2)}](#{slugifyText(matched.group(1))})",
                updatedSegment,
            )
            updatedSegment = re.sub(
                r"\[\[([^|\]#\s][^|\]#]*)\]\]",
                lambda matched: f"[{matched.group(1)}](#{slugifyText(matched.group(1))})",
                updatedSegment,
            )
            processedSegments.append(updatedSegment)
    return "".join(processedSegments)


def preprocessCalloutNewlines(markdownText):
    """Ensures Obsidian callouts are cleanly separated:
    1. Guarantees an empty line before > [!TYPE] if preceded by display math or text.
    2. Inserts '> ' between callout title and content if missing.
    """
    markdownText = re.sub(r"([^\n])\n(>[ \t]*\[![A-Za-z]+\])", r"\1\n\n\2", markdownText)

    sourceLines = markdownText.splitlines()
    formattedLines = []
    for lineIndex, sourceLine in enumerate(sourceLines):
        formattedLines.append(sourceLine)
        if re.match(r"^>[ \t]*\[![A-Za-z]+\]", sourceLine):
            if (
                lineIndex + 1 < len(sourceLines)
                and re.match(r"^>[ \t]*\S", sourceLines[lineIndex + 1])
                and not re.match(r"^>[ \t]*$", sourceLines[lineIndex + 1])
            ):
                formattedLines.append("> ")
    return "\n".join(formattedLines)


def preprocessNestedEmphasis(markdownText):
    """Normalizes Obsidian pattern (**_**Word**_**) or (**_Word_**) -> (<em>Word</em>)
    preventing CommonMark parsers from breaking surrounding bold delimiters.
    """
    return re.sub(r"\(\*{0,2}_+\*{0,2}([^*_]+?)\*{0,2}_+\*{0,2}\)", r"(<em>\1</em>)", markdownText)


def extractTldrSummary(markdownText):
    """Extracts summary text from [!TLDR] or [!SUMMARY] callouts for feed cards.
    Leaves the Markdown body intact so the callout is preserved in the rendered article.
    """
    calloutMatch = re.search(
        r">\s*\[!(?:TLDR|SUMMARY)\][^\n]*\n((?:>[^\n]*\n?)+)",
        markdownText,
        re.IGNORECASE,
    )
    if calloutMatch:
        rawLines = calloutMatch.group(1).splitlines()
        cleanLines = []
        for rawLine in rawLines:
            cleanLine = re.sub(r"^>[ \t]*", "", rawLine).strip()
            if cleanLine:
                cleanLines.append(cleanLine)
        combinedText = " ".join(cleanLines)
        combinedText = re.sub(r"\*\*([^*]+)\*\*", r"\1", combinedText)
        combinedText = re.sub(r"\*([^*]+)\*", r"\1", combinedText)
        return combinedText.strip()
    return ""


def processCallouts(renderedHtml):
    """Transforms Pandoc blockquote elements with [!TYPE] syntax into Dracula styled callout containers."""
    def replaceCallout(matchedCallout):
        calloutType = matchedCallout.group(1).upper()
        customTitle = (matchedCallout.group(2) or "").strip()
        calloutBody = matchedCallout.group(3).strip() if matchedCallout.group(3) else ""

        customTitle = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", customTitle)
        customTitle = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", customTitle)

        flavorName = calloutFlavors.get(calloutType, "note")
        iconSvg = calloutIcons.get(calloutType, calloutIcons["NOTE"])
        displayTitle = customTitle if customTitle else defaultTitles.get(calloutType, calloutType)

        return (
            f'<div class="callout-box {flavorName}">\n'
            f'  <div class="callout-title">\n'
            f'    <span class="callout-icon">{iconSvg}</span>\n'
            f'    <span class="callout-title-text">{displayTitle}</span>\n'
            f'  </div>\n'
            f'  <div class="callout-content">\n'
            f"{calloutBody}\n"
            f"  </div>\n"
            f"</div>"
        )

    calloutPattern = r"<blockquote>\s*<p>\[!([A-Za-z]+)\](?:\s*(.*?))?</p>(.*?)</blockquote>"
    return re.sub(calloutPattern, replaceCallout, renderedHtml, flags=re.DOTALL)


def formatLanguage(rawLanguage):
    cleanedLang = rawLanguage.strip().lower()
    return languageDisplayNames.get(cleanedLang, cleanedLang.capitalize() if cleanedLang else "Text")


def processCodeBlocks(renderedHtml):
    """Wraps pre/code blocks with copy buttons and language labels."""
    def wrapCode(codeLanguage, codeBody):
        displayLanguage = formatLanguage(codeLanguage)
        return (
            f'<div class="code-block-wrapper">\n'
            f'  <button class="copy-code-btn" type="button" data-lang="{displayLanguage}" title="Copiar código al portapapeles">{displayLanguage}</button>\n'
            f'  <pre class="code-pre"><code>{codeBody.strip()}</code></pre>\n'
            f"</div>"
        )

    renderedHtml = re.sub(
        r'<div\s+class="sourceCode"[^>]*>\s*<pre\s+class="sourceCode\s+([^"]*)"\s*><code[^>]*>(.*?)</code>\s*</pre>\s*</div>',
        lambda matched: wrapCode(matched.group(1) or "code", matched.group(2)),
        renderedHtml,
        flags=re.DOTALL | re.IGNORECASE,
    )

    renderedHtml = re.sub(
        r'<pre\s+class="(?!code-pre)([^"]+)"\s*><code[^>]*>(.*?)</code>\s*</pre>',
        lambda matched: wrapCode(matched.group(1) or "code", matched.group(2)),
        renderedHtml,
        flags=re.DOTALL | re.IGNORECASE,
    )

    renderedHtml = re.sub(
        r'<pre(?:\s+class="(?!code-pre)([^"]*)")?\s*><code(?:\s+class="(?:language-)?([^"]*)")?\s*>(.*?)</code>\s*</pre>',
        lambda matched: wrapCode(matched.group(1) or matched.group(2) or "code", matched.group(3)),
        renderedHtml,
        flags=re.DOTALL | re.IGNORECASE,
    )

    return renderedHtml


def extractTocAndAddAnchors(renderedHtml):
    """Adds unique ID anchors to h2 and h3 headings and generates the HTML TOC list."""
    tocItems = []

    def replaceHeading(matchedHeading):
        headingTag = matchedHeading.group(1)
        headingAttributes = matchedHeading.group(2) or ""
        headingTitle = matchedHeading.group(3).strip()
        idMatch = re.search(r'id="([^"]+)"', headingAttributes)
        if idMatch:
            anchorId = idMatch.group(1)
        else:
            anchorId = slugifyText(re.sub(r"<[^>]+>", "", headingTitle))
            headingAttributes = f'{headingAttributes} id="{anchorId}"'.strip()
        cleanTitle = re.sub(r"<[^>]+>", "", headingTitle)
        subClass = " toc-sub" if headingTag == "h3" else ""
        tocItems.append(
            f'<li class="toc-item{subClass}">'
            f'<a class="toc-link" href="#{anchorId}">{cleanTitle}</a></li>'
        )
        return f"<{headingTag} {headingAttributes}>{headingTitle}</{headingTag}>"

    renderedHtml = re.sub(r"<(h[23])([^>]*)>(.*?)</\1>", replaceHeading, renderedHtml, flags=re.DOTALL)
    tocHtml = (
        "\n".join(tocItems)
        if tocItems
        else '<li class="toc-item"><a class="toc-link" href="#main-content">Contenido</a></li>'
    )
    return renderedHtml, tocHtml


def compileMarkdownBody(bodyMarkdown):
    """Preprocesses wikilinks, nested emphasis, and callouts, compiling via Pandoc to HTML5 + KaTeX."""
    bodyMarkdown = re.sub(r'<h1 id="[^"]*"[^>]*>.*?</h1>', "", bodyMarkdown, flags=re.DOTALL)
    bodyMarkdown = preprocessWikilinks(bodyMarkdown)
    bodyMarkdown = preprocessNestedEmphasis(bodyMarkdown)
    bodyMarkdown = preprocessCalloutNewlines(bodyMarkdown)

    pandocCommand = ["pandoc", "--from=markdown", "--to=html5", "--math-method=katex", "--shift-heading-level-by=1"]
    pandocProcess = subprocess.Popen(
        pandocCommand,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    processOutput, processError = pandocProcess.communicate(input=bodyMarkdown)
    if pandocProcess.returncode != 0:
        print(f"  ✗  Pandoc error: {processError}", file=sys.stderr)
        return None

    finalHtml = processCallouts(processOutput)
    finalHtml = processCodeBlocks(finalHtml)
    finalHtml, tocHtml = extractTocAndAddAnchors(finalHtml)

    return finalHtml, tocHtml
