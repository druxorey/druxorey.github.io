#!/usr/bin/env python3
"""
build/prebuild.py — Master pre-build script

Executes all necessary steps in order before Vite bundles the site:
  1. Synchronizes projects and contributions chart from GitHub
  2. Compiles Markdown publications to publications/
  3. Compiles academic Markdown notes to notes/

Invoked automatically from `npm run build`.

Manual usage:
  python3 build/prebuild.py
"""
import subprocess
import sys
import os

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def runScript(scriptPath, stepLabel):
    print(f"\n{stepLabel}")
    processResult = subprocess.run(
        [sys.executable, os.path.join(rootDir, scriptPath)],
        cwd=rootDir,
    )
    if processResult.returncode != 0:
        print(f"\n  ✗ Failed: {scriptPath} (exit code {processResult.returncode})", file=sys.stderr)
        sys.exit(processResult.returncode)


def main():
    runScript("build/fetch-github-projects.py", "1. Syncing GitHub projects and contributions")
    runScript("build/build-publications.py",    "2. Compiling Markdown → HTML publications")
    runScript("build/build-notes.py",           "3. Compiling Markdown → HTML academic notes")
    print("")


if __name__ == "__main__":
    main()
