# src/config/settings.py
import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
#print(__file__)
#print(BASE_DIR)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@dataclass(frozen=True)
class Settings:
    OPENAI_API_KEY: str
    VECTOR_DB_PATH: Path
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int
    LOG_LEVEL: str

def load_settings() -> Settings:
    
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        raise RuntimeError("OPENAI_API_KEY non impostata. Aggiungila in .env o nelle variabili d'ambiente.")

    vector_db_path = Path(os.getenv("VECTOR_DB_PATH", BASE_DIR / "data" / "vector_store"))
    chunk_size = int(os.getenv("CHUNK_SIZE", "500"))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "100"))
    log_level = os.getenv("LOG_LEVEL", "INFO")

    # ensure directories exist
    vector_db_path.mkdir(parents=True, exist_ok=True)

    return Settings(
        OPENAI_API_KEY=openai_key,
        VECTOR_DB_PATH=vector_db_path,
        CHUNK_SIZE=chunk_size,
        CHUNK_OVERLAP=chunk_overlap,
        LOG_LEVEL=log_level
    )

settings = load_settings()
