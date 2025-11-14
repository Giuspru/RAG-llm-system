# src/loaders/txt_loader.py
from pathlib import Path

def load_txt(path, encoding="utf-8"):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File non trovato: {path}")

    with p.open("r", encoding=encoding, errors="replace") as f:
        return f.read().strip()
