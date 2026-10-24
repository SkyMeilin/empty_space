import os
import json
from datetime import datetime
from pathlib import Path

README_PATH = Path("README.md")
LOGS_DIR = Path("test_logs")

def get_dir_structure(root_dir=".") -> str:
    """Generiert eine Verzeichnisbaum-Übersicht des Repositories."""
    ignored = {".git", ".github", "__pycache__", "hf_cache", ".venv"}
    lines = []
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignored]
        depth = root.count(os.sep)
        indent = "  " * depth
        folder_name = os.path.basename(root) if root != "." else "."
        lines.append(f"{indent}📁 {folder_name}/")
        
        sub_indent = "  " * (depth + 1)
        for f in sorted(files):
            if f != ".DS_Store":
                lines.append(f"{sub_indent}📄 {f}")
                
    return "\n".join(lines)

def get_requirements() -> str:
    """Liest die aktuellen Requirements aus."""
    req_file = Path("requirements.txt")
    if req_file.exists():
        content = req_file.read_text(encoding="utf-8").strip()
        return f"```text\n{content}\n```"
    return "_Keine requirements.txt gefunden._"

def count_test_logs() -> int:
    """Zählt vorhandene Test-Logs im lokalen/gemounteten Ordner."""
    if LOGS_DIR.exists():
        return len(list(LOGS_DIR.glob("*.json")))
    return 0

def generate_readme():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tree = get_dir_structure()
    reqs = get_requirements()
    log_count = count_test_logs()

    # Hugging Face Metadata Header (falls im HF Space)
    hf_header = """---
title: JoyAI Orchester Control Center
emoji: 🎛️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 5.9.0
app_file: app.py
pinned: false
---
"""

    readme_content = f"""{hf_header}
# 🎛️ JoyAI Orchester – Control Center & Dashboard

> **Automatisch generierte Dokumentation**  
> *Letzte Aktualisierung:* `{now}`

---

## 📌 Projektübersicht

Dieses Repository enthält das **JoyAI Orchester Dashboard** inklusive automatischer Test-Protokollierung (`/data/test_logs`), Gradio-Interface und ZeroGPU-Anbindung.

---

## 📁 Repository-Struktur

```text
{tree}
