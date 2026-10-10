"""Validate local docs, example data, and syntax without sending API requests."""

import ast
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def main():
    problems = []
    document_count = 0
    block_count = 0
    for path in sorted(ROOT.rglob("*")):
        if ".git" in path.relative_to(ROOT).parts or not path.is_file():
            continue
        name = str(path.relative_to(ROOT))
        try:
            if path.suffix == ".py":
                ast.parse(path.read_text(encoding="utf-8"))
            elif path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
            elif path.suffix in {".md", ".txt"}:
                document_count += 1
                text = path.read_text(encoding="utf-8")
                links = re.findall(r"\]\(([^\s)]+)\)", text)
                links += re.findall(r'(?:href|src)="([^"]+)"', text)
                for link in links:
                    destination = urlsplit(html.unescape(link))
                    if destination.scheme or destination.netloc or not destination.path:
                        continue
                    target = path.parent / unquote(destination.path)
                    if not target.exists():
                        problems.append(f"{name}: missing target {link}")
                for language, code in re.findall(r"```(python|javascript|json)\n(.*?)\n```", text, re.S):
                    block_count += 1
                    if language == "python":
                        ast.parse(code)
                    elif language == "json":
                        json.loads(code)
                    elif shutil.which("node"):
                        subprocess.run(["node", "--check", "--input-type=module"], input=code, text=True, capture_output=True, check=True)
                    else:
                        problems.append(f"{name}: install Node.js to check the JavaScript example")
        except (SyntaxError, ValueError, subprocess.CalledProcessError) as exc:
            problems.append(f"{name}: {exc}")
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"Passed: {document_count} documents, local links, JSON files, Python syntax, and {block_count} code blocks. No API calls made.")


if __name__ == "__main__":
    main()
