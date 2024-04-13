import os
import time
from pathlib import Path

import game_control.screen_control_utils as scu
import game_control.dna_manipulation as dna

from dotenv import load_dotenv
load_dotenv()


SCREENSHOT_WAIT_TIME = float(os.getenv("SCREENSHOT_WAIT_TIME")) # [s]  - the game needs some time between pasting the dna and taking a screenshot to render the image 
MALE_FACE_REGION = (500, 190, 300, 300)
ORIGINAL_RESOLUTION = (1920, 1080)

def open_debug_mode() -> None:
    scu.press("`", direct_x=True)   # open debug panel
    scu.find_and_click("portrait_editor")
    scu.press("`", direct_x=True)   # close debug panel   
   
   
def stabilize_heads() -> None:
    scu.find_and_click("head_state")
    scu.press("1", direct_x=True)
    scu.find_and_click("torso_state")
    scu.press("1", direct_x=True)


def load_dna(dna_text: str) -> None:
    dna.copy_dna(dna_text)
    scu.find_and_click("paste_persistent_dna")
    
def compute_region(res_x, res_y) -> tuple[int, int, int, int]:
    orig_x, orig_y = ORIGINAL_RESOLUTION
    offset_x, offset_y = (orig_x - res_x) // 2, (orig_y - res_y) // 2
    return (MALE_FACE_REGION[0] - offset_x, MALE_FACE_REGION[1] - offset_y, MALE_FACE_REGION[2], MALE_FACE_REGION[3])

def take_screenshot(output_path: str | Path, resolution: tuple[int, int]):
    time.sleep(SCREENSHOT_WAIT_TIME)
    region = compute_region(*resolution)
    scu.screenshot_face(region, output_path)