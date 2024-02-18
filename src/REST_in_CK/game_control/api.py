from datetime import datetime

import game_control.process_management as process_management
import game_control.debug_mode_traversal as debug_mode_traversal
import game_control.dna_manipulation as dna_manipulation
import game_control.io_operations as io


def prepare() -> None:
    process_management.start_game()
    debug_mode_traversal.open_debug_mode()
    debug_mode_traversal.stabilize_heads()
    
# TODO Make an enum for face names
def load_face(face_name: str) -> None: 
    dna_text = dna_manipulation.load_dna(face_name)
    debug_mode_traversal.load_dna(dna_text)
    return dna_text


def process_face(dna_text: str, req: dict[str, dict[str, int]]) -> None:
    for key, genes_to_change in req.items():
        out_folder_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S%f')}_{key}"
        out_path = io.create_folder(out_folder_name)
        
        mod_dna_text = dna_manipulation.change_dna(dna_text, genes_to_change)
        debug_mode_traversal.load_dna(mod_dna_text)
        io.persist_dna(mod_dna_text, out_path)
        debug_mode_traversal.take_screenshot(out_path)
                
        
def terminate() -> None:
    process_management.end_game()