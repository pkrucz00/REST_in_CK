from pathlib import Path

BASE_PATH = Path("./results")

def create_folder(name: str | Path) -> Path:
    path = BASE_PATH / name
    path.mkdir(parents=True, exist_ok=True)
    return path


def persist_dna(dna_text: str, out_folder: Path):
    out_path = out_folder / "dna.txt"
    with open(out_path, "w", encoding="UTF-8") as out_file:
        out_file.write(dna_text)
