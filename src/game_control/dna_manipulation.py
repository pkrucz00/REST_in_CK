import pyperclip
from pathlib import Path


def find_dna_path(face_name: str) -> str:
    dna_dir = Path(__file__).parents[1] / "static/dna"
    return (dna_dir / f"{face_name}.txt").as_posix()

def load_dna(face_name: str) -> str:
    path = find_dna_path(face_name)
    with open(path, 'r') as file:
        return file.read().rstrip('\n')

def copy_dna(text: str) -> None:
    pyperclip.copy(text)
    

def paste_dna() -> str:
    return pyperclip.paste()

def modify_gene_value(line: str, value: str):
    print(f"line: {line}")
    DOM_GENE_VAL_POS = 2
    splitted_line = line.split()
    splitted_line[DOM_GENE_VAL_POS] = value
    result =  " ".join(splitted_line)
    return result
 
def change_line_if_needed(line: str, genes_to_change: dict[str, int]) -> str:
    new_line = line
    for gene_name, gene_value in genes_to_change.items():
        if gene_name in line:
            new_line = modify_gene_value(line, str(gene_value))
    
    return new_line

def change_dna(dna_text: str, genes_to_change: dict[str, int]) -> str:    
    print(dna_text)
    dna_lines = dna_text.split("\n")
    print(dna_lines)
    new_dna_lines = [change_line_if_needed(line, genes_to_change) for line in dna_lines]
    return "\n".join(new_dna_lines)