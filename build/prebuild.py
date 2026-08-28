#!/usr/bin/env python3
"""
build/prebuild.py — Script maestro de pre-compilación

Ejecuta en orden todos los pasos necesarios antes de que Vite haga el bundle:
  1. Sincroniza proyectos y gráfico de contribuciones desde GitHub
  2. Compila los artículos Markdown de build/markdown/ → blog/

Este script se invoca automáticamente desde `npm run build`.

Uso manual:
  python3 build/prebuild.py
"""
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(script, label):
    print(f"\n{label}")
    result = subprocess.run(
        [sys.executable, os.path.join(ROOT, script)],
        cwd=ROOT,
    )
    if result.returncode != 0:
        print(f"\n  ✗ Falló: {script} (código {result.returncode})", file=sys.stderr)
        sys.exit(result.returncode)


def main():
    run("build/fetch-github-projects.py", "1. Syncing GitHub projects and contributions")
    run("build/build-blog.py",            "2. Compiling Markdown → HTML articles")
    print("")

if __name__ == "__main__":
    main()
