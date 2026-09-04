#!/usr/bin/env python3
"""
build/fetch-github-projects.py — Synchronizes GitHub repositories

Fetches public repositories for @druxorey from GitHub API,
updates src/data/projects.ts and regenerates the Dracula-themed
contributions SVG graph.

Usage:
  python3 build/fetch-github-projects.py
"""
import urllib.request
import json
import os
import re
import sys

githubUsername = "druxorey"
apiUrl = f"https://api.github.com/users/{githubUsername}/repos?sort=updated&per_page=50"
outputFile = "src/data/projects.ts"
contributionsSvg = "public/images/github-contributions.svg"

featuredRepos = [
    "dotfiles",
    "drxpkg",
    "dracula-for-stylus",
    "minimal-dracula-for-obsidian",
    "druxorey.github.io",
]

draculaPalette = {
    "0": "#191a21",
    "1": "#483c6c",
    "2": "#70539b",
    "3": "#9d72d6",
    "4": "#bd93f9",
}


def fetchRepos():
    print(f"\n · Synchronizing repositories from @{githubUsername}")
    requestHeaders = {
        "User-Agent": "Mozilla/5.0 (DruxoreyWeb-SyncScript)",
        "Accept": "application/vnd.github.v3+json",
    }
    requestObject = urllib.request.Request(apiUrl, headers=requestHeaders)
    try:
        with urllib.request.urlopen(requestObject, timeout=15) as apiResponse:
            if apiResponse.status == 200:
                return json.loads(apiResponse.read().decode("utf-8"))
            print(f"   ✗  GitHub API error: HTTP {apiResponse.status}", file=sys.stderr)
            return None
    except Exception as networkError:
        print(f"   ✗  Error connecting to GitHub API: {networkError}", file=sys.stderr)
        return None


def transformRepo(rawRepo):
    repoName = rawRepo.get("name", "")
    repoDescription = rawRepo.get("description") or (
        f"Open source repository in {rawRepo.get('language') or 'software development'}."
    )
    repoTags = []
    if rawRepo.get("language"):
        repoTags.append(rawRepo["language"])
    for topicItem in rawRepo.get("topics", []):
        if topicItem.lower() not in [tag.lower() for tag in repoTags]:
            repoTags.append(topicItem.capitalize())
    if not repoTags:
        repoTags = ["Linux", "Open Source"]

    return {
        "id": repoName.lower(),
        "title": repoName,
        "description": repoDescription,
        "tags": repoTags[:5],
        "featured": repoName.lower() in [featuredItem.lower() for featuredItem in featuredRepos],
        "links": {
            "github": rawRepo.get("html_url", f"https://github.com/{githubUsername}/{repoName}"),
            "demo": rawRepo.get("homepage") or None,
        },
        "year": str(rawRepo.get("updated_at", "2025"))[:4],
    }


def fetchContributionsGraph():
    print("\n · Updating contribution chart")
    chartUrl = f"https://ghchart.rshah.org/BD93F9/{githubUsername}"
    chartRequest = urllib.request.Request(chartUrl, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(chartRequest, timeout=15) as chartResponse:
            rawSvg = chartResponse.read().decode("utf-8")

        def transformRect(matchedRect):
            rectTag = matchedRect.group(0)
            scoreMatch = re.search(r'data-score="(\d+)"', rectTag)
            intensityScore = scoreMatch.group(1) if scoreMatch else "0"
            fillColor = draculaPalette.get(intensityScore, "#21222c")
            rectTag = re.sub(r'style="[^"]*"', f'style="fill:{fillColor};shape-rendering:geometricPrecision;"', rectTag)
            rectTag = re.sub(r"<rect ", '<rect rx="2" ry="2" ', rectTag)
            return rectTag

        processedSvg = re.sub(r"<rect [^>]+>", transformRect, rawSvg)
        processedSvg = processedSvg.replace("#767676", "#6272a4").replace("#444", "#6272a4")

        os.makedirs(os.path.dirname(contributionsSvg), exist_ok=True)
        with open(contributionsSvg, "w", encoding="utf-8") as svgFile:
            svgFile.write(processedSvg)
        print(f"   ✓  {contributionsSvg}")
    except Exception as chartError:
        print(f"   ⚠  Could not update chart: {chartError}")


def writeProjectsTs(projectsList):
    typeScriptContent = (
        "export interface Project {\n"
        "  id: string;\n"
        "  title: string;\n"
        "  description: string;\n"
        "  tags: string[];\n"
        "  featured?: boolean;\n"
        "  links: {\n"
        "    github?: string;\n"
        "    demo?: string | null;\n"
        "    docs?: string | null;\n"
        "  };\n"
        "  year?: string;\n"
        "}\n\n"
        "export const projectsData: Project[] = "
        + json.dumps(projectsList, indent=2, ensure_ascii=False)
        + ";\n"
    )
    os.makedirs(os.path.dirname(outputFile), exist_ok=True)
    with open(outputFile, "w", encoding="utf-8") as targetFile:
        targetFile.write(typeScriptContent)
    print(f"   ✓  {outputFile} ({len(projectsList)} projects)")


def main():
    fetchContributionsGraph()

    fetchedRepos = fetchRepos()
    if not fetchedRepos:
        print("   ⚠  The existing projects.ts file will be kept.")
        return

    validRepos = [repoItem for repoItem in fetchedRepos if not repoItem.get("fork", False) or repoItem.get("name") in featuredRepos]
    projectEntries = [transformRepo(repoItem) for repoItem in validRepos]
    projectEntries.sort(key=lambda item: (not item["featured"], item["year"]), reverse=False)

    writeProjectsTs(projectEntries)


if __name__ == "__main__":
    main()
