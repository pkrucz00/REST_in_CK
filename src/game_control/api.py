import game_control.process_management as process_management
import game_control.debug_mode_traversal as debug_mode_traversal
import game_control.clipboard as clipboard
import game_control.screen_control_utils as scu

def prepare() -> None:
    process_management.start_game()
    debug_mode_traversal.open_debug_mode()
    debug_mode_traversal.stabilize_heads()
    
# TODO Make an enum for face names
def load_face(face_name: str) -> None: 
    clipboard.copy_dna(face_name)
    scu.find_and_click("paste_persistent_dna")
    

#TODO Find a type for req
def process_face(req) -> None:
    pass
    # for key, genes_to_change in req:
        
        
        
def terminate() -> None:
    process_management.end_game()