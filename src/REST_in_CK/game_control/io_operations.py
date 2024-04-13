import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_PATH = Path(os.getenv("RESULT_FOLDER"))

def get_folder():
    return BASE_PATH

def create_folder(name: str | Path) -> Path:
    path = BASE_PATH / name
    path.mkdir(parents=True, exist_ok=True)
    return path


def persist_dna(dna_text: str, out_path: Path):
    with open(out_path, "w", encoding="UTF-8") as out_file:
        out_file.write(dna_text)
