# src/loaders/pdf_loader.py
from pathlib import Path
import logging
from PyPDF2 import PdfReader

logger = logging.getLogger(__name__)

def load_pdf(path):
    
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File non trovato: {path}")

    reader = PdfReader(str(p))
    texts = []
    for i, page in enumerate(reader.pages):
        try:
            page_text = page.extract_text() or ""
            texts.append(page_text)
        except Exception as e:
            logger.warning("Errore estrazione testo pagina %s: %s", i, e)
            texts.append("")  # mantieni il posto per la pagina

    return "\n".join(texts).strip()
