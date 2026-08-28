#!/usr/bin/env python3
"""
build/fetch-github-projects.py — Sincroniza repositorios de GitHub

Consulta la API pública de GitHub para obtener los repositorios de @druxorey,
actualiza src/data/projects.ts y regenera el SVG de contribuciones con
la paleta Dracula.

Uso:
  python3 build/fetch-github-projects.py
"""
import urllib.request
import json
import os
import re
import sys

GITHUB_USERNAME = "druxorey"
API_URL         = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?sort=updated&per_page=50"
OUTPUT_FILE     = "src/data/projects.ts"
CONTRIBUTIONS_SVG = "public/images/github-contributions.svg"

FEATURED_REPOS = [
    "dotfiles",
    "drxpkg",
    "dracula-for-stylus",
    "minimal-dracula-for-obsidian",
    "druxorey.github.io",
]

DRACULA_PALETTE = {
    "0": "#191a21",
    "1": "#483c6c",
    "2": "#70539b",
    "3": "#9d72d6",
    "4": "#bd93f9",
}


def fetchRepos():
    print(f"\n · Synchronizing repositories from @{GITHUB_USERNAME}")
    headers = {
        "User-Agent": "Mozilla/5.0 (DruxoreyWeb-SyncScript)",
        "Accept":     "application/vnd.github.v3+json",
    }
    req = urllib.request.Request(API_URL, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8"))
            print(f"   ✗  API GitHub: HTTP {resp.status}", file=sys.stderr)
            return None
    except Exception as e:
        print(f"   ✗  Error connecting to GitHub API: {e}", file=sys.stderr)
        return None


def transformRepo(repo):
    name        = repo.get("name", "")
    description = repo.get("description") or (
        f"Repositorio de software libre en {repo.get('language') or 'código abierto'}."
    )
    tags = []
    if repo.get("language"):
        tags.append(repo["language"])
    for topic in repo.get("topics", []):
        if topic.lower() not in [t.lower() for t in tags]:
            tags.append(topic.capitalize())
    if not tags:
        tags = ["Linux", "Open Source"]

    return {
        "id":       name.lower(),
        "title":    name,
        "description": description,
        "tags":     tags[:5],
        "featured": name.lower() in [f.lower() for f in FEATURED_REPOS],
        "links": {
            "github": repo.get("html_url", f"https://github.com/{GITHUB_USERNAME}/{name}"),
            "demo":   repo.get("homepage") or None,
        },
        "year": str(repo.get("updated_at", "2025"))[:4],
    }


def fetchContributionsGraph():
    print("\n · Updating contribution chart")
    url = f"https://ghchart.rshah.org/BD93F9/{GITHUB_USERNAME}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            rawSvg = resp.read().decode("utf-8")

        def transform_rect(m):
            tag   = m.group(0)
            score = (re.search(r'data-score="(\d+)"', tag) or type("", (), {"group": lambda s, n: "0"})()).group(1)
            col   = DRACULA_PALETTE.get(score, "#21222c")
            tag   = re.sub(r'style="[^"]*"', f'style="fill:{col};shape-rendering:geometricPrecision;"', tag)
            tag   = re.sub(r"<rect ", '<rect rx="2" ry="2" ', tag)
            return tag

        processed = re.sub(r"<rect [^>]+>", transform_rect, rawSvg)
        processed = processed.replace("#767676", "#6272a4").replace("#444", "#6272a4")

        os.makedirs(os.path.dirname(CONTRIBUTIONS_SVG), exist_ok=True)
        with open(CONTRIBUTIONS_SVG, "w", encoding="utf-8") as out:
            out.write(processed)
        print(f"   ✓  {CONTRIBUTIONS_SVG}")
    except Exception as e:
        print(f"   ⚠  Could not update chart: {e}")


def writeProjectsTs(projects):
    ts = (
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
        + json.dumps(projects, indent=2, ensure_ascii=False)
        + ";\n"
    )
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(ts)
    print(f"   ✓  {OUTPUT_FILE} ({len(projects)} projects)")


def main():
    fetchContributionsGraph()

    repos = fetchRepos()
    if not repos:
        print("   ⚠  The existing projects.ts file will be kept.")
        return

    validRepos = [r for r in repos if not r.get("fork", False) or r.get("name") in FEATURED_REPOS]
    projects    = [transformRepo(r) for r in validRepos]
    projects.sort(key=lambda p: (not p["featured"], p["year"]), reverse=False)

    writeProjectsTs(projects)


if __name__ == "__main__":
    main()
