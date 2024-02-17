import pyperclip
from pathlib import Path


def find_dna_path(face_name: str) -> str:
    dna_dir = Path(__file__).parents[1] / "static/dna"
    return (dna_dir / f"{face_name}.txt").as_posix()


def copy_dna(face_name: str) -> None:
    path = find_dna_path(face_name)
    with open(path, 'r') as file:
        text = file.read().rstrip('\n')
    pyperclip.copy(text)
    

def paste_dna() -> str:
    return pyperclip.paste()