# create_project.py
import json
import os
from pathlib import Path

LAUNCH_JSON = {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": True
        }
    ]
}

SETTINGS_JSON = {
    # Base ortamı kullan
    "python.defaultInterpreterPath": r"C:\Users\tcdn\anaconda3\python.exe",
    # Çalıştırmayı dosyanın olduğu klasörde yap
    "python.terminal.executeInFileDir": True,
    # Terminal ve encoding
    "terminal.integrated.defaultProfile.windows": "Command Prompt",
    "files.encoding": "utf8",
    # Editör görünümü (opsiyonel)
    "editor.fontFamily": "JetBrains Mono, Consolas, 'Courier New', monospace",
    "editor.fontLigatures": True,
    "editor.fontSize": 16,
    # Code Runner varsa terminalde çalışsın
    "code-runner.runInTerminal": True,
    "code-runner.executorMap": {"python": "python -u"}
}

GITIGNORE = """
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.ipynb_checkpoints

# Environments
.env
.venv
venv/
ENV/
env/
"""

README_MD = """# Yeni Python Projesi

Bu proje, VS Code ile tek tuşla (F5 / Ctrl+F5 / Shift+Enter) çalışacak şekilde hazırlanmıştır.

## Kısayollar
- Ctrl+F5: Dosyayı entegre terminalde çalıştır
- F5: Debug modunda çalıştır (input destekli, aynı terminal)
- Shift+Enter: Seçili satır/hücreyi çalıştır (# %% hücreleri destekli)

## Yapı
- .vscode/launch.json: F5/Ctrl+F5 davranışı
- .vscode/settings.json: Proje özel VS Code ayarları
- src/: Python kaynak kodları
- data/: veri klasörü
- notebooks/: Jupyter defterleri
"""

SAMPLE_PY = r'''# %%
print("Merhaba abim, proje otomatik kuruldu!")

# %%
x = int(input("Bir sayı gir: "))
print("x^2 =", x*x)
'''

SAMPLE_IPYNB = """{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["# Hoş geldin!\\nBu notebook 'Python (base)' kernelinde çalışacak şekilde hazır."]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": ["import sys\\nprint(sys.version)"]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (base)",
   "language": "python",
   "name": "base"
  },
  "language_info": {"name": "python", "pygments_lexer": "ipython3"}
 },
 "nbformat": 4,
 "nbformat_minor": 5
}"""

def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("Proje klasörünü gir (ör. C:\\\\Users\\\\tcdn\\\\Desktop\\\\yeni_proje):")
    target = input("> ").strip().strip('"')

    if not target:
        print("Geçersiz yol.")
        return

    root = Path(target)
    (root / ".vscode").mkdir(parents=True, exist_ok=True)
    (root / "src").mkdir(exist_ok=True)
    (root / "data").mkdir(exist_ok=True)
    (root / "notebooks").mkdir(exist_ok=True)

    # VS Code dosyaları
    write_json(root / ".vscode" / "launch.json", LAUNCH_JSON)
    write_json(root / ".vscode" / "settings.json", SETTINGS_JSON)

    # Örnek içerikler
    write_text(root / "README.md", README_MD)
    write_text(root / ".gitignore", GITIGNORE)
    write_text(root / "src" / "main.py", SAMPLE_PY)
    write_text(root / "notebooks" / "example.ipynb", SAMPLE_IPYNB)

    print("\n✅ Kurulum tamam!")
    print(f"- Proje klasörü: {root}")
    print("- VS Code'da File → Open Folder → bu klasörü aç")
    print("- 'src/main.py' dosyasında:")
    print("    • Shift+Enter = hücre çalıştır (Jupyter hissi)")
    print("    • Ctrl+F5 = dosyayı terminalde çalıştır")
    print("    • F5 = debug modunda çalıştır (aynı terminal)")
    print("- 'notebooks/example.ipynb' dosyasında Kernel: Python (base) görünecek.")

if __name__ == '__main__':
    main()
